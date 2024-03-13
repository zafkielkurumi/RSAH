import logging
from time import sleep
from typing import Tuple
from Assets.btn.Button_Name import ButtonName

from modules.utils.adb import screenshot
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print



class Task:
  def __init__(self, name) -> None:
    self.name = name
    

    
  def start(self):
    """ 任务开始 """
    pass
  
  def run(self):
    """调用运行"""
    logging_print(self.name)
    self.start()
  
  @staticmethod
  def runUtil(fun1,fun2, sleepTime = 2, time = 15):
    """
      运行func1直到fun2成功，或到达时间限制
    """
    for i in range(time):
      fun1()
      sleep(sleepTime)
      screenshot()
      if(fun2()):
        return True
      sleep(sleepTime)
    screenshot()
    if(fun2()):
      return True
    logging_print("到达时间限制")
    return False

  @staticmethod
  def clickBtn(imgUrl: str):
    def click():
      # 点击开始
      b, point = mathGame(imgUrl)
      if b:
        # 由于无法准确获取开始按钮，朝下挪移一点
        clickScreen((point[0], point[1]))
    return click
    
  @staticmethod
  def homePage():
    """判断首页"""
    return mathGame(btn_pic(ButtonName.BTN_START_MISSION))[0]

  @staticmethod
  def mathCondition(url: str):
    def math():
      return mathGame(url)[0]
    return math
  
  @staticmethod
  def clickPoint(point: Tuple[float, float]):
    def click():
       clickScreen(point)
    return click
  
  @staticmethod
  def mathPic(url: str):
    return mathGame(url)[0]

  