from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
)

agent.print_response("")

