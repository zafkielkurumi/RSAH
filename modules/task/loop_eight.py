import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.adb import screenshot, swiper_on_screen
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print
from modules.config import AHConfig, config


class LoopEight(Task):
  sleepTime = 0.6
  
  def __init__(self, name="LoopEight") -> None:
    super().__init__(name)
    self.conf = config.ah_config["task"]["循环85"]
    self.SURPORT = config.ah_config["SURPORT"]
    
    
  def start(self):    
    while(self.conf["run"]):
      screenshot()
      self.autoSkip()

  def autoSkip(self):
    """自动跳过"""
    conf = self.conf["params"]["auto_skip"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_SKIP))()
      self.clickBtn(btn_pic(ButtonName.BTN_BLANK_CONTINUE))()
      self.clickBtn(btn_pic(ButtonName.BTN_BLANK_CONTINUE1))()