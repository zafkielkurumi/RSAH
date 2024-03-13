import sys
from RSAH import connect_adb, start_app, start_emulator
from modules.task import  ContinuedTask, Login
from modules.utils.log import logging_print
from modules.utils.opencv import match_image
from modules.utils.game import btn_pic, mathGame
from Assets.btn.Button_Name import ButtonName



if __name__ in ["__main__", "__mp_main__"]:
  try:

    from modules.config import AHConfig, config
    if len(sys.argv) > 1:
      config.parseConfig(sys.argv[1])
    else:
      config.parseConfig("config.json")
    logging_print("开始任务")
    
    start_emulator()
    connect_adb()
    start_app()
    Login().run()
    ContinuedTask().run()
  except Exception as e:
    import traceback
    traceback.print_exc()
    input("按回车键继续:")