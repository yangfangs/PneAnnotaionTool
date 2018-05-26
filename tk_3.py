from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.filedialog import askopenfile

from anntool import load_scan, get_pixels_hu, star_img


class Application(Frame):  # 从Frame派生出Application类，它是所有widget的父容器
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack()  # 将widget加入到父容器中并实现布局
        self.createWidgets()

        self.file_path = None
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hi')  # 创建一个标签显示内容到窗口
        self.helloLabel.pack()

        self.quitButton = Button(self, text='Choose file', command=self.selectPath)
        self.quitButton.pack()

        self.txt = Text(self, height=1)
        self.txt.pack()

        self.starButton = Button(self, text='Start', command=self.startAnno)
        self.starButton.pack(side=LEFT)

        self.clearButton = Button(self, text='Clear', command=self.clearText)
        self.clearButton.pack(side=RIGHT)

        self.fileButton = Button(self, text='Save', command=self.quit)
        self.fileButton.pack()


    def hello(self):
        messagebox.showinfo('Message', 'hello,%s' % self.file_path)  # 显示输出

    def selectPath(self):
        path_ = askopenfile()
        path_name = path_.name
        self.txt.insert(1.0,path_name)
        # path.set(path_)
        self.file_path = path_name

    def clearText(self):
        self.name = None
        self.txt.delete(0.0, END)

    def startAnno(self):
        if self.file_path != None:
            first_patient = load_scan(self.file_path)
            first_patient_pixels = get_pixels_hu(first_patient)
            star_img(first_patient_pixels)
        else:
            messagebox.showinfo('Message', "Not found DICOM file path. Please choose file!")

if __name__ == '__main__':

    app = Application()
    app.master.title("Annotation")  # 窗口标题
    app.mainloop()  # 主消息循环</span>