from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import shutil
from threading import Thread

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window_background = QtWidgets.QFrame(self.centralwidget)
        self.window_background.setGeometry(QtCore.QRect(-51, -1, 661, 421))
        self.window_background.setStyleSheet("background-color: rgb(106, 106, 106);\n"
"color: white;\n"
"font: 16pt \"Times New Roman\";")
        self.window_background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_background.setObjectName("window_background")
        self.widget = QtWidgets.QWidget(self.window_background)
        self.widget.setGeometry(QtCore.QRect(60, 10, 311, 181))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_directory = QtWidgets.QVBoxLayout()
        self.verticalLayout_directory.setObjectName("verticalLayout_directory")
        self.directory_label = QtWidgets.QLabel(self.widget)
        self.directory_label.setObjectName("directory_label")
        self.verticalLayout_directory.addWidget(self.directory_label)
        self.horizontalLayout_directory = QtWidgets.QHBoxLayout()
        self.horizontalLayout_directory.setObjectName("horizontalLayout_directory")
        self.directory_line = QtWidgets.QLineEdit(self.widget)
        self.directory_line.setObjectName("directory_line")
        self.horizontalLayout_directory.addWidget(self.directory_line)
        self.directory_btn = QtWidgets.QPushButton(self.widget)
        self.directory_btn.setObjectName("directory_btn")
        self.horizontalLayout_directory.addWidget(self.directory_btn)
        self.verticalLayout_directory.addLayout(self.horizontalLayout_directory)
        self.verticalLayout_2.addLayout(self.verticalLayout_directory)
        spacerItem = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_name = QtWidgets.QHBoxLayout()
        self.horizontalLayout_name.setObjectName("horizontalLayout_name")
        self.name_line = QtWidgets.QLineEdit(self.widget)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout_name.addWidget(self.name_line)
        self.name_btn = QtWidgets.QPushButton(self.widget)
        self.name_btn.setObjectName("name_btn")
        self.horizontalLayout_name.addWidget(self.name_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_name)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.create_btn = QtWidgets.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout_3.addWidget(self.create_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        ############################
        self.backup_file_path = r'C:\Users\maxim\Desktop\rosa\root\file1.txt'
        ############################
        self.directory_default = os.getcwd() + r'\backups'
        self.directory_path = self.directory_default
        self.directory_line.setText(self.directory_path)
        ############################
        self.directory_btn.clicked.connect(self.set_directory)
        self.name_btn.clicked.connect(lambda: self.name_line.setText(''))
        self.create_btn.clicked.connect(self.cl_to_create_copy)
        ################################



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.directory_label.setText(_translate("MainWindow", "Выбрать новую директорию"))
        self.directory_btn.setText(_translate("MainWindow", "Выбрать"))
        self.label.setText(_translate("MainWindow", "Задать имя резервной копии"))
        self.name_btn.setText(_translate("MainWindow", "Очистить"))
        self.create_btn.setText(_translate("MainWindow", "Создать копию"))




    def set_directory(self):
        directory_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.directory_path = directory_path if directory_path else os.getcwd() + r'\backups'
        self.directory_line.setText(str(self.directory_path))

    def get_name(self):
        date = time.strftime("%d-%m-%y_time_%H-%m-%S", time.localtime())
        if self.name_line.text():  # проверку
            return {'name': self.name_line.text(), 'date': date}
        return {'name': f'backup-{date}', 'date': date}


    def cl_to_create_copy(self):
        self.create_backup()


    def create_log(self, file_name, time_create, file_path, size):
        string = '#' * 20 + '\n'
        string += f'Резервная копия: {file_name}\n'
        string += f'Была сохранена: {time_create}\n'
        string += f'Размер копии: {size}байт\n'
        string += '#' * 20
        with open(file_path, 'w') as file:
            file.write(string)





    def create_backup(self):
        info = self.get_name()
        save_name = info['name'] + '.txt'
        save_path = self.directory_path + fr'\{save_name}'
        new_file = open(save_path, 'w')
        new_file.close()
        shutil.copyfile(self.backup_file_path, save_path)
        ###log
        log_path = self.directory_path + fr'\log-{save_name}'
        time_create = info['date']
        size = os.path.getsize(save_path)
        self.create_log(save_name, time_create, log_path, str(size))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
