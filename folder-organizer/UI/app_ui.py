# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 583)
        MainWindow.setStyleSheet(u"*{\n"
"	padding: 0;\n"
"	margin: 0;\n"
"}\n"
"\n"
"#app_page QGroupBox{\n"
"	border: 1px solid #505581;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color:#F4D35E\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 15px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 4px solid #F4D35E;\n"
"}\n"
"/*Main page*/\n"
"#main_page #header{\n"
"	background-color: #F4D35E;\n"
"	color: #2E2F5B;\n"
"	padding-left: 5;\n"
"}\n"
"\n"
"#main_page #body{\n"
"	background-color: #505581;\n"
"	color: white;\n"
"}\n"
"\n"
"#main_page QTextBrowser{\n"
"	background-color: #505581;\n"
"	color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"#main_page #footer{\n"
"	background-color: rgb(97, 104, 157);\n"
"}\n"
"\n"
"#main_page #footer_label{\n"
"	color: #F4D35E;\n"
"}\n"
"\n"
"/*settings page*/\n"
"#settings_page #header_2{\n"
"	background-color: #F4D35E;\n"
"	color: #2E2F5B;\n"
"	padding-left: 5;\n"
"}\n"
"\n"
"#settings_page #body_2{\n"
"	background-color: #50558"
                        "1;\n"
"}\n"
"\n"
"#label_9, #label_10, #label_3, #label_11{\n"
"	color: white;\n"
"}\n"
"\n"
"#dont_touch_add_pushButton{\n"
"	background-color: rgb(72, 217, 0);\n"
"}\n"
"#dont_touch_add_pushButton:hover{\n"
"	background-color: rgb(81, 243, 0);\n"
"}\n"
"\n"
"#dont_touch_delete_pushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"#dont_touch_delete_pushButton:hover{\n"
"	background-color: rgb(255, 93, 0);\n"
"}\n"
"\n"
"#dont_touch_add_frame{\n"
"	background-color: rgb(100, 107, 162);\n"
"	padding: 8px;\n"
"}\n"
"\n"
"/*app page*/\n"
"#app_page{\n"
"	background-color: #505581;\n"
"	color: white;\n"
"}\n"
"\n"
"#label_6, #select_all_checkBox{\n"
"	color: white;\n"
"}\n"
"\n"
"#back_pushButton{\n"
"	background-color: #505581;\n"
"}\n"
"#back_pushButton:hover{\n"
"	background-color: rgb(98, 105, 158);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_2 = QVBoxLayout(self.main_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.main_page)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.header)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(45)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.header)

        self.body = QFrame(self.main_page)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.textBrowser = QTextBrowser(self.body)
        self.textBrowser.setObjectName(u"textBrowser")
        font1 = QFont()
        font1.setPointSize(16)
        self.textBrowser.setFont(font1)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.settings_pushButton = QPushButton(self.body)
        self.settings_pushButton.setObjectName(u"settings_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_pushButton.sizePolicy().hasHeightForWidth())
        self.settings_pushButton.setSizePolicy(sizePolicy1)
        self.settings_pushButton.setMinimumSize(QSize(55, 45))
        self.settings_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_pushButton.setIcon(icon)
        self.settings_pushButton.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.settings_pushButton)

        self.start_program_button = QPushButton(self.body)
        self.start_program_button.setObjectName(u"start_program_button")
        sizePolicy1.setHeightForWidth(self.start_program_button.sizePolicy().hasHeightForWidth())
        self.start_program_button.setSizePolicy(sizePolicy1)
        self.start_program_button.setMinimumSize(QSize(55, 45))
        self.start_program_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_program_button.setIcon(icon1)
        self.start_program_button.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.start_program_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.footer = QFrame(self.body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.footer_label = QLabel(self.footer)
        self.footer_label.setObjectName(u"footer_label")
        self.footer_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.footer_label, 0, Qt.AlignRight)

        self.github_pushButton = QPushButton(self.footer)
        self.github_pushButton.setObjectName(u"github_pushButton")
        sizePolicy1.setHeightForWidth(self.github_pushButton.sizePolicy().hasHeightForWidth())
        self.github_pushButton.setSizePolicy(sizePolicy1)
        self.github_pushButton.setMinimumSize(QSize(55, 45))
        self.github_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.github_pushButton.setIcon(icon2)
        self.github_pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.github_pushButton)


        self.verticalLayout_3.addWidget(self.footer)


        self.verticalLayout_2.addWidget(self.body)

        self.stackedWidget.addWidget(self.main_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_6 = QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.header_2 = QFrame(self.settings_page)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setFrameShape(QFrame.StyledPanel)
        self.header_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 5, 5)
        self.menu_pushButton = QPushButton(self.header_2)
        self.menu_pushButton.setObjectName(u"menu_pushButton")
        sizePolicy1.setHeightForWidth(self.menu_pushButton.sizePolicy().hasHeightForWidth())
        self.menu_pushButton.setSizePolicy(sizePolicy1)
        self.menu_pushButton.setMinimumSize(QSize(55, 45))
        self.menu_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_pushButton.setIcon(icon3)
        self.menu_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.menu_pushButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_2 = QLabel(self.header_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(24)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.header_2, 0, Qt.AlignTop)

        self.body_2 = QFrame(self.settings_page)
        self.body_2.setObjectName(u"body_2")
        sizePolicy.setHeightForWidth(self.body_2.sizePolicy().hasHeightForWidth())
        self.body_2.setSizePolicy(sizePolicy)
        self.body_2.setFrameShape(QFrame.StyledPanel)
        self.body_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.body_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.body_2)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setUnderline(True)
        self.label_9.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.groupBox = QGroupBox(self.body_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.include_folder_yes_radioButton = QRadioButton(self.groupBox)
        self.include_folder_yes_radioButton.setObjectName(u"include_folder_yes_radioButton")
        sizePolicy1.setHeightForWidth(self.include_folder_yes_radioButton.sizePolicy().hasHeightForWidth())
        self.include_folder_yes_radioButton.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(12)
        self.include_folder_yes_radioButton.setFont(font4)

        self.horizontalLayout_12.addWidget(self.include_folder_yes_radioButton)

        self.include_folders_no_radioButton = QRadioButton(self.groupBox)
        self.include_folders_no_radioButton.setObjectName(u"include_folders_no_radioButton")
        sizePolicy1.setHeightForWidth(self.include_folders_no_radioButton.sizePolicy().hasHeightForWidth())
        self.include_folders_no_radioButton.setSizePolicy(sizePolicy1)
        self.include_folders_no_radioButton.setFont(font4)

        self.horizontalLayout_12.addWidget(self.include_folders_no_radioButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_13.addWidget(self.groupBox, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.body_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.groupBox_2 = QGroupBox(self.body_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.include_unk_files_yes_radioButton = QRadioButton(self.groupBox_2)
        self.include_unk_files_yes_radioButton.setObjectName(u"include_unk_files_yes_radioButton")
        sizePolicy1.setHeightForWidth(self.include_unk_files_yes_radioButton.sizePolicy().hasHeightForWidth())
        self.include_unk_files_yes_radioButton.setSizePolicy(sizePolicy1)
        self.include_unk_files_yes_radioButton.setFont(font4)

        self.horizontalLayout_15.addWidget(self.include_unk_files_yes_radioButton)

        self.include_unk_files_no_radioButton = QRadioButton(self.groupBox_2)
        self.include_unk_files_no_radioButton.setObjectName(u"include_unk_files_no_radioButton")
        sizePolicy1.setHeightForWidth(self.include_unk_files_no_radioButton.sizePolicy().hasHeightForWidth())
        self.include_unk_files_no_radioButton.setSizePolicy(sizePolicy1)
        self.include_unk_files_no_radioButton.setFont(font4)

        self.horizontalLayout_15.addWidget(self.include_unk_files_no_radioButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_14.addWidget(self.groupBox_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.frame_2 = QFrame(self.body_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.dont_touch_listWidget = QListWidget(self.frame_2)
        self.dont_touch_listWidget.setObjectName(u"dont_touch_listWidget")
        font5 = QFont()
        font5.setPointSize(14)
        self.dont_touch_listWidget.setFont(font5)

        self.verticalLayout_4.addWidget(self.dont_touch_listWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.dont_touch_add_pushButton = QPushButton(self.frame_2)
        self.dont_touch_add_pushButton.setObjectName(u"dont_touch_add_pushButton")
        sizePolicy1.setHeightForWidth(self.dont_touch_add_pushButton.sizePolicy().hasHeightForWidth())
        self.dont_touch_add_pushButton.setSizePolicy(sizePolicy1)
        self.dont_touch_add_pushButton.setMinimumSize(QSize(55, 45))
        self.dont_touch_add_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dont_touch_add_pushButton.setIcon(icon4)
        self.dont_touch_add_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.dont_touch_add_pushButton)

        self.dont_touch_delete_pushButton = QPushButton(self.frame_2)
        self.dont_touch_delete_pushButton.setObjectName(u"dont_touch_delete_pushButton")
        sizePolicy1.setHeightForWidth(self.dont_touch_delete_pushButton.sizePolicy().hasHeightForWidth())
        self.dont_touch_delete_pushButton.setSizePolicy(sizePolicy1)
        self.dont_touch_delete_pushButton.setMinimumSize(QSize(55, 45))
        self.dont_touch_delete_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dont_touch_delete_pushButton.setIcon(icon5)
        self.dont_touch_delete_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.dont_touch_delete_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.dont_touch_add_frame = QFrame(self.frame_2)
        self.dont_touch_add_frame.setObjectName(u"dont_touch_add_frame")
        self.dont_touch_add_frame.setFrameShape(QFrame.StyledPanel)
        self.dont_touch_add_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.dont_touch_add_frame)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.dont_touch_add_lineEdit = QLineEdit(self.dont_touch_add_frame)
        self.dont_touch_add_lineEdit.setObjectName(u"dont_touch_add_lineEdit")
        self.dont_touch_add_lineEdit.setMinimumSize(QSize(0, 34))
        self.dont_touch_add_lineEdit.setFont(font5)

        self.horizontalLayout_16.addWidget(self.dont_touch_add_lineEdit)

        self.dont_touch_confirm_add_pushButton = QPushButton(self.dont_touch_add_frame)
        self.dont_touch_confirm_add_pushButton.setObjectName(u"dont_touch_confirm_add_pushButton")
        sizePolicy1.setHeightForWidth(self.dont_touch_confirm_add_pushButton.sizePolicy().hasHeightForWidth())
        self.dont_touch_confirm_add_pushButton.setSizePolicy(sizePolicy1)
        self.dont_touch_confirm_add_pushButton.setMinimumSize(QSize(40, 35))
        self.dont_touch_confirm_add_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.dont_touch_confirm_add_pushButton.setIcon(icon4)
        self.dont_touch_confirm_add_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_16.addWidget(self.dont_touch_confirm_add_pushButton)


        self.verticalLayout_4.addWidget(self.dont_touch_add_frame)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.body_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.output_folder_name_lineEdit = QLineEdit(self.body_2)
        self.output_folder_name_lineEdit.setObjectName(u"output_folder_name_lineEdit")
        sizePolicy2.setHeightForWidth(self.output_folder_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.output_folder_name_lineEdit.setSizePolicy(sizePolicy2)
        self.output_folder_name_lineEdit.setMinimumSize(QSize(0, 35))
        self.output_folder_name_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.output_folder_name_lineEdit.setFont(font4)

        self.horizontalLayout_17.addWidget(self.output_folder_name_lineEdit)

        self.output_folder_name_save_pushButton = QPushButton(self.body_2)
        self.output_folder_name_save_pushButton.setObjectName(u"output_folder_name_save_pushButton")
        self.output_folder_name_save_pushButton.setMinimumSize(QSize(70, 30))
        self.output_folder_name_save_pushButton.setMaximumSize(QSize(70, 35))
        self.output_folder_name_save_pushButton.setFont(font4)
        self.output_folder_name_save_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/done.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.output_folder_name_save_pushButton.setIcon(icon6)
        self.output_folder_name_save_pushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_17.addWidget(self.output_folder_name_save_pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)


        self.verticalLayout_6.addWidget(self.body_2)

        self.stackedWidget.addWidget(self.settings_page)
        self.app_page = QWidget()
        self.app_page.setObjectName(u"app_page")
        self.verticalLayout_16 = QVBoxLayout(self.app_page)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.back_pushButton = QPushButton(self.app_page)
        self.back_pushButton.setObjectName(u"back_pushButton")
        sizePolicy1.setHeightForWidth(self.back_pushButton.sizePolicy().hasHeightForWidth())
        self.back_pushButton.setSizePolicy(sizePolicy1)
        self.back_pushButton.setMinimumSize(QSize(55, 45))
        self.back_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_pushButton.setIcon(icon3)
        self.back_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.back_pushButton, 0, Qt.AlignLeft)

        self.label_6 = QLabel(self.app_page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        self.label_6.setFont(font6)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.folder_path_lineEdit = QLineEdit(self.app_page)
        self.folder_path_lineEdit.setObjectName(u"folder_path_lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.folder_path_lineEdit.sizePolicy().hasHeightForWidth())
        self.folder_path_lineEdit.setSizePolicy(sizePolicy4)
        self.folder_path_lineEdit.setMinimumSize(QSize(0, 35))
        self.folder_path_lineEdit.setFont(font4)
        self.folder_path_lineEdit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.folder_path_lineEdit)

        self.browse_folder_pushButton = QPushButton(self.app_page)
        self.browse_folder_pushButton.setObjectName(u"browse_folder_pushButton")
        sizePolicy1.setHeightForWidth(self.browse_folder_pushButton.sizePolicy().hasHeightForWidth())
        self.browse_folder_pushButton.setSizePolicy(sizePolicy1)
        self.browse_folder_pushButton.setMinimumSize(QSize(45, 35))
        self.browse_folder_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browse_folder_pushButton.setIcon(icon7)
        self.browse_folder_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.browse_folder_pushButton)


        self.verticalLayout_16.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.display_frame = QFrame(self.app_page)
        self.display_frame.setObjectName(u"display_frame")
        self.display_frame.setFrameShape(QFrame.StyledPanel)
        self.display_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.display_frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.display_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(230, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.select_all_checkBox = QCheckBox(self.frame)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")
        self.select_all_checkBox.setFont(font4)
        self.select_all_checkBox.setChecked(True)

        self.verticalLayout_10.addWidget(self.select_all_checkBox, 0, Qt.AlignRight)

        self.content_listWidget = QListWidget(self.frame)
        self.content_listWidget.setObjectName(u"content_listWidget")
        self.content_listWidget.setEnabled(False)
        self.content_listWidget.setFont(font4)
        self.content_listWidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_10.addWidget(self.content_listWidget)


        self.horizontalLayout_4.addWidget(self.frame)

        self.content_stats_textBrowser = QTextBrowser(self.display_frame)
        self.content_stats_textBrowser.setObjectName(u"content_stats_textBrowser")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.content_stats_textBrowser.sizePolicy().hasHeightForWidth())
        self.content_stats_textBrowser.setSizePolicy(sizePolicy5)
        self.content_stats_textBrowser.setMaximumSize(QSize(150, 16777215))
        self.content_stats_textBrowser.setFont(font4)

        self.horizontalLayout_4.addWidget(self.content_stats_textBrowser)

        self.scrollArea = QScrollArea(self.display_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 270, 930))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(270, 16777215))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setMaximumSize(QSize(270, 16777215))
        self.groupBox_3.setFont(font5)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 10, -1, -1)
        self.org_extension_radioButton = QRadioButton(self.groupBox_3)
        self.org_extension_radioButton.setObjectName(u"org_extension_radioButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.org_extension_radioButton.sizePolicy().hasHeightForWidth())
        self.org_extension_radioButton.setSizePolicy(sizePolicy7)
        self.org_extension_radioButton.setFont(font5)

        self.verticalLayout_9.addWidget(self.org_extension_radioButton)

        self.org_categories_radioButton = QRadioButton(self.groupBox_3)
        self.org_categories_radioButton.setObjectName(u"org_categories_radioButton")
        sizePolicy7.setHeightForWidth(self.org_categories_radioButton.sizePolicy().hasHeightForWidth())
        self.org_categories_radioButton.setSizePolicy(sizePolicy7)
        self.org_categories_radioButton.setFont(font5)

        self.verticalLayout_9.addWidget(self.org_categories_radioButton)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, 5, 5)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.org_info_pushButton = QPushButton(self.groupBox_3)
        self.org_info_pushButton.setObjectName(u"org_info_pushButton")
        sizePolicy1.setHeightForWidth(self.org_info_pushButton.sizePolicy().hasHeightForWidth())
        self.org_info_pushButton.setSizePolicy(sizePolicy1)
        self.org_info_pushButton.setMinimumSize(QSize(55, 45))
        self.org_info_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"icons/about.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.org_info_pushButton.setIcon(icon8)
        self.org_info_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.org_info_pushButton)

        self.org_run_pushButton = QPushButton(self.groupBox_3)
        self.org_run_pushButton.setObjectName(u"org_run_pushButton")
        sizePolicy1.setHeightForWidth(self.org_run_pushButton.sizePolicy().hasHeightForWidth())
        self.org_run_pushButton.setSizePolicy(sizePolicy1)
        self.org_run_pushButton.setMinimumSize(QSize(55, 45))
        self.org_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.org_run_pushButton.setIcon(icon1)
        self.org_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.org_run_pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy6.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy6)
        self.groupBox_4.setMaximumSize(QSize(270, 16777215))
        self.groupBox_4.setFont(font5)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 35, 5, 0)
        self.rename_name_lineEdit = QLineEdit(self.groupBox_4)
        self.rename_name_lineEdit.setObjectName(u"rename_name_lineEdit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.rename_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.rename_name_lineEdit.setSizePolicy(sizePolicy8)
        self.rename_name_lineEdit.setMinimumSize(QSize(0, 30))
        self.rename_name_lineEdit.setFont(font5)
        self.rename_name_lineEdit.setReadOnly(False)

        self.verticalLayout_11.addWidget(self.rename_name_lineEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, 5, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.rename_info_pushButton = QPushButton(self.groupBox_4)
        self.rename_info_pushButton.setObjectName(u"rename_info_pushButton")
        sizePolicy1.setHeightForWidth(self.rename_info_pushButton.sizePolicy().hasHeightForWidth())
        self.rename_info_pushButton.setSizePolicy(sizePolicy1)
        self.rename_info_pushButton.setMinimumSize(QSize(55, 45))
        self.rename_info_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rename_info_pushButton.setIcon(icon8)
        self.rename_info_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.rename_info_pushButton)

        self.rename_run_pushButton = QPushButton(self.groupBox_4)
        self.rename_run_pushButton.setObjectName(u"rename_run_pushButton")
        sizePolicy1.setHeightForWidth(self.rename_run_pushButton.sizePolicy().hasHeightForWidth())
        self.rename_run_pushButton.setSizePolicy(sizePolicy1)
        self.rename_run_pushButton.setMinimumSize(QSize(55, 45))
        self.rename_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rename_run_pushButton.setIcon(icon1)
        self.rename_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.rename_run_pushButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.groupBox_5.setMaximumSize(QSize(270, 16777215))
        self.groupBox_5.setFont(font5)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 30, 5, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, -1, -1)
        self.ext_from_lineEdit = QLineEdit(self.groupBox_5)
        self.ext_from_lineEdit.setObjectName(u"ext_from_lineEdit")
        sizePolicy1.setHeightForWidth(self.ext_from_lineEdit.sizePolicy().hasHeightForWidth())
        self.ext_from_lineEdit.setSizePolicy(sizePolicy1)
        self.ext_from_lineEdit.setMinimumSize(QSize(0, 40))
        self.ext_from_lineEdit.setMaximumSize(QSize(120, 16777215))
        self.ext_from_lineEdit.setFont(font5)
        self.ext_from_lineEdit.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.ext_from_lineEdit)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.ext_to_lineEdit = QLineEdit(self.groupBox_5)
        self.ext_to_lineEdit.setObjectName(u"ext_to_lineEdit")
        sizePolicy1.setHeightForWidth(self.ext_to_lineEdit.sizePolicy().hasHeightForWidth())
        self.ext_to_lineEdit.setSizePolicy(sizePolicy1)
        self.ext_to_lineEdit.setMinimumSize(QSize(0, 40))
        self.ext_to_lineEdit.setMaximumSize(QSize(120, 16777215))
        self.ext_to_lineEdit.setFont(font5)
        self.ext_to_lineEdit.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.ext_to_lineEdit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 5, 5)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.ext_info_pushButton = QPushButton(self.groupBox_5)
        self.ext_info_pushButton.setObjectName(u"ext_info_pushButton")
        sizePolicy1.setHeightForWidth(self.ext_info_pushButton.sizePolicy().hasHeightForWidth())
        self.ext_info_pushButton.setSizePolicy(sizePolicy1)
        self.ext_info_pushButton.setMinimumSize(QSize(55, 45))
        self.ext_info_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ext_info_pushButton.setIcon(icon8)
        self.ext_info_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.ext_info_pushButton)

        self.ext_run_pushButton = QPushButton(self.groupBox_5)
        self.ext_run_pushButton.setObjectName(u"ext_run_pushButton")
        sizePolicy1.setHeightForWidth(self.ext_run_pushButton.sizePolicy().hasHeightForWidth())
        self.ext_run_pushButton.setSizePolicy(sizePolicy1)
        self.ext_run_pushButton.setMinimumSize(QSize(55, 45))
        self.ext_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ext_run_pushButton.setIcon(icon1)
        self.ext_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.ext_run_pushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy6.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy6)
        self.groupBox_6.setMaximumSize(QSize(270, 16777215))
        self.groupBox_6.setFont(font5)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 30, 5, 5)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.move_location_lineEdit = QLineEdit(self.groupBox_6)
        self.move_location_lineEdit.setObjectName(u"move_location_lineEdit")
        sizePolicy8.setHeightForWidth(self.move_location_lineEdit.sizePolicy().hasHeightForWidth())
        self.move_location_lineEdit.setSizePolicy(sizePolicy8)
        self.move_location_lineEdit.setMinimumSize(QSize(0, 30))
        self.move_location_lineEdit.setMaximumSize(QSize(16777215, 32))
        self.move_location_lineEdit.setFont(font5)
        self.move_location_lineEdit.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.move_location_lineEdit)

        self.move_browse_location_pushButton = QPushButton(self.groupBox_6)
        self.move_browse_location_pushButton.setObjectName(u"move_browse_location_pushButton")
        sizePolicy1.setHeightForWidth(self.move_browse_location_pushButton.sizePolicy().hasHeightForWidth())
        self.move_browse_location_pushButton.setSizePolicy(sizePolicy1)
        self.move_browse_location_pushButton.setMinimumSize(QSize(45, 35))
        self.move_browse_location_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.move_browse_location_pushButton.setIcon(icon7)
        self.move_browse_location_pushButton.setIconSize(QSize(23, 23))

        self.horizontalLayout_19.addWidget(self.move_browse_location_pushButton)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 5, 5, 5)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.move_run_pushButton = QPushButton(self.groupBox_6)
        self.move_run_pushButton.setObjectName(u"move_run_pushButton")
        sizePolicy1.setHeightForWidth(self.move_run_pushButton.sizePolicy().hasHeightForWidth())
        self.move_run_pushButton.setSizePolicy(sizePolicy1)
        self.move_run_pushButton.setMinimumSize(QSize(55, 45))
        self.move_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.move_run_pushButton.setIcon(icon1)
        self.move_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.move_run_pushButton)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.groupBox_7.setMaximumSize(QSize(270, 16777215))
        self.groupBox_7.setFont(font5)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 30, 5, 5)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.copy_location_lineEdit = QLineEdit(self.groupBox_7)
        self.copy_location_lineEdit.setObjectName(u"copy_location_lineEdit")
        sizePolicy8.setHeightForWidth(self.copy_location_lineEdit.sizePolicy().hasHeightForWidth())
        self.copy_location_lineEdit.setSizePolicy(sizePolicy8)
        self.copy_location_lineEdit.setMinimumSize(QSize(0, 30))
        self.copy_location_lineEdit.setMaximumSize(QSize(16777215, 32))
        self.copy_location_lineEdit.setFont(font5)
        self.copy_location_lineEdit.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.copy_location_lineEdit)

        self.copy_browse_location_pushButton = QPushButton(self.groupBox_7)
        self.copy_browse_location_pushButton.setObjectName(u"copy_browse_location_pushButton")
        sizePolicy1.setHeightForWidth(self.copy_browse_location_pushButton.sizePolicy().hasHeightForWidth())
        self.copy_browse_location_pushButton.setSizePolicy(sizePolicy1)
        self.copy_browse_location_pushButton.setMinimumSize(QSize(45, 35))
        self.copy_browse_location_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_browse_location_pushButton.setIcon(icon7)
        self.copy_browse_location_pushButton.setIconSize(QSize(23, 23))

        self.horizontalLayout_23.addWidget(self.copy_browse_location_pushButton)


        self.verticalLayout_14.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, 5, 5)
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_21)

        self.copy_run_pushButton = QPushButton(self.groupBox_7)
        self.copy_run_pushButton.setObjectName(u"copy_run_pushButton")
        sizePolicy1.setHeightForWidth(self.copy_run_pushButton.sizePolicy().hasHeightForWidth())
        self.copy_run_pushButton.setSizePolicy(sizePolicy1)
        self.copy_run_pushButton.setMinimumSize(QSize(55, 45))
        self.copy_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_run_pushButton.setIcon(icon1)
        self.copy_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.copy_run_pushButton)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)


        self.verticalLayout_14.addLayout(self.horizontalLayout_24)


        self.verticalLayout_7.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy6.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy6)
        self.groupBox_8.setMaximumSize(QSize(270, 16777215))
        self.groupBox_8.setFont(font5)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 30, 5, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, 5, 5)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)

        self.delete_run_pushButton = QPushButton(self.groupBox_8)
        self.delete_run_pushButton.setObjectName(u"delete_run_pushButton")
        sizePolicy1.setHeightForWidth(self.delete_run_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_run_pushButton.setSizePolicy(sizePolicy1)
        self.delete_run_pushButton.setMinimumSize(QSize(55, 45))
        self.delete_run_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_run_pushButton.setIcon(icon1)
        self.delete_run_pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.delete_run_pushButton)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_20)


        self.verticalLayout_15.addLayout(self.horizontalLayout_22)


        self.verticalLayout_7.addWidget(self.groupBox_8)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout_10.addWidget(self.display_frame)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.app_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Folder Organizer", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Welcome To Folder Organizer </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A tool that can automatically manage and arrange your files and directories.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You may use this application to arrange the files in your folders in two distinct ways: by categories and by extensions.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Additionally, it does bulk actions that enable you to make numerous changes quickly, such as renaming a large number of files following a name pattern.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settings_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.start_program_button.setToolTip(QCoreApplication.translate("MainWindow", u"start", None))
