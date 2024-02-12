from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from string import ascii_letters
from time import strftime, localtime
import shutil
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 250)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        MainWindow.setMaximumSize(QtCore.QSize(500, 250))
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 466, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_name = QtWidgets.QVBoxLayout()
        self.verticalLayout_name.setObjectName("verticalLayout_name")
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "padding-left: auto;\n"
                                      "padding-right: auto;")
        self.name_label.setObjectName("name_label")
        self.verticalLayout_name.addWidget(self.name_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.name_lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                         "border: 1px solid rgb(127, 127, 127);\n"
                                         "color: rgb(255, 255, 255);")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout.addWidget(self.name_lineEdit)
        self.name_btn = QtWidgets.QPushButton(self.widget)
        self.name_btn.setMinimumSize(QtCore.QSize(65, 30))
        self.name_btn.setMaximumSize(QtCore.QSize(65, 30))
        self.name_btn.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                    "color: rgb(255, 255, 255);")
        self.name_btn.setObjectName("name_btn")
        self.horizontalLayout.addWidget(self.name_btn)
        self.verticalLayout_name.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_name)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_name_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_name_2.setObjectName("verticalLayout_name_2")
        self.dir_label = QtWidgets.QLabel(self.widget)
        self.dir_label.setStyleSheet("font: 75 16pt \"Times New Roman\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "padding-left: auto;\n"
                                     "padding-right: auto;")
        self.dir_label.setObjectName("dir_label")
        self.verticalLayout_name_2.addWidget(self.dir_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dir_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.dir_lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                        "border: 1px solid rgb(127, 127, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.dir_lineEdit.setObjectName("dir_lineEdit")
        self.horizontalLayout_2.addWidget(self.dir_lineEdit)
        self.dir_btn = QtWidgets.QPushButton(self.widget)
        self.dir_btn.setMinimumSize(QtCore.QSize(65, 30))
        self.dir_btn.setMaximumSize(QtCore.QSize(65, 30))
        self.dir_btn.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "color: rgb(255, 255, 255);")
        self.dir_btn.setObjectName("dir_btn")
        self.horizontalLayout_2.addWidget(self.dir_btn)
        self.verticalLayout_name_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_name_2)
        self.create_backup_btn = QtWidgets.QPushButton(self.widget)
        self.create_backup_btn.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                             "color: rgb(255, 255, 255);")
        self.create_backup_btn.setObjectName("create_backup_btn")
        self.verticalLayout.addWidget(self.create_backup_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        ##################################################
        self.rosa_path = r"C:\Users\maxim\Desktop\rosa\root\file1.txt"
        self.save_path_default = str(os.getcwd()) + r'\backups'
        self.save_path = self.save_path_default
        self.dir_lineEdit.setText(self.save_path)

        self.name_btn.clicked.connect(lambda: self.name_lineEdit.setText(''))
        self.dir_btn.clicked.connect(self.select_dir)
        self.create_backup_btn.clicked.connect(self.create_files)
        ##################################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_label.setText(_translate("MainWindow", "Задать имя резервной копии"))
        self.name_btn.setText(_translate("MainWindow", "Очистить"))
        self.dir_label.setText(_translate("MainWindow", "Выбрать путь сохранения"))
        self.dir_btn.setText(_translate("MainWindow", "Выбрать"))
        self.create_backup_btn.setText(_translate("MainWindow", "Создать копию"))


    def set_backup_name(self, date_time_name):
        name = False
        if len(self.name_lineEdit.text()) != 0:
            status = self.check_correct_name()
            if status == False:
                self.get_message()
            else:
                name = self.name_lineEdit.text()
        else:
            name = 'backup_' + date_time_name  #backup_24-02-12_21-52-47
        return name


    def create_log_message(self, name, time, size):
        log = '#' * 30 + '\n'
        log += f'Резервная копия: {name}\n'
        log += f"Была создана {time}\n"
        log += f"С размером {size} байт\n"
        log += '#' * 30 + '\n'
        return log


    def check_correct_name(self):
        text = self.name_lineEdit.text()
        if len(text) == 0:
            return True
        if (not text[0].isalpha()):
            return False
        for char in text:
            if char in '!@#№;%:?*=+}]{[./':
                return False
        return True

    def get_message(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение об ошибке")
        error.setText("Некорректно введенное имя!")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def get_time_creating(self):
        time_date = strftime('%y-%m-%d', localtime())  # 24-02-12
        time_log = strftime('%H:%M:%S', localtime())  # 21:26:58
        time_name = time_log.replace(':', '-')
        date_time_log = time_date + ' ' + time_log  # 24-02-12 21:35:14
        date_time_name = time_date + '_' + time_name  # 24-02-12_21-32-40
        return {'date_time_name': date_time_name, 'date_time_log': date_time_log}

    def select_dir(self):
        dir_path = QFileDialog().getExistingDirectory()
        self.save_path = dir_path if dir_path else self.save_path_default
        self.dir_lineEdit.setText(self.save_path)

    def check_default_dir(self):
        if not os.path.exists(self.save_path_default):
            os.mkdir(self.save_path_default)

    def create_files(self):
        time_ = self.get_time_creating()
        if self.set_backup_name(time_['date_time_name']):
            if self.save_path == self.save_path_default:
                self.check_default_dir()
            file_path = self.save_path + '/' + self.set_backup_name(time_['date_time_name']) + '.txt'
            log_path = self.save_path + '/' + 'logs' + '.txt'
            with open(file_path, 'w', encoding="utf-8"):
                pass
            shutil.copyfile(self.rosa_path, file_path)
            name = self.set_backup_name(time_['date_time_name'])
            time_log = time_['date_time_log']
            size = str(os.path.getsize(file_path))
            with open(log_path, 'a', encoding="utf-8") as f:
                f.write(self.create_log_message(name, time_log, size))





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
