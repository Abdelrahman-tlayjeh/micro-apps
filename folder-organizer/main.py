from UI.app_ui import Ui_MainWindow, QApplication, QMainWindow
from PySide6.QtWidgets import QFileDialog, QLineEdit
from lib.folder_organizer import  FolderOrganizer
from dialogs.message_dialog import MessageBox
from dialogs.results_dialog import ResultsDialog
from dialogs.info_dialog import InfoDialog
from os import DirEntry
from json import load, dump
import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

_organizer = FolderOrganizer(r"config\categories.json")
_folder_content = []
_settings:dict

#=== starting state ===#
ui.dont_touch_add_frame.hide()


#========== buttons to switch between pages ==========#
ui.start_program_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
ui.settings_pushButton.clicked.connect(lambda: show_settings())
ui.menu_pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
ui.back_pushButton.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))


#========== handle dialogs ==========#
def show_message_box(msg:str) -> None:
    MessageBox(msg)


#========== Settings ==========#
#--- settings helpers ---#
def _load_settings() -> None:
    """load setting from [settings.json] and save in [_settings] global variable"""
    global _settings
    with open(r"config\settings.json") as f:
        _settings = load(f)


def _update_settings():
    """change settings in [_settings] and [settings.json] """
    global _settings
    #save all settings
    with open(r"config\settings.json", "w") as f:
        _settings["folders"] = True if ui.include_folder_yes_radioButton.isChecked() else False
        _settings["unknownFiles"] = True if ui.include_unk_files_yes_radioButton.isChecked() else False
        _settings["dontTouch"] = [ui.dont_touch_listWidget.item(index).text() for index in range(ui.dont_touch_listWidget.count())]
        _settings["outputName"] = ui.output_folder_name_lineEdit.text()
        #dump to json file
        dump(_settings, f, indent=4)


#--- settings main methods ---#
def show_settings():
    """Load settings from [Settings.json] and switch to settings page"""
    _load_settings()
    #display saved settings
    ui.include_folder_yes_radioButton.setChecked(True) if _settings["folders"] else ui.include_folders_no_radioButton.setChecked(True)
    ui.include_unk_files_yes_radioButton.setChecked(True) if _settings["unknownFiles"] else ui.include_unk_files_no_radioButton.setChecked(True)
    ui.dont_touch_listWidget.clear()
    ui.dont_touch_listWidget.addItems(_settings["dontTouch"])
    ui.output_folder_name_lineEdit.setText(_settings["outputName"])
    #switch to s3ettings page
    ui.stackedWidget.setCurrentIndex(1)


def toggle_add_new_dont_touch():
    """hide/show the container of [add new dont_touch item]"""
    ui.dont_touch_add_frame.hide() if ui.dont_touch_add_frame.isVisible() else ui.dont_touch_add_frame.show()


def add_new_dont_touch():
    """add new name to dont_touch list if entered name is valid"""
    new_name = ui.dont_touch_add_lineEdit.text().strip()
    #check new name
    if not new_name:
        #empty name
        show_message_box("Invalid Name!")
        return
    if new_name in _settings["dontTouch"]:
        #name already exist
        show_message_box("New name already exist!")
        return

    #add to listWidget and update seettings
    ui.dont_touch_listWidget.addItem(new_name)
    _update_settings()
    #hide new_name container
    ui.dont_touch_add_frame.hide()
    #select added item and set focus on it
    ui.dont_touch_listWidget.setCurrentRow(ui.dont_touch_listWidget.count() - 1)
    ui.dont_touch_listWidget.setFocus()


def delete_selected_dont_touch():
    """delete selected dont_touch item"""
    if not ui.dont_touch_listWidget.selectedItems():
        return
    #remove selected item and update settings
    ui.dont_touch_listWidget.takeItem(ui.dont_touch_listWidget.selectedIndexes()[0].row())
    _update_settings()


