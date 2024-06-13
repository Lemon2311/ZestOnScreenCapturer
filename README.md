# ZestOnScreenCapturer
Dynamic python on-screen app recording solution, Zest records on screen apps in proper fps, and automatically resizes to the size of the window selected with a sampling rate of 1 second.
# Usage
Outputing video stream
```py
import cv2

from zest import capture_and_display, record_window_stream
# Call the function capture_and_display with the desired window title, to output video stream form the desired on-screen window 
capture_and_display('BlueStacks App Player')
# Press q to quit
```
Using video stream in python
```py
# Example usage of record_window_stream, which records the video stream from the desired on-screen window and returns the frames and FPS
# This example simply displays the frames and FPS
for frame, fps in record_window_stream("BlueStacks App Player"):
    # Process the frame and FPS as needed
    print(f"FPS: {fps:.2f}", end='\r')  # Display FPS
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```
This app was created when I wanted to create an AI model that plays a game on BlueStacks (Android Emulator for using Android apps on PC), and I faced the problem of not being able to get a decent fps with the existing libraries I found.
<br><br>
**Note:** The app needs to be visible on screen for Zest to be able to work.
