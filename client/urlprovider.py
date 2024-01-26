import socket

from config.server_conf import SERVER_URL
from config.driver_conf import TARGET_DEVICE_ID

_DEVICE_ID = socket.gethostname()
_DEVICE_TYPE = 'PC'


def getSendMessageUrl():
    return f'{SERVER_URL}?deviceId={TARGET_DEVICE_ID}'


def getSubscriptionUrl():
    return f'{SERVER_URL}/subscribe?deviceType={_DEVICE_TYPE}&deviceId={_DEVICE_ID}'


def getMacropadsUrl():
    return f'{SERVER_URL}/macropads'
