from typing import Tuple
from modules.utils.adb import click_on_screen
from modules.utils.opencv import match_image
from modules.config import AHConfig, config
def btn_pic(btnName):
  # 根据按钮名称返回图片路径
  return "./Assets" + f"/{btnName}.png"


def mathGame(imgUrl: str, showResult = False):
  return match_image(f"./{config.ah_config.get('SCREENSHOT_NAME')}", imgUrl, showResult)

def clickScreen(point: Tuple[float, float]):
  click_on_screen(point[0], point[1])