# Motion Detection and Email Notification
This is a Python script that uses OpenCV to perform motion 
detection on a video stream from the webcam.
When it detects motion in the video, it saves a snapshot of the frame containing the detected 
object and sends an email notification with the snapshot attached.

## Requirements
- Python 3.x  
- OpenCV (cv2) library  
- An email account with SMTP access for sending email notifications
- An app password on your email account


## Setup
Install the required libraries using pip:   
```pip install opencv-python```   
Make sure you have a working email account with SMTP access. 
Replace the emailing module with your own implementation to send emails. 
You can use a library like smtplib to achieve this.

## How to Use
1. Run the script. It will start accessing your webcam and display the video stream in a window titled "My video".

2. When the script detects motion (significant changes between consecutive frames), 
it will save a snapshot of the frame containing the detected object in the "images" folder. 
The snapshot will be named with a numerical index, e.g., 1.png, 2.png, etc.

3. When motion is detected, the script will send an email notification 
containing the snapshot of the detected object. Make sure to configure the send_email() 
function in the emailing module accordingly to match your email server settings.

4. Press 'q' in the video window to stop the script and exit.

# Important Notes
For proper functioning of email notifications, ensure that your email server allows SMTP 
access and that you provide the correct email credentials in the send_email() function.

The motion detection algorithm compares the first frame with the current frame, 
so it is recommended to keep the camera stationary during the detection process for accurate results.

Depending on the image quality of your camera you can adjust the motion detection sensitivity by 
changing the threshold value (60 in the cv2.threshold() function) and the minimum contour area 
(5000 in the cv2.contourArea() check).

The script will keep running until you press 'q' to exit or terminate it manually.

## Additional Information
This script runs two additional threads: one for sending the email notification and another 
for cleaning up the saved images. The send_email() function is executed in a separate thread 
to avoid blocking the main thread. Similarly, the clean_folder() function is run in a separate 
thread to periodically remove saved images from the "images" folder to prevent the folder from 
filling up with images over time.

Note: If you want to use this script in a production environment or as part of a larger application,
you may need to implement error handling, security measures, and possibly integrate it into a user-friendly interface.

Please ensure that you have permission to use surveillance or motion detection in your specific use 
case and location, as laws and regulations regarding privacy and surveillance may vary in different regions.