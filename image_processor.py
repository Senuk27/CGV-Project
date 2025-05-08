import cv2
import numpy as np


class ImageProcessor:
    """
    Image processing techniques for visualization and analysis
    """

    def __init__(self):
        """
        Initialize image processor
        """
        pass

    def process_image(self, img):
        """
        Process image through multiple stages for visualization and analysis

        Args:
            img: Input color image

        Returns:
            tuple: (gray, blur, thresh, edges) - Different processing stages
        """
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply thresholding
        _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Apply edge detection
        edges = cv2.Canny(thresh, 50, 150)

        return (gray, blur, thresh, edges)

    def overlay_image(self, background, overlay_img, position):

        import cvzone

        # Ensure overlay has alpha channel
        if overlay_img is not None:
            if overlay_img.shape[2] == 3:
                overlay_img = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2BGRA)

            return cvzone.overlayPNG(background, overlay_img, position)

        return background