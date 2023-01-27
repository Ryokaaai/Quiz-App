# 期末課題
# ステージをクリアして円周率の実験に参加しよう！

## ステージ1(ジャンケン)
print("ステージをクリアして円周率の実験に参加しよう！\n")
print("＜ステージ1＞ジャンケンで勝負だ！")

# モジュールのインポート
import random as rand

# 変数の定義
# ユーザーの勝ち数、負け数、あいこ数の数
win = lose = draw = 0
# 現在何回目か
now = 1

# 何回勝負にするか決める
time = input("何回勝負にしたいですか？：")
total = int(time)


# ジャンケンの手と0,1,2の対応のリスト
te = ["グー", "チョキ", "パー"]

# 結果を定義する関数
def result(kekka):
    print(f"あなたの手は{te[user_te]}、CPUの手は{te[cpu_te]}なので、{kekka}です。")

# ユーザーが指定した回数までじゃんけんを繰り返す
while now <= total:
    print(f"{now}回目")

    # ユーザーの手を入力
    user_te_str = input("あなたの手を入力してください(0:グー 1:チョキ 2:パー)：")
    user_te = int(user_te_str)

    # コンピュータの手を入力
    cpu_te = int(rand.randint(0,2))

    # 結果の判定
    if (user_te == 0 or user_te == 1 or user_te == 2):
        now += 1
    
        if user_te == cpu_te:
            result("あいこ")
            draw += 1
        elif (user_te == 0 and cpu_te == 1) or (user_te == 1 and cpu_te == 2) or (user_te == 2 and cpu_te == 0):
            result("あなたの勝ち")
            win += 1
        else :
            result("あなたの負け")
            lose += 1
        print(f"現在{win}勝{lose}敗{draw}あいこです。\n")
           
    else : #エラー対処
        print("0~2の数字を入れてください")

    # 最終結果
    print(f"結果：あなたは{win}勝{lose}敗{draw}あいこでした。")

# 結果の判別
if draw == total or win == lose:
    print("勝敗がつきませんでしたね。ゲームオーバーです。")
    key = input("もう一度挑戦するにはEnterキーを、終了するにはqを押してください。\n")
    if key == "":
        import Kadai_Final
        import imp
        imp.reload(Kadai_Final)

    elif key == "q":
        print("お疲れ様でした！")
        exit()

elif win > lose:
    print("あなたの勝ちです。次のステージに進む権利を得ました！\n")
    import Kadai_Final_Quiz

else:
    print("あなたの負けです。ゲームオーバーです。")
    key = input("もう一度挑戦するにはEnterキーを、終了するにはqを押してください。\n")
    if key == "":
        import Kadai_Final
        import imp
        imp.reload(Kadai_Final)

    elif key == "q":
        print("お疲れ様でした！")
        exit()