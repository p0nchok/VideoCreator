import json

import numpy as np
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from moviepy.config import change_settings
from moviepy.video.fx.all import crop

change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def main():
    # Get Data -> START
    print("Stage: Get Data -> START")

    # Get Background Footage -> START
    print("Stage: Get Background Footage -> START")
    background_footage = r'C:\Users\User\PycharmProjects\VideoCreator\BackgroundContent\MC_Parkour_Shaders.mp4'
    print("Stage: Get Background Footage -> DONE")
    # Get Background -> ND

    # Get Text -> START
    print("Stage: Get TEXT -> START")
    text_json_path = r'C:\Users\User\PycharmProjects\VideoCreator\Text\conversations.json'
    data_text = get_text(text_json_path)

    # Dump into temp txt file
    with open(r'C:\Users\User\PycharmProjects\VideoCreator\Text\data.txt', 'w') as f:
        f.write(data_text)
    # print(data_text)

    with open(r'C:\Users\User\PycharmProjects\VideoCreator\Text\data.txt') as f:
        lines = f.readlines()

    new_lines = []
    for line_num, line in enumerate(lines):
        if (int(line_num) % 2) == 0:
            new_lines.append(line)

    # Can delete temp txt file with data

    print("Stage: Get TEXT -> DONE")
    # Get Text -> END
    print("Stage: Get Data -> DONE")
    # Get Data -> END




    # Main Page End

def test_main():

    # Parameters:
    background_footage_path = r'C:\Users\User\PycharmProjects\VideoCreator\BackgroundContent\MC_Parkour_Shaders.mp4'
    output_folder = r'C:\Users\User\PycharmProjects\VideoCreator\Output'

    # Get Data -> START
    print("Stage: Get Data -> START")

    # Get Background Footage -> START
    print("Stage: Get Background Footage -> START")
    # Implement: Add random video
    background_footage_video = background_footage_path
    print("Stage: Get Background Footage -> DONE")
    # Get Background -> ND

    # Get Text -> START
    print("Stage: Get TEXT -> START")
    text_json_path = r'C:\Users\User\PycharmProjects\VideoCreator\Text\conversations.json'
    data_text = get_text(text_json_path)

    # Dump into temp txt file
    with open(r'C:\Users\User\PycharmProjects\VideoCreator\Text\data.txt', 'w') as f:
        f.write(data_text)
    # print(data_text)

    with open(r'C:\Users\User\PycharmProjects\VideoCreator\Text\data.txt') as f:
        lines = f.readlines()

    new_lines = []
    for line_num, line in enumerate(lines):
        if (int(line_num) % 2) == 0:
            new_lines.append(line)

    # Can delete temp txt file with data

    print("Stage: Get TEXT -> DONE")
    # Get Text -> END
    print("Stage: Get Data -> DONE")
    # Get Data -> END

    print("")
    print("Stage: Combine -> START")

    background_footage = VideoFileClip(background_footage_video, audio=False)
    video_title = "10_Interesting_Facts"
    video_output_name = f"{video_title}"
    output_video_path = fr"{output_folder}\{video_output_name}.mp4"
    # temp_combine_content(background_footage, output_video_path)
    temp_combine_video(background_footage_path, new_lines, output_folder)

def temp_combine_video(background_clip_path, text_data, output_video_path):

    screen_size = (1080,1920)
    text_screen_size = (320,1280)
    # Temp output test
    output_video_path = fr"C:\Users\User\PycharmProjects\VideoCreator\Output"

    # loading video dsa gfg intro video
    clip = VideoFileClip(background_clip_path)
    for index, line in enumerate(text_data):
        output = fr"{output_video_path}\Clip{index}.mp4"
        # clipping of the video
        # getting video for only starting 10 seconds
        clip = clip.subclip(0, 10)

    # Generate a text clip

        txt_clip = TextClip(line, fontsize=35, color='black', size=text_screen_size, method='caption', bg_color="white")

        # setting position of text in the center and duration will be 10 seconds
        txt_clip = txt_clip.set_pos('center').set_duration(10)

        color_clip = ColorClip(size=(420, 1330), color=(100, 0, 0)).set_duration(10)
        color_and_text_clip = CompositeVideoClip([color_clip, txt_clip])

        # Overlay the text clip on the first video clip
        # video = CompositeVideoClip([clip, txt_clip])
        video = CompositeVideoClip([clip, color_and_text_clip])

        video = video.resize(height=1920)
        video = video.crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

        # Write the final video to the output file
        video.write_videofile(output, codec='libx264', audio_codec='aac', fps=30)

def get_text(json_path):
    # Get Text
    total_text = json_path
    open_json_file = open(total_text)
    data = json.load(open_json_file)

    # topic_title = data[topic]['title']
    # topic_answers = data[topic]['mapping']
    # relevant_question = data[0]['mapping']['aaa23995-414a-4548-9de3-bc13a518af96']
    relevant_answer = data[0]['mapping']['a7140286-5be1-4a86-97ee-bddcb9e57617']['message']['content']['parts']
    # relevant_answer = relevant_answer['message']['content']['parts']
    # print(relevant_answer[0])
    return relevant_answer[0]

def combine_content(background_clip_path, output_video_path):
    # loading video dsa gfg intro video
    # clip = VideoFileClip(r'C:\Users\User\PycharmProjects\VideoCreator\BackgroundContent\MC_Parkour_Shaders.mp4')
    clip = background_clip_path
    # output_video_path = r'C:\Users\User\PycharmProjects\VideoCreator\Output\testvideo.mp4'

    # clipping of the video
    # getting video for only starting 10 seconds
    clip = clip.subclip(0, 10)

    # Reduce the audio volume (volume x 0.8)
    # clip = clip.volumex(0.8)

    # Generate a text clip

    txt_clip = TextClip("GeeksforGeeks", fontsize=75, color='black')

    # setting position of text in the center and duration will be 10 seconds
    txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # Write the final video to the output file
    video.write_videofile(output_video_path, codec='libx264', audio_codec='aac', fps=30)


if __name__ == "__main__":
    test_main()