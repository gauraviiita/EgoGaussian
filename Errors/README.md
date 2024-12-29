## Error 1:  RuntimeError: CUDA error: an illegal memory access was encountered
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/trainers/eval_metric.py", line 519, in eval_and_metric
    render_results(dataset, opt, pipe, exp_name, save_dir, obj_pose_seq_path, all_gaussians_path, train_eval_split)
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/trainers/eval_metric.py", line 109, in render_results
    rot_cov=True, accum_R=fixed_R, which_object=1, during_training=False)
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/gaussian_renderer/__init__.py", line 106, in render
    "visibility_filter" : radii > 0,
RuntimeError: CUDA error: an illegal memory access was encountered

### Solution: 
Go to File "/EgoGaussian/gaussian_renderer/__init__.py", line 106, in render
change "visibility_filter" : radii > 0, to **"visibility_filter" : (radii > 0).nonzero(),**

## Error 2 ImportError: /home/dr/anaconda3/envs/ego-3dgs/lib/python3.7/site-packages/diff_gaussian_rasterization/_C.cpython-37m-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb
```
$ CUDA_LAUNCH_BLOCKING=1 bash train.sh
Traceback (most recent call last):
  File "train.py", line 13, in <module>
    from trainers.train_static import train_static
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/trainers/train_static.py", line 10, in <module>
    from utils.dynamic_utils import get_viewpoint_split, gray_tensor_to_PIL, get_eval_img
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/utils/dynamic_utils.py", line 7, in <module>
    from gaussian_renderer import render
  File "/home/dr/Desktop/Gaurav/Research/BU/EgoGaussian/gaussian_renderer/__init__.py", line 14, in <module>
    from diff_gaussian_rasterization import GaussianRasterizationSettings, GaussianRasterizer
  File "/home/dr/anaconda3/envs/ego-3dgs/lib/python3.7/site-packages/diff_gaussian_rasterization/__init__.py", line 15, in <module>
    from . import _C
ImportError: /home/dr/anaconda3/envs/ego-3dgs/lib/python3.7/site-packages/diff_gaussian_rasterization/_C.cpython-37m-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb
```

