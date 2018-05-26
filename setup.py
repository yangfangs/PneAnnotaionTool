from setuptools import setup

setup(
    name='PneAnnotaionTool',
    version='0.0.1',
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
