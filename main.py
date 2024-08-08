from pydub import AudioSegment
import os

def convert_audio(input_file_path, output_file_path):
    # Extract file extension to determine format
    input_format = os.path.splitext(input_file_path)[1][1:]  # Removes the dot (.)
    output_format = os.path.splitext(output_file_path)[1][1:]

    # Load audio file
    audio = AudioSegment.from_file(input_file_path, format=input_format)

    # Export audio file in the desired format
    audio.export(output_file_path, format=output_format)

    print(f"Conversion successful! {input_file_path} -> {output_file_path}")


# Example usage:
convert_audio('output.mp3', 'output.wav')
