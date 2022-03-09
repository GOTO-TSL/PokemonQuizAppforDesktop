from multiprocessing import managers
from PokeModel import PokeModel
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sip
import random 

# メインウィンドウ
class MainWindow(QWidget):

    quizLabel = None
    answerView = None
    pokeModel = None

    def __init__(self) -> None:
        super().__init__()

        self.pokeModel = PokeModel(random.randint(1,900))
        self.initUI()

    def initUI(self):
        titleLabel = QLabel("図鑑説明:")
        self.quizLabel = QLabel("")
        self.quizLabel.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Black))

        self.answerView = AnswerWidget()
        self.hintButtonView = HintButtonView()

        self.answerView.answerButton.clicked.connect(self.validAnswer)
        # forループで回すとインデックスが全部3になるからあえてこうしている
        self.hintButtonView.hintButtons[0].clicked.connect(lambda: self.showHint(0))
        self.hintButtonView.hintButtons[1].clicked.connect(lambda: self.showHint(1))
        self.hintButtonView.hintButtons[2].clicked.connect(lambda: self.showHint(2))
        self.hintButtonView.hintButtons[3].clicked.connect(lambda: self.showHint(3))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(self.quizLabel)
        mainLayout.addWidget(self.hintButtonView)
        mainLayout.addWidget(self.answerView)
        self.setLayout(mainLayout)

        self.setWindowTitle("ポケモン図鑑クイズ")

        self.quizLabel.setText(self.pokeModel.flavorText)

    
    def validAnswer(self):
        userAnswer = self.answerView.answerTextBox.text()
        correctAnswer = self.pokeModel.pokemonName
        print(correctAnswer)

        if userAnswer == correctAnswer:
            QMessageBox.information(self, "結果", "正解", QMessageBox.Yes)
            self.pokeModel = PokeModel(random.randint(1, 900))
            self.quizLabel.setText(self.pokeModel.flavorText)
            self.answerView.answerTextBox.setText("")
        else:
            QMessageBox.information(self, "結果", "不正解", QMessageBox.Yes)
            self.answerView.answerTextBox.setText("")

    def showHint(self, index: int):
        QMessageBox.information(self, "結果", f"ヒント{index}\n{self.pokeModel.hints[index]}", QMessageBox.Yes)


# 解答欄をつくるView
class AnswerWidget(QWidget):

    answerTextBox = None
    answerButton = None

    def __init__(self) -> None:
        super().__init__()

        self.initLayout()

    def initLayout(self):

        self.answerTextBox = QLineEdit(self)
        self.answerButton = QPushButton("解答", self)

        layout = QHBoxLayout()
        layout.addWidget(self.answerTextBox)
        layout.addWidget(self.answerButton)

        self.setLayout(layout)

# ヒントのボタン4つをグリッド状に並べるView
class HintButtonView(QWidget):

    hintButtons = []

    def __init__(self) -> None:
        super().__init__()
        
        self.initLayout()

    def initLayout(self):

        self.hintButtons = [ QPushButton(f"ヒント{i}") for i in range(4)]

        layout = QGridLayout()
        layout.addWidget(self.hintButtons[0], 0, 0)
        layout.addWidget(self.hintButtons[1], 0, 1)
        layout.addWidget(self.hintButtons[2], 1, 0)
        layout.addWidget(self.hintButtons[3], 1, 1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # UI
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
