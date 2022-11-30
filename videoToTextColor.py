import time

import numpy as np
import cv2
import pickle
import sys
from ffpyplayer.player import MediaPlayer


aspect_ratio = 4/3
# Dimensions of the output in terminal characters
try:
    width = int(sys.argv[2])

except IndexError:
    print("error width not given")
    exit(1)
height = int(width / (2 * aspect_ratio)) - 20


def framerate(img):  # gets framerate and makes it sleep for that amount of time
    cap = cv2.VideoCapture(img)

    framespersecond = int(cap.get(cv2.CAP_PROP_FPS))

    return framespersecond

    # cv2.destroyAllWindows()


# Our characters, and their approximate brightness values
charSet = " ,(S#g@@g#S(, "


# Generates a character sequence to set the foreground and background colors
def setColor(bg, fg):
    return "\u001b[48;5;%s;38;5;%sm" % (bg, fg)


black = setColor(16, 16)

# Load in color lookup table data
lerped = pickle.load(open("colors.pkl", "rb"))

LUT = np.load("LUT.npy").tolist()   #.tolist() # converted to list because numpy array system has slow one time overhead



# Convert an RGB image to a stream of text with ANSI color codes


def convertImg(img):
    line = ""

    for row in img:
        for color in row:

            color = np.round(color)

            #b, g, r = color[0], color[1], color[2]

            # Lookup the color index in the RGB lookup table
            idx = LUT[color[0]][color[1]][color[2]] # b = 0 g= 1 r =2

            # Get the ANSI color codes and lerp character
            bg, fg, lerp, rgb = lerped[idx]

            char = charSet[lerp]

            line += "%s%c" % (setColor(bg, fg), char)
        # End each line with a black background to avoid color fringe
        line += "%s\n" % black

    # Move the cursor back to the top of the frame to prevent rolling
    line += "\u001b[%iD\u001b[%iA" % (width, height + 1)
    return line



if len(sys.argv) == 3:
    link = sys.argv[1]
    cap = cv2.VideoCapture(link)
    max_frame_len = 1.0 / framerate(link)  # max frame length in sec
    video = cv2.VideoCapture(link)
    layer = MediaPlayer(link)

for i in range(1, 99999999999999,1 ): #  for loop faster than while


    start_time = time.time()
    ret, frame = cap.read()

    if frame is None:
        break

    img = cv2.resize(frame, (width, height))

    sys.stdout.write(convertImg(img))

    # print('ft' , frame_time)
    # execution time minus expected frame time
    # print(wait_time)
    end_time = time.time()
    wait_time = round(max_frame_len - (end_time - start_time), 6)

    if wait_time > 0:
        time.sleep(wait_time)












else:
    print("Expected video file as argument.")
