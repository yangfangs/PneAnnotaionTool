from setuptools import setup

import version

setup(
    name='PneAnnotaionTool',
    version=version,
    packages=[''],
    entry_points={
        "console_scripts": ['PneAnnotaionTool = main:main']
    },
    url='https://github.com/yangfangs/PneAnnotaionTool',
    license='GNU General Public License v3.0',
    author='yangfang',
    author_email='yangfangscu@gmail.com',
    description='A too for DICOM format figure annotation'
)
