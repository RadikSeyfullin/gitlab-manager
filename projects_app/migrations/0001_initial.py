# Generated by Django 2.2.6 on 2019-11-11 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GL_Project',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='GitLab: ID проекта')),
                ('description', models.TextField(verbose_name='GitLab: Описание проекта')),
                ('name', models.CharField(max_length=255, verbose_name='GitLab: Название проекта')),
                ('name_with_namespace', models.CharField(max_length=255, verbose_name='GitLab: Название проекта (полное)')),
                ('created_at', models.DateTimeField(verbose_name='GitLab: Дата создания проекта')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.GL_User', verbose_name='GitLab: Создатель проекта')),
            ],
            options={
                'verbose_name': 'GitLab Проект',
                'verbose_name_plural': 'GitLab Проекты',
            },
        ),
    ]