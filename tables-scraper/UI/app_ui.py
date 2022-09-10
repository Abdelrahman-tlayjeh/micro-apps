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
    QSize, QTime, QUrl, Qt, QAbstractTableModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 580)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(49, 233, 129);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(27, 233, 171);\n"
"	border: 1px solid rgb(182, 182, 182);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"/*Intro Page*/\n"
"#intro_header{\n"
"	background-color: rgb(49, 233, 129);\n"
"	color: black;\n"
"}\n"
"\n"
"#intro_body{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"}\n"
"\n"
"#intro_textBrowser{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"	border: 0;\n"
"}\n"
"\n"
"#footer{\n"
"	background-color: rgb(162, 179, 198);\n"
"}\n"
"\n"
"/*Settings Page*/\n"
"#menu_pushButton{\n"
"	margin-top: 7px;\n"
"}\n"
"\n"
"#settings_header{\n"
"	background-color: rgb(49, 233, 129);\n"
"	color: black;\n"
"}\n"
"\n"
"#settings_body{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"}\n"
"\n"
"#settings_body  QLabel{\n"
"	color: white;\n"
"}\n"
"\n"
"#settings_body QRadioButton{\n"
"	color: white;\n"
"}\n"
""
                        "\n"
"\n"
"/*Main Page*/\n"
"#main_page{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"}\n"
"\n"
"#back_pushButton{\n"
"	background-color: rgb(107, 129, 140);\n"
"}\n"
"#back_pushButton:hover{\n"
"	background-color: rgb(131, 158, 171);\n"
"	border: 0;\n"
"}\n"
"\n"
"#main_page QLabel, QRadioButton, QGroupBox{\n"
"	color: white;\n"
"}\n"
"\n"
"QTableView{\n"
"	background-color: rgb(216, 228, 255);\n"
"}\n"
"\n"
"\n"
"/*About page*/\n"
"#about_header{\n"
"	background-color: rgb(49, 233, 129);\n"
"	color: black;\n"
"}\n"
"\n"
"#about_body{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"}\n"
"\n"
"#go_back_pushButton{\n"
"	margin-top: 7px;\n"
"}\n"
"\n"
"#about_textBrowser{\n"
"	background-color: rgb(107, 129, 140);\n"
"	color: white;\n"
"	border: 0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.intro_page = QWidget()
        self.intro_page.setObjectName(u"intro_page")
        self.verticalLayout = QVBoxLayout(self.intro_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.intro_header = QFrame(self.intro_page)
        self.intro_header.setObjectName(u"intro_header")
        self.intro_header.setFrameShape(QFrame.StyledPanel)
        self.intro_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.intro_header)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 5)
        self.label = QLabel(self.intro_header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(45)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.intro_header)

        self.intro_body = QFrame(self.intro_page)
        self.intro_body.setObjectName(u"intro_body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intro_body.sizePolicy().hasHeightForWidth())
        self.intro_body.setSizePolicy(sizePolicy)
        self.intro_body.setFrameShape(QFrame.StyledPanel)
        self.intro_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.intro_body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.intro_textBrowser = QTextBrowser(self.intro_body)
        self.intro_textBrowser.setObjectName(u"intro_textBrowser")

        self.verticalLayout_3.addWidget(self.intro_textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.about_pushButton = QPushButton(self.intro_body)
        self.about_pushButton.setObjectName(u"about_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.about_pushButton.sizePolicy().hasHeightForWidth())
        self.about_pushButton.setSizePolicy(sizePolicy1)
        self.about_pushButton.setMinimumSize(QSize(55, 45))
        self.about_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/about.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_pushButton.setIcon(icon)
        self.about_pushButton.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.about_pushButton)

        self.settings_pushButton = QPushButton(self.intro_body)
        self.settings_pushButton.setObjectName(u"settings_pushButton")
        sizePolicy1.setHeightForWidth(self.settings_pushButton.sizePolicy().hasHeightForWidth())
        self.settings_pushButton.setSizePolicy(sizePolicy1)
        self.settings_pushButton.setMinimumSize(QSize(55, 45))
        self.settings_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_pushButton.setIcon(icon1)
        self.settings_pushButton.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.settings_pushButton)

        self.start_program_button = QPushButton(self.intro_body)
        self.start_program_button.setObjectName(u"start_program_button")
        sizePolicy1.setHeightForWidth(self.start_program_button.sizePolicy().hasHeightForWidth())
        self.start_program_button.setSizePolicy(sizePolicy1)
        self.start_program_button.setMinimumSize(QSize(55, 45))
        self.start_program_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/start.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_program_button.setIcon(icon2)
        self.start_program_button.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.start_program_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 190, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.footer = QFrame(self.intro_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.footer_label = QLabel(self.footer)
        self.footer_label.setObjectName(u"footer_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.footer_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.footer_label, 0, Qt.AlignRight)

        self.github_pushButton = QPushButton(self.footer)
        self.github_pushButton.setObjectName(u"github_pushButton")
        sizePolicy1.setHeightForWidth(self.github_pushButton.sizePolicy().hasHeightForWidth())
        self.github_pushButton.setSizePolicy(sizePolicy1)
        self.github_pushButton.setMinimumSize(QSize(55, 45))
        self.github_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.github_pushButton.setIcon(icon3)
        self.github_pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.github_pushButton)


        self.verticalLayout_3.addWidget(self.footer)


        self.verticalLayout.addWidget(self.intro_body)

        self.stackedWidget.addWidget(self.intro_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_4 = QVBoxLayout(self.settings_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settings_header = QFrame(self.settings_page)
        self.settings_header.setObjectName(u"settings_header")
        self.settings_header.setFrameShape(QFrame.StyledPanel)
        self.settings_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.settings_header)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 5)
        self.menu_pushButton = QPushButton(self.settings_header)
        self.menu_pushButton.setObjectName(u"menu_pushButton")
        sizePolicy1.setHeightForWidth(self.menu_pushButton.sizePolicy().hasHeightForWidth())
        self.menu_pushButton.setSizePolicy(sizePolicy1)
        self.menu_pushButton.setMinimumSize(QSize(55, 45))
        self.menu_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"icons/back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_pushButton.setIcon(icon4)
        self.menu_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.menu_pushButton, 0, Qt.AlignTop)

        self.label_2 = QLabel(self.settings_header)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(24)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.settings_header)

        self.settings_body = QFrame(self.settings_page)
        self.settings_body.setObjectName(u"settings_body")
        sizePolicy.setHeightForWidth(self.settings_body.sizePolicy().hasHeightForWidth())
        self.settings_body.setSizePolicy(sizePolicy)
        self.settings_body.setFrameShape(QFrame.StyledPanel)
        self.settings_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.settings_body)
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 10, 5, 5)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.settings_body)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setUnderline(True)
        self.label_11.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.driver_path_lineEdit = QLineEdit(self.settings_body)
        self.driver_path_lineEdit.setObjectName(u"driver_path_lineEdit")
        sizePolicy2.setHeightForWidth(self.driver_path_lineEdit.sizePolicy().hasHeightForWidth())
        self.driver_path_lineEdit.setSizePolicy(sizePolicy2)
        self.driver_path_lineEdit.setMinimumSize(QSize(0, 35))
        self.driver_path_lineEdit.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(12)
        self.driver_path_lineEdit.setFont(font4)
        self.driver_path_lineEdit.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.driver_path_lineEdit)

        self.browse_driver_path_pushButton = QPushButton(self.settings_body)
        self.browse_driver_path_pushButton.setObjectName(u"browse_driver_path_pushButton")
        self.browse_driver_path_pushButton.setMinimumSize(QSize(70, 30))
        self.browse_driver_path_pushButton.setMaximumSize(QSize(70, 35))
        self.browse_driver_path_pushButton.setFont(font4)
        self.browse_driver_path_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browse_driver_path_pushButton.setIcon(icon5)
        self.browse_driver_path_pushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_17.addWidget(self.browse_driver_path_pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.label_3 = QLabel(self.settings_body)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_3.setFont(font5)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.settings_body)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.groupBox_5 = QGroupBox(self.settings_body)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.show_browser_yes_radioButton = QRadioButton(self.groupBox_5)
        self.show_browser_yes_radioButton.setObjectName(u"show_browser_yes_radioButton")
        sizePolicy1.setHeightForWidth(self.show_browser_yes_radioButton.sizePolicy().hasHeightForWidth())
        self.show_browser_yes_radioButton.setSizePolicy(sizePolicy1)
        self.show_browser_yes_radioButton.setFont(font4)
        self.show_browser_yes_radioButton.setChecked(False)

        self.horizontalLayout_18.addWidget(self.show_browser_yes_radioButton)

        self.show_browser_no_radioButton = QRadioButton(self.groupBox_5)
        self.show_browser_no_radioButton.setObjectName(u"show_browser_no_radioButton")
        sizePolicy1.setHeightForWidth(self.show_browser_no_radioButton.sizePolicy().hasHeightForWidth())
        self.show_browser_no_radioButton.setSizePolicy(sizePolicy1)
        self.show_browser_no_radioButton.setFont(font4)
        self.show_browser_no_radioButton.setChecked(True)

        self.horizontalLayout_18.addWidget(self.show_browser_no_radioButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)


        self.horizontalLayout_16.addWidget(self.groupBox_5, 0, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.label_7 = QLabel(self.settings_body)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_7)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.settings_body)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.groupBox = QGroupBox(self.settings_body)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.auto_save_yes_radioButton = QRadioButton(self.groupBox)
        self.auto_save_yes_radioButton.setObjectName(u"auto_save_yes_radioButton")
        sizePolicy1.setHeightForWidth(self.auto_save_yes_radioButton.sizePolicy().hasHeightForWidth())
        self.auto_save_yes_radioButton.setSizePolicy(sizePolicy1)
        self.auto_save_yes_radioButton.setFont(font4)

        self.horizontalLayout_12.addWidget(self.auto_save_yes_radioButton)

        self.auto_save_no_radioButton = QRadioButton(self.groupBox)
        self.auto_save_no_radioButton.setObjectName(u"auto_save_no_radioButton")
        sizePolicy1.setHeightForWidth(self.auto_save_no_radioButton.sizePolicy().hasHeightForWidth())
        self.auto_save_no_radioButton.setSizePolicy(sizePolicy1)
        self.auto_save_no_radioButton.setFont(font4)
        self.auto_save_no_radioButton.setChecked(True)

        self.horizontalLayout_12.addWidget(self.auto_save_no_radioButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_13.addWidget(self.groupBox, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.settings_body)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.settings_body)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.groupBox_4 = QGroupBox(self.settings_body)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.visible_yes_radioButton = QRadioButton(self.groupBox_4)
        self.visible_yes_radioButton.setObjectName(u"visible_yes_radioButton")
        sizePolicy1.setHeightForWidth(self.visible_yes_radioButton.sizePolicy().hasHeightForWidth())
        self.visible_yes_radioButton.setSizePolicy(sizePolicy1)
        self.visible_yes_radioButton.setFont(font4)
        self.visible_yes_radioButton.setChecked(True)

        self.horizontalLayout_15.addWidget(self.visible_yes_radioButton)

        self.visible_no_radioButton = QRadioButton(self.groupBox_4)
        self.visible_no_radioButton.setObjectName(u"visible_no_radioButton")
        sizePolicy1.setHeightForWidth(self.visible_no_radioButton.sizePolicy().hasHeightForWidth())
        self.visible_no_radioButton.setSizePolicy(sizePolicy1)
        self.visible_no_radioButton.setFont(font4)
        self.visible_no_radioButton.setChecked(False)

        self.horizontalLayout_15.addWidget(self.visible_no_radioButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_14.addWidget(self.groupBox_4, 0, Qt.AlignLeft)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.label_5 = QLabel(self.settings_body)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 308, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.settings_body)

        self.stackedWidget.addWidget(self.settings_page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.gridLayout_3 = QGridLayout(self.main_page)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 5, 5)
        self.groupBox_3 = QGroupBox(self.main_page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.csv_radioButton = QRadioButton(self.groupBox_3)
        self.csv_radioButton.setObjectName(u"csv_radioButton")
        self.csv_radioButton.setFont(font4)
        self.csv_radioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.csv_radioButton, 0, 0, 1, 1)

        self.xlsx_radioButton = QRadioButton(self.groupBox_3)
        self.xlsx_radioButton.setObjectName(u"xlsx_radioButton")
        self.xlsx_radioButton.setFont(font4)

        self.gridLayout_2.addWidget(self.xlsx_radioButton, 0, 1, 1, 2)

        self.file_name_lineEdit = QLineEdit(self.groupBox_3)
        self.file_name_lineEdit.setObjectName(u"file_name_lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.file_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.file_name_lineEdit.setSizePolicy(sizePolicy5)
        self.file_name_lineEdit.setMinimumSize(QSize(220, 30))
        self.file_name_lineEdit.setFont(font4)

        self.gridLayout_2.addWidget(self.file_name_lineEdit, 1, 0, 1, 2)

        self.extension_label = QLabel(self.groupBox_3)
        self.extension_label.setObjectName(u"extension_label")
        self.extension_label.setFont(font4)

        self.gridLayout_2.addWidget(self.extension_label, 1, 2, 1, 1)

        self.export_pushButton = QPushButton(self.groupBox_3)
        self.export_pushButton.setObjectName(u"export_pushButton")
        sizePolicy1.setHeightForWidth(self.export_pushButton.sizePolicy().hasHeightForWidth())
        self.export_pushButton.setSizePolicy(sizePolicy1)
        self.export_pushButton.setMinimumSize(QSize(50, 40))
        self.export_pushButton.setFont(font4)
        self.export_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/done.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.export_pushButton.setIcon(icon6)

        self.gridLayout_2.addWidget(self.export_pushButton, 1, 3, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 3, 2, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(302, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 4, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.back_pushButton = QPushButton(self.main_page)
        self.back_pushButton.setObjectName(u"back_pushButton")
        sizePolicy1.setHeightForWidth(self.back_pushButton.sizePolicy().hasHeightForWidth())
        self.back_pushButton.setSizePolicy(sizePolicy1)
        self.back_pushButton.setMinimumSize(QSize(45, 45))
        self.back_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_pushButton.setIcon(icon4)
        self.back_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.back_pushButton, 0, Qt.AlignLeft)

        self.label_6 = QLabel(self.main_page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        self.label_6.setFont(font6)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.url_lineEdit = QLineEdit(self.main_page)
        self.url_lineEdit.setObjectName(u"url_lineEdit")
        sizePolicy4.setHeightForWidth(self.url_lineEdit.sizePolicy().hasHeightForWidth())
        self.url_lineEdit.setSizePolicy(sizePolicy4)
        self.url_lineEdit.setMinimumSize(QSize(0, 35))
        self.url_lineEdit.setFont(font4)
        self.url_lineEdit.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.url_lineEdit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.groupBox_2 = QGroupBox(self.main_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setFont(font4)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.basic_radioButton = QRadioButton(self.groupBox_2)
        self.basic_radioButton.setObjectName(u"basic_radioButton")
        self.basic_radioButton.setFont(font4)
        self.basic_radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.basic_radioButton)

        self.advanced_radioButton = QRadioButton(self.groupBox_2)
        self.advanced_radioButton.setObjectName(u"advanced_radioButton")
        self.advanced_radioButton.setFont(font4)

        self.horizontalLayout_4.addWidget(self.advanced_radioButton)

        self.scrape_pushButton = QPushButton(self.groupBox_2)
        self.scrape_pushButton.setObjectName(u"scrape_pushButton")
        sizePolicy1.setHeightForWidth(self.scrape_pushButton.sizePolicy().hasHeightForWidth())
        self.scrape_pushButton.setSizePolicy(sizePolicy1)
        self.scrape_pushButton.setMinimumSize(QSize(50, 40))
        self.scrape_pushButton.setFont(font4)
        self.scrape_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.scrape_pushButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.scrape_pushButton)


        self.horizontalLayout_6.addWidget(self.groupBox_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 3)

        self.tableView = QTableView(self.main_page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font5)

        self.gridLayout_3.addWidget(self.tableView, 2, 0, 1, 3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.prev_pushButton = QPushButton(self.main_page)
        self.prev_pushButton.setObjectName(u"prev_pushButton")
        sizePolicy1.setHeightForWidth(self.prev_pushButton.sizePolicy().hasHeightForWidth())
        self.prev_pushButton.setSizePolicy(sizePolicy1)
        self.prev_pushButton.setMinimumSize(QSize(40, 40))
        self.prev_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.prev_pushButton)

        self.current_index_label = QLabel(self.main_page)
        self.current_index_label.setObjectName(u"current_index_label")
        self.current_index_label.setFont(font4)

        self.horizontalLayout_7.addWidget(self.current_index_label)

        self.total_results_label = QLabel(self.main_page)
        self.total_results_label.setObjectName(u"total_results_label")
        self.total_results_label.setFont(font4)

        self.horizontalLayout_7.addWidget(self.total_results_label)

        self.next_pushButton = QPushButton(self.main_page)
        self.next_pushButton.setObjectName(u"next_pushButton")
        sizePolicy1.setHeightForWidth(self.next_pushButton.sizePolicy().hasHeightForWidth())
        self.next_pushButton.setSizePolicy(sizePolicy1)
        self.next_pushButton.setMinimumSize(QSize(40, 40))
        self.next_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.next_pushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 35))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.loading_text_label = QLabel(self.frame)
        self.loading_text_label.setObjectName(u"loading_text_label")
        sizePolicy3.setHeightForWidth(self.loading_text_label.sizePolicy().hasHeightForWidth())
        self.loading_text_label.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setPointSize(14)
        self.loading_text_label.setFont(font7)

        self.horizontalLayout_9.addWidget(self.loading_text_label, 0, Qt.AlignLeft)

        self.loading_indicator_label = QLabel(self.frame)
        self.loading_indicator_label.setObjectName(u"loading_indicator_label")
        self.horizontalLayout_9.addWidget(self.loading_indicator_label, 0, Qt.AlignLeft)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.main_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.verticalLayout_10 = QVBoxLayout(self.about_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.about_header = QFrame(self.about_page)
        self.about_header.setObjectName(u"about_header")
        self.about_header.setFrameShape(QFrame.StyledPanel)
        self.about_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.about_header)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 0, 5)
        self.go_back_pushButton = QPushButton(self.about_header)
        self.go_back_pushButton.setObjectName(u"go_back_pushButton")
        sizePolicy1.setHeightForWidth(self.go_back_pushButton.sizePolicy().hasHeightForWidth())
        self.go_back_pushButton.setSizePolicy(sizePolicy1)
        self.go_back_pushButton.setMinimumSize(QSize(55, 45))
        self.go_back_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.go_back_pushButton.setIcon(icon4)
        self.go_back_pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.go_back_pushButton, 0, Qt.AlignTop)

        self.label_8 = QLabel(self.about_header)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.about_header)

        self.about_body = QFrame(self.about_page)
        self.about_body.setObjectName(u"about_body")
        sizePolicy.setHeightForWidth(self.about_body.sizePolicy().hasHeightForWidth())
        self.about_body.setSizePolicy(sizePolicy)
        self.about_body.setFrameShape(QFrame.StyledPanel)
        self.about_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.about_body)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.about_textBrowser = QTextBrowser(self.about_body)
        self.about_textBrowser.setObjectName(u"about_textBrowser")

        self.gridLayout_4.addWidget(self.about_textBrowser, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.about_body)

        self.stackedWidget.addWidget(self.about_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tables Scraper", None))
        self.intro_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Welcome To Tables Scraper:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">A tables scraping tool for both static and dynamic websites. "
                        "Tables that have been scraped may require manual cleaning.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.about_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"more info", None))
#endif // QT_CONFIG(tooltip)
        self.about_pushButton.setText("")
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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Browser Driver Path:", None))
        self.driver_path_lineEdit.setText("")
        self.driver_path_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Driver Path (.exe)", None))
#if QT_CONFIG(tooltip)
        self.browse_driver_path_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"browse", None))
