from celery import Celery
from celery.schedules import crontab
import datetime


class Config():
    broker_url = 'redis://127.0.0.1:6379/7'  # 使用Redis存储任务队列
    result_backend = 'redis://127.0.0.1:6379/8' # 使用Redis存储结果
    timezone = 'Asia/Shanghai'  # 时区设置


    # 任务队列配置
    beat_schedule = {
        'my_schedule1': {
            'task': 'eg.func',
            'schedule': crontab()  # 每分钟执行一次
        }
    }
# 实例化app
app = Celery('tasks')
# 加载配置项
app.config_from_object(Config)
# 自动任务
@app.task
def func():
    print(datetime.datetime.now())