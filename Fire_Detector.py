import cv2
import threading
import pygame
from twilio.rest import Client

# Initialize the fire cascade
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

# Initialize video capture
vid = cv2.VideoCapture(0)
runOnce = False  # To ensure that SMS is sent only once

# Twilio credentials (replace with your actual credentials)
account_sid = 'Enter Your account_sid'
auth_token = 'Enter Your auth_token'
twilio_phone_number = '+Your Twilio phone numbe' 
recipient_phone_number = 'The recipient's phone number with country code' 

# Function to play alarm sound using pygame
def play_alarm_sound_function():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('fire_siren.mp3')
        pygame.mixer.music.set_volume(1.0)  # Set volume to maximum
        pygame.mixer.music.play(-1)  # Play the sound in a loop
        while True:
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# Function to send SMS alert
def send_sms_function():
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Warning: A fire accident has been reported at Wabisabi Company.",
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print(f"SMS sent to {recipient_phone_number}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

while True:
    ret, frame = vid.read()  # Capture video frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)  # Detect fire in the frame

    # Highlight detected fire with a rectangle
    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        if not runOnce:
            print("Fire alarm initiated")
            threading.Thread(target=play_alarm_sound_function).start()  # Start the alarm sound thread
            print("SMS send initiated")
            threading.Thread(target=send_sms_function).start()  # Start the SMS sending thread
            runOnce = True  # Ensure SMS is sent only once

    cv2.imshow('Fire Detection', frame)  # Display the video frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the video stream
        break

vid.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
