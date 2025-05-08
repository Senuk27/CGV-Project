import cv2
import numpy as np
import time
import threading

# Import modules
from camera import Camera
from hand_detector import HandDetector
from voice_recognition import VoiceRecognizer
from game_logic import GameLogic
from image_processor import ImageProcessor
from visualization import Visualizer


def main():
    # Initialize components
    camera = Camera()
    hand_detector = HandDetector()
    voice_recognizer = VoiceRecognizer()
    game_logic = GameLogic()
    image_processor = ImageProcessor()
    visualizer = Visualizer()

    # Start voice recognition in a separate thread
    listener_thread = threading.Thread(target=voice_recognizer.listen_for_command, args=(game_logic,), daemon=True)
    listener_thread.start()

    # Create display windows
    cv2.namedWindow("Processing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Processing", 640, 480)

    while True:
        # Capture frame and prepare background
        success, img = camera.capture_frame()
        imgBG = cv2.imread("Resources/BG2.png")

        if not success:
            print("Failed to capture frame")
            break

        # Scale and crop image
        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]

        # Process image and detect hands
        processed_images = image_processor.process_image(imgScaled)
        hands, img_with_hands = hand_detector.find_hands(imgScaled)

        # Update game state
        imgBG, imgAI = game_logic.update_game_state(imgBG, hands, hand_detector)

        # Insert camera feed into background
        imgBG[234:654, 795:1195] = img_with_hands

        # Display scores and results
        imgBG = visualizer.display_scores(imgBG, game_logic.scores)
        imgBG = visualizer.display_timer(imgBG, game_logic.timer)
        imgBG = visualizer.display_result(imgBG, game_logic.resultText, imgAI)

        # Display image processing stages
        stack = np.hstack(processed_images)
        cv2.imshow("Processing", stack)
        cv2.imshow("BG", imgBG)

        # Exit on 'q' press
        if cv2.waitKey(1) == ord('q'):
            break

    # Clean up
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()