import EightFigurePuzzle.eight_figure as ef

count = 0  # 记录总共探索的节点数
flag = False  # 记录是否有解
depth = ef.mp_size * ef.mp_size  # 探索的深度


def in_list(mp, lst):
    """
    判断一个地图的值是否在列表中
    :param mp: 需要判断的地图
    :param lst: 目标列表
    :return: 是否存在
    """
    for mp1 in lst:
        if ef.compare(mp.get("map"), mp1.get("map")):
            return True
    else:
        return False


def F(mp1):
    """
    返回一个数据的总消耗: F + G
    :param mp1: 需要计算的数据
    :return: 消耗
    """
    return mp1.get("G") + mp1.get("H")


def G(begin, map1):
    """
    从起点开始到当前节点的cost, 实际存储到地图的结构体中
    :param begin: 起始节点
    :param map1: 结束节点
    :return: G
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
        # 通过计算当前位置和目标位置的欧几里得距离
        cost += abs(x - end_x) + abs(y - end_y)
    return cost


def a_star(b, e):
    """
    a_star 算法的实现
    :param b: 开始的地图
    :param e: 目标地图
    :return: 存有解题过程的栈
    """
    global flag, depth, count
    print("searching A-Star ...")

    flag = False
    count = 0

    mp = {"map": b, "G": 0, "parent": None, "H": H(b, e)}
    end_pos = e

    untracked = [mp.copy()]  # 所有已经发现但还没有探索过的节点
    tracked = []  # 记录所有已经发现且已经探索过的节点
    temp = None  # 当前正在操作的节点

    while len(untracked):
        # 弹出总消耗（G+H）最小的当前地图
        temp = untracked[0].copy()
        # 加入已经探索的列表
        tracked.append(untracked.pop(0))
        count += 1

        # 如果到达目标则跳出
        if ef.compare(temp.get("map"), end_pos):
            flag = True
            break
        # 若果超过探索深度的限制也跳出
        if temp.get("G") > depth:
            continue

        maybe = []  # 在当前情况的基础下，所有可能出现的情形
        idx = 0
        while idx < 4:
            mmp = temp.get("map")
            # 如果可以朝哪个方向移动，将移动后的情形加入栈
            if ef.can_motion[idx](mmp):
                pos = ef.motion[idx](mmp)
                maybe.append({"map": pos,
                              "G": temp.get("G") + 1,  # 实际的步数在已有的步数上加一
                              "parent": mmp,
                              "H": H(pos, e)})  # 预测到最后的步数
            idx += 1

        for mp1 in maybe:
            # 如果已经探索，则什么操作也不做
            if in_list(mp1, tracked):
                continue
            for idx, mp2 in enumerate(untracked):
                if ef.compare(mp2.get("map"), mp1.get("map")):
                    # 如果已经发现，判断G消耗之间的关系，如果小则替代掉，反之则什么也不做
                    if mp1.get("G") > mp2.get("G"):
                        untracked[idx] = mp2.copy()
                        break
            else:
                # 如果当前节点没有被发现，则加入发现列表
                untracked.append(mp1)

        untracked.sort(key=F)  # 按照总消耗进行升序

    out_asr = []
    # 如果找到通路，则输出
    if flag:
        asr = [temp.get("map")]
        # 通过父节点进行判断
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
