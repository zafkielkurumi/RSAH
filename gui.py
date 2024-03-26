

if __name__ in {"__main__", "__mp_main__"}:
    
  try:
      import os
      from nicegui import ui, native
      from modules.config import AHConfig, config
      from typing import List
      from modules.RSAH import rsah_start
      import _thread

 
      taskList: List = config.ah_config["task"] 


      def save_config_notify():
        config.save_config()
        ui.notify("保存成功", position="top")

      def save_config_run():
         config.save_config()
         ui.notify("开始执行", position="top")
         # os.system(f'start RSAH.exe')
         # rsah_start()
         # ui.
         _thread.start_new_thread(rsah_start, ())

      def change_task(task):
        def change():
          task["run"] = not task["run"]
        return change

      with ui.row():
         ui.label('模拟器路径:')
         ui.input().bind_value(config.ah_config, "EMULATOR_PATH")
      with ui.row():
         ui.label('ADB路径:')
         ui.input().bind_value(config.ah_config, "ADB_PATH")
      with ui.row():
         ui.label('游戏包名:')
         ui.input().bind_value(config.ah_config, "APP_NAME")
      with ui.row():
         ui.label('模拟器运行的端口号:')
         ui.input().bind_value(config.ah_config, "EMULATOR_IP")

      with ui.column():
         for key in taskList:
            task = taskList[key]
            v = ui.checkbox(key, value=task["run"], on_change=change_task(task))
            with ui.column().bind_visibility(v, "value"):
               for p in task["params"]:
                  v = ui.checkbox(task["params"][p]["desc"], value=task["params"][p]["run"], on_change=change_task(task["params"][p]))

      ui.button("保存", on_click=save_config_notify)
      ui.button("保存并运行", on_click=save_config_run)
      ui.run(native=True, window_size=(1280,720), title="雷索纳斯", language="zh-cn", reload=False, port=native.find_open_port())    
  except Exception as e:
    import traceback
    traceback.print_exc()
    input("按任意键退出")