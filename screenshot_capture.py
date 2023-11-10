import pyautogui as user
from time import sleep

# Set a delay to allow time to switch to the book view
sleep(5)

# Move to the page turning area and start capturing
user.moveTo(80, 529)
for i in range(400):
    img = user.screenshot()
    img.save(f"book/{i}.jpg")  # Save each screenshot in a book folder
    user.click()               # Simulate click for turning the page
    sleep(0.5)                 # Short delay between page turns