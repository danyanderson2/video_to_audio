from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_mp3(mp4_file, mp3_file):
    # Load the video file
    video_clip = VideoFileClip(mp4_file)

    # Extract the audio
    audio_clip = video_clip.audio

    # Write the audio to an mp3 file
    audio_clip.write_audiofile(mp3_file, codec='mp3')

    # Close the clips
    audio_clip.close()
    video_clip.close()


for i in range(1,9):
    convert_mp4_to_mp3(f'D:\Le Coffret VIP\Avant le lancement\mois pour devenir mon propre patron\Vidéos\Module {i}.mp4',
                       f'D:\Le Coffret VIP\Avant le lancement\mois pour devenir mon propre patron\Vidéos\Module {i}.mp3')

