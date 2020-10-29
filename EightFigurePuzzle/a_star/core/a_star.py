import EightFigurePuzzle.eight_figure as ef

count = 0
flag = False
depth = ef.mp_size * ef.mp_size


def F(mp1):
    return mp1.get("G") + mp1.get("H")


def G(begin, map1):
    """
    从起点开始到当前节点的cost, 实际存储到地图的结构体中
    :param begin:
    :param map1:
    :return:
    """
    pass


def H(map1: list, end: list):
    """
    从当前到结束的cost, 计算每个数字到目标位置最少的步数
    :param map1: 当前节点
    :param end: 结束节点
    :return: cost
    """
    cost = 0
    size = ef.mp_size
    for idx, i in enumerate(map1):
        end_idx = end.index(i)
        end_x, end_y = int(end_idx / size), end_idx % size
        x, y = int(idx / size), idx % size
        cost += abs(x - end_x) + abs(y - end_y)
    return cost


def a_star(b, e):
    global flag, depth, count
    print("searching A-Star ...")

    mp = {"map": b, "G": 0, "parent": None, "H": H(b, e)}
    end_pos = e

    untracked = [mp.copy()]
    tracked = []
    temp = None

    while len(untracked):
        temp = untracked[0].copy()
        tracked.append(untracked.pop(0))
        count += 1

        # 如果到达目标则跳出
        if ef.compare(temp.get("map"), end_pos):
            flag = True
            break
        # 若果超过探索深度的限制也跳出
        if temp.get("G") > depth:
            continue

        maybe = []                                  # 在当前情况的基础下，所有可能出现的情形
        idx = 0
        while idx < 4:
            mmp = temp.get("map")
            # 如果可以朝哪个方向移动，将移动后的情形加入栈
            if ef.can_motion[idx](mmp):
                pos = ef.motion[idx](mmp)
                maybe.append({"map": pos,
                              "G": temp.get("G") + 1,
                              "parent": mmp,
                              "H": H(pos, e)})
            idx += 1

        for mp1 in maybe:
            in_tracked = False
            for cls in tracked:
                if ef.compare(cls.get("map"), mp1.get("map")):
                    in_tracked = True
                    break
            if in_tracked:
                continue
            for idx, mp2 in enumerate(untracked):
                if ef.compare(mp2.get("map"), mp1.get("map")):
                    if mp1.get("G") > mp2.get("G"):
                        untracked[idx] = mp2
                        break
            else:
                untracked.append(mp1)

        untracked.sort(key=F)

    out_asr = []
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
    print(a_star(b, e))
