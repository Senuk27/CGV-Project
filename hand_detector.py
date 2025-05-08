from cvzone.HandTrackingModule import HandDetector as CVZoneHandDetector


class HandDetector:
    """
    Hand detection and gesture recognition class
    """

    def __init__(self, max_hands=1):
        """
        Initialize the hand detector

        Args:
            max_hands (int): Maximum number of hands to detect
        """
        self.detector = CVZoneHandDetector(maxHands=max_hands)

    def find_hands(self, img, draw=True):
        """
        Find hands in the image

        Args:
            img: Input image
            draw (bool): Whether to draw hand landmarks

        Returns:
            tuple: (hands, img) - Detected hands and processed image
        """
        return self.detector.findHands(img, draw)

    def fingers_up(self, hand):
        """
        Determine which fingers are extended

        Args:
            hand: Hand object from detector

        Returns:
            list: Status of each finger [thumb, index, middle, ring, pinky]
                 1 for extended, 0 for closed
        """
        return self.detector.fingersUp(hand)

    def interpret_gesture(self, fingers):
        """
        Interpret hand gesture for Rock-Paper-Scissors-Lizard-Spock game

        Args:
            fingers: List of finger states

        Returns:
            int: Move ID (1-5) corresponding to the gesture, or None if not recognized
        """
        if fingers == [0, 0, 0, 0, 0]:
            return 1  # Rock
        elif fingers == [1, 1, 1, 1, 1]:
            return 2  # Paper
        elif fingers == [0, 1, 1, 0, 0]:
            return 3  # Scissors
        elif fingers == [0, 1, 0, 0, 0]:
            return 4  # Lizard
        elif fingers == [1, 1, 0, 1, 1]:
            return 5  # Spock
        else:
            return None  # No recognized gesture