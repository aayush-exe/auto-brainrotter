import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/convert"})

#from moviepy.editor import TextClip, concatenate_videoclips


# clip = VideoFileClip("testvideo.mp4") 
  
# # clipping of the video  
# # getting video for only starting 10 seconds 
# clip = clip.subclip(0, 10) 
  
# # rotating video by 180 degree 
# clip = clip.rotate(180) 
  
# # Reduce the audio volume (volume x 0.5) 
# clip = clip.volumex(0.5) 

##clip.resize(width=480)
  


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
    video.write_videofile("captions_video_9_16.mp4", fps=24, logger = None)

# Example usage
captions = [
    ("Hello, world!", 2),
    ("This is a test.", 3),
    ("MoviePy is great!", 4)
]

create_captions_video(captions)

# showing clip 
#clip.write_videofile("movie.mp4", threads=4, audio = False, logger=None) 


