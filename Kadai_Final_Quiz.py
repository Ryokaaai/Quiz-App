# ステージ２(クイズ)

# モジュールのインポート
from distutils import core
import tkinter
from tkinter import messagebox
import random
import csv

print("＜ステージ２＞クイズに挑戦しよう！")
print("合計6問あります。全問正解して次のステージに進む権利を得よう！")

# クイズの情報を格納したファイル
CSV_FILE = "Quizes.csv"

cor = 0
class Quiz():
    def __init__(self, master):
        '''コンストラクタ
            master:クイズ画面を配置するウィジェット
        '''

        # 親ウィジェット
        self.master = master

        # クイズデータリスト
        self.quiz_list = []

        # 現在表示中のクイズ
        self.now_quiz = None

        # 現在選択中の選択肢番号
        self.choice_value = tkinter.IntVar()

        self.getQuiz()
        self.createWidgets()
        self.showQuiz()

    def getQuiz(self):
        '''クイズの情報を取得する'''

        # ファイルを開く
        try:
            f = open(CSV_FILE)
        except FileNotFoundError:
            return None

        # CSVデータとしてファイル読み込み
        csv_data = csv.reader(f)

        # CSVの各行をリスト化
        for quiz in csv_data:
            self.quiz_list.append(quiz)

        f.close()

    def createWidgets(self):
        '''ウィジェットを作成・配置する'''

        # フレームを作成する
        self.frame = tkinter.Frame(
            self.master,
            width=400,
            height=200,
        )
        self.frame.pack()

        # ボタンを作成する
        self.button = tkinter.Button(
            self.master,
            text="OK",
            command=self.checkAnswer
        )
        self.button.pack()

    def showQuiz(self):
        '''問題と選択肢を表示'''

        # まだ表示していないクイズからクイズ情報をランダムに取得
        num_quiz = random.randrange(len(self.quiz_list))
        quiz = self.quiz_list[num_quiz]

        # 問題を表示するラベルを作成
        self.problem = tkinter.Label(
            self.frame,
            text=quiz[0]
        )
        self.problem.grid(
            column=0,
            row=0,
            columnspan=4,
            pady=10
        )

        # 選択肢を表示するラジオボタンを3つ作成
        self.choices = []
        for i in range(3):
            # ラジオボタンウィジェットを作成・配置
            choice = tkinter.Radiobutton(
                self.frame,
                text=quiz[i+1],
                variable=self.choice_value,
                value=i
            )
            choice.grid(
                row=1,
                column=i,
                padx=10,
                pady=10,
            )
            # ウィジェットを覚えておく
            self.choices.append(choice)

        # 表示したクイズは再度表示しないようにリストから削除
        self.quiz_list.remove(quiz)

        # 現在表示中のクイズを覚えておく
        self.now_quiz = quiz

    def deleteQuiz(self):
        '''問題と選択肢を削除'''

        # 問題を表示するラベルを削除
        self.problem.destroy()

        # 選択肢を表示するラジオボタンを削除
        for choice in self.choices:
            choice.destroy()

    
    def checkAnswer(self):
        '''解答が正解かどうかを表示し、次のクイズを表示する'''
        # 正解かどうかを確認してメッセージを表示
        if self.choice_value.get() == int(self.now_quiz[4]):
            messagebox.showinfo("結果", "正解です！！")
            global cor
            cor += 1
            
        else:
            messagebox.showerror("結果", "不正解です...")

        # 表示中のクイズを非表示にする
        self.deleteQuiz()

        if self.quiz_list:
            # まだクイズがある場合は次のクイズを表示する
            self.showQuiz()
        else:
            # もうクイズがない場合はアプリを終了する
            self.endAppli()
        
    


    def endAppli(self):
        '''アプリを終了する'''

        # クイズがもうないことを表示
        self.problem = tkinter.Label(
            self.frame,
            text= (f"クイズはこれで終了です。結果はターミナルを確認してね！")
        )
        self.problem.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )
        # OKボタンのcommandを変更
        self.button.config(
            command=self.master.destroy
        )
        # 最終結果
        global cor
        print(f"結果:6問中{cor}問正解です。")

        if cor == 6:
            print("全問正解おめでとう！次のステージに進む権利を得ました！\n")
            import Kadai_Final_Pi
            
        else:
            print("全問正解ならず...ゲームオーバーです。")
            key = input("もう一度挑戦するにはEnterキーを、終了するにはqを押してください\n")
            if key == "":
                import Kadai_Final_Quiz
                import imp
                imp.reload(Kadai_Final_Quiz)
            elif key == "q":
                print("お疲れ様でした！")
                exit()

app = tkinter.Tk()
quiz = Quiz(app)
app.mainloop()