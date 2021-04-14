import sys
import os
import shutil
import time
from random import shuffle

def showView(name, keyarr):
    os.system("clear")
    print("============================")
    print("專案名稱"+name)
    print("============================")
    print("標籤:")
    for key in keyarr:
        print(key)


name = input('請輸入專案名稱：')
# name = "test"
key = ""
keyarr = []
key = input('請輸入辨識標籤：')
while key != 'q' or key == 'd':
    if(key == 'd'):
        if len(keyarr) > 0:
            keyarr.remove(keyarr[len(keyarr)-1])
        showView(name, keyarr)
        print("刪除完成")
        key = input('請輸入辨識標籤或q結束d取消上一個：')
    else:
        check = False
        for item in keyarr:
            if item == key:
                check = True
        if check:
            showView(name, keyarr)
            print("標籤重複")
            key = input('請輸入辨識標籤或q結束d取消上一個：')
        else:
            keyarr.append(key)
            showView(name, keyarr)
            key = input('請輸入辨識標籤或q結束d取消上一個：')

path = input('請輸入來源圖片資料夾路徑：') #/home/ubuntu/YOLOv4-CSP/person_part
# topath = input('請輸入目的地路徑：')
# path = '/home/ubuntu/YOLOv4-CSP/person_part/images'
topath = "/home/raiyangsunhua/traindataing"
# 建立相關資料夾
if not os.path.isdir(topath):
    os.makedirs(topath)
# os.chdir(topath)
if os.path.isdir(topath+"/"+name):
    oldproject = input('專案已存在，是否刪除(Y/N):')
    if oldproject == 'Y' or oldproject == 'y':
        shutil.rmtree(topath+"/"+name)
    else:
        print("結束")
        exit()
os.makedirs(topath+"/"+name)

# 處理 cfg 檔案
cfgPath = topath + "/"+name+'/'+name+'-yolov4-csp_416.cfg'
os.system('cp models/yolov4-csp.cfg '+cfgPath)
os.chdir(topath+"/"+name)
# 修改網路結構
classes = len(keyarr)
filters = (classes+5)*3
# os.system('sed -n -e 1028p -e 1137p -e 1246p '+ cfgPath)
os.system('sed -i \'8s/512/416/\' '+cfgPath)
os.system('sed -i \'9s/512/416/\' '+cfgPath)
os.system('sed -i \'1022s/255/'+str(filters)+'/\' '+cfgPath)
os.system('sed -i \'1029s/80/'+str(classes)+'/\' '+cfgPath)
os.system('sed -i \'1131s/255/'+str(filters)+'/\' '+cfgPath)
os.system('sed -i \'1138s/80/'+str(classes)+'/\' '+cfgPath)
os.system('sed -i \'1240s/255/'+str(filters)+'/\' '+cfgPath)
os.system('sed -i \'1247s/80/'+str(classes)+'/\' '+cfgPath)
# 建立 *.name
writeStr = ""
for item in keyarr:
    writeStr += item + "\n"
os.system('echo "'+writeStr + '" >> '+name + ".name")
os.chdir(path)
# 建立 val與train
os.system('ls -R '+path+'/*.jpg > '+topath+"/"+name+'/all.txt')
tandv = float(input('請輸入訓練與測試比例(EX:0.8)：'))
fp = open(topath+"/"+name+'/all.txt', "r")
lineArr = []
line = fp.readline()
lineArr.append(line)
# 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    line = fp.readline()
    lineArr.append(line)
fp.close()
p = len(lineArr) * tandv
trainStr = ""
valStr = ""
rdmStr = input('是否亂數排列(EX:y)：')
if rdmStr == 'y':
    shuffle(lineArr)
    print("run shuffle")
for i in range(len(lineArr)):
    if i < p:
        trainStr += lineArr[i]# + '\t'
    else:
        valStr += lineArr[i]# + '\t'
os.chdir(topath+"/"+name)
trainpath = topath+"/"+name+"/"+"train.txt"
valpath = topath+"/"+name+"/"+"val.txt"
os.system('echo "'+trainStr + '" >> train.txt')
os.system('echo "'+valStr + '" >> val.txt')



os.system('echo "train: '+trainpath+'\n'+'val: '+valpath +
          '\n'+'nc: ' + str(classes)+'\n'+
          "names: "+ str(keyarr) +
          '" >> '+name+'.yaml')

os.system('echo "train = '+trainpath+'\n'+'val = '+valpath +
          '\n'+'classes = ' + str(classes)+'" >> '+name+'.data')
# 計算 anchors 值
print("計算 anchors 值:")
# print('/home/ubuntu/darknet/darknet detector calc_anchors '+topath+"/" +
#       name+'/'+name+'.data -num_of_clusters 9 -width 416 -height 416 -showpause')
os.system('yes | /home/raiyangsunhua/darknet/darknet detector calc_anchors '+topath+"/" +
      name+'/'+name+'.data -num_of_clusters 9 -width 416 -height 416 -showpause >> anchors.txt')
time.sleep(1)
f = open('anchors.txt', 'r')
myanchors  = f.read()
anchorsdata = myanchors.split('anchors =')[1].replace('\n','')
print(anchorsdata)
print("查看目前 anchors 值：")
# print("sed -n -e 1028p -e 1137p -e 1246p "+cfgPath)
os.system("sed -n -e 1028p -e 1137p -e 1246p "+cfgPath)
# print("並輸入1")
os.system("sed -i '1028s/ 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401/"+anchorsdata+"/' "+cfgPath)
# print("並輸入2")
os.system("sed -i '1137s/ 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401/"+anchorsdata+"/' "+cfgPath)
# print("並輸入3")
os.system("sed -i '1246s/ 12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401/"+anchorsdata+"/' "+cfgPath)

print("並檢查是否修改為相同樣式")
os.system("sed -n -e 1028p -e 1137p -e 1246p "+cfgPath)
print(',{')
print('"name": "train '+name+'",')
print('"type": "python",')
print('"request": "launch",')
print('"program": "train.py",')
print('"console": "integratedTerminal",')
print('"args": [')
print('"--device",')
print('"0",')
print('"--batch-size",')
print('"4",')
print('"--data",')
print('"'+topath+"/"+name+"/"+name+'.yaml"'+',')
print('"--cfg",')
print('"'+cfgPath+'",')
print('"--name",')
print('"'+name+'",')
print('"--weights",')
print('"",')
print(']')
print('}')
