import cv2

from zest import capture_and_display, record_window_stream
# Call the function capture_and_display with the desired window title, to output video stream form the desired on-screen window 
# capture_and_display('BlueStacks App Player')
# Press q to quit

# Example usage of record_window_stream, which records the video stream from the desired on-screen window and returns the frames and FPS
# This example simply displays the frames and FPS
for frame, fps in record_window_stream("BlueStacks App Player"):
    # Process the frame and FPS as needed
    print(f"FPS: {fps:.2f}", end='\r')  # Display FPS
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()