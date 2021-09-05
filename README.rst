===
pyspace
===

pyspace is an attempt to create a Python project/package for state of the art algorithms used to find the spatial orientation of objects. 


Description
===========

First attempt was to create a script that can use a cery common sensor MPU9250 as an IMU for True-Measurement-of-Roll-ptich-and-yaw. Here I have developed scripts that can perform Filter comparisons, Angle estimations and recording of RAW outputs. Kalman filters and Socket programming were the two techniques deployed. 

Socket programming was used to eliminate the power and data cable harness, enabling more accuracy. The data from the MPU-9250 was trimmed to a lenght of 8. This 
could be adjusted for your application and could be implemented for various application including inverted pendulum projects, stabilty study and many more. Also 
fell free to play around with the delay values for adjusting the senstivity/sampling rate. 

Advantage: You can make your server completly standlone and wireless which means the cable harness willnot be causing any instablity to your system under study. 

All you need is a Wifi-router, IP address of the client, Raspberry Pi4, MPU9250 and a Python IDE (I used Pycharm).

Tip : Load the server code into Raspberry pi and make your PC as client. 

Watch this short video for more details of the setup : https://youtu.be/WDkc80XHgts


