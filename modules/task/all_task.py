from modules.task import login, ContinuedTask
from modules.config import AHConfig, config


task_dict= {
    "登录游戏":[login,{}],
    "持续任务":[ContinuedTask,{'speed':True, "auto_battle": True}],
}

class AllTask:
  taskpool = []
  def __init__(self) -> None:
    self.parse_task()

  def parse_task(self):
    self.taskpool = []
    

  
