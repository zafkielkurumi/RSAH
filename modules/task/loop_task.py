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
    self.changeMode = False
    self.alchemyTime = 0
    
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
      self.autoAlchemy()
      self.autoDoAlchemy()

      time.sleep(self.sleepTime)

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
      # self.runUtil(self.clickBtn(btn_pic(ButtonName.BTN_START_MISSION) ), self.mathPic(btn_pic(ButtonName.BTN_ACTIVITY)))
      # 点击挑战
      # 副本确定
      # 误触编队
      if (self.mathPic(btn_pic(ButtonName.BTN_BD))):
        print("误触编队")
        self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
      if (self.mathPic(btn_pic(ButtonName.BTN_CONFIRM1))):
        self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM1))()
       # 挑战副本
      if (self.mathPic(btn_pic(ButtonName.BTN_CHALLENGE))):
        self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE))()
      if (self.mathPic(btn_pic(ButtonName.BTN_CHALLENGE1))):
        self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE1))()
      if (self.mathPic(btn_pic(ButtonName.BTN_SURPORT))):
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
      # self.runUtil(self.clickBtn(btn_pic(ButtonName.BTN_START_MISSION) ), self.mathPic(btn_pic(ButtonName.BTN_ACTIVITY)))
      # 点击挑战
       # 挑战副本
        if (self.mathPic(btn_pic(ButtonName.BTN_CHALLENGE))):
          self.clickBtn(btn_pic(ButtonName.BTN_CHALLENGE))()

        if (self.mathPic(btn_pic(ButtonName.BTN_CREATE_HOUSE))):
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
                else:
                  swiper_on_screen(startX, startY, 0, endy, 1500)
                  time.sleep(1.5)
                  if(endy < -900):
                    self.clickBtn(btn_pic(ButtonName.BTN_SURPORT), 50, 220)()
                
                
        # 误触编队
        if (self.mathPic(btn_pic(ButtonName.BTN_BD))):
          print("误触编队")
          self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
        if (self.mathPic(btn_pic(ButtonName.BTN_CONFIRM1))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM1))()
        if (self.mathPic(btn_pic(ButtonName.BTN_BATTLE_START))):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_START))()
        if (self.mathPic(btn_pic(ButtonName.BTN_CONFIRM))):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM))()
        
        if self.mathPic(btn_pic(ButtonName.BTN_CONFIRM2)):
          self.clickBtn(btn_pic(ButtonName.BTN_CONFIRM2))()
        if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2)):
          self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_SUCCESS2))()

  def autoAlchemy(self):
    """自动材料本"""
    conf = self.conf["params"]["loop_alchemy"]
    if conf["run"]:
      # 选择助战
      if (self.mathPic(btn_pic(ButtonName.BTN_SURPORT))):
        self.clickBtn(btn_pic(ButtonName.BTN_SURPORT), 50, 220)()
      # 点击挑战
      if (self.mathPic(btn_pic(ButtonName.BTN_START_BATTLE_CL))):
        self.clickBtn(btn_pic(ButtonName.BTN_START_BATTLE_CL))()
      # 开始战斗
      if (self.mathPic(btn_pic(ButtonName.BTN_START_BATTLE_CL_2))):
        self.clickBtn(btn_pic(ButtonName.BTN_START_BATTLE_CL_2))()
        # 开始战斗了
      if self.mathPic(btn_pic(ButtonName.BTN_BLANK_CONTINUE)):
        self.clickBtn(btn_pic(ButtonName.BTN_BLANK_CONTINUE))()
		# 再次挑战
      if self.mathPic(btn_pic(ButtonName.BTN_BATTLE_AGAIN)):
        self.clickBtn(btn_pic(ButtonName.BTN_BATTLE_AGAIN))()

  def autoDoAlchemy(self):
    """自动炼金"""
    conf = self.conf["params"]["auto_alchemy"]
    if conf["run"]:
      if self.alchemyTime >= int(config.ah_config["AlchemyTime"]):
        return
      # 选择炼金瓶
      if (self.mathPic(btn_pic(ButtonName.BTN_LJ))):
        self.clickBtn(btn_pic(ButtonName.BTN_LJ))()
      # 检查右上角是否为道具数量
      if (self.mathPic(btn_pic(ButtonName.BTN_LJ_YJXZ)) and not self.changeMode):
        logging_print("切换模式")
        self.clickBtn(btn_pic(ButtonName.BTN_LJ_XZ))()
        time.sleep(0.6)
        clickScreen((760, 200))
        time.sleep(0.6)
        self.changeMode = True
      # 再次检查是否在道具数量界面
      if (self.mathPic(btn_pic(ButtonName.BTN_LJ_DJSL2))):
        # 检查白材料位置
        b, point = mathGame(btn_pic(ButtonName.BTN_LJ_WHITE))
        if b:
          print("白材料位置 x:", point[0], " y:", point[1])
          if point[0] < 440 and point[1] < 300:
            # 到达左上角, 停止任务
            logging_print("炼金完毕")
            self.clickBtn(btn_pic(ButtonName.BTN_LJ_CANCEL))()
            time.sleep(0.6)
            self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
            time.sleep(2)
        # 一键选择材料
        self.clickBtn(btn_pic(ButtonName.BTN_LJ_YJXZ))()
        logging_print("一键选择, 请确认材料是否有异常!")
        time.sleep(2)
        self.clickBtn(btn_pic(ButtonName.BTN_LJ_CONFIRM))()
        logging_print("确认材料")
        time.sleep(0.4)
        self.alchemyTime = self.alchemyTime + 1
        logging_print("开始炼金,当前第" + str(self.alchemyTime) + "轮")
        clickScreen((1000, 600))
        time.sleep(2)
      if (self.mathPic(btn_pic(ButtonName.BTN_LJ_OBTAIN))):
        clickScreen((1200, 700))
        time.sleep(0.6)
        if self.alchemyTime >= int(config.ah_config["AlchemyTime"]):
          logging_print("炼金完毕")
          self.clickBtn(btn_pic(ButtonName.BTN_LJ_CANCEL))()
          time.sleep(0.6)
          self.clickBtn(btn_pic(ButtonName.BTN_BACK))()
          time.sleep(2)


