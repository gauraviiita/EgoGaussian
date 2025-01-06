# Custum data creation

## Step 1: Run [EgoHOS](https://github.com/owenzlz/EgoHOS) to identify hand segmentation

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu115
pip install mmcv-full==1.6.0 -f https://download.openmmlab.com/mmcv/dist/cu115/torch1.11.0/index.html
pip install -U openmim
cd mmsegmentation
pip install -v -e .
```



## Step 2: Resize the images and mask resolution to 512.

```
$ python resize.py 
```
