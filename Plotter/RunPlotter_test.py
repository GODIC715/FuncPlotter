from PySide2 import QtCore
from RunPlotter import *
import pytest

@pytest.fixture
def window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    return window

# # @pytest.mark.xfail
# def test_sth(window,qtbot):
    
#     # messagebox = window.findChild(QtWidgets.QMessageBox)
#     messagebox = window.findChild(QMessageBox)
#     assert messagebox.text() == "somestringthat is not valid to use in math expression"


def test_Qt(qtbot, monkeypatch):

    qtbot.keyClicks(window.functionInput,"Some String that's bound to fail")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.Yes)
    simple.query()
    assert simple.answer