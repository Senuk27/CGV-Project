import cv2


class Camera:
    """
    Camera class to handle video capture functionality
    """

    def __init__(self, camera_id=0, width=640, height=480):
        """
        Initialize camera with specified settings

        Args:
            camera_id (int): Camera device ID
            width (int): Width resolution
            height (int): Height resolution
        """
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(3, width)  # Width
        self.cap.set(4, height)  # Height

    def capture_frame(self):
        """
        Capture a single frame from the camera

        Returns:
            tuple: (success, frame) - Boolean success flag and the captured frame
        """
        return self.cap.read()

    def release(self):
        """
        Release the camera resources
        """
        self.cap.release()