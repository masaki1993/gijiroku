import subprocess

def remove_silence(input_file_path, output_file_path):
    subprocess.run(
        [
            "ffmpeg",
            "-i", input_file_path,
            "-af", "silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-30dB",
            output_file_path
        ]
    )