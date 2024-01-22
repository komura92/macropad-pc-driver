# Macropad PC driver

This python code is the PC controller part of my open source project called "Ninja-Macropad".

During free time I will make some docs about this project to make it usable for 
those who want to increase productivity level with me.

## Showcase
![Examples of automations](https://github.com/komura92/macropad-android-mobile/blob/master/images/macropad-mobile-gif.gif)
#
## Configuration

You can adapt this project to your needs just doing some small changes in 
[events_conf.py](/config/events_conf.py) and set server URL in [server_conf.py](/config/server_conf.py).
Configuration is very user-friendly. We can define actions on _EVENTS_ list 
just giving action name and function to execute. File provided in project contains
many examples which you can find useful creating your own actions. Enjoy!

Example:

    EVENTS = [
        {
            "action": "RUN_INTELLIJ",
            "function": lambda: (
                pyautogui.hotkey('win', '2')
            )
        },

        ...
    ]

## Roadmap

In the future, I want to add some additional features to this project. It will be probably about 
two things per year, depending on my time availability.

There's a shortly described list:
- ~~supported Windows and Linux platforms [MP-PD-F-01]~~,
- notifying mobile app about active windows changing [MP-PD-F-02],
- basic tests for CRUD [MP-PD-F-03],
- missing dependencies popup ? [MP-PD-F-04],
- more advanced entity definition and tests adaptation [MP-PD-F-05],
- selectable CRUD functions to generate [MP-PD-F-06],
- defining CRUD sub-objects [MP-PD-F-07],
- GUI actions configuration [MP-PD-F-08],
- ~~registration with hostname [MP-PD-F-09].~~
