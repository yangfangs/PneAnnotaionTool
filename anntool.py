
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import dicom
import pydicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection





# Load the scans in given folder path
def load_scan(path):
    slices = pydicom.read_file(path)
    # slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    # try:
    #     slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    # except:
    #     slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    #
    # for s in slices:
    #     s.SliceThickness = slice_thickness

    return slices


def get_pixels_hu(slices):
    image = slices.pixel_array
    # Convert to int16 (from sometimes int16),
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)

    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0

    # Convert to Hounsfield units (HU)


    intercept = slices.RescaleIntercept
    slope = slices.RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image= image.astype(np.int16)

        image += np.int16(intercept)

    return image




def on_press(event):
    print("my position:" ,event.button,event.xdata, event.ydata)
    fig = event.inaxes.figure
    plt.scatter(event.xdata,event.ydata)
    fig.canvas.draw()
# fig.canvas.mpl_connect('button_press_event', on_press)

def star_img(img):
    fig = plt.figure()
    plt.imshow(img, cmap=plt.cm.gray, animated=True)
    fig.canvas.mpl_connect('button_press_event', on_press)
    plt.show()
    fig.savefig('/home/yangfang/example2222.png')
    return fig

def saveimg(fig):
    fig.savefig('/home/yangfang/example2222.png')


if __name__ == '__main__':

    first_patient = load_scan('/home/yangfang/CT/CT_FangYang/sample_huaxi/p1/IM000036')
    first_patient_pixels = get_pixels_hu(first_patient)
    fig = star_img(first_patient_pixels)
    saveimg(fig)



# curr_pos = 0
# plots = first_patient_pixels
# def key_event(e):
#     global curr_pos
#
#     if e.key == "right":
#         curr_pos = curr_pos + 1
#     elif e.key == "left":
#         curr_pos = curr_pos - 1
#     else:
#         return
#     curr_pos = curr_pos % len(plots)
#
#     plt.imshow(first_patient_pixels[curr_pos], cmap=plt.cm.gray, animated=True)

# fig = plt.figure()
# fig.canvas.mpl_connect('key_press_event', key_event)

