# Fire Detection System

## Objective
The objective of this project is to develop an automated fire detection system that can monitor video feeds in real-time to detect the presence of fire. Once fire is detected, the system triggers an alarm and sends an SMS alert to a predefined phone number, ensuring timely notifications of potential fire hazards.

## Application
This fire detection system can be deployed in various environments such as offices, factories, warehouses, and residential buildings. It enhances safety by providing an early warning mechanism, allowing for quick action to prevent the spread of fire and minimize damage.

## Features
- **Real-time Fire Detection:** Continuously monitors video feed for signs of fire using a pre-trained fire detection model.
- **Alarm System:** Plays an alarm sound when fire is detected to alert nearby individuals.
- **SMS Alerts:** Sends an SMS notification to a designated phone number when a fire is detected.
- **Multi-threading:** Utilizes multi-threading to handle alarm sound and SMS alerts concurrently, ensuring the system's efficiency.

## Prerequisites
- Python 3.x
- OpenCV
- Pygame
- Twilio

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/prajwalk-1/fire-detection-system.git
   cd Fire_Detection
   ```

2. **Install Required Packages:**
   ```bash
   pip install opencv-python pygame twilio
   ```

3. **Download the Fire Detection XML File:**
   Place the `fire_detection.xml` file in the project directory. You can download a pre-trained XML file or train one using a machine learning framework.

4. **Add the Alarm Sound:**
   Ensure that the `fire_siren.mp3` file is available in the project directory. This will be the sound played when fire is detected.

5. **Configure Twilio Credentials:**
   Replace the placeholder values in the code with your actual Twilio account credentials and phone numbers.

## Usage

1. **Run the Fire Detection System:**
   ```bash
   python Fire_Detector.py
   ```

2. The system will start capturing video from the default camera. If fire is detected in the video feed, an alarm will sound, and an SMS alert will be sent to the specified phone number.

3. **Stop the System:**
   Press `q` to quit the video stream and stop the fire detection system.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
