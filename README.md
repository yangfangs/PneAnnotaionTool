# An APP for DICOM format file label annotation


An APP for DICOM format file, the main feature are:

1. Read DICOM format figure.
2. Annotating label in the figure.
3. Convert Pixel coordinate system to the word coordinate system.

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

* Download APP in [here](https://pan.baidu.com/s/1CIprPiYAdBZMy2bksB-Kmg) and code is `8zef`

* Double-click the `annotation.exe` application.

![win app](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/annotation2.gif)



# Overview

![main app](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/main.png)

# Annotation

* When click `Save` the coordinate label file will be saved as `csv` format.

![annotation example](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/anno_pig.png)

# label coordinate

![label result](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/label_csv.png)


# PCS to WCS method

![method](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/method.png)

> The detail information in [Defining the DICOM orientation](http://nipy.org/nibabel/dicom/dicom_orientation.html)