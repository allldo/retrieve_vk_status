from urllib.request import urlopen
import json

token = open('.env').read()


def get_music(access_token):
    url = f"https://api.vk.com/method/status.get?&access_token={access_token}&v=5.131"
    response = urlopen(url)

    data_json = json.loads(response.read())

    try:
        audio = data_json['response']['audio']
    except KeyError:
        return False

    answer = data_json['response']['text']
    return answer


