import pyxel

scr_width = 90
scr_height = 90
jumper_power = [1, 2, 3, 4, 5, 6]
jumper_height = [0, 0, 0, 0, 0, 0]
jumper_col = [8, 10, 14, 7, 9, 1]
jumper_time = [0, 0, 0, 0, 0, 0]
jumper_max = [0, 0, 0, 0, 0, 0]
g = 0.327 # 重力加速度
# g = 0.5

def high_cal(o, height):
    return scr_height - height - o

def jumper(who):
    jumper_time[who] += 1
    t = jumper_time[who]
    jumper_height[who] = jumper_power[who] * t - 0.5 * g * t ** 2
    if jumper_height[who] <= 0:
        jumper_height[who] = 0
        jumper_time[who] = 0
    jumper_max[who] = max(jumper_height[who], jumper_max[who])
    pyxel.rect(who * 15 + 5, high_cal(10, jumper_height[who]) - 5, 5, 5, jumper_col[who])
    pyxel.line(who * 15 + 5, high_cal(10, jumper_max[who]) - 5, who * 15 + 15, high_cal(10, jumper_max[who]) - 5, jumper_col[who])

def scr():
    pyxel.cls(6)
    pyxel.rect(0, scr_height - 10, scr_width, 10, 3)
    # pyxel.rect(0, scr_height - 8, scr_width, 8, 11)
    # for i in range(scr_width // 2):
        # pyxel.pset(i * 2, scr_height - 10 + 4, 9)
    # for i in range(scr_width // 4):
            # pyxel.pset(i * 4 + 1, scr_height - 10 + 3, 9)
    # pyxel.rect(0, scr_height - 10 + 5, scr_width, 10 - 5, 9)
    pyxel.text(5, 5, f"g = {g}", 7)


pyxel.init(scr_width, scr_height)

while True:
    scr()
    for who in range(6):
        jumper(who)
    pyxel.flip()
