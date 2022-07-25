import tkinter as tk
from PIL import Image,ImageTk
import tkinter.ttk as ttk
import cv2,os
from opencv_japanese import imread
import imagehash
import tkinter.filedialog

import numpy as np                     #2022/0725:お試し追加

img2             = ""
img3             = ""

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
    ['02.png','トマト'],
    ['03.png','パプリカ'],
    ['04.png','ピーマン'],
    ['05.png','トウモロコシ'],
    #['06.png','ナガネギ'],
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
    global   img2,img3
    input    =  entry.get()
    type     =  combobox.get()

    # 画像比べ処理
    hi_hit            =  255
    hi_hit_image      =  ""
    hi_hit_image_name =  ""

    if type == 'ヒストグラム比較':
        hi_hit   =  0
        dirname  =  os.path.dirname(__file__)
        images1  =  imread(dirname + '\\' + input)
        #images1  =  imread(dirname + '\\images/' + input)     #テスト用にフォルダに入れたらにする

        #入力した画像のサイズ取得
        height = images1.shape[0]
        width  = images1.shape[1]
        img_size = (int(width), int(height))

        # 画像をヒストグラム化する（まず入力のみ）
        image1_hist = cv2.calcHist([images1], [2], None, [256], [0, 256])

    elif type == 'numpy(要素番号比較？）':                      #2022/0725:お試し追加
        images1 = cv2.imread(input)                           #2022/0725:お試し追加
        height = images1.shape[0]
        width  = images1.shape[1]
        img_size = (int(width), int(height))

    else:
        images1  =  Image.open(input)
        hash     =  imagehash.average_hash(images1)
   
    #判定処理
    for i in range(len(gazo)):
        if type == 'ヒストグラム比較':
            images2  =  imread(dirname + '\\images/' + gazo[i][0])
            #入力画像に合わせてサイズを変更     
            image2 = cv2.resize(images2, img_size)
            # 画像をヒストグラム化する
            image2_hist = cv2.calcHist([image2], [2], None, [256], [0, 256])
            hit         = float(cv2.compareHist(image1_hist, image2_hist, 0))

            #print(hit)   #想像以上にレートが高い・・・

            if float(hi_hit) < float(hit):                  #100に近い数字程似ている　95-80くらいの判定が多い
                hi_hit            = hit
                hi_hit_image      = gazo[i][0]
                hi_hit_image_name = gazo[i][1]

        elif type == 'numpy(要素番号比較？）':                #2022/0725:お試し追加
            images2 = cv2.imread('images/' + gazo[i][0])
            image2  = cv2.resize(images2, img_size)
            hit     = float(np.count_nonzero(images1 - image2)/10000)
            print(hit)

            if float(hi_hit) > float(hit):                      #0に近い程似ている
                hi_hit            = hit
                hi_hit_image      = gazo[i][0]
                hi_hit_image_name = gazo[i][1] 

        else:       #ハッシュ値変換比較
            images2    = Image.open('images/' + gazo[i][0])
            otherhash  = imagehash.average_hash(images2)            
            hit        = hash - otherhash

            if int(hi_hit) > int(hit):                     #0に近い程似ている 全然違う画像でも20以内の場合有り
                hi_hit            = hit
                hi_hit_image      = gazo[i][0]
                hi_hit_image_name = gazo[i][1] 

    #判定結果
    if type == 'ヒストグラム比較':
        rate = hi_hit * 100
    elif type == 'numpy(要素番号比較？）': 
        rate = 100- hi_hit    
    else:        
        rate = 100 - (hi_hit * 2)

    if (rate)    == 100:
        word  = 'これなら知ってます！'
        word2 = 'です！絶対！'
    elif (rate)  >= 98:
        word  = 'あっ！これなら'
        word2 = 'だと思います！'
    elif (rate)  >= 90:
        word  = '多分なんですけど・・'
        word2 = 'ですかね・・。'
    elif (rate)  >= 75:
        word  = 'えっ・・・'
        word2 = 'とかだったりして・・・。'
    elif (rate)  >= 40:
        word =  'わからないですけど・・・'
        word2 = 'ですかね・・・ハハ。'
    else:
        word  ='・・・'
        word2 ='・・とか？'
        
    label3['text'] = '{}(判定結果値：{:.2f})'.format(word,rate)
    label4['text'] = '{}{}'.format(hi_hit_image_name,word2)
    #img2  =tk.PhotoImage(file="images/" + hi_hit_image)
    #canvas.create_image(700,350,image=img2)

    #img2 = Image.open('images/' + hi_hit_image)
    #img2e = tk.PhotoImage(img2)

    img2_txt=tk.Label(root,text='～入力した画像～',font=('Arial',14),bg='pink')
    img2_txt.place(x=430,y=150)
    img2 = Image.open(input)
    img2 = img2.resize((200,200))
    img2 = ImageTk.PhotoImage(img2)
    canvas.create_image(525,320,image=img2)

    img3_txt=tk.Label(root,text='～イロハさんの回答～',font=('Arial',14),bg='pink')
    img3_txt.place(x=780,y=150)
    #print('通過' + hi_hit_image)
    img3 = Image.open('images/' + hi_hit_image)
    img3 = img3.resize((200,200))
    img3 = ImageTk.PhotoImage(img3)
    canvas.create_image(880,320,image=img3)

def func(): 
    f_path = tk.filedialog.askopenfilename(title="ファイル選択", initialdir="ディレクトリを入力", filetypes=[("Image file", ".bmp .png .jpg .jpeg .tif")])
    name = os.path.basename(f_path) 
    entry.delete( 0, tk.END )
    entry.insert( 0, name )

root=tk.Tk()
root.title('この画像は何？教えてイロハさん！')
root.resizable(False,False)
canvas = tk.Canvas(root,width=1200,height=800,bg='white')
canvas.pack()

img =tk.PhotoImage(file="images/iroha.png")
canvas.create_image(150,400,image=img)
 
fkd =tk.PhotoImage(file="images/fukidasi.png")
canvas.create_image(700,710,image=fkd)

info =tk.Label(root,text='画像を入れるとイロハさんの「知ってる範囲」で何なのか教えてくれる・・・のだが・・・',font=('Arial',14),bg='white')
info.place(x=300,y=40)

label=tk.Label(root,text='画像入力',font=('Arial',16))
label.place(x=330,y=480)

entry=tk.Entry(width=30)
entry.place(x=430,y=514)

btn2 = tkinter.Button(root, text="ファイル選択", command=func)
btn2.place(x=340,y=514)

btn=tk.Button(text='判定する',command=btn_click)
btn.place(x=630,y=512)

label3 = tk.Label(root,text='お好きな画像を選んでください。',font=('Arial',28),bg='white')
label3.place(x=330,y=600)

label4 = tk.Label(root,text='',font=('Arial',28),bg='white')
label4.place(x=330,y=650)

#module = ('ヒストグラム比較', 'ハッシュ値変換比較')
module = ('ヒストグラム比較', 'ハッシュ値変換比較','numpy(要素番号比較？）')   #2022/0725:お試し追加
v = tk.StringVar()
combobox = ttk.Combobox(root, textvariable= v, values=module, style="office.TCombobox")
combobox.current(0)
combobox.place(x=830,y=515)

root.mainloop()