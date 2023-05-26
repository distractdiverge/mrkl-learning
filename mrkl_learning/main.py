from langchain import LLMMathChain, OpenAI, SerpAPIWrapper
from langchain.agents import Tool

from mrkl_learning.agents.planning_agent import PlanningAgent
from mrkl_learning.agents.zero_shot_agent import ZeroShotAgent


def build_llm():
    return OpenAI(model_name="gpt-4", temperature=0)

def build_tools(llm):
    search = SerpAPIWrapper()
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
    return tools

def main():
    
    llm = build_llm()
    tools = build_tools()    
    
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