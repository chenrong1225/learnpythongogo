from flask import Blueprint
from flask_cors import CORS

#__name__表示当前模块名字,static为静态目录，templates为模板目录
#static_url_path 访问静态资源的url前缀 默认值 static
#static_folder静态文件的目录，默认是static
#template_folder 模板文件的目录，默认template
user=Blueprint('user',__name__)
CORS(user, resources=r"/*")