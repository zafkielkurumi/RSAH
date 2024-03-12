import logging
import subprocess
import time
from modules.config import APP_NAME, EMULATOR_PATH
from modules.utils.adb import check_app_running, check_connect, connect_device, disconnect_adb, open_app
from modules.utils.log import logging_print

from modules.utils.subprocess_helper import subprocess_run

def start_emulator():
  logging_print('开始启动模拟器')
  try:
    subprocess_run(EMULATOR_PATH, isasync=True)
  except Exception as e:
    logging_print("启动模拟器失败, 可能是没有以管理员模式运行 或 配置的模拟器路径有误")



def connect_adb():
  logging_print("开始连接模拟器")
  disconnect_adb()
  for i in range(10):
    time.sleep(i)
    if(check_connect()):
      logging_print("连接模拟器成功")
      return
    else:
      logging_print('未连接模拟器,重试中')   
  raise Exception("连接模拟器失败")
      
def start_app():
  logging_print('开始打开游戏')
  if check_app_running(APP_NAME):
    logging_print("游戏中")
    return True
  for i in range(10):
    open_app(APP_NAME)
    time.sleep(2)
    if check_app_running(APP_NAME):
      logging_print('游戏已打开')
      return True
    else:
      logging_print('游戏打开失败')
      False
    
  
  