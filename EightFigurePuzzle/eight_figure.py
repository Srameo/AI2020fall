import random

mp_size = 3  # 地图大小


def init_map():
    """初始化地图的函数，通过从结束位置随机走来达到一定有解的目的"""
    end_pos = []
    for i in range(1, mp_size * mp_size + 1):
        end_pos.append(i)
    end_pos[-1] = 0
    steps = random.randint(mp_size * mp_size * 2, mp_size * mp_size * 2 + 5)
    print(steps)
    i = 0
    begin_pos = end_pos.copy()
    while i < steps:
        mov = random.randint(0, 3)
        if can_motion[mov](begin_pos):
            begin_pos = motion[mov](begin_pos)
            i += 1
    return begin_pos, end_pos


def zero_loc(mp):
    """查找一个地图中0的位置"""
    i = 0
    while i < mp_size * mp_size:
        if mp[i] == 0:
            return i
        i += 1
    return -1


def can_up(mp):
    """判断能否向上走"""
    zero = zero_loc(mp)
    return zero - mp_size > 0


def can_down(mp):
    """判断能否向下走"""
    zero = zero_loc(mp)
    return zero + mp_size < mp_size * mp_size


def can_left(mp):
    """判断能否往左走"""
    zero = zero_loc(mp)
    return zero % mp_size > 0


def can_right(mp):
    """判断能否往右走"""
    zero = zero_loc(mp)
    return zero % mp_size < mp_size - 1


def up(mp: list):
    """
    0 向上移动
    :return: 移动是否成功
    """
    mp = mp.copy()
    zero = zero_loc(mp)
    mp[zero] = mp[zero - mp_size]
    mp[zero - mp_size] = 0
    zero -= mp_size
    return mp


def down(m: list):
    """
    0 向下移动
    :return: 移动是否成功
    """
    mp = m.copy()
    zero = zero_loc(mp)
    mp[zero] = mp[zero + mp_size]
    mp[zero + mp_size] = 0
    zero += mp_size
    return mp


def left(m: list):
    """
    0 向左移动
    :return: 移动是否成功
    """
    mp = m.copy()
    zero = zero_loc(mp)
    mp[zero] = mp[zero - 1]
    mp[zero - 1] = 0
    zero -= 1
    return mp


def right(m: list):
    """
    0 向右移动
    :return: 移动是否成功
    """
    mp = m.copy()
    zero = zero_loc(mp)
    mp[zero] = mp[zero + 1]
    mp[zero + 1] = 0
    zero += 1
    return mp


motion = [up, down, left, right]
can_motion = [can_up, can_down, can_left, can_right]


def compare(map1, map2):
    """比较两个地图是否相同"""
    i = 0
    while i < mp_size * mp_size:
        if map1[i] != map2[i]:
            return False
        i += 1
    return True


def printMap(mp):
    """打印一个地图"""
    idx = 1
    for i in mp:
        print("{0:4}".format(i), end='')
        if idx % mp_size == 0:
            print('\n', end='')
        idx += 1


def as_str(mp):
    """将地图转换成字符串"""
    idx = 1
    s = ""
    for i in mp:
        s += "{0:4}".format(i)
        if idx % mp_size == 0:
            s += "\n"
        idx += 1
    s += "\n"
    return s


if __name__ == '__main__':
    pass
