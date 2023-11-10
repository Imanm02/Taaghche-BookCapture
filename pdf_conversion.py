import os
import subprocess

def convert_images_to_pdf():
    # Walk through all files in the current directory and its subdirectories
    for path, subdirs, files in os.walk('.'):
        # Skip directories that contain subdirectories
        if subdirs:
            continue

        # Get the name of the current directory
        name = os.path.basename(path)
        # Create an output directory within the current directory
        output_dir = os.path.join(path, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Define the command to crop images using ImageMagick's 'mogrify'
        crop_command = f"mogrify -path \"{output_dir}\" -crop 1672x789+124+197 \"{path}\"/*.jpg"
        # Define the command to convert cropped images to a PDF using ImageMagick's 'convert'
        convert_command = f"convert \"{output_dir}/*.jpg\" \"{output_dir}/{name}.pdf\""

        # Execute the cropping command
        subprocess.run(crop_command, shell=True)
        # Execute the conversion command
        subprocess.run(convert_command, shell=True)

if __name__ == "__main__":
    convert_images_to_pdf()