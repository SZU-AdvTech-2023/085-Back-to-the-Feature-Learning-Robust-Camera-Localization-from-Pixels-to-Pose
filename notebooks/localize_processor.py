from pathlib import Path
from pprint import pformat
import numpy as np
from pixloc.localization.localizer import lysLocalizer
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm
from IPython.display import HTML

from pixloc.settings import DATA_PATH, LOC_PATH
from pixloc.utils.quaternions import rotmat2qvec
from pixloc.localization import RetrievalLocalizer, SimpleTracker
from pixloc.pixlib.geometry import Camera, Pose
from pixloc.visualization.viz_2d import (
    plot_images, plot_keypoints, add_text, features_to_RGB)
from pixloc.visualization.animation import (
    subsample_steps, VideoWriter, create_viz_dump, display_video)
from pixloc.run_scripts import default_paths, default_confs
# from pixloc.utils.eval import evaluate

class Processor:
    def __init__(self, scene_name,do_pose_approximation = False):
        self.scene_name = scene_name
        self.do_pose_approximation = do_pose_approximation
        scene_paths = default_paths.interpolate(scene=self.scene_name)
        print(f'scene paths:\n{pformat(scene_paths.asdict())}')

        self.paths = scene_paths.add_prefixes(DATA_PATH, LOC_PATH)
        self.conf = default_confs['from_retrieval']
        self.conf['refinement']['do_pose_approximation'] = self.do_pose_approximation
        print(f'conf:\n{pformat(self.conf)}')
    
    def loadModel(self):
        self.localizer=lysLocalizer(self.paths, self.conf)
      
    def transCameraIntrinsic(self,w,h,param):
        camIntrinsic = {'id': None, 'model': 'SIMPLE_PINHOLE', 'width': w, 'height': h, 'params': param}
        return camIntrinsic
      
    def local(self, cameraIntrinsic, queryname):
        # ------------------------------------------------------------------------
        # 载入某一张图片
        # name_q = np.random.choice(list(localizer.queries))  # pick a random query
        name_q = queryname # or select one for Aachen
        print('proceess image ' + queryname)
        print('with cameraIntrinsic:')
        print(cameraIntrinsic)

        cam_q = Camera.from_colmap(cameraIntrinsic)
        ret = self.localizer.run_query(name_q, cam_q) 
        R, tvec = [],[]
        if ret['success']:
            # print(ret['T_refined'].detach().numpy())
            R, tvec = ret['T_refined'].detach().numpy()
        elif 'T_init' in ret:
            R, tvec = ret['T_init'].numpy()

        corr_t = - R.T @ tvec
        corr_R = R.T
        # corr_R[...,1:] *= -1
        q = rotmat2qvec(corr_R)
        corr_q = [q[1],q[2],q[3],q[0]]
        output_poses = (corr_q, corr_t)
        return output_poses