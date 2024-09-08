import os
from celery import Celery

"""
启动celery worker服务:
    celery -A 项目名 worker -l info -P threads
启动celery beat服务: (后面的--scheduler 可以在settings文件中配置)
    celery -A 项目名 beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
"""

# 设置从settings文件中配置的DJANGO_SETTINGS_MODULE参数为默认环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApiProjectTest.settings')
# 注册应用并且命名
celery_app = Celery('taskDemo')
# 从settings文件中获取应用的配置参数(namespace表示获取以**值开头的变量名)
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
# 自动从项目中获取tasks.py 文件中获取celery 任务
celery_app.autodiscover_tasks()
