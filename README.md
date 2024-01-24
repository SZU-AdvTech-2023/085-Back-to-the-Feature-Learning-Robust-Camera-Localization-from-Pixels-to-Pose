# pixloc
我们介绍的PixLoc是一种神经网络，可通过与环境的三维模型直接特征对齐**定位给定图像。PixLoc 经过端到端训练，具有可解释性、准确性，并可泛化到新场景和跨领域，例如从室外到室内。


- [Back to the Feature: Learning Robust Camera Localization from Pixels to Pose](https://arxiv.org/abs/2103.09213)
-来自CVPR 2021
- 作者: [Paul-Edouard Sarlin](psarlin.com/)\*, [Ajaykumar Unagar](https://aunagar.github.io/)\*, [Måns Larsson](https://scholar.google.se/citations?user=RoOUjgQAAAAJ&hl=en), [Hugo Germain](https://www.hugogermain.com/), [Carl Toft](https://scholar.google.com/citations?user=vvgmWA0AAAAJ&hl=en), [Victor Larsson](http://people.inf.ethz.ch/vlarsson/), [Marc Pollefeys](http://people.inf.ethz.ch/pomarc/), [Vincent Lepetit](http://imagine.enpc.fr/~lepetitv/), [Lars Hammarstrand](http://www.chalmers.se/en/staff/Pages/lars-hammarstrand.aspx), [Fredrik Kahl](http://www.maths.lth.se/matematiklth/personal/fredrik/), and [Torsten Sattler](https://scholar.google.com/citations?user=jzx6_ZIAAAAJ&hl=en)
- website: [psarlin.com/pixloc](https://psarlin.com/pixloc) with videos, slides, and visualizations

### Setup

PixLoc 使用 Python >=3.6 和 PyTorch 构建。安装 requirements.txt中列出的最小依赖项： 

``` bash
git clone https://github.com/cvg/pixloc/
cd pixloc/
pip install -e .
```

安装 requirements.txt
```shell
pip install -r requirements.txt
```

主要代码在notebook/feature_map中:
在jupyter notebook中运行此代码

修改 notebook/localize.py中的数据集路径和相机内参
然后使用以下命令运行：

```shell
python notebook/localize.py
```

运行后能看到点的位姿和旋转矩阵

### Dataset
数据集可以自己采集，争对某个场景，拍摄的图片间隔不要太远，采集之后通过hloc进行colmap可以得到重建得到点云。








## BibTex Citation

Please consider citing our work if you use any of the ideas presented the paper or code from this repo:

```
@inproceedings{sarlin21pixloc,
  author    = {Paul-Edouard Sarlin and
               Ajaykumar Unagar and
               Måns Larsson and
               Hugo Germain and
               Carl Toft and
               Victor Larsson and
               Marc Pollefeys and
               Vincent Lepetit and
               Lars Hammarstrand and
               Fredrik Kahl and
               Torsten Sattler},
  title     = {{Back to the Feature: Learning Robust Camera Localization from Pixels to Pose}},
  booktitle = {CVPR},
  year      = {2021},
}
```