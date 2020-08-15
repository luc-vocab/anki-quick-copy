# import the main window object (mw) from aqt
import aqt
import aqt.editor
import aqt.gui_hooks
from PyQt5.QtWidgets import QApplication

# using this hook, copy the field we're interested in into the clipboard editor_did_load_note

def editor_loaded_note(editor: aqt.editor.Editor):
    field_data = editor.note["Chinese"]
    clipboard = QApplication.clipboard()
    clipboard.setText(field_data)


aqt.gui_hooks.editor_did_load_note.append(editor_loaded_note)
