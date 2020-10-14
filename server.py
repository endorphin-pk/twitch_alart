import requests
from urllib import parse
import os
import sys
import urllib.request

debug=False

code=""
state=""

access_token=""
refresh_token=""
client_id="r2nZOh5yD_S1QXZCwGbg"
client_secret="2o3UFYxv3r"

def make_token():
    code_get_url="https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={}&state={}&redirect_uri={}"
    code_get_url=code_get_url.format("r2nZOh5yD_S1QXZCwGbg","REWERWERTATE","http://localhost/")
    result_url=requests.get(code_get_url)

    print(code_get_url)
    result_url=input()

    result_params = result_url.split("?")[1]
    if(debug==True):
        print("result_params = ",result_params)
    code = result_params.split("&")[0].split("=")[1]
    state = result_params.split("&")[1].split("=")[1]
    #code="m7glLZXalO6jOHvqOu"
    #state="REWERWERTATE"
    if(debug==True):
        print("code = ", code)
        print("state = ", state)
    access_url = "https://nid.naver.com/oauth2.0/token"
    access_data = {
        "grant_type":"authorization_code",
        "client_id":"r2nZOh5yD_S1QXZCwGbg",
        "client_secret":"2o3UFYxv3r",
        "code":"{}".format(code),
        "state":"{}".format(state)
    }
    if(debug==True):
        print(access_data)

    res = requests.get(access_url,params=access_data)
    res.json()

    ## 정보 backup
    access_token=res.json()['access_token']
    refresh_token= res.json()['refresh_token']
    if(debug==True):
        print("Access_token = {}".format(access_token))

def rfresh_token():
    access_url = "https://nid.naver.com/oauth2.0/token"
    access_data = {
        "grant_type":"authorization_code",
        "client_id":"r2nZOh5yD_S1QXZCwGbg",
        "client_secret":"2o3UFYxv3r",
        "refresh_token":"{}".format(refresh_token)
    }
    if(debug==True):
        print(access_data)

    res = requests.get(access_url,params=access_data)
    access_token=res.json["access_token"]

def del_token():
    #del
    print('')

header = "Bearer " + access_token # Bearer 다음에 공백 추가
clubid = "30248603" # 카페의 고유 ID값
menuid = "1" # (상품게시판은 입력 불가)
url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = parse.quote("[subject] 네이버 Cafe api Test Python")
content = parse.quote("[content] 네이버 Cafe api Test Python")

print("{}\n{}".format(subject,content))

data = "subject=" + subject + "&content=" + content
request = urllib.request.Request(url, data=data.encode("utf-8"))
request.add_header("Authorization", header)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)