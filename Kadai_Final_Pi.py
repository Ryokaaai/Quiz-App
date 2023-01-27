# ステージ3(モンテカルロ法)

print("＜ステージ３＞モンテカルロ法の実験に参加しよう！\n")
key = input("実行回数を入力してね！：")
times = int(key)

# ランダムに点を打つ(0以上1未満)
from ast import increment_lineno
import random
x = []
y = []
for i in range(times):
    x.append(random.random())
    y.append(random.random())
#print(x)
#print(y)

# 点が4分の1の円の中にあるか
import math
circle = 0
for i in range(0,times):
    if math.sqrt(x[i] ** 2 + y[i] ** 2) < 1:
        circle += 1
    
#print(circle)

# 4分の1に収まる確率を求め、それを4倍する
R = circle / times
pi = 4 * R
print(f"確率から計算したPIは、{pi}です。")
print(f"実際のPIとは、{abs(math.pi - pi) / math.pi * 100}%の誤差があります。")

# 描画
import numpy as np
import matplotlib.pyplot as plt

c1 = plt.Circle((0, 0), radius=1, fc="None", ec="r", linewidth=2, color = "black")
ax = plt.gca()
ax.add_patch(c1)
plt.axis("scaled")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("PLOT")

plt.scatter(x, y, marker=".", color = "blue", label = "POINT")
print("グラフを閉じると次に進めます！")
plt.show()

end = input("もう一度実験するにはEnterキーを、実験を終了するにはqを入力してください。")
if end == "":
    import Kadai_Final_Pi
    import imp
    imp.reload(Kadai_Final_Pi)

elif end == "q":
    print("お疲れ様でした！またの挑戦をお待ちしております！")
    exit()