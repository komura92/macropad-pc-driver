import time
import pyautogui
import sseclient

import client.urlprovider as url_provider
import client.sseserverclient as sse_server_client
import config.driver_conf as driver_config

from threading import Thread

from config import AVAILABLE_ACTIONS, FUNCTIONS_BY_EVENT_ACTION
from config.windows_config import ACTIVITIES


def getSseEvents():
    client = sseclient.SSEClient(url_provider.getSubscriptionUrl())
    for event in client:
        print(event)
        if event.event in AVAILABLE_ACTIONS:
            FUNCTIONS_BY_EVENT_ACTION[event.event]()


def activityMonitor():
    lastActiveTab = None
    while True:
        for activity in ACTIVITIES:
            if activity['condition']() and activity['menuIdentifier'] != lastActiveTab:
                sse_server_client.setActiveMacropadTab(activity['menuIdentifier'])
                lastActiveTab = activity['menuIdentifier']
        if driver_config.PRINT_ACTIVE_WINDOW_NAME:
            print(f'"{pyautogui.getActiveWindowTitle()}"')
        time.sleep(0.1)


thread = Thread(target=getSseEvents)
thread.start()

if driver_config.PRINT_AVAILABLE_DEVICES:
    print(sse_server_client.getAvailableMacropads())

if driver_config.ENABLE_WINDOW_MONITORING:
    thread = Thread(target=activityMonitor)
    thread.start()
