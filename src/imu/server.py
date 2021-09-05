import FaBo9Axis_MPU9250
import time
import sys
import socket
import os
import subprocess
import re

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

print("Clearing my port '1234' ####")
command = 'kill -9 $(lsof -t -i:1234)'
os.system(command)

print("Searching for Client #####")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',1248))
s.listen(999)

while True:

           clientsocket, address = s.accept()
           print("Conection from has been established!")

           while True:
                       try:
                             accel = mpu9250.readAccel()
                             ax = (str(accel['x']) + "000000000000")[0:4]
                             print(ax)
                             clientsocket.send(bytes(ax, "utf-8"))
                             ay = (str(accel['y']) + "000000000000")[0:4]
                             print(ay)
                             clientsocket.send(bytes(ay, "utf-8"))
                             az = (str(accel['z']) + "000000000000")[0:4]
                             print(az)
                             clientsocket.send(bytes(az, "utf-8")) 
 
                             gyro = mpu9250.readGyro()
                             gx = (str(gyro['x']) + "000000000000")[0:4]
                             print(gx)
                             clientsocket.send(bytes(gx, "utf-8"))
                             gy = (str(gyro['y']) + "000000000000")[0:4]
                             print(gy)
                             clientsocket.send(bytes(gy, "utf-8"))
                             gz = (str(gyro['z']) + "000000000000")[0:4]
                             print(gz)
                             clientsocket.send(bytes(gz, "utf-8"))
                             time.sleep(0.3)

                       except:
                              print("Waiting for the Client")
                              break








