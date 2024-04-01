# Video-Small-Basic: Programmers Beware!
Made as an April Fools' joke, the worst video encoder and decoder of all time! Definitely not the best that I could do.

## Features:
1. 16-Color playback!
2. Inconsistent video speed across devices (and possibly on the same device)!
3. Absolutely no sound!
4. Colorbleed on the leftmost part of the video!

## Compilation instructions for the video decoder:

### Requirements:
* Microsoft Small Basic 1.2+

### Compilation:

1. Open Microsoft Small Basic, and open the "video.sb" file from within.
2. Change the variable 'video' such that it points to your desired text file.
3. Change fx, fy and fc to meet your video's requirements (video width, video height, number of frames)
4. Running the script with F5 will compile the program.

## Usage instructions for video encoder

### Requirements (Minimum tested):
* Python 3.12+
  * numpy 1.26+
  * opencv-python 4.9+

### Usage

1. Edit 'videoToRaw.py' and edit the video path in line 35 to point to your desired video.
2. Run the file
3. The encoded text will appear as 'data.txt' in the same directory.
- Running the script may take extremely long on lower-end machines.

## Usage of video decoder

1. Just run the executable. If you compiled it and edited the script properly, you should see the video start to play!
