import sys
import time
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QDialog
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt, QTimer
import EightFigurePuzzle.eight_figure as ef
import EightFigurePuzzle.dfs.core.dfs as DFS
import EightFigurePuzzle.bfs.core.bfs as BFS
import EightFigurePuzzle.a_star.core.a_star as ASTAR
import EightFigurePuzzle.backtrack.core.backtrack as BACKTRACK


# 用枚举类表示方向
class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class MainPage(QWidget):
    """ 八数码主体 """

    def __init__(self):
        super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.gltMain = QGridLayout()
        self.mp_size = ef.mp_size
        self.begin, self.end = ef.init_map()
        self.timer = QTimer(self)  # 初始化一个定时器
        self.a_star_timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法

        self.initUI()

    def initUI(self):
        # 设置方块间隔
        self.gltMain.setSpacing(10)

        self.onInit()

        # 设置布局
        self.setLayout(self.gltMain)
        # 设置宽和高
        self.setFixedSize(400, 400)
        # 设置标题
        self.setWindowTitle('八数码问题')
        # 设置背景颜色
        self.setStyleSheet("background-color:gray;")
        self.show()

    # 初始化布局
    def onInit(self):
        # 产生顺序数组
        self.mp_size = ef.mp_size
        self.begin, self.end = ef.init_map()
        self.numbers = self.begin
        self.blocks.clear()

        # 将数字添加到二维数组
        for row in range(self.mp_size):
            self.blocks.append([])
            for column in range(self.mp_size):
                temp = self.numbers[row * self.mp_size + column]

                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)

        self.updatePanel()

    # 检测按键
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_D:
            start = time.time()
            self.asr = DFS.dfs(self.begin, self.end)
            spend_time = time.time() - start
            steps = len(self.asr)
            if DFS.flag:
                self.timer.start(500)  # 设置计时间隔并启动
                ip = InfoPage(self, "Training Success In DFS!\n"
                                    "begin:\n" + ef.as_str(self.begin) +
                                    "time: " + str(spend_time) + "\n"
                                    "visited nodes: " + str(DFS.count) + "\n"
                                    "result steps: " + str(steps))
                ip.show()
            else:
                ip = InfoPage(self, "Training Failed In DFS!\n")
                ip.show()

        elif key == Qt.Key_S:
            ASTAR.a_star_visualize(self, self.begin, self.end)

        elif key == Qt.Key_B:
            start = time.time()
            self.asr = BFS.bfs(self.begin, self.end)
            spend_time = time.time() - start
            steps = len(self.asr)
            if BFS.flag:
                self.timer.start(500)  # 设置计时间隔并启动
                ip = InfoPage(self, "Training Success In BFS!\n"
                                    "begin:\n" + ef.as_str(self.begin) +
                                    "time: " + str(spend_time) + "\n"
                                    "visited nodes: " + str(BFS.count) + "\n"
                                    "result steps: " + str(steps))
                ip.show()
            else:
                ip = InfoPage(self, "Training Failed In BFS!\n")
                ip.show()

        elif key == Qt.Key_A:
            start = time.time()
            self.asr = ASTAR.a_star(self.begin, self.end)
            spend_time = time.time() - start
            steps = len(self.asr)
            if ASTAR.flag:
                self.timer.start(500)  # 设置计时间隔并启动
                ip = InfoPage(self, "Training Success In ASTAR!\n"
                                    "begin:\n" + ef.as_str(self.begin) +
                                    "time: " + str(spend_time) + "\n"
                                    "visited nodes: " + str(ASTAR.count) + "\n"
                                    "result steps: " + str(steps))
                ip.show()
            else:
                ip = InfoPage(self, "Training Failed In ASTAR!\n")
                ip.show()

        elif key == Qt.Key_T:
            start = time.time()
            self.asr = BACKTRACK.backtrack(self.begin, self.end)
            spend_time = time.time() - start
            steps = len(self.asr)
            if BACKTRACK.flag:
                self.timer.start(500)  # 设置计时间隔并启动
                ip = InfoPage(self, "Training Success In BACKTRACK!\n"
                                    "begin:\n" + ef.as_str(self.begin) +
                                    "time: " + str(spend_time) + "\n"
                                    "visited nodes: " + str(BACKTRACK.count) + "\n"
                                    "result steps: " + str(steps))
                ip.show()
            else:
                ip = InfoPage(self, "Training Failed In BACKTRACK!\n")
                ip.show()

        elif key == Qt.Key_R:
            self.begin, self.end = ef.init_map()
            self.numbers = self.begin
            self.onInit()

        elif key == Qt.Key_3:
            ef.mp_size = 3
            for i in range(self.gltMain.count()):
                self.gltMain.itemAt(i).widget().deleteLater()
            self.onInit()

        elif key == Qt.Key_4:
            ef.mp_size = 4
            for i in range(self.gltMain.count()):
                self.gltMain.itemAt(i).widget().deleteLater()
            self.onInit()

    def operate(self):
        if self.asr:
            self.numbers = self.asr.pop()
            self.updateBlocks()
            self.updatePanel()
        else:
            self.timer.stop()

    def updateBlocks(self):
        self.blocks.clear()
        for row in range(self.mp_size):
            self.blocks.append([])
            for column in range(self.mp_size):
                temp = self.numbers[row * self.mp_size + column]
                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)

    def updatePanel(self):
        for row in range(self.mp_size):
            for column in range(self.mp_size):
                self.gltMain.addWidget(Block(self.blocks[row][column]), row, column)
        self.setLayout(self.gltMain)


class Block(QLabel):
    """ 数字方块 """

    def __init__(self, number):
        super().__init__()

        self.number = number
        self.setFixedSize(80, 80)

        # 设置字体
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)

        # 设置字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)

        # 设置文字位置
        self.setAlignment(Qt.AlignCenter)

        # 设置背景颜色\圆角和文本内容
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:brown;border-radius:10px;")
            self.setText(str(self.number))


class InfoPage(QDialog):

    def __init__(self, parent=None, info="No Info"):
        super(InfoPage, self).__init__(parent)
        self.info = info
        self.setStyleSheet("background: black")
        self.label = QLabel(info, self)
        self.label.show()
        # 设置宽和高
        self.setFixedSize(400, 400)
        self.move(0, 0)

    def setString(self, s):
        self.label.setText(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec_())
