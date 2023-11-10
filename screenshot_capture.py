import pyautogui as user
from time import sleep

# Wait for 5 seconds to allow the user to switch to the book view on their screen
sleep(5)

# Move the mouse cursor to the page turning area (coordinates may need adjustment)
user.moveTo(80, 529)

# Loop to capture 400 pages (adjust the range as needed)
for i in range(400):
    # Take a screenshot of the entire screen
    img = user.screenshot()
    # Save the screenshot in the 'book' folder with a sequential filename
    img.save(f"book/{i}.jpg")
    # Simulate a mouse click to turn the page
    user.click()
    # Wait for 0.5 seconds to allow the page turn to complete
    sleep(0.5)