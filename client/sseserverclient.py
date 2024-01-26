import requests
import json
import client.urlprovider as url_provider


def getAvailableMacropads():
    return json.loads(requests.get(url_provider.getMacropadsUrl()).content)


def setActiveMacropadTab(menuIdentifier: str):
    requests.post(url_provider.getSendMessageUrl(), json={
        'action': 'TAB_UPDATE',
        'tabIdentifier': menuIdentifier
    })
