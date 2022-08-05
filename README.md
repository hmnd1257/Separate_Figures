# Separating images from multiple merged images

## Introduction
When the image we want is combined with several images in one image, there are cases where we want to get only the image we want.
It's not difficult when the amount of images you want to get is small, but when the amount of images that humans cannot execute, it's impossible to get the image you want.
So, we propose a code that can easily get the image you want.
* Input

## Requirements
* Python >= 3.6.13
* opencv >= 4.6.0

## Run

1. Our dataset structure
    * This is the dataset structure we used.
```
dataset_sample/
    |____XXXX.jpeg/ # [.png, .jpg] format is also acceptable.
    |____OOOO.jpeg 
    |____....
```
2. Run
    * If the save path doesn't exist, it is automatically created.
```bash
# in <path-to-this-repo>/
python main.py --baseroot './dataset' --contour './results/contour' --ROI './results/ROI'
```

## Run on your own dataset
Step 1: Download your own images datasets.<br />
Step 2: Open `main.py` in python idle.<br />
Step 3: Modify Arguments to set baseroot, contour, ROI and other parameters.<br />
Step 4: Run `main.py`


**Example**: If you leave the other settings as default except for the path option, run the following command. :
```bash
# in <path-to-this-repo>/
python main.py --baseroot <your_image_baseroot> --contour <cnt_save_path> --ROI <ROI_save_path>
```

**Arguments**
* `<baseroot>` (required): path to the dataset directory.
* `<contour>` (required): path to the save contour directory.
* `<ROI>` (required): path to the save Region of Interest directory.
* `<padding>` Add a white background with padding technique to better find the Region of interest (default: True).
* `<pixel>` Sets the padding size (default: 10).
* `<extension>` When saving a separated image, the extension of the image is set (default: .jpeg).


## Results
![(6)](https://user-images.githubusercontent.com/91607691/170524359-370cd3cd-4c34-40dd-8ab4-23cbebf0af69.jpeg)

* output

![(6)_contour](https://user-images.githubusercontent.com/91607691/170524422-2f65e1f1-d04b-4cfb-ab0b-f9986afe599a.jpeg)  
#

![(6)_4](https://user-images.githubusercontent.com/91607691/170524597-d0f1ee8d-3cb2-46cb-bc55-b69c1d82c2bb.jpeg)  
#

![(6)_3](https://user-images.githubusercontent.com/91607691/170524594-151f2aff-db5c-489f-a20c-d0f0cdcb46d6.jpeg)  
#

![(6)_2](https://user-images.githubusercontent.com/91607691/170524593-df2ae4ba-b32a-49df-bbfe-090d3a49cb0b.jpeg)  
#

![(6)_1](https://user-images.githubusercontent.com/91607691/170524591-55eadb31-96bd-4507-8142-07cdf3d92336.jpeg)  
#






# Installation
* Clone this repo:
```
git clone https://github.com/hmnd1257/Separate_Figures.git
```

