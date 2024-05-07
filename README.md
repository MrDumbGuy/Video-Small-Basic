# Video-Small-Basic: Programmers Beware!
Made as an April Fools' joke, the worst video encoder and decoder of all time! Definitely not the best that I could do.

## Features:
1. Grayscale playback with 8 total "colors"!
2. Colorbleed on the leftmost part of the video!

## Compilation instructions for the video decoder:

### Requirements:
* Windows Vista+ 64-bit
* Microsoft Small Basic 1.2
  
### Compilation:

1. Open Microsoft Small Basic, and open the "video.sb" file from within.
2. Change the variable 'apple' such that it points to your desired text file. (Program.Directory returns the executable's folder)
3. Change fc to reflect the number of frames in your video.
4. In line 29, change the audio file to your desired audio.
5. Running the script with F5 will compile the program.

## Usage instructions for video encoder

### Requirements (Minimum tested):
* Python 3.12+
  * opencv-python 4.9+
  * matplotlib 3.8+

### Video preperation for video encoder:
Use FFMPEG to resize the video to 96x72 format with 30 FPS.

### Usage

1. Edit 'videoToRaw.py' and edit the video path in line 37 to point to your desired video.
2. Run the file
3. If compilation is taking long on a laptop, try plugging it in. This shouldn't be a problem anymore.
4. The encoded text will appear as 'datacol.txt' in the same directory.

## Usage of video decoder

1. Just run the executable. If you compiled it and edited the code properly, you should see the video start to play with sound!
