# Video-Small-Basic
**"Once a joke, now very serious"**

# General Instructions:

## Requirements for Compilation and Video Preperation (minimum tested):
1. Small Basic v1.2 (Only necessary for compilation)
2. Python v 3.12 (Only necessary for video preperation)
     - Matplotlib v3.8.4
     - opencv-python v4.9.0.80
3. Any program which can resize and extract audio from videos (required for video preperation only)

## Video preparation:

### Conversion to supported format
*  Resize the video to a very small size (preferable no more than 100x75) and change the framerate to 30FPS
*  You can use tools like FFMPEG for this
*  Edit the python script and assign your target video file to the variable "cap" in line 37
*  Run the script and rename "output.txt" to "(name).txt"
*  Extract the audio from your video as an mp3 file and name it "(name).mp3"

### Placing the video in the right place
*  Place the generated txt and mp3 files in "\path\to\executable\vids\"

## Running the video:

### Arguments and their correct order
1. vname: Should be the (name) you used from earlier
2. qloss: When the video plays, the output is at 30/qloss FPS
3. fx: width of your video
4. fy: height of your video
5. Correct syntax: `video.exe vname qloss fx fy`
For example `video.exe apple 4 96 72` loads apple.txt and apple.mp3, plays output at 30/4 FPS and interprets the text file as 96x72
If you did everything right, the video should play just fine

## Compilation of video decoder
1. Open the video.sb file in small basic
2. Run it with F5
3. Your new code has been compiled
4. If there was an executable witht he same name in the same directory (e.g. video.sb and video.exe), video.exe now runs the updated code.

## User-end fixes for known issues
1.  Some videos are simply too graphically intensive to be played.
     - These include videos with flashing light and lots of background details.
     - You may use higher qloss values to load them.
2.   I do not know any other issues. If you know any, please let me know :)
