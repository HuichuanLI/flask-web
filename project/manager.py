# -*- coding: utf-8 -*-
from application import app, db, manager, scheduler
from www import *
from flask_script import Server, Command
import sys
import traceback
import datetime

## web server
## flask script 设置
manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))


##create_table
@Command
def create_all():
    db.create_all()


# flask_script 添加
manager.add_command("create_all", create_all)


def aps_test():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    app.apscheduler.add_job(func=aps_test, trigger="cron", second="*/5", id="app_test")

    scheduler.start()
    manager.run()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc(e)
