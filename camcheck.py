import cv2


def test_camera():
    cap = cv2.VideoCapture(0)  # Open the default camera

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        success, img = cap.read()  # Capture frame-by-frame

        if not success:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Camera Feed", img)  # Display the resulting frame

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows


if __name__ == "__main__":
    test_camera()
