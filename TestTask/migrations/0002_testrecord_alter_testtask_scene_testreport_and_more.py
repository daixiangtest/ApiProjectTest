# Generated by Django 4.2.15 on 2024-08-29 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scenes', '0002_scenestocase'),
        ('Testproject', '0001_initial'),
        ('TestTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, help_text='执行时间', verbose_name='执行时间')),
                ('all', models.IntegerField(blank=True, default=0, help_text='用例总数', verbose_name='用例总数')),
                ('success', models.IntegerField(blank=True, default=0, help_text='通过用例数', verbose_name='通过用例数')),
                ('fail', models.IntegerField(blank=True, default=0, help_text='失败用例数', verbose_name='失败用例数')),
                ('error', models.IntegerField(blank=True, default=0, help_text='错误用例数', verbose_name='错误用例数')),
                ('pass_rate', models.CharField(blank=True, default='0', help_text='用例通过率', max_length=50, verbose_name='用例通过率')),
                ('tester', models.CharField(blank=True, help_text='执行者', max_length=50, verbose_name='执行者')),
                ('status', models.CharField(help_text='执行状态', max_length=50, verbose_name='执行状态')),
                ('env', models.ForeignKey(help_text='执行环境', on_delete=django.db.models.deletion.PROTECT, to='Testproject.testenv', verbose_name='执行环境')),
            ],
            options={
                'verbose_name_plural': '运行记录表',
                'db_table': 'TestRecord',
            },
        ),
        migrations.AlterField(
            model_name='testtask',
            name='scene',
            field=models.ManyToManyField(blank=True, help_text='关联的任务流', to='Scenes.testscent', verbose_name='关联的任务流'),
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.JSONField(blank=True, default=dict, help_text='报告的数据', verbose_name='报告的数据')),
                ('recode', models.ForeignKey(help_text='测试记录', on_delete=django.db.models.deletion.CASCADE, to='TestTask.testrecord', verbose_name='测试记录')),
            ],
            options={
                'verbose_name_plural': '测试报告表',
                'db_table': 'TestReport',
            },
        ),
        migrations.AddField(
            model_name='testrecord',
            name='task',
            field=models.ForeignKey(help_text='测试任务表', on_delete=django.db.models.deletion.CASCADE, to='TestTask.testtask', verbose_name='测试任务表'),
        ),
    ]