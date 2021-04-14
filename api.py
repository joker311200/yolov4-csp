from flask import Flask, escape, request,jsonify
import json
import os
import time
from api_detect import ApiDetect
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'
# app.run(port=3000,debug= True)

# app.run(debug= True, port=3000)

aiClothetest = ApiDetect(cfg='clothestest/yolov4-csp-clothes.cfg', imgsesize=640,weights='clothestest/best.pt',names='clothestest/clothes_names')#rai 衣服
@app.route("/detect", methods=['POST', "GET"])
def userPhoto():
    detect = json.loads(request.values['detect'])
    detectName = {}
    count = 0
    for item in detect:
        detectName[item] = count
        count += 1
    name = "unknown"
    yolodata = False
    if "yolodata" in request.values and request.values["yolodata"] == "True":
        yolodata = True
    if "token" in request.values:
        name = request.values["token"]
    img = request.files.get('file')
    # 使用時間戳記當作檔案名稱
    fileName = str(time.time())
    # 檢查資料夾是否存在
    if not os.path.isdir("photo/"):
        os.mkdir("photo/")
    if not os.path.isdir("photo/"+name):
        os.mkdir("photo/"+name)
    filename = "photo/"+name+"/"+fileName+".png"
    img.save(filename)

    aiClotheteststr = aiClothetest.detect(filename)
    
    remystr = []
    yolostr = ""
 
    for item in aiClotheteststr:
        if item['name'] in detectName:
            yolostr +=  str(detectName[item['name']]) + " " + str(item['x'])+" "+str(item['y'])+" "+str(item['w'])+" "+str(item['h'])+"\n"
            remystr.append(item)
    if yolodata:
        return yolostr
    else:
        return jsonify(remystr)

    
