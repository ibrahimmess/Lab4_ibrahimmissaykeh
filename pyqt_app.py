import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("PyQt Demo")
    layout = QVBoxLayout()
    label = QLabel("Click the button")
    btn = QPushButton("Say Hello")
    def on_click():
        label.setText("Hello from PyQt!")
    btn.clicked.connect(on_click)
    layout.addWidget(label)
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(320, 160)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
  
