from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

class ZeroShotAgent:
    def __init__(self, llm, tools, verbose = True):
        self._agent = initialize_agent(
            tools, 
            llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=verbose
        )
    
    def run(self, message:str):
        return self._agent.run(message)

    def save(self, path:str):
        return self._agent.save_agent(path)
