from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton,QApplication
import sys


class ChatBot(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)

        # add text area
        self.text_area = QTextEdit(self)
        self.text_area.setGeometry(10,10,400,500)
        self.text_area.setReadOnly(True)

        # add input area
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10,520,400,20)

        # add button

        self.send = QPushButton('send', self)
        self.send.setGeometry(420,520,40,20)

        self.show()


app = QApplication(sys.argv)

main_window = ChatBot()

sys.exit(app.exec())