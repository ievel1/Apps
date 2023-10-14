import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
import requests
import json

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
            "EUR": QLabel("EUR:"),
            "CNY": QLabel("CNY:")
        }

        self.currency_inputs = {
            "ISK": QLineEdit(),
            "DKK": QLineEdit(),
            "USD": QLineEdit(),
            "EUR": QLineEdit(),
            "CNY": QLineEdit()
        }

        layout = QVBoxLayout()
        for currency in ["ISK", "DKK", "USD", "EUR", "CNY"]:
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
    url = "https://cdn.forexvalutaomregner.dk/api/latest.json"
    target_cur = ["DKK", "ISK", "USD", "EUR", "CNY"]
    set_base = ["USD"]
    
    

    try:
        response = requests.get(url)
        # Exchange rates (1 unit of each currency to DKK)
        if response.status_code == 200:
            data = response.json()
            exchange_rates = {currency: data["rates"].get(currency) for currency in target_cur}
            window.set_exchange_rates(exchange_rates)

            with open("exchange_rates.json", "w") as f:
                json.dump(exchange_rates, f)

        else:
            print("Failed to fetch exchange rates, using cached rates")
            with open("exchange_rates" "r") as f:
                exchange_rates = json.load(f)
    except:
        print("No internet connection, using cahced rates")
        with open("exchange_rates.json", "r") as f:
            exchange_rates = json.load(f)
    window.set_exchange_rates(exchange_rates)

    # Set stylesheet for the whole app
    app.setStyleSheet("QMainWindow { background-color: #f2f2f2; }")

    window.show()
    sys.exit(app.exec_())
