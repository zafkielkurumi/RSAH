from modules.task import Login, LoopTask, task, LoopEight, LoopNine
from modules.config import AHConfig, config
from modules.utils.log import logging_print


task_dict= {
    # "登录游戏":[Login,{}],
    "循环任务":[LoopTask,{}],
    # "循环85":[LoopEight,{}],
    # "循环九":[LoopNine,{}],
}

class AllTask:
  taskpool = []
  def __init__(self) -> None:
    self.parse_task()

  def parse_task(self):
    self.taskpool = []
    for task_name in config.ah_config["task"]:
      if( task_name in task_dict): 
        self.taskpool.append(task_dict[task_name][0](**task_dict[task_name][1]))

  def run(self):
    for task in self.taskpool:
      task.run()
    

  
