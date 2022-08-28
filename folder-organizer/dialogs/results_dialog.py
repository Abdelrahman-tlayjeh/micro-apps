from UI.results_dialog_ui import Ui_Dialog, QDialog


class ResultsDialog():
    def __init__(self, title:str, succeed:str, faile:str, details:str) -> None:
        #setuo ui
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        #ok button
        ui.ok_pushButton.clicked.connect(lambda: Dialog.close())
        #display content
        for content, container in zip((title, succeed, faile, details), (ui.title_label, ui.succeed_label, ui.faile_label, ui.textBrowser)):
            container.setText(content)
        #if no details
        if not details:
            ui.textBrowser.hide()

        #minimize size
        Dialog.resize(0, 0)
        #run
        Dialog.exec()