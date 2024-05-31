from PyQt5.QtWidgets import QApplication, QMainWindow
from Xulyrangbuoc import Ui_MainWindow as Ui_Xulyrangbuoc
from HomePage import Ui_MainWindow as Ui_HomePage
from Phanlichthi import Ui_MainWindow as UI_Phanlichthi
import sys

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.ui.Button_Xulyrangbuoc.clicked.connect(self.switch_to_xulyrangbuoc)
        self.ui.Button_Phancathi.clicked.connect(self.switch_to_xeplichthi)

    def switch_to_xulyrangbuoc(self):
        self.window = QMainWindow()  # Tạo một cửa sổ QMainWindow mới
        self.ui_xulyrangbuoc = Ui_Xulyrangbuoc()  # Tạo một đối tượng Ui_Xulyrangbuoc mới
        self.ui_xulyrangbuoc.setupUi(self.window)  # Cài đặt giao diện vào cửa sổ mới
        self.window.show()
    def switch_to_xeplichthi(self):
        self.window = QMainWindow()  
        self.ui_xeplichthi = UI_Phanlichthi()  
        self.ui_xeplichthi.setupUi(self.window) 
        self.window.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())
