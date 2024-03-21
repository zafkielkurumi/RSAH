import sys
from modules.RSAH import rsah_start
from modules.task import  ContinuedTask, Login, AllTask
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
    
    rsah_start()
  except Exception as e:
    import traceback
    traceback.print_exc()
    input("按回车键继续:")