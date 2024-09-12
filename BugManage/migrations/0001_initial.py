# Generated by Django 4.2.15 on 2024-09-12 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestInterface', '0002_alter_iterface_project_alter_iterface_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='提交时间', verbose_name='提交时间')),
                ('status', models.CharField(help_text='bug的状态', max_length=10, verbose_name='bug的状态')),
                ('user', models.CharField(blank=True, help_text='提交者', max_length=20, null=True, verbose_name='提交者')),
                ('info', models.JSONField(blank=True, default=dict, help_text='用例执行信息', verbose_name='用例执行信息')),
                ('interface', models.ForeignKey(help_text='关联用例', on_delete=django.db.models.deletion.CASCADE, to='TestInterface.iterface', verbose_name='关联用例')),
            ],
            options={
                'verbose_name_plural': 'bug管理表',
                'db_table': 'BugManage',
            },
        ),
        migrations.CreateModel(
            name='BugHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='操作时间', verbose_name='操作时间')),
                ('handle', models.TextField(blank=True, help_text='处理操作', null=True, verbose_name='处理操作')),
                ('update_user', models.CharField(blank=True, help_text='操作人', max_length=20, null=True, verbose_name='操作人')),
                ('bug', models.ForeignKey(help_text='关联的bug', on_delete=django.db.models.deletion.CASCADE, to='BugManage.bugmanage', verbose_name='关联的bug')),
            ],
            options={
                'verbose_name_plural': 'bug记录表',
                'db_table': 'BugHandle',
            },
        ),
    ]