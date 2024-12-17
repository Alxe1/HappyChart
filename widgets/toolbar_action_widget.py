import os
import pickle

from PySide6.QtCore import Slot, Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog

import pandas as pd
import matplotlib.pyplot as plt


class ToolbarActionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.df = None

        self.parent = parent

        self.table = self.parent.table

    @Slot()
    def import_file(self):
        file_filter = "Excel file (*.xlsx *.xls);;Data file (*.xlsx *.csv *.dat)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select file",
            filter=file_filter,
            selectedFilter=os.getcwd()
        )
        if response[0] == "":
            return

        if response[0].split(".")[-1] in ["xlsx", "xls"]:
            self.df = pd.read_excel(response[0])
        elif response[0].split(".")[-1] in ["csv", "dat"]:
            self.df = pd.read_csv(response[0], sep=",")
        else:
            return

        if self.df.size == 0:
            return

        self.parent.set_df(self.df)
        dtypes = self.df.dtypes
        for i, dtype in enumerate(dtypes):
            if dtype == "object":
                self.df.fillna({self.df.columns[i]: ""}, inplace=True)
            else:
                self.df.fillna({self.df.columns[i]: 0}, inplace=True)

        self.table.setRowCount(self.df.shape[0])
        self.table.setColumnCount(self.df.shape[1])
        self.table.setHorizontalHeaderLabels(self.df.columns)

        for row in self.df.iterrows():
            values = row[1]
            for col, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = "{0:0}".format(value)
                table_item = QTableWidgetItem(str(value))
                self.table.setItem(row[0], col, table_item)

    @Slot()
    def export_file(self):
        response = QFileDialog.getSaveFileName(parent=self, caption="Save data", filter="Excel file (*.xlsx *xls)")
        if response[0] == "":
            return

        column_headers = []
        for j in range(self.table.model().columnCount()):
            column_headers.append(self.table.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=column_headers)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                df.at[row, column_headers[col]] = item.text()

        # TODO: check dtypes
        df.to_excel(response[0], index=False)

    @Slot()
    def save(self):
        response = QFileDialog.getSaveFileName(parent=self, caption="Save", filter="HappyChart (*.hc)")
        if response[0] == "":
            return
        pickle.dump(self.df, open(response[0], "wb"))

    @Slot()
    def open(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select file",
            filter="HappyChart (*.hc)",
            selectedFilter=os.getcwd()
        )
        if response[0] == "":
            return
        self.df = pickle.load(open(response[0], "rb"))

        self.df.fillna("", inplace=True)
        self.table.setRowCount(self.df.shape[0])
        self.table.setColumnCount(self.df.shape[1])
        self.table.setHorizontalHeaderLabels(self.df.columns)

        for row in self.df.iterrows():
            values = row[1]
            for col, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = "{0:0}".format(value)
                table_item = QTableWidgetItem(str(value))
                self.table.setItem(row[0], col, table_item)

        self.parent.set_df(self.df)

    def create_new_window(self):
        window = type(self.parent)()
        window.setAttribute(Qt.WA_DeleteOnClose)
        window.setGeometry(self.parent.geometry().translated(20, 20))

        self.parent._instances.append(window)
        window.destroyed.connect(lambda: self.parent._instances.remove(window))

        # window.raise_()
        window.show()
        window.activateWindow()

    def export_image(self):
        response = QFileDialog.getSaveFileName(parent=self,
                                               caption="Save Image",
                                               filter="Image file (*.png *.jpg *.jpeg *.svg *.tif *.PDF)")
        if response[0] == "":
            return

        # self.parent.chart.fig.savefig(response[0])
        if response[0].split(".")[-1] in ["pdf", "PDF"]:
            import matplotlib.backends.backend_pdf
            plt.savefig(response[0], format="pdf")
        elif response[0].split(".")[-1] in ["svg", "SVG"]:
            import matplotlib.backends.backend_svg
            plt.savefig(response[0], backend="svg")
        elif response[0].split(".")[-1] in ["png", "PNG"]:
            plt.savefig(response[0], format="png")
        elif response[0].split(".")[-1] in ["jpg", "jpeg", "JPG", "JPEG"]:
            plt.savefig(response[0], format="jpeg")
        else:
            plt.savefig(response[0])

    def doc_help(self):
        QDesktopServices.openUrl(QUrl("https://www.littlely.top/happychart-manual"))

    def chart_layer_triggered(self, e):
        self.parent.chart_dialog_clicked(e)



