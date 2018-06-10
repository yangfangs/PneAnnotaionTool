import os
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.filedialog import askopenfile
import pandas as pd

from anntool import AnnoTool


class Application(Frame):  # 从Frame派生出Application类，它是所有widget的父容器
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack()  # 将widget加入到父容器中并实现布局
        self.createWidgets()
        self.foo = None
        self.file_path = None
        self.read_coord = None

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hi, Welcome to use Annotation tool ')  # 创建一个标签显示内容到窗口
        self.helloLabel.pack()

        self.quitButton = Button(self, text='Choose file', command=self.selectPath)
        self.quitButton.pack()

        self.txt = Text(self, height=1)
        self.txt.pack()

        self.starButton = Button(self, text='Start', command=self.startAnno)
        self.starButton.pack(side=LEFT)

        self.clearButton = Button(self, text='Clear', command=self.clearText)
        self.clearButton.pack(side=RIGHT)

        self.saveButton = Button(self, text='Save', command=self.save)
        self.saveButton.pack()


    def hello(self):
        messagebox.showinfo('Message', 'hello,%s' % self.file_path)  # 显示输出

    def save(self):
        self.foo.save_img()
        self.foo.world_coordinate()
        df_anno = pd.DataFrame(self.foo.w_coordinate, columns=["coordX", "coordY", "coordZ"])
        df_anno.insert(0,'seriesuid',self.foo.seriesuid)
        df_anno.to_csv(self.foo.pic_path + ".csv",index=False)
        df_coor = pd.DataFrame(self.foo.coordinate, columns=["coordX", "coordY"])
        df_coor.insert(0, 'seriesuid', self.foo.seriesuid)
        df_coor.to_csv(self.foo.pic_path + "_coord.csv", index=False)
        messagebox.showinfo('Message', 'Already Saved!')

    def selectPath(self):
        path_ = askopenfile()
        if path_ != None:
            path_name = path_.name
            self.txt.insert(1.0,path_name)
            # path.set(path_)
            self.file_path = path_name
        else:
            pass

    def clearText(self):
        self.name = None
        self.txt.delete(0.0, END)

    def startAnno(self):

        if self.file_path != None:
            foo = AnnoTool(self.file_path)
            self.foo = foo
            self.read_coord_data()
            # print('haha',self.read_coord)
            if self.read_coord:
                self.foo.set_coord(self.read_coord)
            self.foo.get_pixels_hu()
            self.foo.star_img()

        else:
            messagebox.showinfo('Message', "Not found DICOM file path. Please choose file!")

    def read_coord_data(self):
        """ read the coord information if dir have the data"""
        coord_path = self.foo.pic_path + "_coord.csv"

        if os.path.isfile(coord_path):
            df = pd.read_csv(coord_path)
            coord = [df.coordX.tolist(), df.coordY.tolist()]
            self.read_coord = coord
        else:
            self.read_coord = False
if __name__ == '__main__':

    app = Application()
    app.master.title("Annotation tool")  # 窗口标题
    app.mainloop()  # 主消息循环</span>