# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import EightFigurePuzzle.eight_figure as ef
import EightFigurePuzzle.backtrack.core.backtrack as bt
import EightFigurePuzzle.dfs.core.dfs as d
import EightFigurePuzzle.bfs.core.bfs as bf
import EightFigurePuzzle.a_star.core.a_star as astar
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b, e = ef.init_map()

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
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
