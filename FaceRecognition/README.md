# Face Recognition
## About
Program to run facial recognition after training on faces known, and then testing on unknown faces to find matches.<br>
>These programs do not work on the side view of faces.
The face_recognition python library is used from [GitHub](https://github.com/ageitgey/face_recognition)

## Repo structure:

```
|
|
|---- README.md
|
|
|---- code
|	|
|	|--- (all python files)
|
|
|-----data
|	|
|	|--- (encoded data files for images and names)
|	
|
|----pending
	|
	|--- (commented openCV code which will run faster- in progress)
```


## To run:
First, install the required libraries by running the following command:
```sh
$ pip3 install opencv-python face_recognition numpy pickle-mixin Pillow serial
```
Then, create directories:
```sh
$ mkdir known_faces unknown_faces processed
```
Create folders with the name of the person's identity, under the known_faces folder. Insert test images under unknown_faces.<br>
The output of the tested images can be found in the processed directory (this is for code/image).

