# Generated by Django 4.2.15 on 2024-08-24 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Testproject', '0001_initial'),
        ('TestInterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iterface',
            name='project',
            field=models.ForeignKey(help_text='项目id', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='项目id'),
        ),
        migrations.AlterField(
            model_name='iterface',
            name='type',
            field=models.CharField(choices=[('1', '项目接口'), ('2', '外部接口')], help_text='接口类型', max_length=50, verbose_name='接口类型'),
        ),
        migrations.CreateModel(
            name='IterFaceCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='用例名称', max_length=50, verbose_name='用例名称')),
                ('headers', models.JSONField(blank=True, default=dict, help_text='请求头信息', null=True, verbose_name='请求头信息')),
                ('request', models.JSONField(blank=True, default=dict, help_text='请求体参数', null=True, verbose_name='请求体参数')),
                ('file', models.JSONField(blank=True, default=dict, help_text='上传文件参数', null=True, verbose_name='上传文件参数')),
                ('setup_script', models.TextField(blank=True, default='', help_text='前置执行脚本', null=True, verbose_name='前置执行脚本')),
                ('teardown_script', models.TextField(blank=True, default='', help_text='后置执行脚本', null=True, verbose_name='后置执行脚本')),
                ('interface', models.ForeignKey(help_text='所属项目id', on_delete=django.db.models.deletion.CASCADE, to='TestInterface.iterface', verbose_name='所属项目id')),
            ],
            options={
                'verbose_name_plural': '测试用例执行表',
                'db_table': 'IterFaceCase',
            },
        ),
    ]
