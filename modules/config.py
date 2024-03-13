
import json
import os

from modules.utils.log import logging_print
class AHConfig:
  file_name = "config.json"
  file_dir = "./Assets/config"
  ah_config = {}
  file_path = ""
  def __init__(self):
    self.current_dir = os.getcwd()
    self.parseConfig(self.file_name)
  
  def parseConfig(self, file_name):
    self.file_path = os.path.join(self.current_dir, self.file_dir, file_name)
    self.ah_config = self.readConfig()


  def readConfig(self):
    logging_print("读取配置")
    try:
      with open(self.file_path, 'r', encoding="utf8") as f:
        config = json.load(f)
        logging_print('读取配置成功')
        return config
    except FileNotFoundError as e:
      logging_print("读取配置失败")
      raise Exception(f'读取文件时发生错误，请检查文件: {str(e)}')
  
  def save_config(self):
      with open(self.file_path, 'w', encoding="utf8") as file:
        json.dump(self.ah_config, file, indent=4, ensure_ascii=False)
    
config = AHConfig()