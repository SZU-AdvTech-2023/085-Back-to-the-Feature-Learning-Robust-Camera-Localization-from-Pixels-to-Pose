from pixloc.settings import DATA_PATH
from localize_processor import Processor
import os
import json


print("init processor and load model")
sceneId = "lys_new_cheku" #数据集名称
default_localize_processor = Processor(sceneId)
default_localize_processor.loadModel()

requestId = 'test'
#地下车库内参3101.7 2041.1 1488.1

#condition = '{"cameraIntrinsic":[472.73187255859375, 240.0, 320.0],"width": 480,"height": 640}'
condition = '{"cameraIntrinsic":[3101.7, 2041.1, 1488.1],"width": 806,"height": 605}'
#local_file_path = f'{DATA_PATH}/{sceneId}/query/{requestId}/'
local_file_path = f'{DATA_PATH}/{sceneId}/night/{requestId}/'
#/home/lys/Workplace/datasets/lys_new_cheku/night/IMG_5348.JPG
up_images = os.listdir(local_file_path)
if len(up_images) > 0:
    use_image = f'{local_file_path}{up_images[0]}'
    my_processor = default_localize_processor
    conditionObj = json.loads(condition)
    cameraIntrinsic = conditionObj['cameraIntrinsic']
    imw = conditionObj['width']
    imh = conditionObj['height']
    if my_processor is not None:
        cameraIntrinsicTrans = my_processor.transCameraIntrinsic(imw,imh,cameraIntrinsic)
        R,tvec = my_processor.local(cameraIntrinsicTrans, use_image)
        data = {"position": tvec.tolist(),"rotation": R}
        print(json.dumps(data))
    else:
        print("can not get processor")