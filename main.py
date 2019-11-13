import django, gitlab, os
import re, requests, json, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gitlab_manager.settings')
django.setup()

from auth_app.models import GL_User
from projects_app.models import GL_Project
from django.contrib.auth.models import User

URL = 'https://gitlab.com'
SIGN_IN_URL = 'https://gitlab.com/users/sign_in'
API_URL = 'https://gitlab.com/api/v4/'

session = requests.Session()
token = ''

login = session.get(SIGN_IN_URL).content
for i in login.split(b'\n'):
    m = re.search('name="authenticity_token" value="([^"]+)"', str(i))
    if m:
        break
if m:
    token = m.group(1)

data = {
        'user[login]': 'RadikSeyfullin',
        'user[password]': 'losyellowrradikkclawamsterdam1998',
        'authenticity_token': token,
    }

r = session.post(SIGN_IN_URL, data=data)
if r.url != "https://gitlab.com/":
    print('BREAKED ---------------')
gl = gitlab.Gitlab(URL, api_version="4", session=session)

p_get = session.get(API_URL + 'projects?membership=True')
projects = json.loads(p_get.text)
u_get = session.get(API_URL + 'user')
user = json.loads(u_get.text)

projects_to_u = []
for project in projects:
    pid = project['id']
    name = project['name']
    description = project['description']
    name_with_namespace = project['name_with_namespace']
    created_at = project['created_at']
    new_p = GL_Project(pid=pid, name=name, description=description, name_with_namespace=name_with_namespace, created_at=created_at)
    new_p.save()
    projects_to_u.append(new_p)

u = User.objects.get(pk=1)

uid = user['id']
name = user['name']
p_user = 'losyellowrradikkclawamsterdam1998'
member = projects_to_u
l_user = u

new_u = GL_User(uid=uid, name=name, p_user=p_user, user=l_user)
new_u.save()
for p in projects_to_u:
    new_u.member.add(p)

print('SUCCESS!')