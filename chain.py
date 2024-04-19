import json
import os

from langchain_together import Together

llm = Together(
    model="meta-llama/Llama-2-70b-chat-hf",
    temperature=0,
    max_tokens=128,
    top_k=1,
    together_api_key=os.environ["TOGETHER_API_KEY"],
)

input_ = """You are a teacher with a deep knowledge of machine learning and AI. \
You provide succinct and accurate answers. Answer the following question: 

What is a large language model?


Output Instructions:
 Output should be in json string 
 it should not contain any other information except
 following keys
 answer -> answer of the question
 
 For example:
 {"answer" : "answer to the question"}
"""

print(llm.invoke(input_))
