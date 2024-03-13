import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.adb import screenshot
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print
from modules.config import AHConfig, config

Btn_List = [
   btn_pic(ButtonName.BTN_BATTLE),
   btn_pic(ButtonName.BTN_START_BATTLE),
   btn_pic(ButtonName.BTN_NEXT),
   btn_pic(ButtonName.BTN_SPEED),
]


class ContinuedTask(Task):
  sleepTime = 1

  def __init__(self, name="ContinuedTask") -> None:
    super().__init__(name)
  
    
    
  def start(self):
    logging_print('开始持续执行自动点击开始战斗和自动点击加速弹丸')
    self.battleMisson()
    
  def battleMisson(self):
    """用于跑商过程轮询判断点击开始战斗，体力为0"""
    while(True):
      screenshot()
      for btn in Btn_List:
          if  self.mathPic(btn):
            self.clickBtn(btn)()
      time.sleep(self.sleepTime)

