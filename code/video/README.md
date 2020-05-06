# Video
## video_rec.py
Code for recognizing faces through video.

## code_led.py
This code is for connecting to the Arduino Uno via the serial port, lighting up the in-built LED when any face from the training set is recognized.

## trigger_led
The Arduino code to capture serial port activity and light up the LED when needed.

#Running:
###Download all the files
## Training:
```sh
$ python3 training.py -d <data folder> -k <folder containing known images>
```
OR
```sh
$ python3 training.py --data <data folder> --known <folder containing known images>
```

##Face recognition (less laggy and smoother):
```sh
$ python3 raspi_optimized.py -d <data folder>
```
OR
```sh
$ python3 raspi_optimized.py --data <data folder>
```
