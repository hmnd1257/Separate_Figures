#!/bin/python
from func import *
import argparse

# python main.py --baseroot <your_image_baseroot> --results_dir <save_path>

## setup arguments
parser = argparse.ArgumentParser(description='Separating images from multiple merged images')

## Path
parser.add_argument('--baseroot', type=str, help='path to the dataset directory')
parser.add_argument('--results_dir', type=str, help='saves results here')

## Image setting
parser.add_argument('--padding', default=True, help='Image padding') # Use 'False' if you don't want padding
parser.add_argument('--pixel', type=int, default=10, help='Size for image padding')
parser.add_argument('--extension', type=str, default='.jpeg', help='Separated image extension')  # [.jpeg, .png, .jpg]

if __name__ == '__main__':
    args = parser.parse_args()
    args.baseroot = os.path.expanduser(args.baseroot)
    args.results_dir = os.path.expanduser(args.results_dir)

    separate_fig(args)
