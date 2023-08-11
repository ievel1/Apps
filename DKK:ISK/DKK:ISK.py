import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont

class CurrencyConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Currency Converter")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        self.currency_labels = {
            "ISK": QLabel("ISK:"),
            "DKK": QLabel("DKK:"),
            "USD": QLabel("USD:"),
            "EUR": QLabel("EUR:")
        }

        self.currency_inputs = {
            "ISK": QLineEdit(),
            "DKK": QLineEdit(),
            "USD": QLineEdit(),
            "EUR": QLineEdit()
        }

        layout = QVBoxLayout()
        for currency in ["ISK", "DKK", "USD", "EUR"]:
            self.currency_labels[currency].setFont(QFont("Arial", 14))
            self.currency_inputs[currency].setFont(QFont("Arial", 14))
            self.currency_inputs[currency].textChanged.connect(lambda _, c=currency: self.update_equivalents(c))

            layout.addWidget(self.currency_labels[currency])
            layout.addWidget(self.currency_inputs[currency])

            self.currency_inputs[currency].setStyleSheet("QLineEdit { padding: 8px; }")

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_equivalents(self, source_currency):
        try:
            amount = float(self.currency_inputs[source_currency].text())

            # Disconnect the signals temporarily to prevent recursion
            for currency in self.currency_inputs:
                self.currency_inputs[currency].textChanged.disconnect()

            for currency, input_field in self.currency_inputs.items():
                if currency != source_currency:
                    equivalent = amount * self.exchange_rates[currency] / self.exchange_rates[source_currency]
                    input_field.setText(f"{equivalent:.2f}")

            # Reconnect the signals
            for currency in self.currency_inputs:
                self.currency_inputs[currency].textChanged.connect(lambda _, c=currency: self.update_equivalents(c))

        except ValueError:
            for input_field in self.currency_inputs.values():
                input_field.clear()

    def set_exchange_rates(self, exchange_rates):
        self.exchange_rates = exchange_rates

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverterApp()

    # Exchange rates (1 unit of each currency to DKK)
    exchange_rates = {
        "DKK": 1,
        "ISK": 19.39,
        "USD": 0.147,
        "EUR": 0.134
    }
    window.set_exchange_rates(exchange_rates)


    # Set stylesheet for the whole app
    app.setStyleSheet("QMainWindow { background-color: #f2f2f2; }")

    window.show()
    sys.exit(app.exec_())
