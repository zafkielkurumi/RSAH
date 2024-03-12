from CCAH import connect_adb, start_app, start_emulator
from modules.utils.game import mathGame


if __name__=="__main__":
  start_emulator()
  connect_adb()
  start_app()
  print(mathGame("./Assets/TOWER/EMENY.png", showResult=True)) 