import requests

object_streamer="kotlin_kt"

client_id="le6caf43yq3470507wbtp65zhckxlp"
client_secret="in03cyccix7i8ad48614dvfh7lm3x3"

access_token=""

def make_token():
    global client_id
    global client_secret
    #global refresh_token
    global access_token
    res=requests.post('https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials'.format(client_id,client_secret)).json()
    if("error" in res):
        print("{}\n{}".format(res["error"],res["message"]))
        return False
    access_token=res["access_token"]
    return True

def is_streaming():
    data = requests.get('https://api.twitch.tv/helix/streams?user_login={}'.format(object_streamer),headers={'Authorization': 'Bearer {}'.format(access_token), 'Client-ID': '{}'.format(client_id)}).json()
    if(data["data"] != []):
        return True
    else:
        return False#offline