import re

class EscalationAgent:
    def __init__(self):
        self.angry_keywords = [
            "angry",
            "upset",
            "frustrated",
            "complaint",
            "bad service",
            "not happy",
            "disappointed"
        ]

        self.human_request_keywords = [
            "human",
            "real person",
            "representative",
            "talk to someone"
        ]

        self.medical_keywords = [
            "medical",
            "doctor",
            "prescription",
            "treatment",
            "side effect",
            "migraine",
            "pain",
            "health",
            "therapy",
            "condition"
        ]

    def check(self, user_input, faq_result):
        text = user_input.lower()

        # Angry sentiment
        if any(word in text for word in self.angry_keywords):
            return {
                "escalate": True,
                "reason": "Customer complaint",
                "message": (
                    "I’m sorry to hear about your experience. "
                    "I will escalate your concern to a human representative immediately."
                )
            }

        # Explicit human request
        if any(word in text for word in self.human_request_keywords):
            return {
                "escalate": True,
                "reason": "Explicit request for human",
                "message": (
                    "I understand your frustration, and I’m sorry for the inconvenience. "
                    "I will connect you with a human representative for further assistance."
                )
            }

        # Medical question
        if any(word in text for word in self.medical_keywords):
            return {
                "escalate": True,
                "reason": "Medical question",
                "message": (
                    "I do not have enough medical information available in the SOP. "
                    "I will escalate this to a human representative for accurate assistance."
                )
            }

        # Low confidence or unsupported question
        if faq_result.get("confidence", 1.0) < 0.7 or faq_result.get("escalate", False):
            return {
                "escalate": True,
                "reason": faq_result.get("reason", "Low confidence"),
                "message": (
                    "I don't have enough information on that. "
                    "I'll escalate this to a human representative."
                )
            }

        return {
            "escalate": False,
            "reason": None,
            "message": None
        }