from crewai import Agent

blog_researcher = Agent(
    role="Blog researcher from youtube",
    goal = 'get the relevant video content from the topic{topic} from the yt channel',
    verbose=False,
    memory=True,
    backstory=('Expert in understanding the AI DS & Machine learning'),
    tools=[],
    allow_delegation=True
)

blog_researcher = Agent(
    role="Blog researcher from youtube",
    goal = 'get the relevant video content from the topic{topic} from the yt channel',
    verbose=False,
    memory=True,
    backstory=('Expert in understanding the AI DS & Machine learning'),
    tools=[],
    allow_delegation=True
)


