import os

from flask import Blueprint, request, send_from_directory
from src.db.tb import *

data = Blueprint("data", __name__)


@data.route("/api/data/export", methods=["GET"])
def export():
    print(int(request.args.get("table")), request.args.get("type"),
          type(request.args.get("type")))
    file_name = data_export(int(request.args.get("table")),
                            request.args.get("type"))
    return {
        "url": "http://127.0.0.1:3000/download/" + file_name,
    }
#处理数据导出请求。根据请求中的表格编号（table）和文件类型（type），调用 data_export() 函数导出数据，并返回一个包含导出文件的 URL 的 JSON 响应。

@data.route("/download/<filename>")
def download(filename):
    return send_from_directory("download", filename, as_attachment=True)
#处理文件下载请求。根据请求中的文件名（filename），使用 send_from_directory() 函数从指定目录（"download" 文件夹）中发送文件给客户端进行下载。