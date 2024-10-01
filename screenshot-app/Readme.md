# Screenshot App
This is a simple Python application that allows you to take screenshots using the pyautogui and tkinter libraries. The screenshot is saved in the specified folder and displayed after capture.

### Prerequisites
- Python 3.x installed
- Required libraries:
    - `pyautogui`
    - `tkinter`
    - `Pillow` (for displaying the screenshot)
You can install the required libraries by running:

```sh
pip install pyautogui Pillow
```
### How to Use
1. Clone this repository or download the script.
2. Ensure you have the necessary libraries installed as mentioned above.
3. Run the Python script:
```
python screenshot_app.py
```
4. A window will appear with two buttons:
- **Take Screenshot:** Clicking this button will start a 5-second countdown and then capture your screen. The screenshot will be saved in the screenshot.images folder inside the app directory.
- **QUIT:** Clicking this button will close the application.
5. After the screenshot is taken, it will be automatically displayed.

### Note
- Ensure that the screenshot.images directory exists before running the script, or modify the script to create it automatically if it doesn't exist.
- Screenshots are saved with a timestamp in milliseconds as the filename.