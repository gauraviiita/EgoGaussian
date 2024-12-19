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
