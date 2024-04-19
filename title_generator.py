from pprint import pp
from typing import List

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_together import Together


class Report(BaseModel):
    title: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")
