import json
import os
from openai import OpenAI

from utils.prompts import SYSTEM_PROMPT

sop_path= "ai_support_agent/sop_data.json" 

class FAQAgent:
    def __init__(self, sop_path):
        with open(sop_path, "r", encoding="utf-8") as f:
            self.sop_data = json.load(f)

        self.model = "deepseek/deepseek-chat-v3-0324"
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

    def answer(self, question):
        # Search SOP for answer
        for item in self.sop_data.get("faqs", []):
            if question.lower() in item["q"].lower() or item["q"].lower() in question.lower():
                return {
                    "response": item["a"],
                    "confidence": 0.95,
                    "escalate": False,
                    "reason": None,
                }

        # If not found, use OpenRouter (OpenAI-compatible) to check for partial match
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"SOP: {self.sop_data}\n\nCustomer: {question}\nAnswer strictly from SOP. If not found, say so.",
                    },
                ],
                temperature=0.0,
                max_tokens=200,
            )

            answer = completion.choices[0].message.content.strip()
            if "I don't have enough information" in answer or "escalate" in answer.lower():
                return {
                    "response": "I don't have enough information on that. I'll escalate this to a human representative.",
                    "confidence": 0.3,
                    "escalate": True,
                    "reason": "Out of SOP scope",
                }

            return {
                "response": answer,
                "confidence": 0.7,
                "escalate": False,
                "reason": None,
            }
        except Exception as e:
            return {
                "response": "I'm unable to process your request right now. Escalating to a human agent.",
                "confidence": 0.0,
                "escalate": True,
                "reason": str(e),
            }

