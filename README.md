# Taaghche-BookCapture

Taaghche-BookCapture is a suite of Python scripts designed to automate the process of capturing, cropping, renaming, and converting book pages from screenshots into a PDF document. This toolkit is specifically tailored for use with books from Taaghche.com.

This toolkit can actually be used for every book store website, we just need to fix the sizes and variables in the codes.

## Overview

BookCapture-PDFConverter is an automated toolkit designed to streamline the process of converting book pages from Taaghche.com into a cohesive PDF document. This project includes scripts for screenshot capture, image cropping, file renaming, and PDF conversion, offering a complete solution from image capture to PDF creation.

## Features

- **Screenshot Capture:** Automated capturing of book pages.
- **Image Cropping & Renaming:** Sequential renaming and customizable cropping of screenshots.
- **PDF Conversion:** Conversion of processed images into a single PDF.

### 1. Screenshot Capture

- Open the book on Taaghche.com and navigate to the page where you want to start capturing.
- Run the script:  
  `python screenshot_capture.py`
- Quickly switch back to the book view. The script will start capturing screenshots after a 5-second delay.

### 2. Image Cropping & Renaming

- After capturing all the screenshots, run the following script to rename and crop the images:  
  `python image_process_rename.py`
- The script will process all images in the current directory, renaming them sequentially and preparing them for PDF conversion.

### 3. PDF Conversion

- To convert the processed images into a single PDF, run:  
  `python pdf_conversion.py`
- The script will create an 'output' directory within each image folder and save the final PDF there.

### Notes
- Adjust the coordinates in `screenshot_capture.py` if the mouse does not accurately click the 'next page' button.
- Ensure the `book` folder in `screenshot_capture.py` exists or adjust the path as needed.
- The number of pages (400 in the script) can be adjusted based on the book length.
- ImageMagick commands in `pdf_conversion.py` might need adjustments based on your OS and ImageMagick configuration.

## Prerequisites

- Python
- Libraries: `pyautogui`, `subprocess`
- ImageMagick installed for image processing and PDF conversion.

## Maintainer

- [Iman Mohammadi](https://github.com/Imanm02)