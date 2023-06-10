from flask import Blueprint, request
from src.db.tb import add_index, del_index, select_index

index = Blueprint("index", __name__)


@index.route("/api/index/getIndex", methods=["GET"])
def getIndex():
    ret = []
    for i in range(1, 4):
        tmp = select_index(i)
        for ls in tmp:
            try:
                ret.append({"table": ls[0], "name": ls[1], "key": ls[2]})
            except IndexError:
                continue
    return {"indexes": ret}
#获取所有索引。调用 select_index() 函数查询数据库中的索引信息，并将结果处理成特定格式的 JSON 响应。

@index.route("/api/index/addIndex", methods=["POST"])
def addIndex():
    table = request.form["table"]
    name = request.form["name"]
    key = request.form["key"]
    print(key, type(key))
    if table == "tbcell":
        table = 1
    elif table == "tbprb":
        table = 3
    else:
        table = 2
    return {"success": add_index(table, key, name)}
#添加索引。根据请求中的表格名称（table）、索引名称（name）和索引键（key），调用 add_index() 函数添加索引，并返回一个包含添加成功或失败信息的 JSON 响应。

@index.route("/api/index/removeIndex", methods=["POST"])
def delIndex():
    table = request.form["table"]
    if table == "tbcell":
        table = 1
    elif table == "tbprb":
        table = 3
    else:
        table = 2
    return {"success": del_index(table, request.form["name"])}
#删除索引。根据请求中的表格名称（table）和索引名称（name），调用 del_index() 函数删除索引，并返回一个包含删除成功或失败信息的 JSON 响应。