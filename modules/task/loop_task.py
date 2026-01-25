import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.adb import screenshot, swiper_on_screen
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print
from modules.config import AHConfig, config


class LoopTask(Task):
  sleepTime = 0.6
  
  def __init__(self, name="LoopTask") -> None:
    super().__init__(name)
    self.conf = config.ah_config["task"]["循环任务"]
    self.SURPORT = config.ah_config["SURPORT"]
    
    
  def start(self):
  
    self.autoMisson()
    
  def autoMisson(self):
    """用于跑商过程轮询判断点击开始战斗，体力为0"""
    logging_print('开始持续执行自动跳过')
    logging_print('开始持续执行自动AP')
    
    
    while(self.conf["run"]):
      screenshot()
      time.sleep(0.2)
      # self.autoSpeed()
      # self.autoBattle()
      # self.loop_color_tree()
      # self.activity_shi_zhi()
      # self.autoEnteryStation()
      # self.loopMission()
      self.autoSkip()
      self.autoAp()
      self.auto90()
      self.auto85()

      time.sleep(self.sleepTime)

  def autoSpeed(self):
    """自动点击加入弹丸，只有前进才点击""" 
    conf = self.conf["params"]["auto_speed"]
    if conf["run"]:
      if self.mathPic(btn_pic(ButtonName.BTN_GO)):
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

  def autoEnteryStation(self):
    """自动进入站点"""
    conf = self.conf["params"]["enter_station"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_ENTER_STATION))()

  def loopMission(self):
    """自动循环打材料,请先保证已经全部通关"""
    conf = self.conf["params"]["loopMission"]
    startX = 1280
    startY = 360
    btn_list = [
      btn_pic(ButtonName.BTN_DANGER_10),
      btn_pic(ButtonName.BTN_DANGER_6),
      btn_pic(ButtonName.BTN_DANGER_3),
    ]
    if conf["run"]:
      target = True
      while target:
        endx = startX + 100
        swiper_on_screen(startX, startY, endx, 0)
        time.sleep(0.6)
        print(btn_list[conf["level"]])
        if self.mathPic(btn_list[conf["level"]], True):
          target = False
          print("找到目标")

    
  def autoSkip(self):
    """自动跳过"""
    conf = self.conf["params"]["auto_skip"]
    if conf["run"]:
      self.clickBtn(btn_pic(ButtonName.BTN_SKIP))()
      self.clickBtn(btn_pic(ButtonName.BTN_BLANK_CONTINUE))()
      self.clickBtn(btn_pic(ButtonName.BTN_BLANK_CONTINUE1))()

  def autoAp(self):
    """自动AP"""
    conf = self.conf["params"]["auto_ap"]
    if conf["run"]:
      if self.mathPic(btn_pic(ButtonName.BTN_AP_TIP)):
        # 点击4次BTN_AP_USE.png
        self.clickBtn(btn_pic(ButtonName.BTN_AP_USE1))()
        time.sleep(0.6)
        for i in range(4):
          screenshot()
          time.sleep(0.6)
          logging_print("BTN_AP_USE")
          if self.mathPic(btn_pic(ButtonName.BTN_AP_USE)):
            self.clickBtn(btn_pic(ButtonName.BTN_AP_USE))()
        time.sleep(1)  
        self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
        time.sleep(0.5)
        self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
        time.sleep(0.5)
        self.clickBtn(btn_pic(ButtonName.BTN_NEXT_STAGE))()

  def auto85(self):
    """自动85和妹妹"""
    conf = self.conf["params"]["auto_85"]
    if conf["run"]:
      # self.runUtil(self.clickBtn(btn_pic(ButtonName.BTN_START_MISSION) ), self.mathCondition(btn_pic(ButtonName.BTN_ACTIVITY)))
      # 点击挑战
      # 副本确定
      if (self.mathCondition(btn_pic(ButtonName.BTN_CONFIRM1))):
        self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM1))()
       # 挑战副本
      if (self.mathCondition(btn_pic(ButtonName.BTN_CHALLENGE))):
        self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE))()
      if (self.mathCondition(btn_pic(ButtonName.BTN_CHALLENGE1))):
        self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE1))()
      if (self.mathCondition(btn_pic(ButtonName.BTN_SURPORT))):
        self.clickBtn(btn_pic(ButtonName.BTN_SURPORT), 50, 220)()
        # 开始战斗了
      logging_print(self.bttleCount)
      if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2)):
        if self.bttleCount < int(config.ah_config["COUNT85"]):
          logging_print('3333')
          if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2)):
            self.clickBtn(btn_pic(ButtonName.BTN_NEXT_STAGE))()
            self.bttleCount = self.bttleCount + 1
          else :
            logging_print('2222')
            self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM3))()
            self.bttleCount = 0
        else:
            logging_print('111')
            if self.mathPic(btn_pic(ButtonName.BTN_CONFIRM3)):
              self.bttleCount = 0
              self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM3))()
        time.sleep(0.6)

  def auto90(self):
    """自动90以上"""
    conf = self.conf["params"]["auto_90"]
    if conf["run"]:
      # self.runUtil(self.clickBtn(btn_pic(ButtonName.BTN_START_MISSION) ), self.mathCondition(btn_pic(ButtonName.BTN_ACTIVITY)))
      # 点击挑战
       # 挑战副本
        if (self.mathCondition(btn_pic(ButtonName.BTN_CHALLENGE))):
          self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE))()

        if (self.mathCondition(btn_pic(ButtonName.BTN_CREATE_HOUSE))):
          self.clickBtn(btn_pic(ButtonName.BTN_CREATE_HOUSE))()

        # 助战
        if (self.mathPic(btn_pic(ButtonName.BTN_SURPORT))):
            target = True
            startX = 640
            startY = 600
            endy = startY - 300
            SURPORT = btn_pic(ButtonName.BTN_FANG_ZHENG)
            if self.SURPORT == "LAO_WANG":
              SURPORT = btn_pic(ButtonName.BTN_LAO_WANG)
            while target:
                screenshot()
                time.sleep(0.6)

                if self.mathPic(SURPORT, False):
                  target = False
                  print("找到目标")
                  self.clickBtn(SURPORT)()
                  time.sleep(0.6)
                if(endy < -900):
                  self.clickBtn(btn_pic(ButtonName.BTN_SURPORT), 50, 220)()
                
                
                swiper_on_screen(startX, startY, 0, endy, 1500)
                time.sleep(1.5)
                
        if (self.mathCondition(btn_pic(ButtonName.BTN_CONFIRM1))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM1))()
        if (self.mathCondition(btn_pic(ButtonName.BTN_BATTLE_START))):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_START))()
        if (self.mathCondition(btn_pic(ButtonName.BTN_CONFIRM))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM))()
        
        if self.mathPic(btn_pic(ButtonName.BTN_CONFIRM2)):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM2))()
        if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2)):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2))()

