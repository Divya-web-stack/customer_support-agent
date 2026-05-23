from utils.prompts import QUALIFICATION_QUESTIONS

class QualificationAgent:
    def __init__(self, memory):
        self.memory = memory

    def ask_questions(self, console, logger):
        for q in QUALIFICATION_QUESTIONS:
            if q not in self.memory.lead_info:
                answer = console.input(f"[bold cyan]{q} [/bold cyan]")
                self.memory.store_lead_info(q, answer)
                logger.log(f"Lead Info - {q}: {answer}")
