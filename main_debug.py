# -*- coding:utf-8  -*-
# @Time     : 2021-02-25 23:33
# @Author   : BGLB
# @Software : PyCharm

import os
import time
from scheduler.control import task


TaskConfig = {
    "TaskId": "13465786",
    "TaskName": "测试百度",
    "CrawlerConfig": {
        "CrawlerName": "baidu",
        "CrawlerType": "request",  # [request, brower, android]
    },
    "OrtherConfig": {

    }

}


def main():
    task.start_one_task(TaskConfig)
    pass


if __name__ == '__main__':
    main()



