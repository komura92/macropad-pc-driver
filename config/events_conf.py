import os
import sys
import time
import tkinter as tk

import pyautogui
import pyperclip

from crudgenerator import generate


EVENTS = [
    ##################################
    # ######## desktop events ########
    ##################################
    {
        "action": "ADD_DART",
        "function": lambda: (
            pyautogui.hotkey('alt', 'insert'),
            pyautogui.sleep(0.1),
            pyautogui.typewrite('dart'),
            pyautogui.hotkey('enter')
        )
    },
    {
        "action": "RUN_INTELLIJ",
        "function": lambda: (
            pyautogui.hotkey('win', '2')
        )
    },
    {
        "action": "RUN_PYCHARM",
        "function": lambda: (
            pyautogui.hotkey('win', '3')
        )
    },
    {
        "action": "RUN_ANDROID_STUDIO",
        "function": lambda: (
            pyautogui.hotkey('win', '1')
        )
    },
    {
        "action": "RUN_CHROME",
        "function": lambda: (
            pyautogui.hotkey('win', '5')
        )
    },
    {
        "action": "RUN_EXPLORER",
        "function": lambda: (
            pyautogui.hotkey('win', 'e')
        )
    },
    {
        "action": "RUN_TERMINAL",
        "function": lambda: (
            runTerminalOrCmd()
        )
    },
    ##################################
    # ######## gaming events #########
    ##################################
    {
        "action": "RUN_DISCORD",
        "function": lambda: (
            pyautogui.hotkey('win', '4')
        )
    },
    {
        "action": "RUN_STEAM",
        "function": lambda: (
            pyautogui.hotkey('win', '6')
        )
    },
    {
        "action": "RUN_CS",
        "function": lambda: (
            runCs()
        )
    },
    {
        "action": "CLICK_ACCEPT",
        "function": lambda: (
            pyautogui.moveTo(626, 425, 0.5),
            pyautogui.leftClick()
        )
    },
    #######################################
    # ######## programming events #########
    #######################################
    {
        "action": "SWITCH_CASE_SHORTCUT",
        "function": lambda: (
            pyautogui.hotkey('ctrl', 'alt', 'num1')
        )
    },
    {
        "action": "GENERATE_CRUD",
        "function": lambda: (
            generateCrud()
        )
    },
    {
        "action": "ANALYZE_STACKTRACE",
        "function": lambda: (
            pyautogui.hotkey('ctrl', 'alt', 'num2')
        )
    },
    {
        "action": "EVALUATOR_SHORTCUT",
        "function": lambda: (
            pyautogui.hotkey('alt', 'shift', '8')
        )
    },
    {
        "action": "MVN_BUILD",
        "function": lambda: (
            pyautogui.press('ctrl'),
            pyautogui.press('ctrl'),
            time.sleep(0.2),
            pyautogui.typewrite('mvn clean install -T 1.5C -U'),
            pyautogui.press('enter')
        )
    },
    {
        "action": "DEV_DEPLOY_SCRIPT",
        "function": lambda: (
            runDeployScript()
        )
    }
]


def runDeployScript():
    # select dir with deploy script in IntelliJ
    pyautogui.hotkey('ctrl', 'shift', 'c')
    projectDir = getStringFromClipboard()

    # run script if exists
    filePath = projectDir + "/deploy.sh"
    if os.path.exists(filePath):
        os.system(filePath)


def getStringFromClipboard():
    return pyperclip.paste()


def showEntityWizard(projectDir):
    frame = tk.Tk()
    frame.title("Create CRUD API for entity")
    frame.geometry('400x200')

    # Label Creation
    lbl = tk.Label(frame, text="Entity name:")
    lbl.pack()

    # TextBox Creation
    inputText = tk.Text(frame,
                        height=5,
                        width=20)

    inputText.pack()

    # Button Creation
    printButton = tk.Button(frame,
                            text="Generate",
                            command=lambda: (generate(inputText.get(1.0, "end-1c"), projectDir), frame.destroy()))

    printButton.pack()

    frame.attributes('-topmost', True)
    frame.update()
    frame.attributes('-topmost', False)
    frame.mainloop()


def generateCrud():
    pyautogui.hotkey('ctrl', 'shift', 'c')
    projectDir = getStringFromClipboard()
    showEntityWizard(projectDir)


def runTerminalOrCmd():
    if sys.platform == 'linux':
        pyautogui.hotkey("ctrl", "alt", "t")
    elif sys.platform == 'win32':
        executeCommandInBackground("start cmd")


def executeCommandInBackground(command: str):
    os.system(command + " &")


def runCs():
    if sys.platform == 'win32':
        cs_command = "\"C:\\Users\\Damian\\Desktop\\Counter-Strike 2.url\""
        executeCommandInBackground(cs_command)
