# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(583, 424)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #505581;\n"
"}\n"
"\n"
"#title_label{\n"
"	color: white;\n"
"	margin-bottom: 15px;\n"
"}\n"
"\n"
"#succeed_label{\n"
"	color: rgb(85, 255, 0);\n"
"}\n"
"\n"
"#faile_label{\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: #F4D35E;\n"
"	color: #505581;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(244, 187, 95);\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.succeed_label = QLabel(Dialog)
        self.succeed_label.setObjectName(u"succeed_label")
        font1 = QFont()
        font1.setPointSize(14)
        self.succeed_label.setFont(font1)
        self.succeed_label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.succeed_label)

        self.faile_label = QLabel(Dialog)
        self.faile_label.setObjectName(u"faile_label")
        self.faile_label.setFont(font1)
        self.faile_label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.faile_label)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.ok_pushButton = QPushButton(Dialog)
        self.ok_pushButton.setObjectName(u"ok_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_pushButton.sizePolicy().hasHeightForWidth())
        self.ok_pushButton.setSizePolicy(sizePolicy)
        self.ok_pushButton.setMinimumSize(QSize(0, 30))
        self.ok_pushButton.setFont(font1)
        self.ok_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.ok_pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_label.setText("")
        self.succeed_label.setText("")
        self.faile_label.setText("")
        self.ok_pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

