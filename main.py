import sseclient

from threading import Thread

from config import AVAILABLE_ACTIONS, FUNCTIONS_BY_EVENT_ACTION
from config.server_conf import SERVER_URL


def getSseEvents():
    client = sseclient.SSEClient(SERVER_URL)
    for event in client:
        print(event)
        if event.event in AVAILABLE_ACTIONS:
            FUNCTIONS_BY_EVENT_ACTION[event.event]()


thread = Thread(target=getSseEvents)
thread.start()
