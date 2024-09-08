import time
from ApiTestEngine.core2.cases import run_test
import TestTask
from ApiProjectTest.celery import celery_app
from Scenes.serializer import SceneCaseReadSerializer
from TestTask.models import TestRecord, TestReport
from TestTask.models import TestTask as TaskTable
from Testproject.models import TestEnv


@celery_app.task
def run_demo():
    print('开始执行用例')
    time.sleep(3)
    return '用例执行完成'


@celery_app.task
def run_task(env_id, task_id, username):
    # 获取测试环境数据
    env = TestEnv.objects.get(id=env_id)
    # 组装请求的配置数据
    env_config = {
        "ENV": {
            "host": env.host,
            "headers": env.headers,
            **env.global_variable,
            **env.debug_global_variable
        },
        "DB": env.db,
        "global_func": env.global_func
    }
    # 获取测试任务的执行数据进行组装
    task = TaskTable.objects.get(id=task_id)
    # 获取任务中的任务流信息
    scenes = task.scene.all()
    case_data = []
    for scene in scenes:
        # 通过任务流来获取测试的任务执行用例
        cases = scene.scenestocase_set.all()
        # 对执行用例的数据对象进行序列化
        res = SceneCaseReadSerializer(cases, many=True).data
        # 对执行用例的数据进行排序
        datas = sorted(res, key=lambda x: x['sort'])
        # 添加任务到执行顺序中
        case_data.append({
            "name": scene.name,
            "Cases": [item['icase'] for item in datas]
        })
    # 运行测试前创建一个运行记录
    record = TestRecord.objects.create(task=task, env=env, tester=username, status='执行中')
    # 运行测试任务
    result = run_test(env_config=env_config, case_data=case_data, debug=False)[0]
    # 更新测试报告
    record.all = result['all']
    record.success = result['success']
    record.fail = result['fail']
    record.error = result['error']
    record.pass_rate = '{:.2f}'.format(result['success'] / result['all'])
    record.status = '执行结束'
    record.save()
    # 保存测试报告
    TestReport.objects.create(info=result, recode=record).save()
    print(result)
    return result
