#!/bin/python
from func import *

# python main.py --baseroot <your_image_baseroot> --contour <cnt_save_path> --ROI <ROI_save_path>
## setup arguments
parser = argparse.ArgumentParser(description='Separating images from multiple merged images')

## Path
parser.add_argument('--baseroot', type=str, help='path to the dataset directory')
parser.add_argument('--contour', type=str, help='path to the save contour directory')
parser.add_argument('--ROI', type=str, help='path to the save Region of Interest directory')

## Image setting
parser.add_argument('--padding', default=True, help='Image padding') # Use 'False' if you don't want padding
parser.add_argument('--pixel', type=int, default=10, help='Size for image padding')
parser.add_argument('--extension', type=str, default='.jpeg', help='Separated image extension')  # [.jpeg, .png, .jpg]

if __name__ == '__main__':
    args = parser.parse_args()
    args.baseroot = os.path.expanduser(args.baseroot)
    args.contour = os.path.expanduser(args.contour)
    args.ROI = os.path.expanduser(args.ROI)

    separate_fig(args)
