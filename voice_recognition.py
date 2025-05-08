import speech_recognition as sr
import time


class VoiceRecognizer:
    """
    Voice command recognition for game control
    """

    def __init__(self):
        """
        Initialize voice recognizer
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_command(self, game_logic):
        """
        Listen for voice commands in a continuous loop

        Args:
            game_logic: GameLogic instance to control
        """
        with self.microphone as source:
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source)
            print("🎙️ Listening for: 'rock paper scissors shoot'...")

            while True:
                try:
                    # Listen for audio
                    audio = self.recognizer.listen(source)

                    # Recognize speech
                    phrase = self.recognizer.recognize_google(audio).lower()
                    print(f"Detected: {phrase}")

                    # Check for trigger phrase
                    if "shoot" in phrase:
                        print("✅ Triggering game!")
                        game_logic.start_new_game()
                        time.sleep(5)  # Prevent fast re-trigger

                except sr.UnknownValueError:
                    print("❌ Could not understand audio.")
                except sr.RequestError:
                    print("⚠️ Could not request results from Google.")