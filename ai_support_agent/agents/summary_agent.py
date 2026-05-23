class SummaryAgent:
    def __init__(self, memory):
        self.memory = memory

    def generate(self, last_user_input):
        summary = [
            "## Customer Intent",
            f"{last_user_input}",
            "\n## Key Questions Asked",
            f"{', '.join(self.memory.key_questions) if self.memory.key_questions else 'N/A'}",
            "\n## Lead Information",
            '\n'.join([f"- {k}: {v}" for k, v in self.memory.lead_info.items()]) or 'N/A',
            "\n## SOP Gaps",
            '\n'.join(self.memory.sop_gaps) or 'None',
            "\n## Escalation Reason",
            f"{self.memory.escalation_reason or 'None'}",
            "\n## Recommended Next Action",
            "Escalate to human agent" if self.memory.escalation_reason else "Follow up with lead"
        ]
        return '\n'.join(summary)
