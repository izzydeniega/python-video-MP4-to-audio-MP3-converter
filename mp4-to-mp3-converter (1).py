import os
import subprocess
import sys

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def install_ffmpeg():
    print("FFmpeg is not installed. Please install FFmpeg manually and add it to your system PATH.")
    print("Installation instructions: https://ffmpeg.org/download.html")
    sys.exit(1)

def validate_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower() == '.mp4'

def convert_mp4_to_mp3(input_file, output_file):
    try:
        subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-q:a", "2", output_file], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Start
    print("MP4 to MP3 Converter")

    # Open Python script
    script_name = os.path.basename(__file__)
    print(f"Running script: {script_name}")

    # Check if video file exists
    input_file = input("Enter the path to the MP4 file: ")
    if not os.path.exists(input_file):
        print("Error: The specified file does not exist.")
        return

    # Validate file format
    if not validate_file_format(input_file):
        print("Error: Unsupported file format. Please provide an MP4 file.")
        return

    # Check if FFmpeg is installed
    if not check_ffmpeg():
        install_ffmpeg()

    # Extract audio using FFmpeg
    output_file = os.path.splitext(input_file)[0] + ".mp3"
    print("Converting MP4 to MP3...")
    if convert_mp4_to_mp3(input_file, output_file):
        print(f"Conversion successful. MP3 file saved as: {output_file}")
    else:
        print("Error: Conversion failed.")

if __name__ == "__main__":
    main()
