import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


def login():
    response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                             data={'username': data['login'], 'password': data['passwd']})
    return response.json()['token']


def get_post(token):
    resource = requests.get("https://test-stand.gb.ru/api/posts",
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})

    # for i in resource.json()['data']:
    #  print(i['description'])

    return resource.json()


print(get_post(login()))