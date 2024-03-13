import os


if __name__ in {"__main__", "__mp_main__"}:
    
  try:
      from nicegui import ui, native
      from modules.config import AHConfig, config
      from typing import List
      print("参数：")
      task: List = config.ah_config["task"] 
      def include_str(str):
        return task.count(str) > 0

      def save_config_notify():
        config.save_config()
        ui.notify("保存成功", position="top")

      def save_config_run():
         config.save_config()
         ui.notify("开始执行", position="top")
         os.system(f'start RSAH.exe')

      def change_task(task_name):
        def change():
          if (include_str(task_name)):
             task.remove(task_name)
          else:
             task.append(task_name)
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
         ui.checkbox("登录游戏", value=include_str("登录游戏"), on_change=change_task("登录游戏"))
         v = ui.checkbox("持续任务", value=include_str("持续任务"), on_change=change_task("持续任务"))
         with ui.column().bind_visibility(v, "value"):
            ui.label("自动点击开始战斗和点击加速弹丸")
            ui.checkbox("自动开始战斗").bind_value(config.ah_config, "auto_battle")
            ui.checkbox("自动点击加速弹丸").bind_value(config.ah_config, "auto_speed")

      ui.button("保存", on_click=save_config_notify)
      ui.button("保存并运行", on_click=save_config_run)
      ui.run(native=True, window_size=(1280,720), title="雷索纳斯", language="zh-cn", reload=False, port=native.find_open_port())    
  except Exception as e:
    import traceback
    traceback.print_exc()
    input("按任意键退出")