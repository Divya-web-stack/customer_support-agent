class Memory:
    def __init__(self):
        self.lead_info = {}
        self.sop_gaps = []
        self.escalation_reason = None
        self.key_questions = []

    def store_lead_info(self, question, answer):
        self.lead_info[question] = answer

    def lead_info_complete(self):
        return len(self.lead_info) == 3
