# Load database
# Load the database from the file

Database = dict()
with open('Dictionary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line[0] in Database:
            Database[line[0]].append(line.strip())
        else:
            Database[line[0]] = [line.strip()]

print('Database loaded')
print('Database key size:', len(Database), 'characters / 11172 characters')
print('Database value size:', sum([len(Database[key]) for key in Database]), 'words')

def Heuristics(EndingLetter):
    if EndingLetter not in Database:
        return 0
    return len(Database[EndingLetter])

print("Processing Database...")
for ky in Database:
    Database[ky].sort(key=lambda x: Heuristics(x[-1]))
print("Database processed")

TwoSoundRule = {
    '냑' : '약',
    '략' : '약',
    '냥' : '양',
    '량' : '양',
    '녀' : '여',
    '려' : '여',
    '녁' : '역',
    '력' : '역',
    '년' : '연',
    '련' : '연',
    '녈' : '열',
    '렬' : '열',
    '념' : '염',
    '렴' : '염',
    '녕' : '영',
    '령' : '영',
    '녜' : '예',
    '례' : '예',
    '뇨' : '요',
    '료' : '요',
    '뉴' : '유',
    '류' : '유',
    '뉵' : '육',
    '륙' : '육',
    '니' : '이',
    '리' : '이',
    '라' : '나',
    '락' : '낙',
    '란' : '난',
    '랄' : '날',
    '람' : '남',
    '랍' : '납',
    '랑' : '낭',
    '래' : '내',
    '랭' : '냉',
    '렵' : '엽',
    '로' : '노',
    '록' : '녹',
    '론' : '논',
    '롱' : '농',
    '뢰' : '뇌',
    '룡' : '용',
    '루' : '누',
    '륜' : '윤',
    '률' : '율',
    '륭' : '융',
    '륵' : '늑',
    '름' : '늠',
    '릉' : '능',
    '린' : '인',
    '림' : '임',
    '립' : '입',
}

def TwoSounds(Letter):
    if Letter in TwoSoundRule:
        return [TwoSoundRule[Letter]]+[Letter]
    return [Letter]

maxdepth = 4
def Negamax(EndingLetter, depth, alpha, beta):
    global History, maxdepth
    if not IsThereAWordStartingWith(EndingLetter):
        return (-100000+(maxdepth - depth)*10, '')
    if depth == 0:
        heu = 0
        for letter in TwoSounds(EndingLetter):
            heu += Heuristics(letter)
        return (10*heu, '')
    bestValue = -float('inf')
    bestMove = ''
    DB = []
    for letter in TwoSounds(EndingLetter):
        if letter in Database:
            DB += Database[letter]
    # print(DB)
    for word in DB:
        if word in History:
            continue
        Calculated = -Negamax(word[-1], depth-1, -beta, -alpha)[0]
        if Calculated > bestValue:
            bestValue = Calculated
            bestMove = word
        alpha = max(alpha, bestValue)
        if alpha >= beta:
            break
    return (bestValue, bestMove)


def IsInDatabase(word):
    TSD = TwoSounds(word[0])
    for i in TSD:
        if i in Database:
            return word in Database[i]
    return False

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

History = set()
LastWord = ''

def IsThereAWordStartingWith(letter):
    TSR = TwoSounds(letter)
    for i in TSR:
        if i in Database:
            return True
    return False