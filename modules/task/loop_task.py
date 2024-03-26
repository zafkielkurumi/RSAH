import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.adb import screenshot
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print
from modules.config import AHConfig, config



class LoopTask(Task):
  sleepTime = 1

  def __init__(self, name="LoopTask") -> None:
    super().__init__(name)
    self.conf = config.ah_config["task"]["循环任务"]
    
    
  def start(self):
    logging_print('开始持续执行自动点击开始战斗和自动点击加速弹丸')
    self.autoMisson()
    
  def autoMisson(self):
    """用于跑商过程轮询判断点击开始战斗，体力为0"""
    while(self.conf["run"]):
      screenshot()
      self.autoSpeed()
      self.autoBattle()
      self.loop_color_tree()
      self.activity_shi_zhi()
      time.sleep(self.sleepTime)

  def autoSpeed(self):
    conf = self.conf["params"]["auto_speed"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_SPEED))()

  def autoBattle(self):
    """自动开始战斗"""
    conf = self.conf["params"]["auto_battle"]
    if conf["run"]:
      Btn_List = [
        btn_pic(ButtonName.BTN_BATTLE),
        btn_pic(ButtonName.BTN_START_BATTLE),
        btn_pic(ButtonName.BTN_NEXT),
      ]
      for btn in Btn_List:
        self.clickBtn(btn)()
  
  def loop_color_tree(self):
    """循环彩树"""
    conf = self.conf["params"]["color_tree"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_LOOP_CAI_SHU))()

  def activity_shi_zhi(self):
    """活动石芝"""
    conf = self.conf["params"]["activity_shi_zhi"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_ACTIVITY_SHI_ZHI))()
          

