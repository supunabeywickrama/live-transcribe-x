import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class SubtitleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 24px;")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.resize(800, 120)
        self.move(100, 800)

    def set_text(self, text):
        self.label.setText(text)

def run_test_ui():
    app = QApplication(sys.argv)
    window = SubtitleWindow()
    window.set_text("Test subtitle line")
    window.show()
    sys.exit(app.exec())
