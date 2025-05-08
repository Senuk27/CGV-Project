import cv2
import cvzone


class Visualizer:
    """
    Visualization components for the game UI
    """

    def __init__(self):
        """
        Initialize visualizer
        """
        self.ai_position = (149, 310)
        self.timer_position = (602, 432)
        self.result_position = (560, 410)
        self.ai_score_position = (410, 215)
        self.player_score_position = (1112, 215)
        self.font = cv2.FONT_HERSHEY_PLAIN
        self.text_color = (232, 12, 0)

    def display_scores(self, img, scores):
        """
        Display scores on the image

        Args:
            img: Background image
            scores: [AI score, Player score]

        Returns:
            image: Updated image with scores
        """
        cv2.putText(img, str(scores[0]), self.ai_score_position,
                    self.font, 4, self.text_color, 4)
        cv2.putText(img, str(scores[1]), self.player_score_position,
                    self.font, 4, self.text_color, 4)
        return img

    def display_timer(self, img, timer):
        """
        Display countdown timer

        Args:
            img: Background image
            timer: Timer value

        Returns:
            image: Updated image with timer
        """
        if timer > 0:
            cv2.putText(img, str(int(timer)), self.timer_position,
                        self.font, 6, self.text_color, 4)
        return img

    def display_result(self, img, result_text, imgAI):
        """
        Display game result and AI's move

        Args:
            img: Background image
            result_text: Text result to display
            imgAI: AI move image


        """
        # Add AI move image
        if imgAI is not None:
            img = cvzone.overlayPNG(img, imgAI, self.ai_position)

        # Add result text
        if result_text:
            cv2.putText(img, result_text, self.result_position,
                        self.font, 2, self.text_color, 4)

        return img