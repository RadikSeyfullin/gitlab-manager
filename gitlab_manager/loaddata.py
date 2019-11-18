import gitlab, os
import re, requests, json, sys, time

from auth_app.models import GL_User
from projects_app.models import GL_Project
from django.contrib.auth.models import User

URL = 'https://gitlab.com'
SIGN_IN_URL = 'https://gitlab.com/users/sign_in'
API_URL = 'https://gitlab.com/api/v4/'

user_login = ''
user_password = ''

session = requests.Session()

def loadData(request):
    global token
    user_login = request.user.username
    user_password = request.user.gl_user.p_user

    start_time = time.time()

    is_logged_get = session.get(API_URL + 'user')
    if is_logged_get.status_code == 401:
        print('-------------------------------------------------------')
        print('Loading data from gitlab')
        print('-------------------------------------------------------')
        login = session.get(SIGN_IN_URL).content
        for st in login.split(b'\n'):
            m = re.search('name="authenticity_token" value="([^"]+)"', str(st))
            if m:
                break
        
        if m:
            token = m.group(1)
        
        data = {
            'user[login]': user_login,
            'user[password]': user_password,
            'authenticity_token': token,
        }

        req = session.post(SIGN_IN_URL, data=data)
        if req.url != "https://gitlab.com/":
            print('-------------------------------------------------------')
            print('Error! Failed to load data from gitlab')
            print(req.url + '\n' + user_login + ' ' + user_password + '\n' + token)
            print()
            print('-------------------------------------------------------')
        gl = gitlab.Gitlab(URL, api_version="4", session=session)

    projects_get = session.get(API_URL + 'projects?membership=True')
    projects = json.loads(projects_get.text)

    # Adding Projects
    projects_of_user = []
    for project in projects:
        pid = project['id']
        if not GL_Project.objects.filter(pid=pid).exists():
            name = project['name']
            description = project['description']
            name_with_namespace = project['name_with_namespace']
            created_at = project['created_at']
            creator = request.user
            new_project = GL_Project(pid=pid, name=name, description=description, name_with_namespace=name_with_namespace, created_at=created_at, creator=creator)
            new_project.save()
            projects_of_user.append(new_project)
    
    if len(projects_of_user) > 0:
        for project in projects_of_user:
            request.user.gl_user.member.add(project)
    
    end_time = time.time()
    timing = end_time - start_time
    print('-------------------------------------------------------')
    print('Data was loaded' + '\n' + str(timing))
    print('-------------------------------------------------------')