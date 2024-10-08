# Generated by Django 4.2.15 on 2024-09-08 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestTask', '0003_alter_testrecord_create_time'),
        ('Testproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cronjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('name', models.CharField(help_text='任务名称', max_length=100, verbose_name='任务名称')),
                ('rule', models.CharField(default='* * * * *', help_text='定时任务的规则', max_length=200, verbose_name='定时任务的规则')),
                ('status', models.BooleanField(default=False, help_text='状态', verbose_name='状态')),
                ('env', models.ForeignKey(help_text='执行环境', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testenv', verbose_name='执行环境')),
                ('project', models.ForeignKey(help_text='关联项目id', on_delete=django.db.models.deletion.CASCADE, to='Testproject.testproject', verbose_name='关联项目id')),
                ('task', models.ForeignKey(help_text='关联的测试任务', on_delete=django.db.models.deletion.CASCADE, to='TestTask.testtask', verbose_name='关联的测试任务')),
            ],
            options={
                'verbose_name_plural': '定时任务表',
                'db_table': 'cronjob',
            },
        ),
    ]
