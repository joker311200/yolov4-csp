from flask import Flask  , request, make_response,  jsonify,abort
from flask import render_template
from flask_script import Manager

import os
import re
import base64
import random
from PIL import Image,ImageTk
import tkinter as tk
from cv2 import cv2
import json
from io import BytesIO ,BufferedReader
import requests
from skimage import io
import datetime
import time
import shutil

app = Flask(__name__)
clothesname = []
i = []
imagefolder = []
url = "http://127.0.0.1:60882/detect"
# image1 = 'C:/Users/jack3/Desktop/DataSave/static/test1/'
yolopath = 'C:/Users/jack3/Desktop/camtest/'
path = 'C:/Users/jack3/Desktop/DataSave/static/img/'
yolotype = '["overcoat","suit","shrit","short sleeve","vest","long sleeve","hoodie","dress","coat","polo shirt"]'
allFileList = os.listdir(path)
foldername = ""
filecount = 0
resulttxtC =0
c = 0
for file in allFileList:
    imagefolder.append(file)

if not os.path.isdir("./images/flaskcamera/"):
        os.mkdir("./images/flaskcamera/")
else:
    shutil.rmtree("./images/flaskcamera/")
    os.mkdir("./images/flaskcamera/")



@app.route("/txt", methods=['GET','POST'])
def txtchange():
    global resulttxtC
    payload={'detect': yolotype,'token': 'test','yolodata': 'True'}

    timeString = datetime.datetime.now().replace(microsecond=0)  
    timet = str(timeString).replace("-","")
    timet2 = timet.replace(":","")
    time3 = timet2.replace(" ","")
    data = request.get_data()
    data = str(data, encoding='utf-8')
    imgtxt = data
    imgtest = Image.open(BytesIO(base64.b64decode(imgtxt.replace("data:image/png;base64,"," "))))
    imgtest.save('./images/flaskcamera/'+time3+".png", 'PNG')
    files=[
              ('file',   (time3+'.png', open('./images/flaskcamera/'+time3+".png", 'rb'), 'application/octet-stream'))
            ]
            
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    resulttxt = response.text
    if resulttxt is None:
        resulttxtC =resulttxtC
    else:
        resulttxtC = int(resulttxt[0])
    print(resulttxt)
    # print(resulttxtC)
    # # resulttxtC = 3
    # # img = str(io.imread(imgtest))
    # # print(imgtxt)
    # # print(type(files))
    # # savetxt = open('C:/Users/jack3/Desktop/test.txt','w')
    # # savetxt.write(data)
    # # print(img)

    # imgtest.save('test123.png', 'PNG')
    return jsonify(data)

@app.route("/ImgChange", methods=['GET','POST'])

