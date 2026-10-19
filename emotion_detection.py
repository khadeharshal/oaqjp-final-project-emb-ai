
import requests
import json


def emotion_detector(text_to_analyze):
    """Detect emotions in the supplied text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url, json=payload, headers=headers, timeout=30
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response.raise_for_status()
    result = json.loads(response.text)["emotionPredictions"][0][
        "emotion"
    ]

    emotions = {
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"]
    }

    emotions["dominant_emotion"] = max(
        emotions, key=emotions.get
    )
    return emotions
