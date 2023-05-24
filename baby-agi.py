from typing import Optional

from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.base import VectorStore
from langchain.experimental import BabyAGI

from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore

from langchain.tools import ShellTool

# Define your embedding model
embeddings_model = OpenAIEmbeddings()

# Initialize the vectorstore as empty
import faiss

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import OpenAI, SerpAPIWrapper, LLMChain

todo_prompt = PromptTemplate.from_template(
    "You are a planner who is an expert at coming up with a todo list for a given objective. Come up with a todo list for this objective: {objective}"
)
todo_chain = LLMChain(llm=OpenAI(temperature=0), prompt=todo_prompt)

analyze_prompt = PromptTemplate.from_template(
    "You are a multi-disciplinary scientist. You have extensive background in human biology, and chemistry. Review the following information and produce an analysis of the claim.: {information}"
)
analyze_chain = LLMChain(llm=OpenAI(temperature=0), prompt=analyze_prompt)

search = SerpAPIWrapper()

tools = [
    ShellTool(),
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Analyze",
        func=analyze_chain.run,
        description="useful for when you need to analyze a large amount of information",
    ),
    Tool(
        name="TODO",
        func=todo_chain.run,
        description="useful for when you need to come up with todo lists. Input: an objective to create a todo list for. Output: a todo list for that objective. Please be very clear what the objective is!",
    ),
]


prefix = """You are an AI who performs one task based on the following objective: {objective}. Take into account these previously completed tasks: {context}."""
suffix = """Question: {task}
{agent_scratchpad}"""
prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["objective", "task", "context", "agent_scratchpad"],
)

llm = OpenAI(temperature=0)
llm_chain = LLMChain(llm=llm, prompt=prompt)
tool_names = [tool.name for tool in tools]
agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)


OBJECTIVE = "Find summer camps or day programs for a 12 year old boy in acting, improv or theater and voice-over. The camp must be within 20 minutes of Warrington, PA."
# Logging of LLMChains
verbose = False
# If None, will keep on going forever
max_iterations: Optional[int] = 20
baby_agi = BabyAGI.from_llm(
    llm=llm, vectorstore=vectorstore, task_execution_chain=agent_executor, verbose=verbose, max_iterations=max_iterations
)
baby_agi({"objective": OBJECTIVE})