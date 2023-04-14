import sys

from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,
QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1=QPushButton('Message',self) # 버튼 추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 핸들러 함수 연결
        
        self.btn2 = QPushButton('Message',self)
        self.btn1.clicked.connect(self.activateMessage)
        
        hbox = QHBoxLayout() # 수평박스 레이아웃을 추가하고 버튼 1, 2 추가
        hbox.addStretch(1) # 공백
        hbox.addWidget(self.btn1) # 버튼1 배치
        hbox.addWidget(self.btn2) # 버튼2 배치

        
        vbox=QVBoxLayout() # 수직 레이아웃 위젯 생성
        vbox.addStretch(self.te1) # 빈 공간
        # vbox.addWidget(self.btn1) # 버튼 위치
        # vbox.addStretch(1) # 빈 공간
        vbox.addLayout(hbox) # 빈공간 - 버튼 - 빈공간 순으로 수직 배치된 레이아웃 설정
        
        
        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) # 윈도우 아이콘 추가
        self.resize(256,256)
        self.show()
        
    def activateMessage(self): # 버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        # QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
    
    
    
    