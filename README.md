# Taaghche-BookCapture
Taaghche-BookCapture is a suite of Python scripts designed to automate the process of capturing, cropping, renaming, and converting book pages from screenshots into a PDF document. This toolkit is specifically tailored for use with books from Taaghche.com.


## Overview
BookCapture-PDFConverter is an automated toolkit designed to streamline the process of converting book pages from Taaghche.com into a cohesive PDF document. This project includes scripts for screenshot capture, image cropping, file renaming, and PDF conversion, offering a complete solution from image capture to PDF creation.

## Features
- **Screenshot Capture:** Automated capturing of book pages.
- **Image Cropping & Renaming:** Sequential renaming and customizable cropping of screenshots.
- **PDF Conversion:** Conversion of processed images into a single PDF.

### 1. Screenshot Capture Script
This script automates the process of taking screenshots of each page of a book. It saves each screenshot as a JPEG file in a designated folder.

**Usage:**
- Run `python screenshot_capture.py`
- Ensure the book is open and positioned correctly on your screen.
- The script will automatically take screenshots and save them.

### 2. Image Cropping & Renaming Script
This script renames the captured image files sequentially and crops them to a specified size.

**Usage:**
- Run `python image_process_rename.py`
- The script will rename and crop the images based on predefined dimensions.
