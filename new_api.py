from flask import Flask, escape, request,jsonify
import json
import os
import time
from api_detect import ApiDetect
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'
raiyolo = ApiDetect(cfg="/home/ubuntu/YOLOv4-CSP/traindata/rai_check_630/rai_check_630-yolov4-csp_416.cfg", imgsesize=640,weights="/home/ubuntu/YOLOv4-CSP/yolov4-csp/runs/exp67_rai_check_630/weights/best.pt",names="/home/ubuntu/YOLOv4-CSP/traindata/rai_check_630/rai_check_630.name")#rai 主要辨識核心
# raiyolo = ApiDetect(cfg="run_weights/raiyolo/raiyolo-yolov4-csp_416.cfg", imgsesize=640,weights="run_weights/raiyolo/best.pt",names="run_weights/raiyolo/raiyolo.name")#raitest
personPart = ApiDetect(cfg="run_weights/person_part/person_part-yolov4-csp_416.cfg", imgsesize=416,weights="run_weights/person_part/best_person_part.pt",names="run_weights/person_part/person_part.name")#身形
aiYolo = ApiDetect(cfg='run_weights/yolov4-csp/yolov4-csp.cfg', imgsesize=640,weights='run_weights/yolov4-csp/yolov4-csp.pt',names='run_weights/yolov4-csp/coco.names')#coco 辨識
aiMask = ApiDetect(cfg='run_weights/mask/yolov4-csp_416.cfg', imgsesize=640,weights='run_weights/mask/mask.pt',names='run_weights/mask/face.names')#口罩辨識

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
    mystr = aiMask.detect(filename)
    cocostr = aiYolo.detect(filename)
    personPartStr = personPart.detect(filename)
    raiyoloStr = raiyolo.detect(filename)
    remystr = []
    yolostr = ""
    for item in mystr:
        if item['name'] in detectName:
            yolostr +=  str(detectName[item['name']]) + " " + str(item['x'])+" "+str(item['y'])+" "+str(item['w'])+" "+str(item['h'])+"\n"
            remystr.append(item)
    for item in cocostr:
        if item['name'] in detectName:
            yolostr +=  str(detectName[item['name']]) + " " + str(item['x'])+" "+str(item['y'])+" "+str(item['w'])+" "+str(item['h'])+"\n"
            remystr.append(item)
    for item in personPartStr:
        if item['name'] in detectName:
            yolostr +=  str(detectName[item['name']]) + " " + str(item['x'])+" "+str(item['y'])+" "+str(item['w'])+" "+str(item['h'])+"\n"
            remystr.append(item)
    for item in raiyoloStr:
        if item['name'] in detectName:
            yolostr +=  str(detectName[item['name']]) + " " + str(item['x'])+" "+str(item['y'])+" "+str(item['w'])+" "+str(item['h'])+"\n"
            remystr.append(item)
    if yolodata:
        return yolostr
    else:
        return jsonify(remystr)
