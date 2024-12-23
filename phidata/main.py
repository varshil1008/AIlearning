from dotenv import load_dotenv
from phi.agent import Agent, RunResponse
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app


#this is to get and load the env variable for the Groq Key
load_dotenv()

web_agent = Agent(
    name = 'Finance Agent',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode = True

)

web_agent.print_response('''
                        Summarize the price and show the analyst recommendations and top 5 latest news 
                         for AI companies in India Stock market , feel free to proceed with the additional function calls 
                         and provide me with the details''')

