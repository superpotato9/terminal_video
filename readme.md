# Color Video to Text Conversion

updated version of the video to ascii text version made by science elf 

 ## Check out [this video](https://www.youtube.com/watch?v=uGoR3ZYZqjc) for more information and to see sample output for video to text conversion.

![Screenshot](screenshot.png)
A sample image converted to text and printed to the terminal.

# changes:
the main issue with the original version is it could not play nor sync to music this was fixed by 
1. adding frame rate cap using time delta 
2. adidng simple audio playback
3. optimmization mostly through the removal of numpy arrays due to their large overhead this moves the computing time to before the video plays reducing frame compute time
# limitations:
currently the code is admitally slow this is because of terminal out lag and the lag from the code a c# version might be coming soon






---

**Note:** To run these programs, you will need Python 3 installed, alongside NumPy and OpenCV (for image io).


## Displaying Videos as Text
The python script videoToTextColor.py will play back a video provided as an argument along with the width in text chars as text to the terminal.

`python3 videoToTextColor.py your_video_here.mp4 200`

The aspect ratio of the output can be configured in the header of the python file.
