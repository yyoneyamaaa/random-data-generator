import random
import os
import csv

num= input("文字入力")
moji = ['テスト名', 'テスト名2', 'テスト名3', 'テスト名4', 'テスト名5']
moji2 = ['太郎', '一郎', '次郎', '三郎', '四郎']
kana=['テスト タロウ','テスト ジロウ','テスト シロウ','テスト サブロウ']
old=[20,21,22,23,24,25,26,27,28,29,30]
seibetu=['男性','女性']
telnumberkai=[1000,9999]
telnumber=['090','080']
seinen=[1990,2025]
tuki30=[4,6,9,11]
tuki31=[1,3,5,7,8,10,12]
uruu=[2]
yubintokyo=['1000004','1131040','1131200','1131110','1840013']

addressnumber=[10,99]
addres=['test','meruado','testtest']
addresm=['@test.com','@meruado.com','@testtest.com']

num= int(num)



for i in range(num):
    random_char = random.choice(moji)
    random_char2 = random.choice(moji2)
    kana1=random.choice(kana)
    old1=random.choice(old)
    seibetu1=random.choice(seibetu)

    #電話番号
    teljou=random.choice(telnumber)
    teltyuu=random.randint(1000,9999)
    telnumberkai1=random.randint(1000,9999)

    tel=f"{teljou}-{teltyuu}-{telnumberkai1}"

    #生年月日
    seinenn1=random.choice(seinen)
    tuki301=random.choice(tuki30)
    tuki311=random.choice(tuki31)
    uruu1=random.choice(uruu)
    hi1=random.randint(1,30)
    h2=random.randint(1,31)
    h3=random.randint(1,28)
    birthday=f"{seinenn1}-{tuki301}-{hi1}"
    birthday2=f"{seinenn1}-{tuki311}-{h2}"
    birthday3=f"{seinenn1}-{uruu1}-{h3}"
    birthdayaaa=random.choice([birthday,birthday2,birthday3])

    #郵便番号
    yubintokyo1=random.choice(yubintokyo)
    if yubintokyo1 == '1000004':
        juusyo="東京都千代田区"
    elif yubintokyo1 == '1131040':
        juusyo="東京都新宿区"
    elif yubintokyo1=='1131200':
        juusyo="東京都練馬区"
    elif yubintokyo1=='1131110':
        juusyo="東京都大田区"
    elif yubintokyo1 =='1840013':
        juusyo="東京都小金井市"

    #メルアド
    addres1=random.choice(addres)
    addressnumber1=random.randint(10,99)
    addresm1=random.choice(addresm)

    ad=f"{addres1}{addressnumber1}{addresm1}"


    #ターミナル出力
    print(random_char+random_char2+kana1+f"{old1}"+seibetu1,tel,birthdayaaa,yubintokyo1,juusyo,ad)


    filename = "ランダムデータ.csv"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, filename)

# CSVファイルを書き込みモードで開く
with open(file_path, mode="w", newline="", encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    writer.writerow([ "氏名", "氏名(カナ)","年齢", "性別","電話番号","生年月日","郵便番号","住所","メールアドレス"])

    # ランダムなデータを生成してCSVに書き込む
    for i in range(num):
        random_char = random.choice(moji)
        random_char2 = random.choice(moji2)
        kana1=random.choice(kana)
        old1 = random.choice(old)
        seibetu1 = random.choice(seibetu)

        #電話番号
        teljou=random.choice(telnumber)
        teltyuu=random.randint(1000,9999)
        telnumberkai1=random.randint(1000,9999)
        tel=f"{teljou}-{teltyuu}-{telnumberkai1}"

        #生年月日
        seinenn1=random.choice(seinen)
        tuki301=random.choice(tuki30)
        tuki311=random.choice(tuki31)
        uruu1=random.choice(uruu)
        hi1=random.randint(1,30)
        h2=random.randint(1,31)
        h3=random.randint(1,28)

        birthday=f"{seinenn1}-{tuki301}-{hi1}"
        birthday2=f"{seinenn1}-{tuki311}-{h2}"
        birthday3=f"{seinenn1}-{uruu1}-{h3}"

        birthdayaaa=random.choice([birthday,birthday2,birthday3])

        yubintokyo1=random.choice(yubintokyo)

        if yubintokyo1 == '1000004':
            juusyo="東京都千代田区"
        elif yubintokyo1 == '1131040':
            juusyo="東京都新宿区"
        elif yubintokyo1=='1131200':
            juusyo="東京都練馬区"
        elif yubintokyo1=='1131110':
             juusyo="東京都大田区"
        elif yubintokyo1 =='1840013':
             juusyo="東京都小金井市"

        #メルアド
        addres1=random.choice(addres)
        addressnumber1=random.randint(10,99)
        addresm1=random.choice(addresm)
        ad=f"{addres1}{addressnumber1}{addresm1}"


        # データを書き込み
        name=random_char+" "+random_char2
        writer.writerow([name,kana1, old1, seibetu1,tel,birthdayaaa,yubintokyo1,juusyo,ad])

print(f"CSVファイルに保存しました。{desktop_path}")