def change_output_folder_name():
    """change the output folder name if entered name is valid"""
    if (not ui.output_folder_name_lineEdit.text().strip()):
        show_message_box("Invalid name!")
        ui.output_folder_name_lineEdit.setText(_settings["outputName"])
        return
    #change and update in json
    _update_settings()


#--- settings buttons ---#
ui.include_folder_yes_radioButton.clicked.connect(_update_settings)
ui.include_folders_no_radioButton.clicked.connect(_update_settings)
ui.include_unk_files_yes_radioButton.clicked.connect(_update_settings)
ui.include_unk_files_no_radioButton.clicked.connect(_update_settings)
ui.output_folder_name_save_pushButton.clicked.connect(change_output_folder_name)
ui.dont_touch_add_pushButton.clicked.connect(toggle_add_new_dont_touch)
ui.dont_touch_confirm_add_pushButton.clicked.connect(add_new_dont_touch)
ui.dont_touch_delete_pushButton.clicked.connect(delete_selected_dont_touch)


#========== App ==========#
#--- helpers ---#
def _getFolderPath() -> str:
    """open a FileDialog and return the path of selected folder"""
    return QFileDialog.getExistingDirectory(caption="Choose a Folder")


def _get_selected_content() -> list[DirEntry]:
    """return a list of selected items as [os.DirEntry]"""
    if ui.select_all_checkBox.isChecked():
        #return all
        return _folder_content
    #return selected
    return [_folder_content[m.row()] for m in ui.content_listWidget.selectedIndexes()]


def _select_location(lineEdit:QLineEdit):
    location =  _getFolderPath()
    if location:
        lineEdit.setText(location)


#--- Load content ---#
def browse_location():
    location =  _getFolderPath()
    if location:
        _organizer.change_path(location)
        ui.folder_path_lineEdit.setText(location)
        show_content()
        show_stats()
        

def show_content():
    global _folder_content
    #clear listWidget
    ui.content_listWidget.clear()
    _folder_content = []
    for item in _organizer._scandir():
        _folder_content.append(item)
        ui.content_listWidget.addItem(item.name)


def show_stats():
    #clear textBox
    ui.content_stats_textBrowser.clear()
    stats = _organizer.get_stats()
    for k, v in stats.items():
        ui.content_stats_textBrowser.append(f"{k}: {v}")


def toggle_content_list():
    #select all
    if ui.select_all_checkBox.isChecked():
        ui.content_listWidget.clearSelection()
        ui.content_listWidget.setEnabled(False)
    #enable manual selection
    else:
        ui.content_listWidget.setEnabled(True)


#load/handle content buttons
ui.select_all_checkBox.clicked.connect(toggle_content_list)
ui.browse_folder_pushButton.clicked.connect(browse_location)


#--- organize ---#
def show_results(done_items:int, errors:list):
    ResultsDialog(
                "Task Finished...",
                f"{done_items} Successfully moved.",
                f"{len(errors)} errors.",
                "\n".join([f"{name} --> {error}" for name, error in errors])
            )

def organize():
    content = _get_selected_content()
    #if no content
    if not content:
        return

    #if no selected option
    if not any((ui.org_categories_radioButton.isChecked(), ui.org_extension_radioButton.isChecked())):
        return

    #by extension
    if ui.org_extension_radioButton.isChecked():
        out = _organizer.organize_by_extensions(output_folder_name=_settings["outputName"], content=content, include_folders=_settings["folders"], include_unknown=_settings["unknownFiles"],dont_touch=_settings["dontTouch"])
    #by categories
    else:
        out = _organizer.organize_by_categories(output_folder_name=_settings["outputName"], content=content, include_folders=_settings["folders"], include_unknown=_settings["unknownFiles"],dont_touch=_settings["dontTouch"])

    show_results(*out)    
    show_content()
    show_stats()
    

#buttons
ui.org_run_pushButton.clicked.connect(organize)
ui.org_info_pushButton.clicked.connect(lambda: InfoDialog("""
Organizing by extensions will place all files with the same extension in One folder.
Organizing by categories will place all files with the same category in one folder.(Check config\categories.json)
""", size=(500, 270)))


