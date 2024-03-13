import time
from Assets.btn.Button_Name import ButtonName
from modules.task.task import Task
from modules.utils.game import btn_pic, clickScreen, mathGame
from modules.utils.log import logging_print


class Login(Task):
  def __init__(self, name="Login") -> None:
    super().__init__(name)
    
    
  def start(self):
    logging_print('登录游戏')
    if self.runUtil(self.enterGame, self.homePage):
      logging_print('登录成功')
    else:
      logging_print('登录失败')
      
  
  def enterGame(self):
    # 点击开始
    b, point = mathGame(btn_pic(ButtonName.BTN_LOGIN))
    
    if b:
      # 由于无法准确获取开始按钮，朝下挪移一点
      print(point)
      clickScreen((point[0], point[1] + 50))

    