import EightFigurePuzzle.eight_figure as ef

flag = False
tracked = []
max_depth = ef.mp_size * ef.mp_size * 4
count = 0


def backtrack(b, e):
    print("searching backtrack ...")

    m = {"map": b, "parent": None}
    temp = __backtrack(m, e, 0)
    out_asr = None
    if flag:
        asr = [temp.get("map")]
        p = temp.get("parent")
        while p is not None:
            for i in tracked:
                if ef.compare(p, i.get("map")):
                    asr.append(i.get("map"))
                    p = i.get("parent")
                    break
        out_asr = asr
        print("answer: ")
        while len(asr):
            ef.printMap(asr.pop())
            print()
    else:
        print(flag)
    return out_asr


def __backtrack(b, e, depth):
    global flag, tracked, count

    # 如果结果一致，则弹出
    if ef.compare(b.get("map"), e):
        flag = True
        return b
    # 到达最大搜索路径
    if depth > max_depth:
        return None
    if b in tracked:
        return None
    else:
        tracked.append(b)
    count += 1
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

    for i in nxt_pos:
        asr = __backtrack(i, e, depth + 1)
        if flag:
            return asr

    return b


if __name__ == '__main__':
    b, e = ef.init_map()
    backtrack(b, e)
    print(count)
