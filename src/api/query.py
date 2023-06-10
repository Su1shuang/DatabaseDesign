from flask import Blueprint, request
from src.db.query import *

query = Blueprint("query", __name__)


@query.route("/api/query/sector", methods=["GET"])
def sector():
    if request.args.get("sectorID") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_SectorId(request.args.get("sectorID"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
    elif request.args.get("sectorName") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_SectorName(
            request.args.get("sectorName"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
#根据扇区ID（sectorID）或扇区名称（sectorName）查询扇区信息。根据请求参数的不同，调用不同的查询函数，并将查询结果处理成特定格式的 JSON 响应。

@query.route("/api/query/eNodeB", methods=["GET"])
def eNodeB():
    if request.args.get("eNodeBID") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_eNodeBId(request.args.get("eNodeBID"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
    elif request.args.get("eNodeBName") is not None:
        ret = {}
        d = select_SectorAllo_From_tbCell_eNodeBName(
            request.args.get("eNodeBName"))
        for key, value in d.items():
            ret[key] = value[0]
        return {"result": ret}
#根据eNodeB ID（eNodeBID）或eNodeB名称（eNodeBName）查询eNodeB信息。根据请求参数的不同，调用不同的查询函数，并将查询结果处理成特定格式的 JSON 响应。

@query.route("/api/query/kpi", methods=["GET"])
def kpi():
    ls = select_Data_From_tbKPI_SectorName(request.args.get("name"),
                                           request.args.get("attribute"),
                                           request.args.get("start"),
                                           request.args.get("end"))
    ret = [float(x[0]) for x in ls]
    return {"value": ret}
#根据扇区名称（name）、指标属性（attribute）、起始时间（start）和结束时间（end）查询KPI数据。调用 select_Data_From_tbKPI_SectorName() 函数进行查询，并将查询结果处理成特定格式的 JSON 响应。

@query.route("/api/query/prb", methods=["GET"])
def prb():
    ls = select_Data_From_tbPRB_SectorName(request.args.get("name"),
                                           request.args.get("prb"),
                                           request.args.get("start"),
                                           request.args.get("end"))
    ret = [float(x[0]) for x in ls]
    return {"value": ret}
#根据扇区名称（name）、PRB号（prb）、起始时间（start）和结束时间（end）查询PRB数据。调用 select_Data_From_tbPRB_SectorName() 函数进行查询，并将查询结果处理成特定格式的 JSON 响应。

@query.route("/api/query/candidate", methods=["GET"])
def candidate():
    type = request.args.get("key")
    ls = select_BasicData_From_tb(int(type))
    ret = list(set([x[0] for x in ls]))
    return {"candidate": ret}
#根据键值（key）查询候选项数据。调用 select_BasicData_From_tb() 函数进行查询，并将查询结果处理成特定格式的 JSON 响应。