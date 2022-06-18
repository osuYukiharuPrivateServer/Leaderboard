# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from flask import Flask, render_template
import api_dealing
import requests
import json_dealing
from gevent import pywsgi #added this for production environment
app = Flask(__name__)


@app.route('/')



def index():
    # return "Hi,Flask!"
    result = json_dealing.DealJson()
    print(result)
    if(len(result)<24):
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-','pp': '-', 'plays': '-',  'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})


    return render_template('index.html', p1='done', p2=result)

if "__main__"==__name__:
    #app.run(port="5008")  #this is only for test environment on the localhost. Use the following as the production environment.
    
    server = pywsgi.WSGIServer(('0.0.0.0',5008),app)  #The server would be running at 5008 port
    server.serve_forever()  #Service start

