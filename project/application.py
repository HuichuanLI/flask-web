# -*- coding: utf-8 -*-
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from flask_apscheduler import APScheduler

app = Flask(__name__)
manager = Manager(app)

app.config.from_pyfile("config/base_setting.py")
if "ops_config" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % (os.environ['ops_config']))

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/mysql"
db = SQLAlchemy(app)

scheduler = APScheduler()
scheduler.init_app(app)
