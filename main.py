from langchain.chat_models import ChatOpenAI, ChatGooglePalm
from langchain import LLMMathChain, OpenAI, SerpAPIWrapper
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType


class PlanningAgent:
    def __init__(self, tools, verbose = True):
        self._model = ChatOpenAI(temperature=0)
        self._planner = load_chat_planner(self._model)
        self._executor = load_agent_executor(self._model, tools, verbose=verbose)
        self._agent = PlanAndExecute(planner=self._planner, executor=self._executor, verbose=verbose)

    def run(self, message:str):
        return self._agent.run(message)
    
    def save(self, path:str):
        return self._agent.save_agent(path)

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


def main():
    search = SerpAPIWrapper()
    llm = OpenAI(model_name="gpt-4", temperature=0)
    llm_math_chain = LLMMathChain.from_llm(llm)
    
    tools = [
            Tool(
                name = "Search",
                func=search.run,
                description="useful for when you need to answer questions about current events. You should ask targeted questions"
            ),
            Tool(
                name="Calculator",
                func=llm_math_chain.run,
                description="useful for when you need to answer questions about math"
            ),
        ]
    
    agent = ZeroShotAgent(llm, tools, verbose=True)
    prompt = "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
    print("Prompt: ", prompt)
    agent.run(prompt)
    agent.save("agents/zero-shot-agent.json")

    planning_agent = PlanningAgent(tools, verbose=True)
    prompt = "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"
    print("Prompt: ", prompt)
    planning_agent.run(prompt)
    agent.save("agents/planning-agent.json")



if __name__ == "__main__":
    main()