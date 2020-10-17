import naver_func
import twitch_func
from time import sleep
from datetime import datetime
import options

title=options.title
text=options.text
online_log=False
naver_func.make_token()
debug=options.debug

if(debug==True):
    refresh_term = 10
else:
    refresh_term=naver_func.ttl/3#sec

while True:
    if(debug==True):
        tmp=naver_func.rfresh_token()
        if(tmp==False):
            print("Error")
    else:
        naver_func.rfresh_token()
    twitch_func.make_token()
    if(twitch_func.is_streaming()==True):#started
        if(online_log==False):
            online_log=True
            print("{}\'s broadcast was started:{}".format(twitch_func.object_streamer,datetime.now()))
            naver_func.write_cafe(title,text)
        else:
            print("{}\'s broadcast was already started:{}".format(twitch_func.object_streamer,datetime.now()))
    else:
        online_log=False
        print("Checked, Offline:{}".format(datetime.now()))
    if(debug==True):
        input()
    else:
        sleep(refresh_term)
