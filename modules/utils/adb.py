import logging
import os
import time
from modules.config import AHConfig, config
from modules.utils.opencv import imgShape
from modules.utils.subprocess_helper import subprocess_run
import subprocess


def disconnect_adb():
  """
  The function disconnect_adb disconnects the current adb connection.
  """
  subprocess_run([ config.ah_config["ADB_PATH"] , 'disconnect', config.ah_config["EMULATOR_IP"] ])

def connect_device():
  """
  连接设备
  """
  subprocess_run([config.ah_config["ADB_PATH"], 'connect', config.ah_config["EMULATOR_IP"],])



def check_connect():
    """
    根据截图来判断是否连接
    """
    if os.path.exists(config.ah_config["SCREENSHOT_NAME"],):
      os.remove(config.ah_config["SCREENSHOT_NAME"])
    connect_device()
    screenshot()
    time.sleep(2)
    if os.path.exists(config.ah_config["SCREENSHOT_NAME"]):
      if os.path.getsize(config.ah_config["SCREENSHOT_NAME"]) != 0:
        print('已连接到模拟器')
        logging.info('已连接到模拟器')
        #  如果截图有大小说明连接成功, 然后判断图片大小
        if imgShape(config.ah_config["SCREENSHOT_NAME"]):      
          return True
   
    else:
        print('截图不存在')
    return False
#   for in range(10):
     


def screenshot():
  """
  The function captures a screenshot from an Android emulator and saves it as a file.
  """
  with open(f"./{config.ah_config.get('SCREENSHOT_NAME')}","wb") as out:    
    subprocess_run([config.ah_config["ADB_PATH"], '-s', config.ah_config["EMULATOR_IP"], 'shell', 'screencap', '-p'], stdout=out)
  with open(f"./{config.ah_config.get('SCREENSHOT_NAME')}", "rb") as f:
        bys = f.read()
        bys_ = bys.replace(b"\r\n",b"\n")  # 二进制流中的"\r\n" 替换为"\n"
  with open(f"./{config.ah_config.get('SCREENSHOT_NAME')}", 'wb') as file:
    file.write(bys_)
    
def check_app_running(targetApp):
  cmd = [config.ah_config["ADB_PATH"], '-s', config.ah_config["EMULATOR_IP"], 'shell', 'dumpsys window windows | grep -E  "mCurrentFocus"']
  output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
  return targetApp in output

def open_app(targetApp):
  subprocess_run([config.ah_config["ADB_PATH"], '-s', config.ah_config["EMULATOR_IP"], 'shell', 'am', 'start', targetApp])
  
def click_on_screen(x, y):
    """Click on the given coordinates."""
    subprocess_run([config.ah_config["ADB_PATH"], "-s", config.ah_config["EMULATOR_IP"], "shell", "input", "tap", str(int(x)), str(int(y))])

def swiper_on_screen(startx, starty, endx, endy, duration = 500):
   subprocess_run([config.ah_config["ADB_PATH"], "-s", config.ah_config["EMULATOR_IP"], "shell", "input", "swipe", str(int(startx)), str(int(starty)), str(int(endx)), str(int(endy)), str(int(duration))])