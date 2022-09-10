from UI.app_ui import Ui_MainWindow, QApplication, QMainWindow, QAbstractTableModel, Qt
from PySide6.QtWidgets import QFileDialog
from json import load, dump
from scraper.tables_scraper import TablesScraper, pd
from dialogs.message_dialog import MessageBox
from PySide6.QtGui import QMovie
from os import path, mkdir
from datetime import datetime
import  sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

_settings:dict
_currentIndex:int = 0
_resultsCount:int = 0
_scraper = TablesScraper()

#========== navigations buttons ==========#
ui.start_program_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
ui.settings_pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
ui.menu_pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
ui.back_pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))


#========== settings ==========#
#--- settings helpers ---#
def _load_settings() -> None:
    """load setting from [settings.json] and save in [_settings] global variable"""
    global _settings
    with open(r"config\settings.json") as f:
        _settings = load(f)
    
    #show saved settings on UI
    ui.driver_path_lineEdit.setText(_settings["driverPath"])
    ui.show_browser_yes_radioButton.setChecked(_settings["showBrowser"])
    ui.auto_save_yes_radioButton.setChecked(_settings["autoSave"])
    ui.visible_no_radioButton.setChecked(not _settings["visibleOnly"])

#load settings
_load_settings()


def _update_settings() -> None:
    """change settings in [_settings] and [settings.json] """
    global _settings
    with  open(r"config\settings.json", "w") as f:
        _settings["driverPath"] = ui.driver_path_lineEdit.text().strip()
        _settings["showBrowser"] = ui.show_browser_yes_radioButton.isChecked()
        _settings["autoSave"] = ui.auto_save_yes_radioButton.isChecked()
        _settings["visibleOnly"] = ui.visible_yes_radioButton.isChecked()
        dump(_settings, f, indent=4)


def browse_driver_path():
    path = QFileDialog.getOpenFileName(caption="Select The Driver...", filter="Executable (*.exe)")
    if path:
        ui.driver_path_lineEdit.setText(path[0])


#--- settings buttons ---#
#driver path
ui.browse_driver_path_pushButton.clicked.connect(browse_driver_path)
ui.driver_path_lineEdit.textChanged.connect(_update_settings)
#show the browser
ui.show_browser_yes_radioButton.clicked.connect(_update_settings)
ui.show_browser_no_radioButton.clicked.connect(_update_settings)
#auto save
ui.auto_save_yes_radioButton.clicked.connect(_update_settings)
ui.auto_save_no_radioButton.clicked.connect(_update_settings)
#only visible
ui.visible_yes_radioButton.clicked.connect(_update_settings)
ui.visible_no_radioButton.clicked.connect(_update_settings)


#========== Main ==========#
#--- table model ---#
class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row()][index.column()]
            return value
    
    def rowCount(self, index) -> int:
        return self._data.shape[0]

    def columnCount(self, index) -> int:
        return self._data.shape[1]

    def clear(self):
        self.clear()


#--- main helpers ---#
def _display_table():
    try:
        table = _scraper._results[_currentIndex]
    except IndexError:
        table = pd.DataFrame()

    ui.tableView.setModel(TableModel(table))


def _handle_next_prev_buttons():
    ui.total_results_label.setText(f"/{_resultsCount}")
    ui.current_index_label.setText(f"{_currentIndex + 1 if _resultsCount else 0}")
    if _currentIndex + 1 < _resultsCount:
        ui.next_pushButton.setDisabled(False)
    else:
        ui.next_pushButton.setDisabled(True)

    if _currentIndex > 0:
        ui.prev_pushButton.setDisabled(False)
    else:
        ui.prev_pushButton.setDisabled(True)


def _handle_scraper_output(out):
    global _resultsCount, _currentIndex
    
    #error msg
    if type(out) is str:
        MessageBox(f"Error: {out}")
        _resultsCount = 0
        _currentIndex = 0
        _handle_next_prev_buttons()
        _display_table()

        return
    
    #if no result
    if out == 0:
        MessageBox(f"No Tables found! Re-check the URL or use advanced mode...")
        _resultsCount = 0
        _currentIndex = 0
        _handle_next_prev_buttons()
        _display_table()
        return

    #there is results
    _resultsCount = out
    _currentIndex = 0
    _handle_next_prev_buttons()
    _display_table()


def _auto_save():
    if not path.exists("History"):
        mkdir("History")

    for i in range(_resultsCount):
        file_name = f"{int(datetime.now().timestamp())}_{i}.csv"
        _scraper._results[i].to_csv(rf"History\{file_name}")


#--- Loading handler class---#
class LoadingIndicator:
    def __init__(self, starting_text:str) -> None:
        ui.loading_text_label.setText(starting_text)
        #indicator
        self.indicator = QMovie(r"icons\loading_gear.gif")
        ui.loading_indicator_label.setMovie(self.indicator)
        ui.frame.show()
        self.indicator.start()

    def update_text(self, new_text:str):
        ui.loading_text_label.setText(new_text)

    def end(self):
        self.indicator.stop()
        ui.frame.hide()

#--- main methods ---#
def next_result():
    global _currentIndex
    _currentIndex += 1
    _display_table()
    _handle_next_prev_buttons()


def prev_result():
    global _currentIndex
    _currentIndex -= 1
    _display_table()
    _handle_next_prev_buttons()
    
    
def run_scraper():
    #check url
    url = ui.url_lineEdit.text().strip()
    if not url:
        return

    #mode
    advanced = ui.advanced_radioButton.isChecked()
    if advanced:
        #if driver path is not given
        if not _settings["driverPath"]:
            MessageBox("The Driver Path is not given! Please enter it from settings in order to use the advanced mode.")
            ui.settings_pushButton.click()
            return

    #show loading indicator
    loading = LoadingIndicator("Working...")

    try:
        QApplication.instance().processEvents() #avoid Testil el GUI
        out = _scraper.scrape_tables(url, _settings["visibleOnly"], JsMode=advanced, driver_path=_settings["driverPath"], show_browser=_settings["showBrowser"])
    except Exception as e:
        out = e

    #hide loading indicator
    loading.end()
    
    #handle the output
    _handle_scraper_output(out)

    #auto save (if on)
    if _settings["autoSave"]:
        _auto_save()
    

ui.scrape_pushButton.clicked.connect(run_scraper)
ui.next_pushButton.clicked.connect(next_result)
ui.prev_pushButton.clicked.connect(prev_result)


#========== Export ==========#
def show_selected_extension():
    ext = ".csv" if ui.csv_radioButton.isChecked() else ".xlsx"
    ui.extension_label.setText(ext)


def export():
    #if there is nothing to export
    if not _resultsCount:
        return

    name = ui.file_name_lineEdit.text().strip()
    #if name is not entered
    if not name:
        return

    #checck output folder path
    if not path.exists("Output"):
        mkdir("Output")

    #export to csv
    if ui.csv_radioButton.isChecked():
        _scraper._results[_currentIndex].to_csv(rf"Output\{name}.csv")
        MessageBox(f"Successfully Saved as '{name}.csv'")
    #export to excel
    else:
        _scraper._results[_currentIndex].to_excel(rf"Output\{name}.xlsx")
        MessageBox(f"Successfully Saved as '{name}.xlsx'")


#--- export buttons---#
ui.export_pushButton.clicked.connect(export)
ui.csv_radioButton.clicked.connect(show_selected_extension)
ui.xlsx_radioButton.clicked.connect(show_selected_extension)


    
#--- Runnnn---#
def run():
    ui.frame.hide()
    _handle_next_prev_buttons()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()