import cv2
import threading   # Library for threading -- which allows code to run in backend
import playsound   # Library for alarm sound
from playsound import playsound
#import smtplib     # Library for email sending
import serial
fire_cascade = cv2.CascadeClassifier(r'C:\Users\ICT_LAB\Desktop\oencv_compitition\Fire-detection-and-alarm--main\cascade.xml') # To access xml file which includes positive and negative images of fire. (Trained images)
                                                                         # File is also provided with the code.

vid = cv2.VideoCapture(0) # To start camera this command is used "0" for laptop inbuilt camera and "1" for USB attahed camera
runOnce = False # created boolean
ser = serial.Serial('COM3', 9600) # Replace 'COM3' with the appropriate port

#Please make sure to replace 'COM3' with the appropriate port where your arduino is connected.

def play_alarm_sound_function(): # defined function to play alarm post fire detection using threading
    playsound(r'C:\Users\ICT_LAB\Desktop\oencv_compitition\Fire-detection-and-alarm--main\Fire_alarm.mp3',True) # to play alarm # mp3 audio file is also provided with the code.
    print("Fire alarm end") # to print in consol

		
while(True):
    Alarm_Status = False
    ret, frame = vid.read() # Value in ret is True # To read video frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5) # to provide frame resolution

    ## to highlight fire with square 
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
         # Send a signal to Arduino to blink the light
        if len(fire) > 0:
            # Code to send a signal to Arduino to blink the light
            pass
            ser.write(b'1')
            print("Fire alarm initiated")
            print("Bazar alarm initiated")
        threading.Thread(target=play_alarm_sound_function).start()  # To call alarm thread

        if runOnce == False:
           """print("Mail send initiated")
        # threading.Thread(target=send_mail_function).start() # To call alarm thread
            runOnce = True
        if runOnce == True:
            print("Mail is already sent once")"""
        runOnce = True

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# # Close the serial connection and release the capture
ser.close()
vid.release()
cv2.destroyAllWindows()
