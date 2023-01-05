import torch
import argparse
import net
import cv2
import os
import numpy as np
from deploy import inference_img_whole
import pickle
from scipy.ndimage import morphology

from trimap_module import trimap,extractImage

'''
    Load model exported by python2 with python3 will cause error:
        ascii' codec can't decode byte 0xda in position 5
    The following codes will fix the bug
'''
def my_torch_load(fname):
    try:
        ckpt = torch.load(fname)
        return ckpt
    except Exception as e:
        print("Load Error:{}\nTry Load Again...".format(e))
        class C:
            pass
        def c_load(ss):
            return pickle.load(ss, encoding='latin1')
        def c_unpickler(ss):
            return pickle.Unpickler(ss, encoding='latin1')
        c = C
        c.load = c_load
        c.Unpickler = c_unpickler
        ckpt = torch.load(args.resume, encoding='latin1')
        return ckpt

def generate_trimap(alpha):
    fg = np.array(np.equal(alpha, 255).astype(np.float32))
    unknown = np.array(np.not_equal(alpha, 0).astype(np.float32))
    unknown = unknown - fg
    unknown = morphology.distance_transform_edt(unknown==0) <= np.random.randint(1, 20)
    trimap = fg * 255
    trimap[unknown] = 128
    return trimap.astype(np.uint8)

if __name__ == "__main__":
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    # input file list
    image_list = [
        "result/example/image/dog.png",
        "result/example/image/dog2.png",
        "result/example/image/duex.png",
    ]
    trimap_list = [
        "result/example/trimap/dog_trimap.png",
        "result/example/trimap/dog_trimap2.png",
        "result/example/trimap/duex_trimap.png",
    ]
    result_dir = "result/example/pred"
    
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # parameters setting
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.cuda = True
    args.resume = "model/stage1_skip_sad_52.9.pth"
    args.stage = 1
    args.crop_or_resize = "whole"
    args.max_size = 1600

    # init model
    model = net.VGG16(args).to(0)
    ckpt = my_torch_load(args.resume)

    model.load_state_dict(ckpt['state_dict'], strict=True)
    model = model.cuda()

    # infer one by one
    for image_path, trimap_path in zip(image_list, trimap_list):
        _, image_id = os.path.split(image_path)
        print("For " + image_id)
        
        image = cv2.imread(image_path)
        trimap = cv2.imread(trimap_path)[:, :, 0]
        torch.cuda.empty_cache()
        with torch.no_grad():
            pred_mattes = inference_img_whole(args, model, image, trimap)

        pred_mattes = (pred_mattes * 255).astype(np.uint8)
        #pred_mattes[trimap == 255] = 255
        #pred_mattes[trimap == 0  ] = 0
        print(result_dir, image_id)
        cv2.imwrite(image_id, pred_mattes)

    from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
    from torchvision.models.detection import fasterrcnn_resnet50_fpn
    detect_model = fasterrcnn_resnet50_fpn(pretrained = True)
    num_cls = 2
    