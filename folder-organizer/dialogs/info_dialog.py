from UI.info_dialog_ui import Ui_Dialog, QDialog


class InfoDialog():
    def __init__(self, msg:str, size:tuple[int]=(600,300)) -> None:
        #setup ui
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        #display message
        ui.textBrowser.setText(msg)
        #setup ok button
        ui.ok_pushButton.clicked.connect(lambda: Dialog.close())
        #minimize box size
        Dialog.resize(*size)
        #run
        Dialog.exec_()
