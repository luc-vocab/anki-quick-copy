# import the main window object (mw) from aqt
import aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
#from aqt.utils import getFile
import aqt.utils
import anki.lang
# import all of the Qt GUI library
#from aqt.qt import *
import aqt.importing
from anki import hooks
from aqt import gui_hooks
import anki.importing.csvfile 

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

class SmartImportDialog(aqt.importing.ImportDialog):
    def __init__(self, mw, importer) -> None:
        aqt.importing.ImportDialog.__init__(self, mw, importer)

class SmartTextImporter(anki.importing.csvfile.TextImporter):

    def __init__(self, col, file: str) -> None:
        anki.importing.csvfile.TextImporter.__init__(self, col, file)

def smartImport():
    # launch import dialog

    # ask user for file
    filt = "*.csv"
    file = aqt.utils.getFile(mw, anki.lang._("Smart Import"), None, key="import", filter=filt)
    if not file:
        return
    file = str(file)

    #aqt.qt.importing.importFile(mw, file)
    #importer = aqt.importing.Im(mw.col, file)
    importer = SmartTextImporter(mw.col, file)
    diag = SmartImportDialog(mw, importer)

    


# create a new menu item, "test"
action = aqt.QAction("Smart Import...", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(smartImport)
# and add it to the tools menu
mw.form.menuTools.addAction(action)