#endif // QT_CONFIG(tooltip)
        self.start_program_button.setText("")
        self.footer_label.setText(QCoreApplication.translate("MainWindow", u"By Abdelrahman Tlayjeh", None))
#if QT_CONFIG(tooltip)
        self.github_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"see on Github", None))
#endif // QT_CONFIG(tooltip)
        self.github_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.menu_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"back", None))
#endif // QT_CONFIG(tooltip)
        self.menu_pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Include Folders:", None))
        self.include_folder_yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.include_folders_no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Include Unknown files:", None))
        self.include_unk_files_yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.include_unk_files_no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dont Touch:", None))
#if QT_CONFIG(tooltip)
        self.dont_touch_listWidget.setToolTip(QCoreApplication.translate("MainWindow", u"list of names that the program will dont touch", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dont_touch_add_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"add new name", None))
#endif // QT_CONFIG(tooltip)
        self.dont_touch_add_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.dont_touch_delete_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"delete selected name", None))
#endif // QT_CONFIG(tooltip)
        self.dont_touch_delete_pushButton.setText("")
        self.dont_touch_add_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Folder/File Name", None))
#if QT_CONFIG(tooltip)
        self.dont_touch_confirm_add_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"confirm", None))
#endif // QT_CONFIG(tooltip)
        self.dont_touch_confirm_add_pushButton.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Output folder name:", None))
        self.output_folder_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output Folder Name", None))
