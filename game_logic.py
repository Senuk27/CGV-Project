import cv2
import random
import time
import cvzone


class GameLogic:
    """
    Game logic for Rock-Paper-Scissors-Lizard-Spock
    """

    def __init__(self):
        """
        Initialize game state variables
        """
        # Game state
        self.timer = 0
        self.stateResult = False
        self.startGame = False
        self.scores = [0, 0]  # [AI, Player]
        self.resultText = ""
        self.initialTime = 0
        self.lastAIMove = None

        # Moves dictionary
        self.moves = {
            1: "Rock",
            2: "Paper",
            3: "Scissors",
            4: "Lizard",
            5: "Spock"
        }

        # Result matrix according to official rules
        # [Row][Column] where Row is player move and Column is AI move
        self.resultMatrix = [
            [0, -1, 1, 1, -1],  # Rock
            [1, 0, -1, -1, 1],  # Paper
            [-1, 1, 0, 1, -1],  # Scissors
            [-1, 1, -1, 0, 1],  # Lizard
            [1, -1, 1, -1, 0]  # Spock
        ]

    def start_new_game(self):
        """
        Start a new game round
        """
        self.startGame = True
        self.initialTime = time.time()
        self.stateResult = False
        self.resultText = ""  # Clear the previous result text

    def update_game_state(self, imgBG, hands, hand_detector):
        """
        Update game state based on current input

        Returns:
            tuple: (imgBG, imgAI) - Updated background image and AI move image
        """
        imgAI = None

        if self.startGame:
            if not self.stateResult:
                # Clear result text while timer is active
                self.resultText = ""
                self.timer = time.time() - self.initialTime

                if self.timer > 1:
                    self.stateResult = True
                    self.timer = 0

                    if hands:
                        playerMove = None
                        hand = hands[0]
                        fingers = hand_detector.fingers_up(hand)

                        # Get player move based on gesture
                        playerMove = hand_detector.interpret_gesture(fingers)

                        # Generate AI move
                        aiMove = random.randint(1, 5)
                        imgAI = cv2.imread(f'Resources/{aiMove}.png', cv2.IMREAD_UNCHANGED)
                        self.lastAIMove = imgAI

                        # Determine winner
                        if playerMove and 1 <= playerMove <= 5:
                            result = self.resultMatrix[playerMove - 1][aiMove - 1]
                            if result == 1:
                                self.scores[1] += 1
                                self.resultText = "You Win!"
                            elif result == -1:
                                self.scores[0] += 1
                                self.resultText = "AI Wins!"
                            else:
                                self.resultText = "It's a Tie!"
                        else:
                            self.resultText = "Gesture Not Recognized!"

        # If we have a result and an AI move image from a previous state, overlay it
        if self.stateResult and self.lastAIMove is not None:
            imgAI = self.lastAIMove

        return imgBG, imgAI

    def get_move_name(self, move_id):

        return self.moves.get(move_id, "Unknown")