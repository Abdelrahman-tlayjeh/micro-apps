from UI.loading_screen_ui import Ui_Dialog, QDialog
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QSplashScreen
from PySide6.QtCore import Qt


class LoadingScreen:
    def __init__(self, starting_text:str) -> None:
        #setup ui
        self.Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(self.Dialog)
        #loading indicator
        self.indicator = QMovie(r"icons\loading_gear.gif")
        ui.indicator_label.setMovie(self.indicator)
        self.indicator.start()
        #set msg
        ui.text_label.setText(starting_text)
        #show dialog
        self.Dialog.show()        



# class LoadingScreen(QSplashScreen):
#     def __init__(self, flags=0):
#         super().__init__()
#         self.movie = QMovie(r"icons\loading_gear.gif", parent=self)
#         self.movie.frameChanged.connect(self.handleFrameChange)
#         self.movie.start()

#     def updateProgress(self, count=0):
#         if count == 0:
#             message = 'Starting...'
#         elif count > 0:
#             message = f'Processing... {count}'
#         else:
#             message = 'Finished!'
#         self.showMessage(
#             message, Qt.AlignHCenter | Qt.AlignBottom, Qt.white)

#     def handleFrameChange(self):
#         pixmap = self.movie.currentPixmap()
#         self.setPixmap(pixmap)
#         self.setMask(pixmap.mask())