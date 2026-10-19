
"""Unit tests for emotion detection."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the dominant emotion for sample statements."""

    def test_emotions(self):
        """Check the expected dominant emotions."""
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for text, expected in cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(
                    result["dominant_emotion"], expected
                )


if __name__ == "__main__":
    unittest.main()
