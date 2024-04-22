## QUESTION1 : Camera Calibration MATRIX

Using the matlab calibration tool, calibrated my webcam with a distance of 30 cm away from a checkerboard with 25mm squares

These are the intrinsic and extrensic parameters
![calibration_result](https://github.com/pvdsan/Assignment1/assets/22724124/2df851f0-b8cc-48f1-9bc1-618622ae87cd)


## QUESTION2 : Calculating actual 3D points with using individual rotation and translational vectors
There is a buffer padding of squares Ive used so checker board size is 7x5
### original Centre Position with 3D points [ 0,0,30]
![image](https://github.com/pvdsan/Assignment1/assets/22724124/671b1fcb-02b5-4516-947e-66245f51c91d)

### The projected point is shifted perfectly by one square in the image in the X direction with 3D points [25,0,30] i.e 25 mmm up in X direction 
![image](https://github.com/pvdsan/Assignment1/assets/22724124/d2dda28b-be9a-42f5-bd27-652b548772e8)

### The projected point is shifted perfectly by one square in the image in the Y direction with 3D points [0,25,30] i.e 25 mmm up in Y direction 
![image](https://github.com/pvdsan/Assignment1/assets/22724124/093fd227-0c67-474a-94db-e285f7f386cf)


