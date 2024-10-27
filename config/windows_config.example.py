import pyautogui

PROGRAMMING_TAB_WINDOW_TITLES_ELEMENTS = ['.java',
                                          '.py',
                                          '.md',
                                          '.xml',
                                          '.sh',
                                          '.dart']


def validateProgrammingSwitch():
    activeWindowTitle = pyautogui.getActiveWindowTitle()
    return activeWindowTitle and (
            len([x for x in PROGRAMMING_TAB_WINDOW_TITLES_ELEMENTS if
                 (x in activeWindowTitle)]) > 0)


def validateDesktopSwitch():
    activeWindowTitle = pyautogui.getActiveWindowTitle()
    return activeWindowTitle is not None and ('Program Manager' in activeWindowTitle or activeWindowTitle == '')


# List conditions to switch options on macropad
ACTIVITIES = [
    {
        'condition': validateProgrammingSwitch,
        'menuIdentifier': 'PROGRAMMING'
    },
    {
        'condition': validateDesktopSwitch,
        'menuIdentifier': 'DESKTOP'
    }
]
