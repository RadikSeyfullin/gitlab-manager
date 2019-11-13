from django.contrib import admin
from auth_app.models import GL_User

# Register your models here.
class GLUserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'user')

admin.site.register(GL_User, GLUserAdmin)