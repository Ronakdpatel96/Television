import os
from os import startfile
import cv2 
import datetime
import random
import time

#startfile('C:/Users/ronak/Desktop/media/shows/Spongebob - Dying For Pie;Imitation Krabs.mp4')

import os
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
script_directory = script_directory.replace('\\','/')
show_path = script_directory + '/media/shows'
com_path = script_directory + '/media/commercials'

episodes = os.listdir(show_path)
ep_count = len(episodes)
commercials = os.listdir(com_path)
com_count = len(commercials)

#loop from here
while(True):
    tv_random = random.randint(0,ep_count)
    commercial_random = random.randint(0,com_count)

    episode = episodes[tv_random]
    commercial = commercials[commercial_random]

    startfile(show_path + '/' + episode)

    # create video capture object 
    data = cv2.VideoCapture(show_path + '/' + episode) 
      
    # count the number of frames 
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
    fps = data.get(cv2.CAP_PROP_FPS) 
      
    # calculate duration of the video 
    seconds = round(frames / fps) 
    video_time = datetime.timedelta(seconds=seconds) 
    print(f"duration in seconds: {seconds}") 
    print(f"video time: {video_time}")

    time.sleep(seconds)

    startfile(com_path + '/' + commercial)

    data = cv2.VideoCapture(com_path + '/' + commercial) 
      
    # count the number of frames 
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
    fps = data.get(cv2.CAP_PROP_FPS) 
      
    # calculate duration of the video 
    seconds = round(frames / fps) 
    video_time = datetime.timedelta(seconds=seconds) 
    print(f"duration in seconds: {seconds}") 
    print(f"video time: {video_time}")

    time.sleep(seconds)

#Next, construct the fuil program, and download the files afterward
