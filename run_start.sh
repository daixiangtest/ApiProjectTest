#收集静态文件
python3 manage.py collectstatic
# 启动Django服务
python3 manage.py runserver
# 运行celery 服务
celery -A ApiProjectTest worker -l info -P threads
celery -A 项目名ApiProjectTest beat -l INFO