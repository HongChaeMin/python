import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setCustomToolTip()
        self.setPushButton()
        self.setQuitButton()
        self.setWindow()

    def setCustomToolTip(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁에 사용될 폰트를 설정
        self.setToolTip('This is a <b>QWidget</b> widget') # setToolTip() 메서드를 사용해서, 표시될 텍스트를 입력

    def setPushButton(self):
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 푸시 버튼을 하나 만들고, 이 버튼에도 툴팁을 달아준다
        btn.move(10, 10)
        btn.resize(btn.sizeHint())

    def setQuitButton(self):
        # 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 객체 (app)
        btn = QPushButton('Quit', self)  # 푸시 버튼을 하나 만들기
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

    def setWindow(self):
        self.setWindowTitle('My First Application')  # 제목 설정
        # self.move(300, 300) # 위젯의 스크린 이동
        # self.resize(400, 200) # 위젯 크기
        self.setWindowIcon(QIcon('web.png'))  # 에플리케이션 아이콘을 설정
        self.setGeometry(300, 300, 700, 500)  # 창의 위치와 크기를 설정 move() + resize()
        self.show()  # 스크린에 보여주기


if __name__ == '__main__':  # 현재 모듈의 이름이 저장되는 내장 변수
    app = QApplication(sys.argv)  # 모든 PyQt5 에플리케이션은 에플리케이션 객체를 생성
    ex = MyApp()
    sys.exit(app.exec_())
