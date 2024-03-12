from CCAH import connect_adb, start_app, start_emulator
from modules.task import  ContinuedTask, Login
from modules.utils.opencv import match_image
from modules.utils.game import btn_pic, mathGame
from Assets.btn.Button_Name import ButtonName


if __name__ in ["__main__", "__mp_main__"]:
  start_emulator()
  connect_adb()
  start_app()
  Login().run()
  ContinuedTask().run()