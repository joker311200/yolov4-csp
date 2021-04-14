import os
import platform
import shutil
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, plot_one_box, strip_optimizer)
from utils.torch_utils import select_device, load_classifier, time_synchronized

from models.models import *
from models.experimental import *
from utils.datasets import *
from utils.general import *

class ApiDetect:
    def load_classes(self,path):
        
        # Loads *.names file at 'path'
        with open(path, 'r') as f:
            names = f.read().split('\n')
        return list(filter(None, names))  # filter removes empty strings (such as last line)

    def __init__(self,cfg='models/yolov4-csp_416.cfg', imgsesize=640,weights='weights/mask.pt',names='data/face.names'):
        
        self.imgsz = imgsesize
        self.device = select_device("")
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA
        self.model = Darknet(cfg, self.imgsz).cuda()
        try:
            self.model.load_state_dict(torch.load(weights, map_location=self.device)['model'])
        except:
            self.model = self.model.to(self.device)
            load_darknet_weights(self.model, weights)
        self.model.to(self.device).eval()
        if self.half:
            self.model.half()  # to FP16
        self.classesNames = self.load_classes(names)
        img = torch.zeros((1, 3, self.imgsz, self.imgsz), device=self.device)  # init img
        _ = self.model(img.half() if self.half else img) if self.device.type != 'cpu' else None  # run once
    def detect(self,source):
        dataset = LoadImages(source, img_size=self.imgsz)
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            t1 = time_synchronized()
            pred = self.model(img)[0]

            # Apply NMS
            pred = non_max_suppression(pred, 0.4, 0.5)
            t2 = time_synchronized()
            saveTrainData = []
            # Process detections
            for i, det in enumerate(pred):  # detections per image
                p, s, im0 = path, '', im0s
                s += '%gx%g ' % img.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                    # Print results
                    
                    # Write results
                    for *xyxy, conf, cls in det:
                        # 存入訓練資料
                        c1, c2 = (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3]))
                        xmin = c1[0]
                        xmax = c2[0]
                        ymin = c1[1]
                        ymax = c2[1]
                        img_w = im0.shape[1]
                        img_h = im0.shape[0]
                        x = (xmin + (xmax-xmin)/2) * 1.0 / img_w
                        y = (ymin + (ymax-ymin)/2) * 1.0 / img_h
                        w = (xmax-xmin) * 1.0 / img_w
                        h = (ymax-ymin) * 1.0 / img_h
                        name = self.classesNames[int(cls)]
                        saveTrainData.append({"name":name,"x":x,"y":y,"w":w,"h":h})
                        # saveTrainData +=  str(int(cls)) + " " + str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n"
                # Print time (inference + NMS)
                print('%sDone. (%.3fs)' % (s, t2 - t1))
            return saveTrainData