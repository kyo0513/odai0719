import tkinter as tk
from PIL import Image
import imagehash

img2             = ""

#['00.png',''],

gazo =[
    ['cry.png'  ,'ハカセ'],
    ['smile.png','ハカセ'],
    ['iroha.png','いろは（私）'],
    #['kaba1.jpg','コビトカバ'],
    #['kaba2.jpg','コビトカバ'],
    #['kaba3.jpg','コビトカバ'],
    #['cat1.png','ネコ'],
    #['cat2.jpg','ネコ'],
    #['cat3.jpg','ネコ'],
    ['01.png','レタス'],
    ['02.png','とまと'],
    ['03.png','パプリカ'],
    ['04.png','ピーマン'],
    ['05.png','トウモロコシ'],
    ['06.png','ナガネギ'],
    ['07.png','じゃがいも'],
    ['08.png','ラデッシュ'],
    ['09.png','さやえんどう'],
    ['10.png','じてんしゃ'],
    ['11.png','黄色い電車'],
    ['12.png','上からみた車'],
    ['13.png','テニスラケット'],
    ['14.png','野球のボール'],
    ['15.png','バレーのボール'],
    ['16.png','アメフトのボール?'],
    ['17.png','サッカーボール'],
    ['18.png','カレーライス'],
    ['19.png','えびフライ！'],
    ['20.png','スパゲティ'],
    ['21.png','おみそしる'],
    ['22.png','ころっけ'],
    ['23.png','ロールケーキ'],
    ['24.png','いちごのショートケーキ'],
    ['25.png','私の好きなミルクレープ'],
    ['26.png','パンダ'],
    ['27.png','ひよこさん'],
    ['28.png','シマリスさん'],
    ['29.png','アルパカ！！'],
    ['30.png','ぺんぎん'],
    ['31.png','なんか鳥'],
    ['32.png','ネズミ'],
    ['31.png','ヒョウ'],
    ['31.png','サーバルキャット'],
    ['31.png','お馬さん'],
    ['36.png','レッサーパンダ'], 
    ['37.png','きりんさん'],
    ['38.png','ネコさん'], 
    ['39.png','ネコさん'], 
    ['40.png','いぬ'],
    ['41.png','いぬ'], 
    ['42.png','青い鳥さん'],  
    ['43.png','ひよこさん'],       

]

def btn_click():
    global   img2
    input    =  entry.get()
    images1  =  Image.open(input)
    hash     =  imagehash.average_hash(images1)

    hi_hit            =  255
    hi_hit_image      =  ""
    hi_hit_image_name =  ""

    for i in range(len(gazo)):
        images2    = Image.open('images/' + gazo[i][0])
        otherhash  = imagehash.average_hash(images2)
        difference = hash - otherhash
    
        print(difference)   #想像以上にレートが高い・・・

        if int(hi_hit) > int(difference):
            hi_hit            = difference
            hi_hit_image      = gazo[i][0]
            hi_hit_image_name = gazo[i][1]
            print(hi_hit_image_name)

    if hi_hit == 0:
        word  = 'これなら知ってます！'
        word2 = 'です！絶対！'
    elif hi_hit  <= 25:
        word  = 'ああ、これなら'
        word2 = 'だと思います。'
    elif hi_hit  <= 50:
        word  = 'う～ん多分'
        word2 = 'かなぁ・・・。'
    elif hi_hit  <= 75:
        word  = 'えっ・・・'
        word2 = 'とかだったりして・・・。'
    elif hi_hit  <= 90:
        word =  'わからないですけど・・・'
        word2 = 'ですかね・・・ハハ。'
    else:
        word  ='・・・'
        word2 ='・・とか？'
        
    #label3['text'] = '{}{:.2f}%の確率で'.format(word,hi_hit *100)
    label3['text'] = '{}{}%の確率で'.format(word,100-(hi_hit*2))
    label4['text'] = '{}{}'.format(hi_hit_image_name,word2)
    img2  =tk.PhotoImage(file="images/" + hi_hit_image)    
    canvas.create_image(700,350,image=img2) 

root=tk.Tk()
root.title('この画像は何の画像？')
root.resizable(False,False)
canvas = tk.Canvas(root,width=1200,height=800,bg='white')
canvas.pack()

img =tk.PhotoImage(file="images/iroha.png")
#canvas.create_image(100,450,image=img)
canvas.create_image(250,400,image=img)

label=tk.Label(root,text='画像入力',font=('Arial',16))
label.place(x=300,y=510)

entry=tk.Entry(width=30)
entry.place(x=400,y=514)

btn=tk.Button(text='判定する',command=btn_click)
btn.place(x=600,y=512)

label3 = tk.Label(root,text='お好きな画像を選んでください。',font=('Arial',30),bg='white')
label3.place(x=300,y=600)

label4 = tk.Label(root,text='',font=('Arial',30),bg='white')
label4.place(x=300,y=650)

root.mainloop()