# -*-coding:utf8-*-
from functools import wraps
from flask import session,request,redirect,url_for


def admin_login(f):
    """管理员登录装饰器 """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def user_login(f):
    """用户登录装饰器"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("home.login"))
        return f(*args, **kwargs)
    return decorated_function
