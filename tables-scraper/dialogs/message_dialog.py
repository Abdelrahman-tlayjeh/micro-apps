from UI.message_dialog_ui import Ui_Dialog, QDialog


class MessageBox():
    def __init__(self, msg:str) -> None:
        #setup ui
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        #display message
        ui.label.setText(msg)
        #setup ok button
        ui.pushButton.clicked.connect(lambda: Dialog.close())
        #run
        Dialog.exec()