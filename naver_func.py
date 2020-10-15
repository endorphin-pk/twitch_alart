import requests
from urllib import parse
from datetime import datetime
import urllib.request

debug = False

code = ""
state = ""

expired_time = ""
ttl = ""
access_token = ""
refresh_token = ""
client_id = "r2nZOh5yD_S1QXZCwGbg"
client_secret = "2o3UFYxv3r"


# noinspection PyTypeChecker
def is_expired():
    global expired_time
    global ttl
    nowtime = datetime.now()
    if (ttl < (nowtime - expired_time).second):
        return (nowtime - expired_time).second
    else:
        return False


def make_token():
    global debug

    global code
    global state

    global access_token
    global refresh_token
    global client_id
    global ttl
    global client_secret

    code_get_url = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={}&state={}&redirect_uri={}"
    code_get_url = code_get_url.format("{}".format(client_id), "REWERWERTATE", "http://localhost/")

    print(code_get_url)
    result_url = input()

    result_params = result_url.split("?")[1]
    if (debug == True):
        print("result_params = ", result_params)
    code = result_params.split("&")[0].split("=")[1]
    state = result_params.split("&")[1].split("=")[1]
    # code="m7glLZXalO6jOHvqOu"
    # state="REWERWERTATE"
    if (debug == True):
        print("code = ", code)
        print("state = ", state)
    access_url = "https://nid.naver.com/oauth2.0/token"
    access_data = {
        "grant_type": "authorization_code",
        "client_id": "{}".format(client_id),
        "client_secret": "{}".format(client_secret),
        "code": "{}".format(code),
        "state": "{}".format(state)
    }
    if (debug == True):
        print(access_data)

    res = requests.get(access_url, params=access_data)
    if("error" in res.json()):
        if(debug==True):
            print("{}\n{}".format(res.json()["error"],res.json()["error_description"]))
        return False
    ## 정보 backup
    access_token = res.json()['access_token']
    refresh_token = res.json()['refresh_token']
    ttl=int(res.json()["expires_in"])
    if (debug == True):
        print("Access_token = {}".format(access_token))
    return True

def rfresh_token():
    global access_token
    global ttl
    global client_id
    global client_secret
    global refresh_token

    access_url = "https://nid.naver.com/oauth2.0/token"
    access_data = {
        "grant_type": "authorization_code",
        "client_id": "{}".format(client_id),
        "client_secret": "{}".format(client_secret),
        "refresh_token": "{}".format(refresh_token)
    }
    if (debug == True):
        print(access_data)

    res = requests.get(access_url, params=access_data)

    if ("error" in res.json()):
        if (debug == True):
            print("{}\n{}".format(res.json()["error"], res.json()["error_description"]))
        return False
    access_token = res.json()["access_token"]
    ttl=int(res.json()["expires_in"])
    return True

def del_token():
    global access_token
    global client_id
    global client_secret

    access_url = "https://nid.naver.com/oauth2.0/token"
    access_data = {
        "grant_type": "delete",
        "client_id": "{}".format(client_id),
        "client_secret": "{}".format(client_secret),
        "access_token": "{}".format(parse.quote(access_token)),
        "service_provider":"NAVER"
    }
    res=requests.get(access_url,params=access_data)
    if ("error" in res.json()):
        if (debug == True):
            print("{}\n{}".format(res.json()["error"], res.json()["error_description"]))
        return False
    access_token=""
    return True


def write_cafe(title,text):
    global access_token

    header = "Bearer " + access_token  # Bearer 다음에 공백 추가
    clubid = "30248603"  # 카페의 고유 ID값
    menuid = "1"  # (상품게시판은 입력 불가)
    url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
    subject = parse.quote(title)
    content = parse.quote(text)
    if(debug==True):
        print("{}\n{}".format(subject, content))
    data = "subject=" + subject + "&content=" + content
    data_enc=data.encode("utf-8")
    request = urllib.request.Request(url, data=data_enc)
    request.add_header("Authorization", header)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        if(debug==True):
            print(response_body.decode('utf-8'))
        return True
    else:
        if(debug==True):
            print("Error Code:" + rescode)
        return False