# Generated by Django 4.2.15 on 2024-08-20 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='文件', upload_to='', verbose_name='文件')),
                ('info', models.JSONField(default=list, help_text='文件信息', verbose_name='文件信息')),
            ],
            options={
                'verbose_name': '测试文件表',
                'db_table': 'TestFile',
            },
        ),
        migrations.CreateModel(
            name='TestProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=50, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='负责人', max_length=50, verbose_name='负责人')),
                ('create_time', models.TimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '测试项目表',
                'db_table': 'TestProject',
            },
        ),
        migrations.CreateModel(
            name='TestEnv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_variable', models.JSONField(blank=True, default=dict, help_text='全局变量', null=True, verbose_name='全局变量')),
                ('debug_global_variable', models.JSONField(blank=True, default=dict, help_text='调试模式全局变量', null=True, verbose_name='调试模式全局变量')),
                ('db', models.JSONField(blank=True, default=dict, help_text='数据库配置', null=True, verbose_name='数据库配置')),
                ('host', models.CharField(help_text='测试环境的host地址', max_length=50, verbose_name='测试环境的host地址')),
                ('headers', models.JSONField(blank=True, default=dict, help_text='全局请求头信息', null=True, verbose_name='全局请求头信息')),
                ('global_func', models.TextField(blank=True, default='', help_text='全局工具函数', null=True, verbose_name='全局工具函数')),
                ('name', models.CharField(help_text='测试环境名称', max_length=50, verbose_name='测试环境名称')),
                ('project', models.ForeignKey(help_text='项目名称', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '测试环境表',
                'db_table': 'TestEnv',
            },
        ),
    ]
