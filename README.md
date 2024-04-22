# Video-Small-Basic: Programmers Beware!
Made as an April Fools' joke, the worst video encoder and decoder of all time! Definitely not the best that I could do.

## Features:
1. 22-Color playback!
2. Colorbleed on the leftmost part of the video!

## Compilation instructions for the video decoder:

### Requirements:
* Microsoft Small Basic 1.2
  
### Compilation:

1. Open Microsoft Small Basic, and open the "video.sb" file from within.
2. Change the variable 'apple' such that it points to your desired text file.
3. Change fc to reflect the number of frames in your video.
4. In line 20, change the audio file to your desired audio.
5. Running the script with F5 will compile the program.

## Usage instructions for video encoder

### Requirements (Minimum tested):
* Python 3.12+
  * numpy 1.26+
  * opencv-python 4.9+
  * matplotlib 3.8+

### Video preperation for video encoder:
Use FFMPEG to resize the video to 96x72 and apply the palette "palette.png" provided in the source

### Usage

1. Edit 'videoToRaw.py' and edit the video path in line 53 to point to your desired video.
2. Run the file
3. If you are using a laptop, please plug it in. Otherwise, even 3 minutes of video will take days to encode. Not may, will.
4. The encoded text will appear as 'datacol.txt' in the same directory.
- Running the script may take extremely long on lower-end machines.

## Usage of video decoder

1. Just run the executable. If you compiled it and edited the code properly, you should see the video start to play with sound!
