"""
Script to count the number of people and populate the database with time stamps
"""

import time
# to generate the time stamps

import jetson.inference
import jetson.utils

# Model
net = jetson.inferencedetectNet("ssd-mobilenet-v2",threshold=0.5)
# Camera Resolution Setting
camera = jetson.utils.gstCamera(1280,720,"dev/video1")
# -
display =jetson.utils.glDisplay()


# Check if the display is open
while display.IsOpen():
    # Convert the image inout into RGB values and store it into the computer
    img,width,height = camera.CaptureRGBA()
    # Returns list containing the detected objects
    detections = net.Detect(img,width,height)
    """
    We need to count the number of detections and store it
    """
    # CODE TO COUNT THE NUMBER OF DETECTIONS OF CLASS PERSON
    # Assuming coco dataset stores the id of person as 1
    """
    person:The number of people in the shop at an instant
    """
    person=0
    for i in detections:
        if i.ClassID == 1:#or 'person' or 2 if index starts from 1
            person=person+1

    """
    HERE ONWARDS WE WILL TRY TO POPULATE THE DATABASE
    """
    # here we can log in time stamps with the count
    timestamp=time.time()
    # for us to keep record
    print(timestamp)
    print(person)








    # # Render the box on the image
    # display.RenderOnce(img,width,height)
    # # Set title of the window
    # display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))


