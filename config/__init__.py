from config.events_conf import ACTIONS

AVAILABLE_ACTIONS = [event['action'] for event in ACTIONS]

FUNCTIONS_BY_EVENT_ACTION = {}

for action in ACTIONS:
    if 'function' in action.keys():
        FUNCTIONS_BY_EVENT_ACTION[action['action']] = action['function']
