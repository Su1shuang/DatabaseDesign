from flask import Blueprint, request
from src.db.user import *
from src.db.common import *
import time

admin = Blueprint("admin", __name__)


@admin.route("/api/admin/login", methods=["POST"])
def login():
    return {
        "success":
            True if user_signin(request.form["username"],
                                request.form["password"], 1) else False
    }
#处理管理员登录请求。根据请求中的用户名和密码，调用 user_signin() 函数进行验证，并返回一个包含登录成功或失败信息的 JSON 响应。

@admin.route("/api/admin/passwd", methods=["POST"])
def passwd():
    return {
        "success":
            True if user_change_passwd(request.form["username"],
                                       request.form["oldPasswd"],
                                       request.form["newPasswd"], 1) else False
    }
#处理管理员修改密码请求。根据请求中的用户名、旧密码和新密码，调用 user_change_passwd() 函数进行密码修改，并返回一个包含密码修改成功或失败信息的 JSON 响应。

@admin.route("/api/admin/userList", methods=["GET"])
def get_user_list():
    ls = user_get_list(2)
    ret = []
    for info in ls:
        ret.append({"username": info[0], "time": str(info[1])[:10]})
    return {"users": ret}
#获取用户列表。调用 user_get_list() 函数获取用户信息列表，并将结果处理成特定格式的 JSON 响应。

@admin.route("/api/admin/createUser", methods=["POST"])
def create_user():
    return {
        "success":
            True if user_add(request.form["username"], request.form["password"],
                             2) else False
    }
#创建用户。根据请求中的用户名和密码，调用 user_add() 函数创建用户，并返回一个包含创建成功或失败信息的 JSON 响应。

@admin.route("/api/admin/removeUser", methods=["POST"])
def remove_user():
    return {
        "success": True if user_delete(request.form["username"], 2) else False
    }
#移除用户。根据请求中的用户名，调用 user_delete() 函数移除用户，并返回一个包含移除成功或失败信息的 JSON 响应。

@admin.route("/api/admin/DBInfo", methods=["GET"])
def get_db_info():
    return db_get_inf()
    # return {
    #     "host": "127.0.0.1",
    #     "port": 3306,
    #     "db": "ltedb",
    #     "username": "root",
    #     "password": "wushuang123",
    #     "interactiveTimeout": 0,
    #     "waitTimeout": 0,
    #     "partition": "",
    #     "queryCacheSize": ""
    # }
#获取数据库信息。调用 db_get_inf() 函数获取数据库的相关信息，并返回一个 JSON 响应。

@admin.route("/api/admin/setTimeout", methods=["POST"])
def set_timeout():
    db_change_timeout(request.form["interactiveTimeout"],
                      request.form["waitTimeout"])
    return {"success": True}
#设置数据库连接超时时间。根据请求中的交互超时时间和等待超时时间，调用 db_change_timeout() 函数修改数据库连接超时时间，并返回一个包含修改成功或失败信息的 JSON 响应。

@admin.route("/api/admin/setCache", methods=["POST"])
def set_query_cache_size():
    db_change_cache_size(request.form["queryCacheSize"])
    return {"success": True}
#设置查询缓存大小。根据请求中的查询缓存大小，调用 db_change_cache_size() 函数修改查询缓存大小，并返回一个包含修改成功或失败信息的 JSON 响应。