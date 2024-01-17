from config.events_conf import EVENTS

AVAILABLE_ACTIONS = [event['action'] for event in EVENTS]

FUNCTIONS_BY_EVENT_ACTION = {}

for event in EVENTS:
    if 'function' in event.keys():
        FUNCTIONS_BY_EVENT_ACTION[event['action']] = event['function']
