import sys

from PyQt5.QtWidgets import QApplication

import EightFigurePuzzle.eight_figure as ef
import EightFigurePuzzle.backtrack.core.backtrack as bt
import EightFigurePuzzle.dfs.core.dfs as d
import EightFigurePuzzle.bfs.core.bfs as bf
import EightFigurePuzzle.a_star.core.a_star as astar
import time

from EightFigurePuzzle.visualize.core.printMatrix import MainPage


b, e = ef.init_map()


def print_hi(name):
    print(f'Hi, {name}')


def run_func(f, cls):
    global b, e

    start = time.time()
    steps = len(f(b, e))
    all_time = time.time() - start

    tplt = "{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}"
    print(tplt.format("method", "result", "nodes", "steps", "time"))
    print(tplt.format(cls.name, cls.flag, cls.count, steps, all_time))
    print("begin:\n" + ef.as_str(b))

    print_hi('AI Search')


def run():
    global b, e

    start = time.time()
    d_steps = len(d.dfs(b, e))
    d_time = time.time() - start

    start = time.time()
    bt_steps = len(bt.backtrack(b, e))
    bt_time = time.time() - start

    start = time.time()
    bf_steps = len(bf.bfs(b, e))
    bf_time = time.time() - start

    start = time.time()
    a_star_steps = len(astar.a_star(b, e))
    a_star_time = time.time() - start

    tplt = "{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}"
    print(tplt.format("method", "result", "nodes", "steps", "time"))
    print(tplt.format("dfs", d.flag, d.count, d_steps, d_time))
    print(tplt.format("bfs", bf.flag, bf.count, bf_steps, bf_time))
    print(tplt.format("backtrack", bt.flag, bt.count, bt_steps, bt_time))
    print(tplt.format("A-Star", astar.flag, astar.count, a_star_steps, a_star_time))
    print("begin:\n" + ef.as_str(b))

    print_hi('AI Search')


def command_help():
    print("指令集")
    print("3      :   把地图变为3*3，即8数码问题")
    print("4      :   把地图变为4*4，即15数码问题")
    print("begin  :   显示开始map")
    print("end    :   显示结束map")
    print("h      :   显示指令集")
    print("r      :   刷新地图")
    print("run    :   分别使用dfs, bfs, backtrack, A-star算法搜索当前地图")
    print("v      :   显示可视化界面")
    print("\t在可视化界面中的操作")
    print("\ta : 使用A-star算法搜索当前地图")
    print("\tb : 使用bfs算法搜索当前地图")
    print("\td : 使用dfs算法搜索当前地图")
    print("\tt : 使用backtrack算法搜索当前地图")
    print("\tr : 刷新初始地图")
    print("\t3 : 把地图变为3*3，即8数码问题")
    print("\t4 : 把地图变为4*4，即15数码问题")
    print("\ts : 显示A-star算法的搜索过程")
    print("backtrack: 使用backtrack算法搜索当前地图")
    print("astar  :   使用A-star算法搜索当前地图")
    print("bfs    :   使用bfs算法搜索当前地图")
    print("dfs    :   使用dfs算法搜索当前地图")
    print("q      :   退出")


def command(c):
    global b, e
    if c == '3':
        ef.mp_size = 3
        b, e = ef.init_map()
        print("map size changed to 3!")
    elif c == '4':
        ef.mp_size = 4
        b, e = ef.init_map()
        print("map size changed to 4!")
    elif c == 'h' or c == 'help':
        command_help()
    elif c == 'r' or c == 'refresh':
        b, e = ef.init_map()
        print("map refreshed!")
    elif c == "run":
        run()
    elif c == "v" or c == "visualize":
        app = QApplication(sys.argv)
        ex = MainPage()
        app.exec_()
    elif c == "dfs":
        run_func(d.dfs, d)
    elif c == "bfs":
        run_func(bf.bfs, bf)
    elif c == "astar":
        run_func(astar.a_star, astar)
    elif c == "backtrack":
        run_func(bt.backtrack, bt)
    elif c == "begin" or c == "b":
        print("begin:")
        ef.printMap(b)
    elif c == "end" or c == "e":
        print("end:")
        ef.printMap(e)
    else:
        print("没有此指令，请重新输入！")


def lab1_main_thread():
    command_help()
    c = input("请输入指令: ")
    while c != 'q':
        command(c)
        c = input("请输入指令: ")
    print("bye!")
