## This is example code 

import os

from pprint import pp
from typing import List

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_together import Together


# model = Together(
#     model="codellama/CodeLlama-70b-Instruct-hf",
#     temperature=0,
#     max_tokens=128,
#     top_k=1,
#     together_api_key=os.environ["TOGETHER_API_KEY"],
# )

model = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo-0125",
    api_key=os.environ["OPENAI_API_KEY"],
    verbose=True,
)


# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")


# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me a joke."

# Set up a parser + inject instructions into the prompt template.
parser = JsonOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"query": joke_query})

pp(result)
