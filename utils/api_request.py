# utils/api_request.py
def send_post(url, data):
    # 模拟真实接口行为
    if data["username"] == "admin" and data["password"] == "123456":
        return {"code": 200, "msg": "login success"}
    else:
        return {"code": 401, "msg": "invalid password"}