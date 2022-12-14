from UI.message_dialog_ui import Ui_Dialog, QDialog


class MessageBox():
    def __init__(self, msg:str, size:tuple[int]=(0,0)) -> None:
        #setup ui
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        #display message
        ui.label.setText(msg)
        #setup ok button
        ui.ok_pushButton.clicked.connect(lambda: Dialog.close())
        #minimize box size
        Dialog.resize(*size)
        #run
        Dialog.exec_()
