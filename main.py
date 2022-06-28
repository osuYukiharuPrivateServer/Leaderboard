# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from flask import Flask, render_template, request, redirect
import api_dealing
import requests
import json_dealing
app = Flask(__name__)


@app.route('/')
def index():
    # return "Hi,Flask!"
    if 'mode' and 'sort' in request.args:
        mode = str(request.args['mode'])
        sort = str(request.args['sort'])
    else:
        return redirect('/?mode=0&sort=pp')
    result = json_dealing.DealJson(mode,sort)
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
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
    modeout = ""
    if(mode == "0"):
        modeout = "osu! mode"
    if(mode == "1"):
        modeout = "osu!taiko mode"
    if(mode == "2"):
        modeout = "osu!catch mode"
    if(mode == "3"):
        modeout = "osu!mania mode"
    if(mode !="0" and mode !="1" and mode!="2" and mode!="3"):
        modeout = "WTF mode it is !!??"
    return render_template('index.html', p1=modeout, p2=result, p3="Order by: "+sort)

if "__main__"==__name__:
    app.run(port="5008")

