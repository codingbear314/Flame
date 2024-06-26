from Flame import *

print("Let's start the game!")

while True:
    WordEntered = input("Enter a starting word >>> ")
    if not WordEntered:
        continue
    if not IsInDatabase(WordEntered):
        print("Enter a valid word!")
        continue
    if not IsThereAWordStartingWith(WordEntered[-1]):
        print("There is no word starting with {}".format(WordEntered[-1]))
        continue
    break
print("First word is {}".format(WordEntered))
LastWord = WordEntered

while True:
    response = Negamax(WordEntered[-1], 3, -float('inf'), float('inf'))[1]
    LastWord = response
    print("AI : {}".format(response))
    if len(TwoSounds(response[-1])) == 2:
        print("두음법칙 사용 가능! : {}".format(*TwoSounds(response[-1])))
    if not IsThereAWordStartingWith(response[-1]):
        print("{}으로 시작하는 단어는 없으므로, AI 승리".format(response[-1]))
        exit()
    WordEntered = None
    while True:
        WordEntered = input("Enter a starting word >>> ")
        if not WordEntered:
            continue
        if WordEntered in ['hint', '도움', '힌트', '도와줘', '모르겠어']:
            print(f"{LastWord[-1]}로 시작하는 단어는 총 {Heuristics(LastWord[-1])}개 있습니다. 이중 하나로는 '{Negamax(LastWord[-1], 1, -float('inf'), float('inf'))[1]}' (이)가 있습니다.")
            continue
        if WordEntered in ['기권', 'resign', 'give up', 'exit', 'quit', 'stop']:
            print("인간 기권, AI 승리")
            exit()
        # if not IsInDatabase(WordEntered):
        #    print("Enter a valid word!")
        #    continue
        if WordEntered[0] not in TwoSounds(LastWord[-1]):
            print("Enter a word starting with {}".format(LastWord[-1]))
            continue
        if WordEntered in History:
            print("Enter a new word!")
            continue
        break
    LastWord = WordEntered
    History.add(WordEntered)
    if not IsThereAWordStartingWith(WordEntered[-1]):
        print("You win!")
        break