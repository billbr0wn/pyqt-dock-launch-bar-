#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.uic import *

import os
import sys
import subprocess
import launch_variables

#-------------------------------------------------
    
__author__ = '__Bill__'


class _Window_(QMainWindow):
    """
    -------------------(_Window_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)


        print(os.name)
        print(os.getcwd()) 

        self.frame =  str("""QFrame {background: black py_i.png);
                            background-repeat: repeat-y;
                            background-position: left;}""")

##        command_1_text = ('')
##        icon_1_text = ('')
##
##        command_2_text = ('')
##        icon_2_text = ('')
##
##        command_3_text = ('')
##        icon_3_text = ('')
##
##        command_4_text = ('')
##        icon_4_text = ('')
##
##        command_5_text = ('')
##        icon_5_text = ('')
##
##        command_6_text = ('')
##        icon_6_text = ('')


        
#--------------- variables from py inmport -----------o

        
        self.launch_variables = launch_variables
        
        self.icon_1_text = launch_variables.icon_1_text
        print('icon_1_text = ', self.icon_1_text)
        self.command_1_text = launch_variables.command_1_text
        print('command_1_text = ', self.command_1_text)

        self.icon_2_text = launch_variables.icon_2_text
        self.command_2_text = launch_variables.command_2_text
##
            
        self.icon_3_text = launch_variables.icon_3_text
        self.command_3_text = launch_variables.command_3_text
       

        self.icon_4_text = launch_variables.icon_4_text
        self.command_4_text = launch_variables.command_4_text
       

        self.icon_5_text = launch_variables.icon_5_text
        self.command_5_text = launch_variables.command_5_text

            
        self.icon_6_text = launch_variables.icon_6_text
        self.command_6_text = launch_variables.command_6_text


        self.mime = QMimeData()


        self.setMouseTracking(True)
##        self.grabMouse()

        self.QWidget = QWidget



#------------------- Create menu ---------------------o
        
        self.menu = QMenu()
        
        self.action_1 = QAction("Exit")#<----menu text
        self.action_1.triggered.connect(self.exit__)
        self.action_2 = QAction("run_command")


        self.menu.addAction(self.action_1)
##        self.menu.addAction(self.action_2)
##        self.menu.addAction(self.action_3)
        


#---------------------- Create the tray icon ------------o

        self.icon = QIcon("py_i.png")#<----picture for icon
     
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        self.tray.setContextMenu(self.menu)


#<--------------- set Main Picture ----------------->#

        #main_picture      = QPixmap ('//home//bill//Launch_bar//bg3.png')#<------pic and folder 675 x 1010 px
        main_picture      = QPixmap ('bg3.png')
        self.main_picture = main_picture
        main_label        = QLabel  (self)
        self.main_label = main_label#<----------must link self. to label for import from module
        main_label.setPixmap    (main_picture)
        main_label.move         (0, 0)
        main_label.raise_()
        self.main_label.adjustSize()
        

#-------------------- Create drop shadow for widget --------------o

        #self.task = QWinTaskbarProgress()
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(1)
        self.shadow.setXOffset(3)
        self.shadow.setXOffset(3)


#------------ call functions ----------o
        
        self.slots__()   
        self.initGUI()



    def slots__(self):

        #launches command
        self.button_1 = QPushButton(self)


        self.button_1.setIcon(QIcon(self.icon_1_text))
        self.button_1.setIconSize (QSize(50,50))
        self.button_1.setGeometry(QRect(55,55, 50,50))
        self.button_1.move(20,25)
        self.button_1.sizeHint()

        self.button_1.clicked.connect(self.button_1__)
        self.button_1.raise_()
        self.button_1.setFlat(True)
        self.button_1.show()
        
#---------------
        
        self.button_2 = QPushButton(self)

        self.button_2.setStyleSheet ("""background-color:
                                    rgba(0,0,0, 0)""")
        self.button_2.setIcon(QIcon(self.icon_2_text))
        self.button_2.setIconSize (QSize(50,50))
        self.button_2.setGeometry(QRect(55,55, 50,50))
        self.button_2.move(20,125)

        self.button_2.clicked.connect(self.button_2__)
        self.button_2.raise_()
        self.button_2.setFlat(True)
        self.button_2.show()

#---------------
        
        self.button_3 = QPushButton(self)

        self.button_3.setStyleSheet ("""background-color:
                                    rgba(0,0,0, 0)""")
        self.button_3.setIcon(QIcon(self.icon_3_text))
        self.button_3.setIconSize (QSize(50,50))
        self.button_3.setGeometry(QRect(55,55, 50,50))
        self.button_3.move(20,225)

        self.button_3.clicked.connect(self.button_3__)
        self.button_3.raise_()
        self.button_3.setFlat(True)
        self.button_3.show()


#---------------
        
        self.button_4 = QPushButton(self)

        self.button_4.setStyleSheet ("""background-color:
                                    rgba(0,0,0, 0)""")
        self.button_4.setIcon(QIcon(self.icon_4_text))
        self.button_4.setIconSize (QSize(50,50))
        self.button_4.setGeometry(QRect(55,55, 50,50))
        self.button_4.move(20,325)

        self.button_4.clicked.connect(self.button_4__)
        self.button_4.raise_()
        self.button_4.setFlat(True)
        self.button_4.show()

#---------------
        
        self.button_5 = QPushButton(self)

        self.button_5.setStyleSheet ("""background-color:
                                    rgba(0,0,0, 0)""")
        self.button_5.setIcon(QIcon(self.icon_5_text))
        self.button_5.setIconSize (QSize(50,50))
        self.button_5.setGeometry(QRect(55,55, 50,50))
        self.button_5.move(20,425)

        self.button_5.clicked.connect(self.button_5__)
        self.button_5.raise_()
        self.button_5.setFlat(True)
        self.button_5.show()


#---------------
        
        self.button_6 = QPushButton(self)

        self.button_6.setStyleSheet ("""background-color:
                                    rgba(0,0,0, 0)""")
        self.button_6.setIcon(QIcon(self.icon_6_text))
        self.button_6.setIconSize (QSize(50,50))
        self.button_6.setGeometry(QRect(55,55, 50,50))
        self.button_6.move(20,525)

        self.button_6.clicked.connect(self.button_6__)
        self.button_6.raise_()
        self.button_6.setFlat(True)
        self.button_6.show()



    def mousePressEvent(self, event):
        self.oPos = event.globalPos()
        
##        if event.buttons() == Qt.NoButton:
##            self.raise_()

        if event.buttons() == Qt.RightButton:
            self.right_click__()
        else:
            pass




##    def left_click__(self):
##        print('left')
        
    def right_click__(self):
        print('right')
        self.dnd_window2__()



    def dnd_window2__(self):
        print('dnd_window2__')

        self.window_2 = QWidget()
        self.window_2.setAcceptDrops(True)


#------------------window2 text edit ----------------o

        self.edit_1_command = QLineEdit(self.command_1_text, self)
        self.edit_1_command.setDragEnabled(True)
        self.edit_1_command.resize(550, 50)
        self.edit_1_command.move(0, 5)
        self.edit_1_command.show()


        self.edit_1_icon = QLineEdit(self.icon_1_text, self)
        self.edit_1_icon.setDragEnabled(True)
        self.edit_1_icon.resize(550, 50)
        self.edit_1_icon.move(0, 5)
        self.edit_1_icon.show()






#-----------

        self.edit_2_command = QLineEdit(self.command_2_text, self)
        self.edit_2_command.setDragEnabled(True)
        self.edit_2_command.resize(550, 50)
        self.edit_2_command.move(0, 5)
        self.edit_2_command.show()


        self.edit_2_icon = QLineEdit(self.icon_2_text, self)
        self.edit_2_icon.setDragEnabled(True)
        self.edit_2_icon.resize(550, 50)
        self.edit_2_icon.move(0, 5)
        self.edit_2_icon.show()


#-------
        
        self.edit_3_command = QLineEdit(self.command_3_text, self)
        self.edit_3_command.setDragEnabled(True)
        self.edit_3_command.resize(550, 50)
        self.edit_3_command.move(0, 5)
        self.edit_3_command.show()


        self.edit_3_icon = QLineEdit(self.icon_3_text, self)
        self.edit_3_icon.setDragEnabled(True)
        self.edit_3_icon.resize(550, 50)
        self.edit_3_icon.move(0, 5)
        self.edit_3_icon.show()
        
#-------
        
        self.edit_4_command = QLineEdit(self.command_4_text, self)
        self.edit_4_command.setDragEnabled(True)
        self.edit_4_command.resize(550, 50)
        self.edit_4_command.move(0, 5)
        self.edit_4_command.show()


        self.edit_4_icon = QLineEdit(self.icon_4_text, self)
        self.edit_4_icon.setDragEnabled(True)
        self.edit_4_icon.resize(550, 50)
        self.edit_4_icon.move(0, 5)
        self.edit_4_icon.show()
        
#-------
        
        self.edit_5_command = QLineEdit(self.command_5_text, self)
        self.edit_5_command.setDragEnabled(True)
        self.edit_5_command.resize(550, 50)
        self.edit_5_command.move(0, 5)
        self.edit_5_command.show()


        self.edit_5_icon = QLineEdit(self.icon_5_text, self)
        self.edit_5_icon.setDragEnabled(True)
        self.edit_5_icon.resize(550, 50)
        self.edit_5_icon.move(0, 5)
        self.edit_5_icon.show()


#-------
        
        self.edit_6_command = QLineEdit(self.command_6_text, self)
        self.edit_6_command.setDragEnabled(True)
        self.edit_6_command.resize(550, 50)
        self.edit_6_command.move(0, 5)
        self.edit_6_command.show()


        self.edit_6_icon = QLineEdit(self.icon_6_text, self)
        self.edit_6_icon.setDragEnabled(True)
        self.edit_6_icon.resize(550, 50)
        self.edit_6_icon.move(0, 5)
        self.edit_6_icon.show()



#---------------text label for widget-------------o

        
        label_1 = QLabel  (self)
        self.label_1 = label_1#<----------must link self to label for import from module
        self.label_1.setAlignment(Qt.AlignLeft)
        self.label_1.setGeometry(25,25,25,25)
        label_1.move(0, 0)
        self.label_1.raise_()
        self.label_1.setText('slot 1')
        label_1.adjustSize()


        label_2 = QLabel  (self)
        self.label_2 = label_2#<----------must link self to label for import from module
        self.label_2.setAlignment(Qt.AlignLeft)
        self.label_2.setGeometry(25,25,25,25)
        label_2.move(0, 0)
        self.label_2.raise_()
        self.label_2.setText('slot 2')
        label_2.adjustSize()


        
        label_3 = QLabel  (self)
        self.label_3 = label_3#<----------must link self to label for import from module
        self.label_3.setAlignment(Qt.AlignLeft)
        self.label_3.setGeometry(25,25,25,25)
        label_3.move(0, 0)
        self.label_3.raise_()
        self.label_3.setText('slot 3')
        label_3.adjustSize()
##

        
        label_4 = QLabel  (self)
        self.label_4 = label_4#<----------must link self to label for import from module
        self.label_4.setAlignment(Qt.AlignLeft)
        self.label_4.setGeometry(25,25,25,25)
        label_4.move(0, 0)
        self.label_4.raise_()
        self.label_4.setText('slot 4')
        label_4.adjustSize()

        label_5 = QLabel  (self)
        self.label_5 = label_5#<----------must link self to label for import from module
        self.label_5.setAlignment(Qt.AlignLeft)
        self.label_5.setGeometry(25,25,25,25)
        label_5.move(0, 0)
        self.label_5.raise_()
        self.label_5.setText('slot 5')
        label_5.adjustSize()


       
        label_6 = QLabel  (self)
        self.label_6 = label_6#<----------must link self to label for import from module
        self.label_6.setAlignment(Qt.AlignLeft)
        self.label_6.setGeometry(25,25,25,25)
        label_6.move(0, 0)
        self.label_6.raise_()
        self.label_6.setText('slot 6')
        label_6.adjustSize()



#---------------Widget layout--------------o
        
        layout_v = QVBoxLayout(self)
        self.layout_v = layout_v
        self.window_2.setLayout(layout_v);
        self.setAcceptDrops(True)
        
##        layout_v.addWidget(self.label_1_command);
##        layout_v.addWidget(self.label_1_icon);
##




#-------------------icon/command buttons------------o


        self.button_command = QPushButton(self)

        self.button_command.setStyleSheet ("""background-color:
                                    rgba(150,150,150, 50)""")
        self.button_command.setText('save')
        self.button_command.setGeometry(QRect(55,55, 50,50))
        self.button_command.move(0,0)
        self.button_command.sizeHint()

        self.button_command.clicked.connect(self.set_icon_command__)
        self.button_command.clicked.connect(self.win2_exit__)
        self.button_command.raise_()
##        self.button_command.setFlat(True)
        self.button_command.show()
        
###---


#<--------------- set Horozontal lines ----------------->#

        self.line1 = QFrame (self)
        self.line1.setGeometry    (QRect(1475,400, 0,0))
        self.line1.setFrameShape  (QFrame.HLine)
        self.line1.setFrameShadow (QFrame.Raised)
        self.line1.setObjectName  ("h line 1")

        self.line2 = QFrame (self)
        self.line2.setGeometry    (QRect(1475,400, 0,0))
        self.line2.setFrameShape  (QFrame.HLine)
        self.line2.setFrameShadow (QFrame.Raised)
        self.line2.setObjectName  ("h line 2")

        self.line3 = QFrame (self)
        self.line3.setGeometry    (QRect(1475,400, 0,0))
        self.line3.setFrameShape  (QFrame.HLine)
        self.line3.setFrameShadow (QFrame.Raised)
        self.line3.setObjectName  ("h line 3")

        self.line4 = QFrame (self)
        self.line4.setGeometry    (QRect(1475,400, 0,0))
        self.line4.setFrameShape  (QFrame.HLine)
        self.line4.setFrameShadow (QFrame.Raised)
        self.line4.setObjectName  ("h line 4")

        self.line5 = QFrame (self)
        self.line5.setGeometry    (QRect(1475,400, 0,0))
        self.line5.setFrameShape  (QFrame.HLine)
        self.line5.setFrameShadow (QFrame.Raised)
        self.line5.setObjectName  ("h line 5")

        self.line6 = QFrame (self)
        self.line6.setGeometry    (QRect(1475,400, 0,0))
        self.line6.setFrameShape  (QFrame.HLine)
        self.line6.setFrameShadow (QFrame.Raised)
        self.line6.setObjectName  ("h line 6")

        
#-----
        layout_v.addWidget(self.label_1);
        layout_v.addWidget(self.edit_1_command);
        layout_v.addWidget(self.edit_1_icon);
        self.layout_v.addWidget(self.line1)

#-----
        layout_v.addWidget(self.label_2);
        layout_v.addWidget(self.edit_2_command);
        layout_v.addWidget(self.edit_2_icon);
        self.layout_v.addWidget(self.line2)

#-----

        layout_v.addWidget(self.label_3);
        layout_v.addWidget(self.edit_3_command);
        layout_v.addWidget(self.edit_3_icon);
        self.layout_v.addWidget(self.line3)

#-----

        layout_v.addWidget(self.label_4);        
        layout_v.addWidget(self.edit_4_command);
        layout_v.addWidget(self.edit_4_icon);
        self.layout_v.addWidget(self.line4)

#-----
        
        layout_v.addWidget(self.label_5);        
        layout_v.addWidget(self.edit_5_command);
        layout_v.addWidget(self.edit_5_icon);
        self.layout_v.addWidget(self.line5)

#-----
        
        layout_v.addWidget(self.label_6);        
        layout_v.addWidget(self.edit_6_command);
        layout_v.addWidget(self.edit_6_icon);
        self.layout_v.addWidget(self.line6)

        

#----------------horozontal layout--------------o
        
        self.layout_h = QHBoxLayout(self)
        self.window_2.setLayout(self.layout_h)
        self.layout_h.addStretch(1)
        
        self.layout_v.addLayout(self.layout_h)#<---add to previous layout
        
        
        self.layout_h.addWidget(self.button_command)
##        self.layout_h.addWidget(self.button_icon)



#---------------widget setup----------------o
        
        self.window_2.move(1310,75)
        self.window_2.resize(600, 200)
        self.window_2.setWindowTitle('Window_2')
##        self.window_2.setWindowFlags(Qt.FramelessWindowHint)
        self.window_2.raise_()
        self.window_2.show()





    def set_icon_command__(self):
        print('set_icon_command__')
        self.command_1_text = self.edit_1_command.text()
        self.command_2_text = self.edit_2_command.text()
        self.command_3_text = self.edit_3_command.text()
        self.command_4_text = self.edit_4_command.text()
        self.command_5_text = self.edit_5_command.text()
        self.command_6_text = self.edit_6_command.text()
##        print('command_6: ', self.command_6_text)






        self.icon_1_text = self.edit_1_icon.text()
#<-----strip text from string
        self.icon_1_text = self.icon_1_text.replace("file://", "")
##        print('self.icon_1_text = ', self.icon_1_text)
           
        self.icon_2_text = self.edit_2_icon.text()
        self.icon_2_text = self.icon_2_text.replace("file://", "")
            
        self.icon_3_text = self.edit_3_icon.text()
        self.icon_3_text = self.icon_3_text.replace("file://", "")

        self.icon_4_text = self.edit_4_icon.text()
        self.icon_4_text = self.icon_4_text.replace("file://", "")  

        self.icon_5_text = self.edit_5_icon.text()
        self.icon_5_text = self.icon_5_text.replace("file://", "")
            
        self.icon_6_text = self.edit_6_icon.text()
        self.icon_6_text = self.icon_6_text.replace("file://", "")








        

#------------
        
        file = open("launch_variables.py", "w")
        file.write("\r\n" + "command_1_text = str('{}') ".format(self.command_1_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_1_text = str('{}') ".format(self.icon_1_text));
        file.close()



#-----
        
        file = open("launch_variables.py", "a")
        file.write("\r\n" + "command_2_text = str('{}') ".format(self.command_2_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_2_text = str('{}') ".format(self.icon_2_text));
        file.close()

#-----
            

        file = open("launch_variables.py", "a")
        file.write("\r\n" + "command_3_text = str('{}') ".format(self.command_3_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_3_text = str('{}') ".format(self.icon_3_text));
        file.close()

#-----
            

        file = open("launch_variables.py", "a")
        file.write("\r\n" + "command_4_text = str('{}') ".format(self.command_4_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_4_text = str('{}') ".format(self.icon_4_text));
        file.close()

            
#-----

        file = open("launch_variables.py", "a")
        file.write("\r\n" + "command_5_text = str('{}') ".format(self.command_5_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_5_text = str('{}') ".format(self.icon_5_text));
        file.close()

#-----
            

        file = open("launch_variables.py", "a")
        file.write("\r\n" + "command_6_text = str('{}') ".format(self.command_6_text));
        file.close()


        file = open("launch_variables.py", "a")
        file.write("\r\n" + "icon_6_text = str('{}') ".format(self.icon_6_text));
        file.close()


#-----

        self.set_icons__()


    def set_icons__(self):
        #print('set_icons__')
        #print('self.icon_1_text', self.icon_3_text)
        self.button_1.setIcon(QIcon(self.icon_1_text))
        self.button_2.setIcon(QIcon(self.icon_2_text))
        self.button_3.setIcon(QIcon(self.icon_3_text))
        self.button_4.setIcon(QIcon(self.icon_4_text))
        self.button_5.setIcon(QIcon(self.icon_5_text))
        self.button_6.setIcon(QIcon(self.icon_6_text))




    def button_1__(self):
        print('button_1__')
        self.process = QProcess()
        self.process.execute(self.command_1_text)
    def button_2__(self):
        print('button_2__')
        self.process = QProcess()
        self.process.start(self.command_2_text)
    def button_3__(self):
        print('button_3__')
        self.process = QProcess()
        self.process.start(self.command_3_text)
    def button_4__(self):
        print('button_4__')
        self.process = QProcess()
        self.process.start(self.command_4_text)
    def button_5__(self):
        print('button_5__')
        self.process = QProcess()
        self.process.start(self.command_5_text)
    def button_6__(self):
        print('button_6__')
        self.process = QProcess()
        self.process.start(self.command_6_text)

     
        
    def exit__(self):
        print('exit')
        exit()
    def win2_exit__(self):
        print('exit2')
        self.window_2.hide()
        

    def initGUI(self):

        self.setGraphicsEffect(self.shadow)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint
                            #| Qt.WindowStaysOnBottomHint
                              | Qt.Tool)
        self.setGeometry(700,500, 400,150)
        
        self.move(1650,275)
        self.resize(100, 600)
        self.setWindowTitle('My Window')
##        self.setQuitOnLastWindowClosed(False);
        self.show()
##        self.raise_()




        

if __name__ == '__main__':
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    _Win_ = _Window_()
    
    app.exec_()
    