#if QT_CONFIG(tooltip)
        self.output_folder_name_save_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"confirm", None))
#endif // QT_CONFIG(tooltip)
        self.output_folder_name_save_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.back_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"back", None))
#endif // QT_CONFIG(tooltip)
        self.back_pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Browse a Folder", None))
#if QT_CONFIG(tooltip)
        self.browse_folder_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"browse folder", None))
#endif // QT_CONFIG(tooltip)
        self.browse_folder_pushButton.setText("")
        self.select_all_checkBox.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.content_stats_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.org_extension_radioButton.setText(QCoreApplication.translate("MainWindow", u"By Extensions", None))
        self.org_categories_radioButton.setText(QCoreApplication.translate("MainWindow", u"By Categories", None))
#if QT_CONFIG(tooltip)
        self.org_info_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"learn more", None))
#endif // QT_CONFIG(tooltip)
        self.org_info_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.org_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.org_run_pushButton.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.rename_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Name Pattern", None))
#if QT_CONFIG(tooltip)
        self.rename_info_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"learn more", None))
#endif // QT_CONFIG(tooltip)
        self.rename_info_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.rename_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.rename_run_pushButton.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Change Extension", None))
        self.ext_from_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"from", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.ext_to_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"to", None))
#if QT_CONFIG(tooltip)
        self.ext_info_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"learn more", None))
#endif // QT_CONFIG(tooltip)
        self.ext_info_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.ext_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.ext_run_pushButton.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Move", None))
        self.move_location_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Move To", None))
#if QT_CONFIG(tooltip)
        self.move_browse_location_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"browse folder", None))
#endif // QT_CONFIG(tooltip)
        self.move_browse_location_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.move_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.move_run_pushButton.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.copy_location_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Copy To", None))
#if QT_CONFIG(tooltip)
        self.copy_browse_location_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"browse folder", None))
#endif // QT_CONFIG(tooltip)
        self.copy_browse_location_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.copy_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.copy_run_pushButton.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.delete_run_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
#endif // QT_CONFIG(tooltip)
        self.delete_run_pushButton.setText("")
    # retranslateUi

