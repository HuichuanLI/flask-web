# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, request

'''
post/index 列表
post/info 详情
post/set 添加|编辑
post/ops 操作（删除|恢复）
'''

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "index page"


@index_page.route("/me")
def hello():
    return "hello ,I Love Imooc"


@index_page.route("/get")
def get():
    req = request.values
    var_a = req['a'] if "a" in req else "huichuan"
    # var_a = request.args.get("a", "huichuan");
    return "request:%s,params:%s,var_a:%s" % (request.method, request.args, var_a)


@index_page.route("/post", methods=["POST"])
def post():
    # var_a = request.form['a'] if "a" in request.form else "i love imooc"
    # return "request:%s,params:%s,var_a:%s" % (request.method, request.form, var_a)
    req = request.values
    var_a = req['a'] if "a" in req else "i love imooc"
    return "request:%s,params:%s,var_a:%s" % (request.method, request.form, var_a)


@index_page.route("/upload", methods=["POST"])
def upload():
    f = request.files['file'] if "file" in request.files else None
    return "request:%s,params:%s,file:%s" % (request.method, request.files, f)
