
import numpy as np
import pydicom
import matplotlib.pyplot as plt


class AnnoTool(object):

    def __init__(self,pic_path):
        self.pic_path = pic_path
        self.image = None
        self.fig = None
        self.coordinate = []
        self.w_coordinate = []
        self.seriesuid = None

    def get_pixels_hu(self):
        """read dicom and trans to figure"""
        slices = pydicom.dcmread(self.pic_path)
        self.position = slices.ImagePositionPatient
        self.orientation = slices.ImageOrientationPatient
        self.pixelSpa = slices.PixelSpacing
        self.seriesuid = slices.SeriesInstanceUID
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
        self.image = image

    def on_press(self,event):
        """mouse action"""
        print("my position:" ,event.button,event.xdata, event.ydata)
        fig = event.inaxes.figure
        self.coordinate.append([event.xdata,event.ydata])
        self.w_coordinate.append(self.ics_2_pcs([event.xdata,event.ydata]))
        plt.scatter(event.xdata,event.ydata)
        fig.canvas.draw()

    def world_coordinate(self):
        """tans annotation coordinate to word coordinate system"""
        w_coor = list(map(self.ics_2_pcs,self.coordinate))
        self.w_coordinate = w_coor
        print(w_coor)
    def ics_2_pcs(self,coor):

        """
        trans image coordinate system (ICS) to DICOM Patient Coordinate System (PCS).
        PCS: also is the world coordinate syestem.

        example:
        impos = np.array([100, 100, 50])
        x = 5
        y = 6
        orient_x = np.array([1, 0, 0])
        orient_y = np.array([0, 1, 0])
        pixels_x = 0.5
        pixels_y = 0.5


        :param x: coord x
        :param y: coord y
        :return: voxel coord
        """
        x = coor[0]
        y = coor[1]
        impos = np.array(self.position)
        orient_x = np.array(self.orientation[:3])
        orient_y = np.array(self.orientation[-3:])
        pixels_x = self.pixelSpa[0]
        pixels_y = self.pixelSpa[1]
        voxel_x_y_z = impos + orient_x * pixels_x * x + orient_y * pixels_y * y
        return voxel_x_y_z

    def star_img(self):
        fig = plt.figure()
        plt.imshow(self.image, cmap=plt.cm.gray, animated=True)
        fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig = fig
        plt.show()

        # fig.savefig('/home/yangfang/example2222.png')

    def save_img(self):
        self.fig.savefig(self.pic_path + '.png')


if __name__ == '__main__':

    foo = AnnoTool('/home/yangfang/CT/CT_FangYang/sample_huaxi/p1/IM000036')
    foo.get_pixels_hu()
    foo.star_img()
    foo.save_img()
    foo.world_coordinate()


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

