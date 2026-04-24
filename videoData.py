import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# WINDOWS -- *'DIVX'
# MACOS or LINUX -- *'XVID'

writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

# Print the width and height of the video frames
while True:
    ret, frame = cap.read()
    writer.write(frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame in grayscale
    #cv2.imshow('frame' , gray)

    # Display the resulting frame in colors
    cv2.imshow('frame' , frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()