from window.main import Main, QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("")
    main = Main()
    main.show()
    app.exec()