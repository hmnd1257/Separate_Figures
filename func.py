#!/bin/python
import cv2
import os

def createFolder(args):
    if os.path.exists(args) is False:
        os.makedirs(args)

def padding(image, args):
    WHITE = [255, 255, 255]

    if args.padding == True:
        images = cv2.copyMakeBorder(image, args.pixel, args.pixel, args.pixel, args.pixel,
                                cv2.BORDER_CONSTANT, value=WHITE)  # Image padding
        return images
    else:
        images = image
        return images

def RGB_Average(ROI):
    Red = [y[0] for x in ROI for y in x]
    Green = [y[1] for x in ROI for y in x]
    Blue = [y[2] for x in ROI for y in x]
    try:
        R_avg = sum(Red) / len(Red)
        G_avg = sum(Green) / len(Green)
        B_avg = sum(Blue) / len(Blue)
    except ZeroDivisionError:
        print("ZeroDivision")

    return R_avg, G_avg, B_avg


def separate_fig(args):

    # Create a folder if it does`t folder
    cnt_folder = args.results_dir + '/contour'
    ROI_folder = args.results_dir + '/ROI'
    if os.path.exists(cnt_folder) is False:
        os.makedirs(cnt_folder)
        print('contour folder is created! : %s' % cnt_folder)
    if os.path.exists(ROI_folder) is False:
        os.makedirs(ROI_folder)
        print('ROI folder is created! : %s' % ROI_folder)

    print('-------------------------Loading images -------------------------')

    if len(os.listdir(args.baseroot)) == False:
        print('The overall number of images equals to %d' % len(os.listdir(args.baseroot)))
        print('Please check the image folder path again')
    else:
        print('-------------------------images Loaded-------------------------')
        print('The overall number of images equals to %d' % len(os.listdir(args.baseroot)))

        ## Read image
        img_cnt = 0
        for i in os.listdir(args.baseroot):
            filename = args.baseroot + '/' + i

            # Load image, grayscale, Otsu's threshold
            image = cv2.imread(filename)

            threshold_w = image.shape[0] / 4
            threshold_h = image.shape[1] / 4

            # image padding
            image = padding(image, args)

            original = image.copy()

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # Find contours, obtain bounding box, extract and save ROI
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            ROI_number = 0
            for c in cnts:
                x, y, w1, h1 = cv2.boundingRect(c)

                if w1 < threshold_w and h1 < threshold_h:
                    continue

                cv2.rectangle(image, (x, y), (x + w1, y + h1), (36, 255, 12), 2)

                ROI = original[y:y+h1, x:x+w1]

                # RGB average
                R_avg, G_avg, B_avg = RGB_Average(ROI)
                temp = max(R_avg, G_avg, B_avg) - min(R_avg, G_avg, B_avg)
                if R_avg < 150 and G_avg < 150 and B_avg < 150 and temp < 15:
                    h, w, _ = ROI.shape  # h : ROI image height, w : ROI image width

                    # To classify images that are not well separated
                    if not (h > (w + 0.3*w) or w > (h + 0.3*h) or h > w*2 or w > h*2 or 10 <= (h-w) <= 20 or (h-10) > w):
                        filename_ROI = i[:-5] + "_" + str(ROI_number + 1) + args.extension
                        cv2.imwrite(ROI_folder + "/{}".format(filename_ROI), ROI) # save ROI

                ROI_number += 1
            img_cnt += 1

            filename_contour = i[:-5] + "_contour" + args.extension
            cv2.imwrite(cnt_folder + "/{}".format(filename_contour), image) # save contour images

            print('The image has been successfully separated and saved. [{} / {}]'.format(img_cnt, len(os.listdir(args.baseroot))))