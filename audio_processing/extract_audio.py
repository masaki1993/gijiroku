import subprocess
import os

def extract_audio_from_video(input_file_path, output_file_path):
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_file_path,
            "-q:a",
            "0",
            "-map",
            "a",
            output_file_path,
        ]
    )