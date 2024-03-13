import zipfile
import shutil
import os
import subprocess
from pathlib import Path
import nicegui


def package_copyfile(src, dst):
    try:
        shutil.copyfile(src, dst)
        print(f"{dst}已拷贝")
    except FileExistsError as e:
        print(f"{dst}已存在!")

def package_copyfolder(src, dst):
    try:
        # 拷贝文件夹
        shutil.copytree(src, dst)
        print(f"{dst}文件夹已拷贝")
    except FileExistsError as e:
        print(f"{dst}文件夹已存在!")

ahcmd = [
    'pyinstaller',
    'main.py',
    '-n', 'RSAH',
    "-y"
]
subprocess.call(ahcmd)

guicmd = [
    'pyinstaller',
    'gui.py',
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui',
    "-y"
]
subprocess.call(guicmd)

# 遍历./dist/jsoneditor/_internal里的所有文件夹和文件，将它们拷贝到./dist/BAAH/_internal，如果已存在则跳过
for dirpath, dirnames, filenames in os.walk(os.path.join('./dist', 'gui', '_internal')):
    for filename in filenames:
        package_copyfile(os.path.join(dirpath, filename), os.path.join('./dist/RSAH/_internal', filename))
    for dirname in dirnames:
        package_copyfolder(os.path.join(dirpath, dirname), os.path.join('./dist/RSAH/_internal', dirname))
    # 走一层就终止
    break

package_copyfolder('./Assets','./dist/RSAH/Assets')

package_copyfile("./dist/gui/gui.exe", "./dist/RSAH/gui.exe")
package_copyfolder('./tools','./dist/RSAH/tools')
