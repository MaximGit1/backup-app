from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import time
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 296)
        MainWindow.setMinimumSize(QtCore.QSize(434, 296))
        MainWindow.setMaximumSize(QtCore.QSize(434, 296))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(110, 20, 231, 21))
        self.main_label.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);")
        self.main_label.setObjectName("main_label")
        self.create_backup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_backup_btn.setGeometry(QtCore.QRect(150, 250, 123, 32))
        self.create_backup_btn.setMinimumSize(QtCore.QSize(123, 32))
        self.create_backup_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.create_backup_btn.setStyleSheet("QPushButton {\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "font: 10pt \"Times New Roman\";\n"
                                             "border: 1px solid rgb(91, 91, 91);\n"
                                             "background-color: rgb(29, 29, 29);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton::hover {\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "font: 10pt \"Times New Roman\";\n"
                                             "border: 1px solid rgb(91, 91, 91);\n"
                                             "    background-color: rgb(144, 144, 144);\n"
                                             "}")
        self.create_backup_btn.setObjectName("create_backup_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 60, 398, 165))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.directory_label = QtWidgets.QLabel(self.widget)
        self.directory_label.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                           "color: rgb(255, 255, 255);")
        self.directory_label.setObjectName("directory_label")
        self.verticalLayout.addWidget(self.directory_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.directory_line = QtWidgets.QTextEdit(self.widget)
        self.directory_line.setMinimumSize(QtCore.QSize(0, 32))
        self.directory_line.setMaximumSize(QtCore.QSize(16777215, 31))
        self.directory_line.setStyleSheet("border: 1px solid white;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(29, 29, 29);\n"
                                          "font: 12pt \"Times New Roman\";")
        self.directory_line.setObjectName("directory_line")
        self.horizontalLayout.addWidget(self.directory_line)
        self.directory_btn = QtWidgets.QPushButton(self.widget)
        self.directory_btn.setMinimumSize(QtCore.QSize(75, 32))
        self.directory_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.directory_btn.setStyleSheet("QPushButton {\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 10pt \"Times New Roman\";\n"
                                         "border: 1px solid rgb(91, 91, 91);\n"
                                         "background-color: rgb(29, 29, 29);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::hover {\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 10pt \"Times New Roman\";\n"
                                         "border: 1px solid rgb(91, 91, 91);\n"
                                         "    background-color: rgb(144, 144, 144);\n"
                                         "}")
        self.directory_btn.setObjectName("directory_btn")
        self.horizontalLayout.addWidget(self.directory_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        self.verticalLayout_2.addWidget(self.name_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_line = QtWidgets.QTextEdit(self.widget)
        self.name_line.setMinimumSize(QtCore.QSize(0, 32))
        self.name_line.setMaximumSize(QtCore.QSize(16777215, 31))
        self.name_line.setStyleSheet("border: 1px solid white;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(29, 29, 29);\n"
                                     "font: 12pt \"Times New Roman\";")
        self.name_line.setObjectName("name_line")
        self.horizontalLayout_2.addWidget(self.name_line)
        self.name_btn = QtWidgets.QPushButton(self.widget)
        self.name_btn.setMinimumSize(QtCore.QSize(75, 32))
        self.name_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.name_btn.setStyleSheet("QPushButton {\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Times New Roman\";\n"
                                    "border: 1px solid rgb(91, 91, 91);\n"
                                    "background-color: rgb(29, 29, 29);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover {\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"Times New Roman\";\n"
                                    "border: 1px solid rgb(91, 91, 91);\n"
                                    "    background-color: rgb(144, 144, 144);\n"
                                    "}")
        self.name_btn.setObjectName("name_btn")
        self.horizontalLayout_2.addWidget(self.name_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        ###################################################################start
        self.save_path_default = 'C:/Users/maxim/Desktop/wow2'
        self.save_path = self.save_path_default

        ###################################################################
        self.directory_line.setText(self.save_path)
        ######
        self.directory_btn.clicked.connect(self.select_save_dir)
        self.name_btn.clicked.connect(lambda: self.name_line.setText(''))
        self.create_backup_btn.clicked.connect(self.run_program)

        ###################################################################end
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "Создание резервной копии"))
        self.create_backup_btn.setText(_translate("MainWindow", "Создать копию"))
        self.directory_label.setText(_translate("MainWindow", "Выбор директории сохранения резервной копии"))
        self.directory_btn.setText(_translate("MainWindow", "Обзор"))
        self.name_label.setText(_translate("MainWindow", "Выбор имени сохранения резервной копии"))
        self.name_btn.setText(_translate("MainWindow", "Очистить"))

    def select_save_dir(self):
        directory = QFileDialog.getExistingDirectory()
        if directory:
            self.save_path = directory
            self.directory_line.setText(directory)
        else:
            self.save_path = self.save_path_default
            self.directory_line.setText(self.save_path_default)

    def set_name(self, date_, time_):
        file_name = self.name_line.toPlainText()
        if file_name:
            return file_name
        else:
            return 'backup_' + date_ + '_' + time_

    def set_log_text(self, name, date_, time_: str, size_):
        log = '#' * 35 + '\n'
        log += f"Файл: {name}\n"
        log += f"Время создания: {date_} {time_.replace('-', ':')}\n"
        log += f"Размер: {str(size_)}\n"
        log += '#' * 35 + '\n'
        return log

    def get_time(self):
        date_ = time.strftime('%Y-%m-%d', time.localtime())
        time_ = time.strftime('%H-%M-%S', time.localtime())
        return date_, time_

    def run_program(self):
        dir_ = self.save_path
        date_, time_ = self.get_time()
        name = self.set_name(date_, time_)
        os.system(f'Echo rosa_backup > {dir_}/{name}.txt')
        size_ = os.path.getsize(f"{dir_}/{name}.txt")
        log_ = self.set_log_text(name, date_, time_, size_)
        log_path = f"{dir_}/{name}_log.txt"
        with open(log_path, 'a') as log_file:
            log_file.write(log_)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
