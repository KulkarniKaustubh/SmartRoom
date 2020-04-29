# Code
### face_rec.py
This program takes a ton of time to execute. No image optimization.

### training.py and test.py
Image optimization is done here. Takes lesser time to execute but images are smaller (of course).<br>
The extra time taken is by the face_locations function. You can use haarcascade to reduce the time significantly.

## To run:
First, install the required libraries by running the following command:
```sh
$ pip3 install opencv-python face_recognition numpy pickle-mixin Pillow
```
Then, create directories:
```sh
$ mkdir known_faces unknown_faces processed
```
Create folders with the name of the person's identity, under the known_faces folder. Insert test images under unknown_faces.<br>
The output of the tested images can be found in the processed directory.

## Optimization:
The optimized version of this code has runs faster. I have used ```Pillow``` to optimize the code slightly and ```pickle``` for dumping trained data into data files.<br>
To train based on images in the subfolders of known_faces:
```sh
$ python3 training.py
```
To test on unknown images placed in the unknown_faces directory:
```sh
$ python3 test.py
```
To see the output, open the folder named "processed" and open images from there. They will be smaller, optimized images but the program runs faster. And the output is pretty accurate.<br>
For less accurate results, but almost instantaneous testing, you can change the ``` MODEL ``` variable in ``` test.py ``` to ``` "hog" ```.
