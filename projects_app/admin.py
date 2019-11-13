from django.contrib import admin
from projects_app.models import GL_Project

# Register your models here.
class GLPorjectAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name', 'description', 'name_with_namespace', 'created_at',)

admin.site.register(GL_Project, GLPorjectAdmin)