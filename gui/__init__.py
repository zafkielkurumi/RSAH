if __name__ in {"__main__", "__mp_main__"}:
    
  try:
    from tkinter import * 
    from modules.config import AHConfig

    root = Tk()  
    AHConfig()

    saveBtn = Button(root)

    li     = ['C','python','php','html','SQL','java']
    movie  = ['CSS','jQuery','Bootstrap']
    listb  = Listbox(root)          #  创建两个列表组件
    listb2 = Listbox(root)
    for item in li:                 # 第一个小部件插入数据
        listb.insert(0,item)
    
    for item in movie:              # 第二个小部件插入数据
        listb2.insert(0,item)
    
    listb.pack()                    # 将小部件放置到主窗口中
    listb2.pack()

    root.mainloop()                 # 进入消息循环
  except Exception as e:
    import traceback
    traceback.print_exc()
    input("按任意键退出")