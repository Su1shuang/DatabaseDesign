from flask import Blueprint, request
from src.db.user import user_signin, user_change_passwd

user = Blueprint("user", __name__)


@user.route("/api/user/login", methods=["POST"])
def login():
    return {
        "success":
            True if user_signin(request.form["username"],
                                request.form["password"], 2) else False
    }
#处理用户登录请求。根据请求中的用户名（username）和密码（password）调用 user_signin() 函数进行身份验证。根据验证结果返回一个包含成功/失败信息的 JSON 响应。

@user.route("/api/user/passwd", methods=["POST"])
def passwd():
    return {
        "success":
            True if user_change_passwd(request.form["username"],
                                       request.form["oldPasswd"],
                                       request.form["newPasswd"], 2) else False
    }
#处理用户修改密码请求。根据请求中的用户名（username）、旧密码（oldPasswd）和新密码（newPasswd）调用 user_change_passwd() 函数进行密码修改。根据修改结果返回一个包含成功/失败信息的 JSON 响应。