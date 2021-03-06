import EightFigurePuzzle.eight_figure as ef

flag = False
tracked = []
max_depth = ef.mp_size * ef.mp_size
count = 0
name = "backtrack"


def in_tracked(map1):
    for mp in tracked:
        if ef.compare(mp.get("map"), map1.get("map")):
            return True
    else:
        return False


def backtrack(b, e):
    global flag, count

    count = 0

    print("searching backtrack ...")

    flag = False

    m = {"map": b, "parent": None}
    temp = __backtrack(m, e, 0)
    out_asr = []
    if flag:
        asr = [temp.get("map")]
        p = temp.get("parent")
        while p is not None:
            for i in tracked:
                if ef.compare(p, i.get("map")):
                    asr.append(i.get("map"))
                    p = i.get("parent")
                    break
        out_asr = asr.copy()
        print("answer: ")
        while len(asr):
            ef.printMap(asr.pop())
            print()
    else:
        print(flag)
    return out_asr


def __backtrack(b, e, depth):
    """
    回溯算法递归函数
    :param b: 当前情形
    :param e: 结束情形
    :param depth: 当前搜索的步数
    :return: 结果节点
    """
    global flag, tracked, count

    count += 1
    # 如果结果一致，则弹出
    if ef.compare(b.get("map"), e):
        flag = True
        return b
    # 到达最大搜索路径
    if depth >= max_depth:
        return None
    if in_tracked(b):
        return None
    else:
        tracked.append(b)
    pos = b
    nxt_pos = []
    idx = 0
    while idx < 4:
        mmp = pos.get("map")
        # 如果可以朝哪个方向移动，将移动后的情形加入栈
        if ef.can_motion[idx](mmp):
            nxt_pos.append({"map": ef.motion[idx](mmp),
                            "parent": mmp})
        idx += 1

    # 对于所有可能出现的情况，都进行一次递归
    for i in nxt_pos:
        asr = __backtrack(i, e, depth + 1)
        # 如果找到结果
        if flag:
            return asr

    # 没找到结果返回当前节点
    return b


if __name__ == '__main__':
    b, e = ef.init_map()
    backtrack(b, e)
    print(count)
