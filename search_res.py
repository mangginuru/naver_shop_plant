import json
import requests


def search_res(inputText):
    text = {
        "data": inputText
    }
    text_str = json.dumps(text)

    headers = {
        "Content-Type": "application/json"
    }

    resp = requests.post("http://121.125.216.89:43210/product", data=text_str, headers=headers)

    result = resp.json()
    return result
