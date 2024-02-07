from func import get_post
import requests
import yaml

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


def test_1(login):
    result = get_post(login)['data']
    lst = []
    for item in result:
        lst.append(item['id'])
    print(lst)
    assert 97556 in lst, "test_1 fail"

def test_2(login):
    result1 = requests.post(data['address'],
                            headers={"X-Auth-Token": login},
                            params={'title': data['title'], 'description': data['description'],
                                    'content': data['content']})
    result2 = requests.get(data['address'], headers={"X-Auth-Token": login},
                           params={'description': data['description']})

    assert result1.status_code == 200 and result2.status_code == 200, "test_2 fail"
    assert result1.json()['description'] == data['description'], "test_2 fail"