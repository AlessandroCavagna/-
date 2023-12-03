import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.initUI()

    def initUI(self):
        connection = sqlite3.connect("coffee.sqlite")
        a = connection.cursor()

        all_brands = a.execute("SELECT Brand FROM CoffeeInfo").fetchall()
        connection.close()

        self.NameCoffee.addItems(["Все"] + [i[0] for i in all_brands])

        self.GetInfo.clicked.connect(self.getData)

        self.colums = [
            "Sort",
            "Degree of roasting",
            "Ground/In grains",
            "Taste",
            "Price",
            "Packing value",
        ]

    def getData(self):
        index = self.NameCoffee.currentText()

        connection = sqlite3.connect("coffee.sqlite")
        a = connection.cursor()

        if index != "Все":
            self.InfoTable.setColumnCount(6)
            self.InfoTable.setRowCount(0)
            self.InfoTable.setHorizontalHeaderLabels(
                ["Сорт", "Обжарка", "Статус", "Какой вкус", "Цена", "Объем упаковки"]
            )

            def getting_names(argument):
                name = str(
                    a.execute(
                        f'SELECT "{argument}" FROM CoffeeInfo WHERE Brand == "{index}"'
                    ).fetchall()[0][0]
                )
                return name

            id = str(
                a.execute(
                    f'SELECT ID FROM CoffeeInfo WHERE Brand == "{index}"'
                ).fetchall()[0][0]
            )
            column = 0
            self.InfoTable.setRowCount(1)
            self.InfoTable.setRowHeight(0, 75)
            for i in self.colums:
                self.InfoTable.setItem(0, column, QTableWidgetItem(getting_names(i)))
                column += 1

            connection.close()
        else:
            self.InfoTable.setColumnCount(7)
            self.InfoTable.setRowCount(0)
            self.InfoTable.setHorizontalHeaderLabels(
                [
                    "Бренд",
                    "Сорт",
                    "Обжарка",
                    "Статус",
                    "Какой вкус",
                    "Цена",
                    "Объем упаковки",
                ]
            )

            def getting_names(argument, i):
                name = str(
                    a.execute(
                        f'SELECT "{argument}" FROM CoffeeInfo WHERE Brand == "{i}"'
                    ).fetchall()[0][0]
                )
                return name

            id = "All"

            indexes = [
                i[0] for i in a.execute("SELECT Brand FROM CoffeeInfo").fetchall()
            ]

            row = 0
            for i in indexes:
                column = 1
                self.InfoTable.setRowCount(4)
                self.InfoTable.setItem(row, 0, QTableWidgetItem(str(i)))
                for j in self.colums:
                    self.InfoTable.setItem(
                        row, column, QTableWidgetItem(getting_names(j, i))
                    )
                    self.InfoTable.setRowHeight(row, 75)
                    column += 1
                row += 1

            self.CoffeeId.setText(f"ID: {id}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CoffeeInfo()
    ex.show()
    sys.exit(app.exec())