def ImgChange():
    data = request.get_data()
    data = str(data, encoding='utf-8')
    # ImgList =  json.loads(data)
    # resulttxtC =3
    if resulttxtC ==0:
        imagepath01 = "https://media.boohoo.com/i/boohoo/mzz77850_black_xl?pdp.template"
        imagepath02 = "https://media.boohooman.com/i/boohooman/mzz51028_ecru_xl?pdp.template"
        imagepath03 = "https://cf.shopee.tw/file/a53735df41d64451fba98b4d6a9e82d9"
        imagepath04 = "http://cdn.shopify.com/s/files/1/0951/3596/products/zane-barlas-overcoat-brown-cashmere-overcoat-13058660925534.jpg?v=1593585749"
        imagepath05 = "https://ae01.alicdn.com/kf/H05102d940ef14e62ad242fd20bc41547k/Men-Jacket-Warm-Winter-Trench-Coat-Long-Outwear-Button-Overcoat-Male-Casual-Windbreaker-Overcoat-Jackets-coats.jpg"
        imagepath06 = "https://www.gentlemansgazette.com/wp-content/uploads/2017/01/Green-triple-checked-overcoat-with-fur-collar-dark-suit-90s-tie-and-white-shirt-with-flat-cap-and-clear-glasses.jpg"
        imagepath07 = "https://www.reiss.com/media/product/617/022/wool-blend-epsom-overcoat-mens-gable-in-navy-blue-5.jpg?format=jpeg&auto=webp&quality=85&width=632&height=725&fit=bounds"
        imagepath08 = "https://ct.yimg.com/xd/api/res/1.2/R3hV6wKqKm6GPdZGljezWA--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD04MDA7cT04NTtyb3RhdGU9YXV0bzt3PTgwMA--/https://s.yimg.com/ob/image/920df096-2bd8-471d-b30f-f9e29330a3e4.jpg"
        imagepath09 = "https://menshaircuts.com/wp-content/uploads/2019/12/mens-overcoat-grey.jpg"
    elif resulttxtC ==1:
        imagepath01 = "http://cdn.shopify.com/s/files/1/0120/0311/5089/products/PR7681.0901_1_1200x.jpg?v=1607695743"
        imagepath02 = "https://a.suitsupplycdn.com/image/upload/ar_10:22,b_rgb:efefef,bo_300px_solid_rgb:efefef,c_pad,g_north,w_2600/b_rgb:efefef,c_lfill,g_north,dpr_1,w_768,h_922,f_auto,q_auto,fl_progressive/products/Suits/default/P4302E_1.jpg"
        imagepath03 = "https://cdn.suitdirect.co.uk/upload/siteimages/large/0061358_250_a.jpg"
        imagepath04 = "https://www.tmlewin.co.uk/dw/image/v2/BBQF_PRD/on/demandware.static/-/Sites-tml-catalog-en/default/dwbce231b6/images/portrait/57983S.jpg?sw=1556&sh=1680&sm=fit"
        imagepath05 = "https://suits-me.co.uk/wp-content/uploads/2020/02/martez-brown-MAIN.jpg"
        imagepath06 = "https://www.heavencostumes.com.au/media/catalog/product/cache/3ca7c4de79fd9294a778cbfdebc9dde4/o/b/obbo-0039-suitmeister-brand-deluxe-men-s-multi-coloured-rainbow-fun-business-suit-front-1500.jpg"
        imagepath07 = "https://www.mossbroshire.co.uk/images/original/7606_01.jpg"
        imagepath08 = "https://lh3.googleusercontent.com/proxy/FmQvZAtkZK51-wE6PPvmF36Madr8OHaUbJc1cOZ56K9xpH7tx9qD1ku0UQPrqQZO1guQP9Wl4hVy6hWd8S8HanQfJWr_hzTl_IqZMEy3A0LNECNPKksO9QCNK8zXFj-mZI3hLLUiWAO1frqp43qRkJyAmH_GdrwnJVLf6SxWlV9IC2mHUXLPyjSJq5iEU-NJiZTHX-ospDsuEeFC6e8JgLaA-lAsccJ2jR-asGQtxT6PDBKQ6x2845Fda9QvvddjYB3yVHfatnOcBPMuNRWmPqIXbYopUAeVo9AeG7ZAb3OrsPrrR-_7PuKGq7RHB3dutGQchxZJoWeCKljTHIUHdBPTqu3dRvWAMrc69anUUzz2qsoGbv8euiuD"
        imagepath09 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcLybLQSp62o6P_DeFPW5W3PH2VqL-Br9JxQ&usqp=CAU"
        
    elif resulttxtC ==2:
        imagepath01 = "https://images-na.ssl-images-amazon.com/images/I/51SkhEGRNwL.jpg"
        imagepath02 = "https://5.imimg.com/data5/ST/PE/MY-47609367/stylish-slim-fit-casual-shirt-500x500.jpg"
        imagepath03 = "https://5.imimg.com/data5/HO/BC/MY-44869874/mens-casual-check-shirt-500x500.jpg"
        imagepath04 = "https://5.imimg.com/data5/UC/TY/MY-9601095/100-25-cotton-fancy-casual-shirt-for-men-500x500.jpg"
        imagepath05 = "https://elegant-man.com/wp-content/uploads/2016/12/Autumn-Men-Cotton-Shirt-9-1.jpg"
        imagepath06 = "https://5.imimg.com/data5/PO/MS/MY-13007104/anry-cotton-casual-shirt-for-men-500x500.jpg"
        imagepath07 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp1suRDDTtYh7rRF2FzuhPlJwyuX0MKb94UkQUzmX4nCtl7twsK8gI-WX7VL8UMx62-D8&usqp=CAU"
        imagepath08 = "https://i.pinimg.com/564x/a0/bf/1d/a0bf1d1620db7aa2a896c08f658d7a93.jpg"
        imagepath09 = "https://ae01.alicdn.com/kf/HTB1xaIzKpXXXXXGaXXXq6xXFXXXa/2014-New-Arrival-Trend-Long-Sleeve-Shirts-Fashionable-City-Men-s-Shirts-Slim-Fit-Leisure-Shirt.jpg"

    elif resulttxtC ==3:
        imagepath01 = "https://derekrose.scdn4.secure.raxcdn.com/media/catalog/product/m/e/mens_short_sleeve_t_shirt_basel_micro_modal_denim_main.jpg"
        imagepath02 = "https://www.bulk.com.tw/_i/assets/upload/product/4c501fca48b3b3d70f53935a5a87bfb0.jpg"
        imagepath03 = "https://www.kickers.co.uk/images/short-sleeve-striped-t-shirt-p6680-20730_zoom.jpg"
        imagepath04 = "https://diz36nn4q02zr.cloudfront.net/webapi/imagesV3/Cropped/SalePage/6906490/0/637522775631230000?v=1"
        imagepath05 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI1rP-xOKWzy5kFge-WrI7CnxXl2Xx_1VZcg&usqp=CAU"
        imagepath06 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbUfSvbmZX3oQ-7ozYaTJFH8LJ6VA24HJH4bx6pXYJE_IcJbP8Ut-irVAlwNacMNH7ktc&usqp=CAU"
        imagepath07 = "https://underarmour.scene7.com/is/image/Underarmour/V5-1361733-035_FC?rp=standard-0pad|gridTileDesktop&scl=1&fmt=jpg&qlt=50&resMode=sharp2&cache=on,on&bgc=F0F0F0&wid=512&hei=640&size=512,640"
        imagepath08 = "https://cdn.shopify.com/s/files/1/1850/9807/products/YT5-168_patriot-blue_STYLE_67d39c18-9ba1-4615-800f-8be196f19cbf.jpg?v=1615408285"
        imagepath09 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2FmXu6LtNfFIOVXxYfTa-Vt0L-V69TXQFHw&usqp=CAU"

    elif resulttxtC ==4:
        imagepath01 = "https://cdn.jobeline.com/images/600x600/264c4ba7/264c4ba7cd8e4500/264c4ba7cd8e4500b2633b4a/264c4ba7cd8e4500b2633b4ad2026b58/JL1481FS018MC_214794_2019-01-14_14-35-28.JPG"
        imagepath02 = "https://eu.patagonia.com/dw/image/v2/BDJB_PRD/on/demandware.static/-/Sites-patagonia-master/default/dw05db0e2f/images/hi-res/25882_STH.jpg?sw=1600&sh=1600&sfrm=png&q=80&bgcolor=f6f6f6"
        imagepath03 = "https://rfis.freetls.fastly.net/public/content/4917714?w=480&h=600&q=85"
        imagepath04 = "https://cdn.store-assets.com/s/271663/i/21278661.jpg?width=480&format=webp"
        imagepath05 = "https://cf.shopee.tw/file/9dcc149d837940a116bd1398b3bd0184"
        imagepath06 = "https://cf.shopee.tw/file/9cd84b029ab380bf15b49f16b9266db5"
        imagepath07 = "https://cdn.shopify.com/s/files/1/0274/4293/7933/products/001113547.jpg?v=1613574253"
        imagepath08 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd_LEq1rgHuLsAq53Appe7si4Ynb3XBidoj7QPN0bT3gxUdu_VV9lOVGG8wbN2Zu4rEvM&usqp=CAU"
        imagepath09 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2iI79BIMw79hdH_tcGLPtkKBWQSELB6KASw&usqp=CAU"

    elif resulttxtC ==5:
        imagepath01 = "https://cdn.shopify.com/s/files/1/0150/0643/3380/products/Viacom_Spongebob_Delta61748_00023_Gold_800x.jpg?v=1563223299"
        imagepath02 = "https://media.endclothing.com/media/catalog/product/0/9/09-12-2019_airjordan_longsleevefearlesstee_multi_ct6196-100_jm_1.jpg"
        imagepath03 = "https://cdn2.salewa.com/media/image/3f/c0/c3/193a7e79-775c-47e4-816a-1cbbeed4a43a_salewa_600x600.jpg"
        imagepath04 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9i57msXUUOs2RYh69Z92XdzMQKF0ECahEf0Jo9EaauGb8-fgJdkKOkTHrWuUv4di9DI4&usqp=CAU"
        imagepath05 = "https://dynamic.zacdn.com/37uLH8sKcmTvUjytXnVVSiHPbcg=/fit-in/346x500/filters:quality(95):fill(ffffff)/http://static.hk.zalora.net/p/cotton-on-7494-3094455-1.jpg"
        imagepath06 = "https://cottonon.com/dw/image/v2/BBDS_PRD/on/demandware.static/-/Sites-catalog-master-men/default/dw73bc3bf1/361192/361192-132-2.jpg?sw=566&sh=849&sm=fit"
        imagepath07 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKx6ePycaGHIbcXauFQW5bPy73m8a35EkMTw&usqp=CAU"
        imagepath08 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHKYj8qZsY_FLhkw4MpGXF-9vX36kjxsvXvw&usqp=CAU"
        imagepath09 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_SdwHYZURAJg0g5Pd1M_53f-ff4O5ZWh11w&usqp=CAU"

    elif resulttxtC ==6:
        imagepath01 = "https://i.pinimg.com/originals/8f/1b/1b/8f1b1b15d2f13df9c7233f8f521fdf94.jpg"
        imagepath02 = "https://cdn.shopify.com/s/files/1/1722/0531/products/TruthHoodie-BlackBack_1024x1024.jpg?v=1571439084"
        imagepath03 = "https://images-na.ssl-images-amazon.com/images/I/71SwXtwWTHL._AC_UX385_.jpg"
        imagepath04 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdshNgjBMqu5x2LgajOeP6Tv3URNXVNH-Uc_TrgDdZs1YArSITU2XRrT7SF9bZBLhj5pg&usqp=CAU"
        imagepath05 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTI_klNUHo1qyQ9XV7XFnsvwedPrC4n0mkVAw&usqp=CAU"
        imagepath06 = "https://forever21.imgix.net/img/app/product/4/430765-2721091.jpg?w=412&auto=format"
        imagepath07 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFqdywvlWbh9RIs1xDextt3equzinB31sg1ZA60pDbdpZfaNwEW5_7XXvIbTb421WnmNI&usqp=CAU"
        imagepath08 = "https://i8.amplience.net/i/nlyscandinavia/919893-0014_01/i-oversized-hoodie/?$categorypage_M$"
        imagepath09 = "https://ddpzd2b97pj2g.cloudfront.net/pub/media/catalog/product/large/VN0A4BR3WHT1_DisentangledFleeceHoodie_2.jpg"


    elif resulttxtC ==7:
        imagepath01 = "https://assets.ajio.com/medias/sys_master/root/20201024/E4kZ/5f933d7faeb269d563ee93c2/-473Wx593H-461521529-green-MODEL.jpg"
        imagepath02 = "https://img.promgirl.com/_img/PGPRODUCTS/2267471/1000/navy-dress-DQ-2459-a.jpg"
        imagepath03 = "https://allensolly.imgix.net/img/app/product/2/291710-1252219.jpg"
        imagepath04 = "https://m.media-amazon.com/images/I/61ypNMyv9LL._SY606._SX._UX._SY._UY_.jpg"
        imagepath05 = "https://dazedimg-dazedgroup.netdna-ssl.com/1080/azure/dazed-prod/1290/5/1295031.jpg"
        imagepath06 = "https://images-na.ssl-images-amazon.com/images/I/71E5HudSn%2BL._UL1500_.jpg"
        imagepath07 = "https://assets.ajio.com/medias/sys_master/root/h2f/he2/15678454366238/-473Wx593H-461001523-multi-MODEL.jpg"
        imagepath08 = "https://img.simplydresses.com/_img/SDPRODUCTS/2267471/1000/navy-dress-DQ-2459-a.jpg"
        imagepath09 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSulve3zQMFKxiXQQml8iq5mxSEZSdmhCQn8Q&usqp=CAU"
        
    elif resulttxtC ==8:
        imagepath01 = "https://img1.momoshop.com.tw/goodsimg/0008/052/160/8052160_R.jpg?t=1599241928"
        imagepath02 = "https://tpe1cciscloudhost.chiefappc.com/cac/CmiProd/WNA056_20_M_01_m.jpg"
        imagepath03 = "https://www.giftparty.com.tw/data/goods/gallery/202001/1578541443523926023.jpg"
        imagepath04 = "https://d.ecimg.tw/items/DEBLH1A900AZ7BG/000001_1611191344.jpg"
        imagepath05 = "https://ct.yimg.com/xd/api/res/1.2/u4V9QsHVTV0xlAdk.AcGuA--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD02NDE7cT04NTtyb3RhdGU9YXV0bzt3PTcwMA--/https://s.yimg.com/ob/image/896b5197-97e7-4de3-99d4-85090213ff79.jpg"
        imagepath06 = "https://cf.shopee.tw/file/9c72e175235a00ba6152c88edc102b3c"
        imagepath07 = "https://im.uniqlo.com/images/tw/uq/pc/img/feature/uq/contentspage/functional-outer/200918_m_mainlook_02.jpg"
        imagepath08 = "https://tpe1cciscloudhost.chiefappc.com/cac/CmiProd/B1NA030_63_V_01_m.jpg"
        imagepath09 = "https://photo.3gun.com.tw/Photo/UE033520/UE033520-UF3-01.jpg"

    elif resulttxtC ==9:
        imagepath01 = "https://b.ecimg.tw/items/DXAQ0KA900B1EVC/000001_1614218783.jpg"
        imagepath02 = "https://www.unisky.com.tw/wp-content/uploads/mens-uniform-design-polo-shirts-9172502701-front.jpg"
        imagepath03 = "https://cdn.suitableshop.com/img/p378x/superdry-polo-shirt-malibu-grey--66231-1.jpg"
        imagepath04 = "https://d.ecimg.tw/items/DICUBWA900ANZQW/000001_1592465235.jpg"
        imagepath05 = "https://d.ecimg.tw/items/DICUBWA900ANOHM/000001_1592466173.jpg"
        imagepath06 = "https://og.momoshop.com.tw/1616502336091/goodsimg/0008/694/578/8694578_R.jpg"
        imagepath07 = "https://www.edwin.com.tw/upload_files/fonlego-rwd/prodpic/U70144-058-31.jpg"
        imagepath08 = "https://efshop3-wabow.cdn.hinet.net/files/1/products/71497_710_E6A183E7B485.jpg?v=21449"
        imagepath09 = "https://lh3.googleusercontent.com/proxy/gdTiEBAGN9DGTQn2ekQf7bx5Mg5N0FiKRptFVmfbZmfLLpv9FcsjwiKmivPoiqXB4S984kyK5habR8nr6SLfnoX2iQlRMMFxd2o9cDTHubu8hv6Y_-iDKt4ysW2Jvj8vnpvRVQ"

    else:
        imagepath01 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath02 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath03 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath04 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath05 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath06 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath07 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath08 = "/static/img/"+foldername+"/"+clothesname[0]
        imagepath09 = "/static/img/"+foldername+"/"+clothesname[0]
        print("error")
        
    print(resulttxtC)
    # foldername =imagefolder[1]
    # for filename in os.listdir(path+foldername+"/"):
    #     fname = os.path.join(filename)
    #     clothesname.append(fname)
    
    # imagepath01 = "/static/"+foldername+"/"+clothesname[0]
    # imagepath02 = "/static/"+foldername+"/"+clothesname[1]
    # imagepath03 = "/static/"+foldername+"/"+clothesname[2]

    # imagepath01 = "https://p0.ssl.img.360kuai.com/t01ee1ea62322899194.jpg?size=640x585"
    # imagepath02 = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UNIQLO_logo.svg/1200px-UNIQLO_logo.svg.png"
    # imagepath03 = "https://image.shutterstock.com/image-photo/kiev-ukraine-march-31-2015-260nw-275940803.jpg"
    # imagepath04 = "https://keedan.com/track/files/2020/05/levis-logo-1.jpg"
    # imagepath05 = "https://i.pinimg.com/originals/f4/de/05/f4de052f3cc67412f510f77033d95e07.jpg"
    # imagepath06 = "https://www.brandinlabs.com/wp-content/uploads/2016/01/20160107035052581.png"
    # imagepath07 = "https://i.pinimg.com/originals/cc/ca/81/ccca814ddf541c32510dd70538ce6174.jpg"
    # imagepath08 = "https://kenlu.net/wp-content/uploads/2013/02/Puma-Logo.jpg"
    # imagepath09 = "https://gss0.baidu.com/-vo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/d833c895d143ad4b547328108e025aafa50f0684.jpg"

    dataB ={ "img1": imagepath01,
             "img2": imagepath02,
             "img3": imagepath03,
             "img4": imagepath04,
             "img5": imagepath05,
             "img6": imagepath06,
             "img7": imagepath07,
             "img8": imagepath08,
             "img9": imagepath09}
    return jsonify(dataB)

@app.route("/", methods=['GET','POST'])

def htmlimages():
    foldername =imagefolder[0]
    for filename in os.listdir(path+foldername+"/"):
        fname = os.path.join(filename)
        clothesname.append(fname)
     
    imagepath01 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath02 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath03 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath04 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath05 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath06 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath07 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath08 = "/static/img/"+foldername+"/"+clothesname[0]
    imagepath09 = "/static/img/"+foldername+"/"+clothesname[0]


    return render_template('webtest.html', images01 = imagepath01, images02 = imagepath02, images03 = imagepath03, images04 = imagepath04, images05 = imagepath05, images06 = imagepath06, images07 = imagepath07, images08 = imagepath08, images09 = imagepath09)




        

if __name__ == '__main__':
#     # live_server = Server(app.wsgi_app)
#     # live_server.watch("**/*.*")
#     # live_server.serve(open_url=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True   
    # app.run()
    # app.run(debug = True)
    app.run(host='127.0.0.1', port=3000,debug = True)

