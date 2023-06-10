from flask import Blueprint, request
from src.db.query import select_all_from_tbC2inew, select_all_from_tbC2i3
from lib.draw import draw

advanced = Blueprint("advanced", __name__)


@advanced.route("/api/advanced/c2i", methods=["GET"])
def c2i():
    tmp = select_all_from_tbC2inew()
    ret = []
    for _, row in tmp.iterrows():
        ret.append({
            "servingSector": row["ServingSector"],
            "interfereringSector": row["InterferingSector"],
            "mean": row["mean"],
            "std": row["std"],
            "diff9": row["PrbC2I9"],
            "abs6": row["PrbABS6"]
        })
    return {"result": ret}
#获取 c2i 数据。调用 select_all_from_tbC2inew() 函数获取 c2i 数据，将结果处理成特定格式的 JSON 响应。

@advanced.route("/api/advanced/c2i3", methods=["GET"])
def c2i3():
    x = request.args.get("x")
    tmp = select_all_from_tbC2i3(x)
    ret = []
    for _, row in tmp.iterrows():
        ret.append([row["SectorA"], row["SectorB"], row["SectorC"]])
    return {"result": ret}
#获取 c2i3 数据。根据请求中的参数 x，调用 select_all_from_tbC2i3() 函数获取对应的 c2i3 数据，并将结果处理成特定格式的 JSON 响应。

@advanced.route("/api/advanced/louvain", methods=["GET"])
def louvain():
    x = float(request.args.get("x"))
    return {"img": draw.get_base64(x)}
#获取 Louvain 图像。根据请求中的参数 x，调用 draw.get_base64() 函数生成 Louvain 图像，并将结果处理成特定格式的 JSON 响应。