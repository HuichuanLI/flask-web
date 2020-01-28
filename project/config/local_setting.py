# -*- coding: utf-8 -*-
# 本地开发环境配置文件
from config.base_setting import *

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/movie_cat"

SECRET_KEY = "huichuan123456"

DOMAIN = {
    "www":"http://0.0.0.0:5000"
}