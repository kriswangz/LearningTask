

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox
import sys
sys.path.append('..')
from josephus.person import person
from josephus.josephus import Josephus
from josephus.file_adapter import read_files


class QTUI(object):
    def __init__(self, title: str):
        pass


class JosephusUIOnPyside2(QTUI):
    def __init__(self, title) -> None:
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 310)
        self.window.setWindowTitle(title)

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("Please input people's items")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('Generate survior', self.window)
        self.button.move(380, 80)
        self.button.clicked.connect(self.handle_button)

    def handle_button(self) -> None:
        people_info = self.textEdit.toPlainText()

        reader = []
        for row in people_info:
            data = row(read_files.str2list_row)
            reader.append(data)

        ring = Josephus.Ring(reader)
        ring.start = 0
        ring.step = 1

        res = ring.query_list_all()
        size_res = len(res)
        generator = ring.iter()

        survior = ''
        for i in range(size_res):
            some_one = next(generator)

            if some_one == None:
                break

            if i == size_res - 1:
                survior = 'Survivor\'s name is' + some_one.name + \
                    'age is' + some_one.age + 'gender is' + some_one.gender

            else:
                continue
        
        QmessageBox.about(self.window, 'Survior\'s items', survior)

if __name__ == "__main__":
    
    app = QApplication([])

    josephus_ui = JosephusUIOnPyside2('Josephus Project')

    josephus_ui.window.show()

    app.exec_()
