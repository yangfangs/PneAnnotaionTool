from setuptools import setup, find_packages

import version
pen_version = version.version

setup(
    name='PneAnnotaionTool',
    version=pen_version,
    packages=find_packages(),
    entry_points={
        "console_scripts": ['PneAnnotaionTool = main:main']
    },
    install_requires=[
        "numpy",
        "pydicom",
        "matplotlib",
        "pandas",
    ],
    url='https://github.com/yangfangs/PneAnnotaionTool',
    license='GNU General Public License v3.0',
    author='yang　fang',
    author_email='yangfangscu@gmail.com',
    description='A too for DICOM format figure annotation'
)
