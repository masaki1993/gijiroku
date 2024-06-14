import subprocess
import os
from loguru import logger

def get_audio_duration(file_path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def calculate_bitrate(duration):
    target_size_mb = 5
    return f"{int(target_size_mb * 8 * 1024 / duration)}k"

class AudioProcessor:
    @classmethod
    def compress_audio(cls, input_file_path, output_file_path):
        logger.info("=== compress audio ===")
        
        duration = get_audio_duration(input_file_path)
        bitrate = calculate_bitrate(duration)
        logger.info(f"Target bitrate: {bitrate}")
        
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i", input_file_path,
                "-codec:a", "mp3",
                "-ar", "16000",
                "-ac", "1",
                "-b:a", bitrate,
                output_file_path,
            ]
        )
        logger.info(f"Compressed audio size: {os.path.getsize(output_file_path)}")