#endif // QT_CONFIG(tooltip)
        self.browse_driver_path_pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"* Required Only in Advanced Scraping", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Show automated browser", None))
        self.show_browser_yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.show_browser_no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"* In Advanced mode, show the automated browser", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Auto Save All:", None))
        self.auto_save_yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.auto_save_no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"* Automatically save all scraped tables in csv format. (Can be found in History Folder)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Only Visible", None))
        self.visible_yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.visible_no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"* Ignore hidden, and scrapes only visible tables", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
#if QT_CONFIG(tooltip)
        self.csv_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"comma seperated values", None))
#endif // QT_CONFIG(tooltip)
        self.csv_radioButton.setText(QCoreApplication.translate("MainWindow", u"csv", None))
#if QT_CONFIG(tooltip)
        self.xlsx_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"excel", None))
#endif // QT_CONFIG(tooltip)
        self.xlsx_radioButton.setText(QCoreApplication.translate("MainWindow", u"xlsx", None))
        self.file_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.extension_label.setText(QCoreApplication.translate("MainWindow", u".csv", None))
#if QT_CONFIG(tooltip)
        self.export_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Export", None))
#endif // QT_CONFIG(tooltip)
        self.export_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.back_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"back", None))
#endif // QT_CONFIG(tooltip)
        self.back_pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.url_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://tables-site.com", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
#if QT_CONFIG(tooltip)
        self.basic_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"basic mode to scrape tables from static pages", None))
#endif // QT_CONFIG(tooltip)
        self.basic_radioButton.setText(QCoreApplication.translate("MainWindow", u"Basic", None))
#if QT_CONFIG(tooltip)
        self.advanced_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"advanced mode to scrapes tables from  javascript-driven pages", None))
#endif // QT_CONFIG(tooltip)
        self.advanced_radioButton.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
#if QT_CONFIG(tooltip)
        self.scrape_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Run", None))
#endif // QT_CONFIG(tooltip)
        self.scrape_pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.prev_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.prev_pushButton.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.current_index_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.total_results_label.setText(QCoreApplication.translate("MainWindow", u"/3", None))
#if QT_CONFIG(tooltip)
        self.next_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next_pushButton.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.loading_text_label.setText("")
        self.loading_indicator_label.setText("")
#if QT_CONFIG(tooltip)
        self.go_back_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"back", None))
#endif // QT_CONFIG(tooltip)
        self.go_back_pushButton.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.about_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

