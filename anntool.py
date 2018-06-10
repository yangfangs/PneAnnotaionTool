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
        self.org_coord = None

    def get_pixels_hu(self):
        """read dicom and trans to figure"""
        slices = pydicom.dcmread(self.pic_path)
        self.position = slices.ImagePositionPatient
        self.orientation = slices.ImageOrientationPatient
        self.pixelSpa = slices.PixelSpacing
        self.seriesuid = slices.SeriesInstanceUID
        self.WinWidth = slices.WindowWidth
        self.WinCenter = slices.WindowCenter
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
        image2 = self.setDicomWinWidthWinCenter(image,3000,-500)

        self.image = image2

    def setDicomWinWidthWinCenter(self,img_data, winwidth, wincenter):
        img_temp = img_data
        img_temp.flags.writeable = True
        rows = img_data.shape[0]
        cols = img_data.shape[1]
        min = (2 * wincenter - winwidth) / 2.0 + 0.5
        max = (2 * wincenter + winwidth) / 2.0 + 0.5
        dFactor = 255.0 / (max - min)

        for i in range(rows):
            for j in range(cols):
                img_temp[i, j] = int((img_temp[i, j] - min) * dFactor)

        min_index = img_temp < 0
        img_temp[min_index] = 0
        max_index = img_temp > 255
        img_temp[max_index] = 255

        return img_temp


    def on_press(self,event):
        global b
        global fig
        """mouse action"""
        # print("my position:" ,event.button,event.xdata, event.ydata)
        # try:
        #     fig = event.inaxes.figure
        # except AttributeError as e:
        #     print(e)
        # self.coordinate.append([event.xdata,event.ydata])
        # self.w_coordinate.append(self.ics_2_pcs([event.xdata,event.ydata]))
        # b = plt.scatter(event.xdata,event.ydata,picker=5)
        # b.set_offsets(self.coordinate)
        # #
        # plt.draw()
        if event.button == 1:
            """mouse left key"""
            # exclude event click are not in fig
            if event.xdata != None:
                self.coordinate.append([event.xdata, event.ydata])
            # self.w_coordinate.append(self.ics_2_pcs([event.xdata, event.ydata]))

                b.set_offsets(self.coordinate)
            # fig.canvas.draw()
            plt.draw()

        elif event.button == 3:
            """mouse right key"""
            fig.canvas.mpl_connect('pick_event', self.onpick)
            plt.draw()

    def onpick(self,event):
        """pick event"""
        global b

        thisline = event.artist
        xdata = thisline.get_offsets()[:,0]
        ydata = thisline.get_offsets()[:,1]
        ind = event.ind
        points = [xdata[ind].tolist()[0], ydata[ind].tolist()[0]]
        self.coordinate.remove(points)
        # print(points)
        # print(self.coordinate)
        if self.coordinate != []:
            b.set_offsets(self.coordinate)
        else:
            b.set_offsets([None,None])


    def world_coordinate(self):
        """tans annotation coordinate to word coordinate system"""
        # print(self.coordinate)
        w_coor = list(map(self.ics_2_pcs,self.coordinate))
        self.w_coordinate = w_coor


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
        global b
        global fig
        fig = plt.figure()
        plt.imshow(self.image, cmap=plt.cm.gray, animated=True)
        fig.canvas.mpl_connect('button_press_event', self.on_press)
        # with picker
        if self.coordinate != []:
            # print(self.coordinate)
            b = plt.scatter(self.org_coord[0],self.org_coord[1], s=8, c = 'r', norm=0.8, picker=5)
        else:
            b = plt.scatter(x=None, y=None, s=8, c = 'r', norm=0.8, picker=5)
        self.fig = fig
        plt.show()

        # fig.savefig('/home/yangfang/example2222.png')

    def save_img(self):
        self.fig.savefig(self.pic_path + '.png')


    def set_coord(self,coord_data):
        """ get  pixel data if this data in dir"""
        self.org_coord = coord_data
        for i in range(len(coord_data[0])):
            self.coordinate.append([coord_data[0][i],coord_data[1][i]])

        print(self.coordinate)


if __name__ == '__main__':

    foo = AnnoTool('/home/yangfang/CT/CT_FangYang/sample_huaxi/p1/IM000036')
    foo.get_pixels_hu()
    foo.star_img()
    foo.save_img()
    foo.world_coordinate()


