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

# install

```python

$ python setup.py install

```

# usage

```python
$ PneAnnotaionTool

```

# Overview

![main app](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/main.png)

# annotation

![annotation example](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/anno_pig.png)

# label coordinate

![label result](https://github.com/yangfangs/PneAnnotaionTool/blob/master/example_figure/label_csv.png)


# PCS to WCS method

$\begin{split}\begin{bmatrix} P_x\\
                P_y\\
                P_z\\
                1 \end{bmatrix} =
\begin{bmatrix} X_x\Delta{i} & Y_x\Delta{j} & 0 & S_x \\
                X_y\Delta{i} & Y_y\Delta{j} & 0 & S_y \\
                X_z\Delta{i} & Y_z\Delta{j} & 0 & S_z \\
                0   & 0   & 0 & 1 \end{bmatrix}
\begin{bmatrix} i\\
                j\\
                0\\
                1 \end{bmatrix}
= M
\begin{bmatrix} i\\
                j\\
                0\\
                1 \end{bmatrix}\end{split}$

> The detail information in [Defining the DICOM orientation](http://nipy.org/nibabel/dicom/dicom_orientation.html)