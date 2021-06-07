import sys
import time
import random
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('panel.ui')[0]

def nlen(n):
    r = 0
    while n != 0:
        n //= 10; r += 1
    return r

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Pushbuttons
        self.btn_go.clicked.connect(self.pick)
        self.btn_quit.clicked.connect(self.qexit)
        # DEV-ING self.btn_save.clicked.connect(self.save)

    # Pick!
    def pick(self):
        try:
            start = int(self.numstart.text())
            end = int(self.numend.text())
            l = list(x for x in range(start, end+1))
            exclude = self.numexclude.text().split()
            for i in exclude:
                i = int(i)
                if i in l: l.remove(i)
            n = end-start+1 - len(exclude)
            if start <= 0:
                self.result.setText("?")
            elif n > 80:
                self.result.setText("80명 이상은 작동하지 않습니다.")
            else:
                pick = random.sample(l, n)
                ret = ''
                for i in range(max(0, n//10)+1):
                    ret += ', '.join(str(x).rjust(nlen(end)) for x in pick[10*i:10*(i+1)]) + '\n'
                self.result.setText(ret.rstrip())
        except Exception:
            pass

    # Saves result as txt file
    # NEEDS FURTHER DEVELOPMENT
    '''
    def save(self):
        with open(f'{time.strftime("%Y%m%d %H:%M 추첨 결과")}.txt', mode=='w') as f:
            f.write(self.result.text())
    '''

    # Custom sys.exit() function
    def qexit(self):
        print("프로그램 종료"); sys.exit()

# Run
if __name__ == '__main__':
    print("프로그램 준비 중...")
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    print("프로그램 준비 완료")
    app.exec_()
