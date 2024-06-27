import os
import random
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/convert"})

video_duration = 14

# chooses random background from "backgrounds" folder
items = os.listdir("backgrounds")
file_count = sum(1 for item in items if os.path.isfile(os.path.join("backgrounds", item))) - 1

clip_number = str(random.randint(0,file_count-1))
background = VideoFileClip("backgrounds/background_"+clip_number+".mp4")

# selects random 
starting = random.randint(0,int( background.duration - video_duration))
background = background.subclip(starting, starting+video_duration) 

print("using clip #"+clip_number+" with starting time "+str(starting//60)+":"+str(starting%60))

background.write_videofile("output/testingmore.mp4", threads=4, audio = False, logger=None) 


# Function to create a video with captions from an array of tuples
def create_captions_video(captions):
    clips = []
    video_width, video_height = 720, 1280  # 9:16 aspect ratio

    # Iterate over the captions array
    for text, duration in captions:
        if not text == "":
        # Create a TextClip for each caption
            txt_clip = TextClip(text, fontsize=70, color='white', size=(video_width, video_height), bg_color='black')
            # Set the duration for each TextClip
            txt_clip = txt_clip.set_duration(duration)
            clips.append(txt_clip)
    
    # Concatenate all TextClips
    video = concatenate_videoclips(clips)
    
    # Write the result to a file
    video.write_videofile("output/captions_video_9_16.mp4", fps=24, logger = None)


captions = [
    ("Hello, world!", 2),
    ("This is a test.", 3),
    ("MoviePy is great!", 4)
]

#create_captions_video(captions)

# showing clip 
#clip.write_videofile("movie.mp4", threads=4, audio = False, logger=None) 


