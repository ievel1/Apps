import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class CurrencyConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Currency Converter")
        self.setGeometry(100, 100, 300, 200)

        self.init_ui()

    def init_ui(self):
        self.isk_label = QLabel("ISK:")
        self.isk_input = QLineEdit()

        self.dkk_label = QLabel("DKK:")
        self.dkk_input = QLineEdit()

        self.convert_to_dkk_button = QPushButton("Convert to DKK")
        self.convert_to_isk_button = QPushButton("Convert to ISK")

        layout = QVBoxLayout()
        layout.addWidget(self.isk_label)
        layout.addWidget(self.isk_input)
        layout.addWidget(self.dkk_label)
        layout.addWidget(self.dkk_input)
        layout.addWidget(self.convert_to_dkk_button)
        layout.addWidget(self.convert_to_isk_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.convert_to_dkk_button.clicked.connect(self.convert_to_dkk)
        self.convert_to_isk_button.clicked.connect(self.convert_to_isk)

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()

    def convert_to_dkk(self):
        try:
            isk_amount = float(self.isk_input.text())
            dkk_equivalent = isk_amount * 0.051  # hardcoded exchange rate
            self.dkk_input.setText(f"{dkk_equivalent:.2f}")
        except ValueError:
            self.show_error_message("Invalid input. Please enter a valid number.")

    def convert_to_isk(self):
        try:
            dkk_amount = float(self.dkk_input.text())
            isk_equivalent = dkk_amount * 19.36  # hardcoded exchange rate
            self.isk_input.setText(f"{isk_equivalent:.2f}")
        except ValueError:
            self.show_error_message("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverterApp()
    window.show()
    sys.exit(app.exec_())
