from langchain.chat_models import ChatOpenAI, ChatGooglePalm
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

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
