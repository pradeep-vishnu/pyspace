pyspace — A DIY Project for IMU Applications

pyspace is a Python-based project exploring state-of-the-art algorithms for estimating the spatial orientation of objects using an Inertial Measurement Unit (IMU).

The project is primarily focused on experimentation, learning, and practical applications of IMU-based orientation estimation.

Description

The project started as an attempt to build an IMU system using the commonly available MPU-9250 sensor for real-time measurement and estimation of roll, pitch, and yaw.

The current implementation includes tools and scripts for:

Comparing different filtering techniques

Estimating object orientation and angles

Recording raw IMU sensor data

Experimenting with Kalman filters

Transmitting sensor data using socket programming

The goal is to provide a flexible platform that can be adapted to different IMU-based applications.

Wireless IMU Setup

Socket programming is used to separate the sensor from the computer running the processing software. This removes the need for a physical data cable between the IMU and the host system.

A wireless setup can be particularly useful in experiments where cables may introduce unwanted mechanical disturbances or instability.

The MPU-9250 data is currently transmitted in packets with a length of 8, but this can be modified depending on the requirements of your application.

The same approach could potentially be adapted for applications such as:

Inverted pendulum experiments

Stability and vibration studies

Robotics

Motion tracking

Orientation estimation

Other IMU-based control and measurement systems

You can also experiment with the delay values in the code to adjust the sampling rate and system responsiveness according to your application.

Advantages

A wireless configuration allows the measurement system to become largely standalone and cable-free.

This can help:

Reduce cable-related mechanical disturbances

Improve experimental flexibility

Allow the sensor to move freely

Simplify experimental setups

Enable remote data collection

Requirements

To reproduce the setup, you will need:

Raspberry Pi 4

MPU-9250 IMU

Wi-Fi router/network

A computer to act as the client

Python

A Python IDE (the project was originally developed using PyCharm)

Recommended Setup

The recommended configuration is:

MPU-9250
    │
    ▼
Raspberry Pi 4
    │
    │ Wi-Fi / Socket
    ▼
PC / Laptop
    │
    ▼
Python Processing & Visualization

Tip

Load and run the server code on the Raspberry Pi, and configure your PC as the client.

The Raspberry Pi collects data from the MPU-9250 and transmits it wirelessly to the PC, where the data can be processed, filtered, recorded, and analyzed.

Project Status

This is a DIY / experimental project intended for learning, experimentation, and further development.

Feel free to modify the filtering algorithms, packet structure, sampling delays, and communication architecture to suit your own application.

Contributions, experiments, improvements, and new ideas are welcome.
