from moviepy.editor import VideoFileClip
import os



# Hi!!! No need to go beneath the area below if you're a nove at coding ;)
######################################################################################################################
PATH_TO_FOLDER_WITH_VIDEO_FILES = ''    # path to input folder
PATH_TO_OUTPUT_FOLDER =r"D:\folder"              # path to output folder

#######################################################################################################################
# in case you have n files in a folder which you want to convert all to audio with single


def convert_video_to_mp3(video_path, output_folder):
    # Check if the video file exists
    if not os.path.isfile(video_path):
        print(f"The file {video_path} does not exist.")
        return

    # Extract the file name without extension
    file_name = os.path.splitext(os.path.basename(video_path))[0]

    # Load the video file
    video_clip = VideoFileClip(video_path) # instantiate a VideoFileClip object

    # Construct the output file path
    output_file_path = os.path.join(output_folder, f"{file_name}.mp3")

    # Write the audio to an MP3 file
    video_clip.audio.write_audiofile(output_file_path)  # actual conversion
    print(f"Converted {video_path} to {output_file_path}")

# Calling function
video_formats = ['avi', 'mp4', 'mkv', 'mov', 'mpeg', 'flv', 'wmv']

# Create the output folder if it doesn't exist
os.makedirs(PATH_TO_OUTPUT_FOLDER, exist_ok=True)

# Loop through the video files in the input folder and convert them
try:
    os.listdir(PATH_TO_FOLDER_WITH_VIDEO_FILES)
except FileNotFoundError:
    print('File not found')
else:
    for file_name in os.listdir(PATH_TO_FOLDER_WITH_VIDEO_FILES):
        if file_name.split('.')[-1].lower() in video_formats:
            video_path = os.path.join(PATH_TO_FOLDER_WITH_VIDEO_FILES, file_name)
            convert_video_to_mp3(video_path, PATH_TO_OUTPUT_FOLDER)
# single file converters
