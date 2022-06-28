import requests


def request_data(mode,sort):
    url = "https://api.yukiharu.pw/get_leaderboard"
    url = url+"?mode="+mode+"&sort="+sort
    req = requests.get(url, timeout=30)  # 请求连接
    req_json = req.json()  # 获取数据
    return req_json
