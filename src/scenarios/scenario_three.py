import os.path

import pyautogui
import time


class ScenarioThreeData:
    def __init__(self, manufacturer: str, screen_size: str, screen_resolution: str):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.screen_resolution = screen_resolution

    def is_valid(self) -> bool:
        """
        Validate if the class attributes are valid.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Check if all attributes are strings and not None, with a minimum length of 1
        return all(isinstance(attr, str) and attr is not None and len(attr) >= 1
                   for attr in [self.manufacturer, self.screen_size, self.screen_resolution])


def run_scenario_three(data: ScenarioThreeData):
    print("tests fired")
    pyautogui.PAUSE = 0.3

    find_and_click(1)
    find_and_click(2)
    enter_text(data.manufacturer)
    find_and_click(3)
    enter_text(data.screen_size)
    find_and_click(4)
    enter_text(data.screen_resolution)
    take_screenshot("filled_forms")
    find_and_click(5)
    enter_text("export1.xml")
    take_screenshot("exporting")
    find_and_click(6)
    take_screenshot("finish")


def find_and_click(step: int, double: bool = False, risky: bool = False):
    clicks = 1
    if double:
        clicks = 2

    confidence = 0.9
    if risky:
        confidence = 0.8

    pos = pyautogui.locateOnScreen("scenarios/three/step{}.png".format(str(step).zfill(3)), confidence=confidence)
    pyautogui.click(x=pos.left+(pos.width/2), y=pos.top+(pos.height/2), clicks=clicks, duration=0.5, button="left")


def enter_text(text: str, confirm: bool = False):
    print("Entering text: {}".format(text))
    for char in text:
        pyautogui.press(char, presses=1)

    if confirm:
        pyautogui.press("enter")


def take_screenshot(step_name: str):
    ss_dir_name = "{}/scenarios/three/screenshots/".format(os.getcwd())
    current_dir_name = "test_{}".format(str(time.time_ns()))

    output_dir = "{}{}".format(ss_dir_name, current_dir_name)

    if not os.path.exists(output_dir) or not os.path.isdir(output_dir):
        os.mkdir("{}".format(output_dir))

    pyautogui.screenshot("{}/{}.png".format(output_dir, step_name))
