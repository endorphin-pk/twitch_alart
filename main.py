import naver_func
import twitch_func

twitch_func.make_token()
if(twitch_func.is_streaming()==True):
    print("on")
else:
    print("off")