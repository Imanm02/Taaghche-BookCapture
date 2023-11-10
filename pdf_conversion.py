import os
import subprocess

def convert_images_to_pdf():
    for path, subdirs, files in os.walk('.'):
        if subdirs:
            continue  # Skip directories with subdirectories

        name = os.path.basename(path)
        output_dir = os.path.join(path, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Define ImageMagick commands
        crop_command = f"mogrify -path \"{output_dir}\" -crop 1672x789+124+197 \"{path}\"/*.jpg"
        convert_command = f"convert \"{output_dir}/*.jpg\" \"{output_dir}/{name}.pdf\""

        # Execute commands
        subprocess.run(crop_command, shell=True)
        subprocess.run(convert_command, shell=True)

if __name__ == "__main__":
    convert_images_to_pdf()