# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session, request, redirect
from common.models.user import User
from common.lib.Helper import ops_render, iPagenation
from common.lib.UrlManager import UrlManager
from application import app, db
from common.models.movie import Movie
from sqlalchemy.sql.expression import func

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    req = request.values
    req = request.values
    order_by_f = str(req['order']) if ("order" in req and req['order']) else "lastest"
    query = Movie.query
    page = 1
    if 'p' in req and req['p']:
        page = int(req['p'])

    page_params = {
        'total_count': query.count(),
        "page_size": 30,
        'page': page,
        'url': "/?"
    }
    pages = iPagenation(page_params)
    offset = (page - 1) * page_params['page_size']
    limit = page * page_params['page_size']

    if order_by_f == "hot":
        query = query.order_by(Movie.view_counter.desc(), Movie.id.desc())
    else:
        query = query.order_by(Movie.pub_date.desc(), Movie.id.desc())

    list_movie = query[offset:limit]

    return ops_render("index.html", {"data": list_movie, "pages": pages})


@index_page.route("/info")
def info():
    req = request.values

    id = int(req['id']) if ('id' in req and req['id']) else 0
    if id < 1:
        return redirect(UrlManager.buildUrl("/"))

    info = Movie.query.filter_by(id=id).first()
    if not info:
        return redirect(UrlManager.buildUrl("/"))

    '''
    更新阅读数量
    '''
    info.view_counter += 1
    db.session.add(info)
    db.session.commit()

    '''
    获取推荐
    '''
    recommend_list = Movie.query.order_by(func.rand()).limit(4)
    return ops_render("info.html", {"info": info, "recommend_list": recommend_list})
