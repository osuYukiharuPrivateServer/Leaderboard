import api_dealing
import json



def DealJson():
    jsonn = api_dealing.request_data()
    json_str = json.dumps(jsonn)
    data2 = json.loads(json_str)
    sta = data2['status']
    lb = data2['leaderboard']
    return lb
