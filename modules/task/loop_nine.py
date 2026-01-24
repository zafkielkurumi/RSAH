import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.adb import screenshot, swiper_on_screen
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print
from modules.config import AHConfig, config


class LoopNine(Task):
  sleepTime = 0.6
  
  def __init__(self, name="LoopNine") -> None:
    super().__init__(name)
    self.conf = config.ah_config["task"]["循环九"]
    self.SURPORT = config.ah_config["SURPORT"]
    logging_print('循环九')
    
  def start(self):
  
    self.autoMisson()
    
  def autoMisson(self):
    """用于跑商过程轮询判断点击开始战斗，体力为0"""
    logging_print('90')
    
    self.auto90()
    
    time.sleep(self.sleepTime)

  def auto90(self):
    """自动90以上"""
    logging_print("auto90")
    while self.conf["run"]:
      # self.runUtil(self.clickBtn(btn_pic(ButtonName.BTN_START_MISSION) ), self.mathCondition(btn_pic(ButtonName.BTN_ACTIVITY)))
      # 点击挑战
       # 挑战副本
        screenshot()
        time.sleep(0.6)
        if (self.mathCondition(btn_pic(ButtonName.BTN_CHALLENGE))):
          self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE))()

        if (self.mathCondition(btn_pic(ButtonName.BTN_CREATE_HOUSE))):
          self.clickBtn(btn_pic(ButtonName.BTN_CREATE_HOUSE))()

        # 助战
        if (self.mathPic(btn_pic(ButtonName.BTN_SURPORT))):
            target = True
            startX = 640
            startY = 600
            SURPORT = btn_pic(ButtonName.BTN_FANG_ZHENG)
            if self.SURPORT == "LAO_WANG":
              SURPORT = btn_pic(ButtonName.BTN_LAO_WANG)
            while target:
                logging_print(1111)
                screenshot()
                time.sleep(0.6)
                endy = startY - 300
                swiper_on_screen(startX, startY, 0, endy, 1500)
                time.sleep(1.5)

                if self.mathPic(SURPORT, False):
                  target = False
                  print("找到目标")
                  self.clickBtn(SURPORT)()
                if(endy > 600):
                  self.clickBtn(btn_pic(ButtonName.BTN_SURPORT), 50, 220)()
        time.sleep(0.6)
        if (self.mathCondition(btn_pic(ButtonName.BTN_CONFIRM1))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM1))()
        if (self.mathCondition(btn_pic(ButtonName.BTN_BATTLE_START))):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_START))()
        if (self.mathCondition(btn_pic(ButtonName.BTN_CONFIRM))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM))()
          # 开始战斗了
        logging_print(self.bttleCount)
        if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2)):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2))()
        if self.mathPic(btn_pic(ButtonName.BTN_CONFIRM)):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM))()
