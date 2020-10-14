import os
import sys
import urllib.request
token = "YOUR_ACCESS_TOKEN"
header = "Bearer " + token # Bearer 다음에 공백 추가

#clubid = "29066157" # 탬탬카페의 고유 ID값
#menuid = "6" #자게의 메뉴 ID

clubid="30248603"#테스트 카페의 ID
menuid="1"#자게의 ID

text_title="오뱅온"
text_contents="탬탬님이 방송을 켰습니다.\nhttp://twitch.tv/2chamcham2/"

url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote(text_title)
content = urllib.parse.quote(text_contents)
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
