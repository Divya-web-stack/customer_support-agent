import os
import sys
from agents.faq_agent import FAQAgent
from agents.qualification_agent import QualificationAgent
from agents.escalation_agent import EscalationAgent
from agents.summary_agent import SummaryAgent
from utils.memory import Memory
from utils.logger import Logger
from utils.prompts import WELCOME_MSG, GOODBYE_MSG
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

load_dotenv()
console = Console()

SOP_PATH = os.path.join(os.path.dirname(__file__), 'sop_data.json')
LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'conversation_log.txt')


def main():
    memory = Memory()
    logger = Logger(LOG_PATH)
    faq_agent = FAQAgent(SOP_PATH)
    qualification_agent = QualificationAgent(memory)
    escalation_agent = EscalationAgent()
    summary_agent = SummaryAgent(memory)

    console.print(WELCOME_MSG, style="bold green")
    logger.log(WELCOME_MSG)

    interaction_count = 0
    last_user_input = ""
    qualification_started = False

    while True:
        user_input = Prompt.ask("[bold blue]Customer[/bold blue]")
        if user_input.lower() in ["exit", "quit"]:
            break
        logger.log(f"Customer: {user_input}")
        last_user_input = user_input


        # FAQ Agent
        faq_result = faq_agent.answer(user_input)

        # Escalation Agent
        escalation = escalation_agent.check(user_input, faq_result)

        # If escalation triggered, print escalation message
        if escalation['escalate']:
            console.print(f"[bold magenta]AI:[/bold magenta] {escalation['message']}")
            logger.log(f"AI: {escalation['message']}")

            memory.escalation_reason = escalation['reason']

            # Better SOP gap handling
            if escalation['reason'] in [
                "Medical question",
                "Out of SOP scope"
            ]:
                memory.sop_gaps.append(user_input)

            # Ask qualification questions before escalating
            console.print("\n[bold yellow]Before connecting you, I'd like to gather a few details to help our team assist you better.[/bold yellow]", style="bold yellow")
            logger.log("Qualification stage started before escalation")
            qualification_agent.ask_questions(console, logger)

            console.print(f"[bold red]Escalation:[/bold red] {escalation['reason']}")
            logger.log(f"Escalation: {escalation['reason']}")

            break

        # Otherwise print normal FAQ response
        else:
            logger.log(f"AI: {faq_result['response']}")
            console.print(f"[bold magenta]AI:[/bold magenta] {faq_result['response']}")
            
        

        # Track successful customer interactions (non-escalation)
        interaction_count += 1

        # After 3 successful interactions, transition into Lead Qualification exactly once
        if interaction_count >= 3 and not qualification_started:
            qualification_started = True
            console.print("\nBefore we continue, I'd like to ask a few quick questions.", style="bold yellow")
            logger.log("Qualification stage started")
            qualification_agent.ask_questions(console, logger)
            break

    # Summary
    try:
        summary = summary_agent.generate(last_user_input)

        console.print("\n[bold yellow]Conversation Summary[/bold yellow]\n")
        console.print(summary)
        logger.log("\nConversation Summary\n" + summary)
    except Exception as e:
        logger.log(f"\nError generating summary: {str(e)}")
        console.print(f"[bold red]Error generating summary: {str(e)}[/bold red]")
    
    console.print(GOODBYE_MSG, style="bold green")
    logger.log(GOODBYE_MSG)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\nSession ended.", style="bold red")
    except Exception as e:
        console.print(f"\nError: {str(e)}", style="bold red")
        # Still try to log the error even if something goes wrong
        try:
            logger = Logger(LOG_PATH)
            logger.log(f"\nERROR: {str(e)}")
        except:
            pass
