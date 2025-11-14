import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainUI import Ui_MainWindow  # replace 'your_ui_file' with the actual filename without .py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect toolbar actions to page switching methods
        self.ui.actionHome.triggered.connect(self.show_home_page)
        self.ui.actionEmployees.triggered.connect(self.show_employees_page)
    
    def show_home_page(self):
        # Set stackedWidget to show page_1 (index 0)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def show_employees_page(self):
        # Set stackedWidget to show page_2 (index 1)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