#--- Rename ---#
def rename():
    content = _get_selected_content()
    #no content
    if not content:
        return

    name_pattern = ui.rename_name_lineEdit.text().strip()
    #if no name pattern
    if not name_pattern:
        return

    #rename
    out = _organizer.rename_content(name_pattern, content)
    ResultsDialog(
                "Task Finished...",
                f"{len(out[0])} Successfully renamed.",
                f"{len(out[1])} errors.",
                "\n".join([f"{name} --> {error}" for name, error in out[1]])
            )
    
    show_content()
    show_stats()


#buttons
ui.rename_run_pushButton.clicked.connect(rename)
ui.rename_info_pushButton.clicked.connect(lambda: InfoDialog("""
a pattern should be a string with at least one sepecial character such that:
    - []: to be replaced by an indexe.
    - {}: to be replaced by the old name.
[!] If the pattern does not contain any special character and many files are selected, an '[]' will be added automatically at the end of the pattern.
""", size=(600, 320)))


#--- Change extension ---#
def change_extension():
    content = _get_selected_content()
    #not selected content
    if not content:
        return

    current_extension = ui.ext_from_lineEdit.text().strip()
    new_extension = ui.ext_to_lineEdit.text().strip()
    #if no inputs
    if not (current_extension and new_extension):
        return
    
    out = _organizer.change_extensions(current_extension, new_extension, content)
    ResultsDialog(
            "Task Finished...",
            f"{out[0]} Successfully changed.",
            f"{len(out[1])} errors.",
            "\n".join([f"{name} --> {error}" for name, error in out[1]])
            )

    show_content()
    show_stats()


#buttons
ui.ext_run_pushButton.clicked.connect(change_extension)
ui.ext_info_pushButton.clicked.connect(lambda: InfoDialog("""
Change the extension of all selected files that have the entered <from> extension to the entered <to> extension.
e.g: [png] >> [jpeg]
""", size=(450, 250)))


#--- move ---#
def move():
    content = _get_selected_content()
    #not selected content
    if not content:
        return
    
    destination = ui.move_location_lineEdit.text().strip()
    #if no destination path
    if not destination:
        return

    #move
    out = _organizer.move_content(destination, content)
    ResultsDialog(
            "Task Finished...",
            f"{out[0]} Successfully moved.",
            f"{len(out[1])} errors.",
            "\n".join([f"{name} --> {error}" for name, error in out[1]])
            )

    show_content()
    show_stats()


#buttons
ui.move_run_pushButton.clicked.connect(move)
ui.move_browse_location_pushButton.clicked.connect(lambda: _select_location(ui.move_location_lineEdit))

#--- copy ---#
def copy():
    content = _get_selected_content()
    #not selected content
    if not content:
        return
    
    destination = ui.copy_location_lineEdit.text().strip()
    #if no destination path
    if not destination:
        return

    #move
    out = _organizer.copy_content(destination, content)
    ResultsDialog(
            "Task Finished...",
            f"{out[0]} Successfully copied.",
            f"{len(out[1])} errors.",
            "\n".join([f"{name} --> {error}" for name, error in out[1]])
            )

    show_content()
    show_stats()

#buttons
ui.copy_run_pushButton.clicked.connect(copy)
ui.copy_browse_location_pushButton.clicked.connect(lambda: _select_location(ui.copy_location_lineEdit))


#--- Delete ---#
def delete():
    content = _get_selected_content()
    #not selected content
    if not content:
        return

    out = _organizer.delete_content(content)
    ResultsDialog(
            "Task Finished...",
            f"{out[0]} Successfully deleted.",
            f"{len(out[1])} errors.",
            "\n".join([f"{name} --> {error}" for name, error in out[1]])
            )
            
    show_content()
    show_stats()


#buttons
ui.delete_run_pushButton.clicked.connect(delete)


#========== Run ==========#
def run_app():
    #load settings
    _load_settings()
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_app()