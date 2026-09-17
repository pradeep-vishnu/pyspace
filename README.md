<p align="center"> <strong> pyspace : A Python Project for IMU Applications</strong> </p> <p align="center"> Algorithms and tools for IMU-based orientation estimation, filtering, and wireless data acquisition. </p>
📌 About

pyspace is a Python-based project for experimenting with algorithms used to estimate the spatial orientation of objects using an Inertial Measurement Unit (IMU).

The project started with the MPU-9250 IMU sensor and focuses on real-time estimation of:

Roll

Pitch

Yaw

The project is intended primarily for experimentation, learning, and developing IMU-based applications.

🚀 Features

The project currently includes tools and scripts for:

📐 Roll, pitch, and yaw estimation

📊 Filter comparison

🎯 Angle estimation

💾 Raw IMU data recording

🔄 Kalman filtering

📡 Wireless data transmission

🔌 Socket-based client/server communication

📡 Wireless IMU System

The project uses socket programming to transmit IMU data wirelessly between a Raspberry Pi and a PC.

This eliminates the need for a physical data cable between the sensor and the computer. Removing the cable harness can be useful in experiments where cables may introduce unwanted mechanical disturbances or instability.

The current implementation transmits MPU-9250 data in packets with a length of 8. This can be modified according to your application.

System Architecture
                MPU-9250
                    │
                    ▼
             Raspberry Pi 4
                (Server)
                    │
              Wi-Fi / Socket
                    │
                    ▼
               PC / Laptop
                 (Client)
                    │
                    ▼
          Data Processing & Analysis

🛠️ Requirements

The basic setup requires:

Component	Description
Raspberry Pi 4	IMU server
MPU-9250	IMU sensor
Wi-Fi Router	Wireless communication
PC / Laptop	Client and data processing
Python	Programming environment
PyCharm	IDE used during development
⚙️ Getting Started
1. Connect the MPU-9250

Connect the MPU-9250 to the Raspberry Pi and configure the required communication interface.

2. Configure the Raspberry Pi

Load the server code onto the Raspberry Pi and start the server.

3. Configure the PC

Run the client code on your PC and configure it with the Raspberry Pi's IP address.

4. Start the system

Once the client and server are connected, the Raspberry Pi can transmit the IMU data wirelessly to the PC.

The PC can then be used for:

Data processing

Filtering

Angle estimation

Visualization

Data recording

Algorithm comparison

🔧 Configuration

Several parameters can be adjusted depending on the requirements of your application.

For example:

Sampling delay

Sampling rate

Data packet length

Server IP address

Port number

Filter parameters

Kalman filter parameters

Tip: Experiment with the delay values to find a suitable balance between sampling rate, responsiveness, and system performance.

💡 Possible Applications

The system can be adapted for a variety of IMU-based applications, including:

🤖 Robotics

Orientation estimation for robotic platforms and moving systems.

⚖️ Inverted Pendulum

IMU-based angle measurement for inverted pendulum experiments and control systems.

📐 Stability Studies

Measurement and analysis of roll, pitch, and yaw during stability experiments.

🔬 Experimental Research

Wireless IMU data acquisition for experiments where physical cables may interfere with the system under study.

✨ Advantages of the Wireless Setup

A wireless configuration makes the measurement system largely standalone and cable-free.

Potential advantages include:

Reduced cable-related disturbances

Greater experimental flexibility

Free movement of the sensor

Simplified experimental setup

Remote data acquisition

Reduced mechanical interference from cable harnesses

🤝 Contributing

This is a DIY and experimental project, and contributions are welcome.

Feel free to:

Fork the repository

Experiment with the code

Improve existing algorithms

Add new features

Submit a pull request

📄 License

This project is available under the MIT license.

<p align="center"> <i>Built for experimentation, learning, and IMU-based applications.</i> </p>
