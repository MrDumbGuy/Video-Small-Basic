# Video-Small-Basic
**"Once a joke, now very serious"**

# Attention users of Windows 11 23H2
As I had been putting the update off myself, I only recently learned about the fall of performance. To increase your performance (and get the program running), follow these steps:
1. Open PowerShell as admin and run the two following scripts
  - `Set-ExecutionPolicy Unrestricted`
  - `Get-AppxPackage Microsoft.SecHealthUI -AllUsers | Reset-AppxPackage`
2. Enable hardware virtualisation (usually done in UEFI or BIOS)
3. Disable memory integrity (you may be unable to turn it back on depending on your drivers)

# General Instructions:

## Requirements for Compilation and Video Preperation (minimum tested):
1. Small Basic v1.2 (Only necessary for compilation of the video player)
2. Python v 3.12 (Only necessary for video preperation)
     - Matplotlib v3.8.4
     - opencv-python v4.9.0.80
3. An external program to resize and extract audio from videos (required for video preperation only)

## Video preparation:

### Conversion to supported format
*  Resize the video to 96x72
*  If the video framerate is 50 or 60 FPS, you may want to lower it to 25 or 30 FPS.
*  Edit the python script and assign your target video file to the variable "cap" in line 37
*  Run the script and rename "output.txt" to "(name).txt"
*  Extract the audio from your video as an mp3 file and name it "(name).mp3"

### Placing the video in the right place
*  Place the generated txt and mp3 files in "\path\to\video.exe\vids\"

## Running the video:

### Arguments and their correct order
1. videoName: Should be the (name) you used from earlier
2. inputFramerate: The framerate of the original video file
3. frameRatio: The program plays only one in n frames. Try to not increase it too much.
4. Correct syntax: `video.exe videoName inputFramerate frameRatio`
For example: `video.exe apple 30 4` loads apple.txt and apple.mp3, and plays output at 30/4 FPS.

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
