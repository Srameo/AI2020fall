import EightFigurePuzzle.eight_figure as ef

count = 0
flag = False  # flag 表示最终是否找到数据
name = "bfs"


def in_list(mp, lst):
    for mp1 in lst:
        if ef.compare(mp.get("map"), mp1.get("map")):
            return True
    else:
        return False


def bfs(b, e):
    """
    宽度优先搜索实现
    :param b: 起始状态
    :param e: 结束状态
    :return: 一个包含路径的栈
    """
    global count, flag
    print("searching bfs ...")

    mp = {"map": b, "board": 0, "parent": None}  # 最初的情形，宽度用于判断是否跳出，parent用于最后输出所有路径
    end_pos = e  # 结束节点
    board = ef.mp_size * ef.mp_size  # 探索的最大深度
    untracked = []  # 维护一个所有没探索过节点的队列
    tracked = []  # 维护一个所有已经探索过节点的队列

    untracked.append(mp)
    out_asr = []  # 输出的结果
    temp = None
    flag = False
    count = 0

    # 当还有没探索过的节点时
    while len(untracked):
        # 探索队列内第一个节点
        temp = untracked[0].copy()
        tracked.append(untracked.pop(0))
        count += 1
        # 如果到达目标则跳出
        if ef.compare(temp.get("map"), end_pos):
            flag = True
            break
        # 若果超过探索宽度的限制也跳出
        if temp.get("board") > board:
            continue

        maybe = []  # 在当前情况的基础下，所有可能出现的情形
        idx = 0
        while idx < 4:
            mmp = temp.get("map")
            # 如果可以朝哪个方向移动，将移动后的情形加入队列
            if ef.can_motion[idx](mmp):
                maybe.append({"map": ef.motion[idx](mmp),
                              "board": temp.get("board") + 1,
                              "parent": mmp})
            idx += 1

        # 如果可能出现的情形并没有在未探索队列中且未在已探索队列中，则加入未探索队列
        for mb in maybe:
            if not in_list(mb, untracked):
                if not in_list(mb, tracked):
                    untracked.append(mb.copy())

    # 如果找到通路，则输出
    if flag:
        asr = [temp.get("map")]
        p = temp.get("parent")
        while p is not None:
            for i in tracked:
                if ef.compare(p, i.get("map")):
                    asr.append(i.get("map"))
                    p = i.get("parent")
                    break
        print("answer: ")
        out_asr = asr.copy()
        while len(asr):
            ef.printMap(asr.pop())
            print()
    else:
        print(flag)

    return out_asr


if __name__ == '__main__':
    b, e = ef.init_map()
    bfs(b, e)
