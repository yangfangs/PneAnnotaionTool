# An APP for DICOM format file label annotation


An APP for DICOM format file, the main feature are:

1. Read DICOM format figure.

2. Annotating label in the figure by click left mouse button.

3. Delete label in the figure by click right mouse button.

4. Save Annotation labels as Pixel coordinate to local disk.

5. Save Annotation labels as world coordinate system.

3. Convert Pixel coordinate system to the world coordinate system.

# Dependencies

* Python 3.6
* numpy
* pydicom
* matplotlib
* pandas

# For Linux

## install

```python

$ python setup.py install

```

## usage

```python
$ PneAnnotaionTool

```

## Other way you can start in terminal

* First of all, you must ensure that all the above dependencies are installed.

```
$ Python3 main.py

```

# For windows(Test for win 10)

* Download APP in [PneAnnotaionTool v0.0.2](https://pan.baidu.com/s/1CIprPiYAdBZMy2bksB-Kmg) and code is `8zef`

* Download APP in [PneAnnotaionTool v0.0.3](https://pan.baidu.com/s/1doW1mo_HqrYPxLH1BUrUTQ) and code is `kkke`

* Double-click the `annotation.exe` application.

![win app](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/annotation2.gif)



# Overview

![main app](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/main.png)

# Annotation

* When click `Save` the annotation figure will be saved as `png` format.

![annotation example](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/anno_pig.png)

# label coordinate

* When click `Save` the coordinate label file will be saved as `csv` format.

* The label contain `series UID`, `Coord X`, `Coord Y` and `coord Z` by world coordinate system.

![label result](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/label_csv.png)


# PCS to WCS method

![method](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/method.png)

> The detail information in [Defining the DICOM orientation](http://nipy.org/nibabel/dicom/dicom_orientation.html)