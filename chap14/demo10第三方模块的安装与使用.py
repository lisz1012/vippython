# Author: lisz1012
# Creation date and time: 6/2/24 5:12 PM

import schedule
import time


def job():
    print('job running...')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()  # 运行所有可以运行的任务. 检查当前是否有需要运行的任务，如果有，就执行它们。
    time.sleep(10)  # 每隔 19 秒检查一次, 任务间隔是 3 秒,早该执行了, 所以总体来说是 10 秒执行一次
# 也可以使用 schedule.every(3).seconds.do(job).tag('my_job') 为任务添加标签, 然后使用 schedule.clear('my_job') 清除任务