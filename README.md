
# PySpace 🚀

**A DIY Python project for wireless IMU applications and spatial orientation.**

PySpace is a Python package designed to implement state-of-the-art algorithms for determining the spatial orientation (Roll, Pitch, and Yaw) of physical objects. 

## Overview

The initial focus of PySpace utilizes the popular **MPU-9250 sensor** as an Inertial Measurement Unit (IMU) to achieve true measurement of roll, pitch, and yaw. This repository provides scripts to perform:
*   **Filter comparisons** (including Kalman filters)
*   **Angle estimations**
*   **Recording of RAW sensor outputs**

By deploying **Socket programming**, PySpace intentionally eliminates the need for power and data cable harnesses during operation. This allows your hardware setup to be completely standalone and wireless, ensuring that heavy or stiff cables do not cause mechanical instability, drag, or interference to the system under study.

## Key Applications

The data payload from the MPU-9250 is currently trimmed to a length of 8, but this can be easily adjusted to fit your specific needs. PySpace is ideal for:
*   Inverted pendulum projects
*   Stability and control studies
*   Robotics and drone orientation tracking
*   Any application requiring remote, high-accuracy IMU telemetry

## Hardware Requirements

*   **Raspberry Pi 4**
*   **MPU-9250** IMU Sensor
*   **Wi-Fi Router** (for local network connection)
*   **PC/Laptop** (to run the client)

## Setup & Architecture

> **💡 Pro Tip:** Load the server code onto the Raspberry Pi and set up your PC as the client.

1. **Server (Raspberry Pi 4):** Connects to the MPU-9250, reads the raw data, and broadcasts the telemetry over a wireless socket.
2. **Client (PC):** Connects to the Pi via its IP address, receives the telemetry data, and handles processing/visualization using your preferred Python IDE (such as PyCharm).

## Configuration

*   **Sampling Rate:** Feel free to experiment with the `delay` values in the scripts to adjust the sensitivity and sampling rate of the sensor to match your project's physics.
*   **Data Length:** Modify the trimmed data length depending on how many parameters you need to transmit over the socket.

---
*Contributions, issues, and feature requests are welcome!*
