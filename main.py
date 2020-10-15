import naver_func
import twitch_func
from time import sleep
from datetime import datetime

title="ON AIR"
text="ON AIR\ntwitch.tv/{}".format(twitch_func.object_streamer)


naver_func.make_token()
debug=naver_func.debug
if(debug==True):
    refresh_term = 10
else:
    refresh_term=naver_func.ttl/3#sec

while True:
    naver_func.rfresh_token()
    twitch_func.make_token()
    if(twitch_func.is_streaming()==True):#started
        print("{}\'s broadcast was started:{}".format(twitch_func.object_streamer,datetime.now()))
        naver_func.write_cafe(title,text)
    else:
        print("Checked, Offline:{}".format(datetime.now()))
    if(debug==True):
        input()
    else:
        sleep(refresh_term)