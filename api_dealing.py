import requests
url = "https://api.yukiharu.pw/get_leaderboard"

def request_data():
    req = requests.get(url, timeout=30)  # 请求连接
    req_json = req.json()  # 获取数据
    return req_json