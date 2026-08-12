from openai import OpenAI
from dotenv import load_dotenv
from app.services.search import search
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
query = input("Type in a query:")
retrieved_chunks = search(query)
context = " "
for i,chunk in enumerate(retrieved_chunks,start =1):
	context += f""" 
				Chunk{i}:{chunk}/n/n"""

llm_input  = f"""Context:
				{context},
				Query : 
				{query}
				You are answering questions about a document.

Use ONLY the information provided in the Context.

If the answer is not present, reply:
"I couldn't find that information in the document."

Be concise.
Use bullet points whenever appropriate.
Do not mention "the context" or "the document" unless the user explicitly asks.
				"""

response = client.responses.create(model = "gpt-4o-mini",input = llm_input)
print(response.output_text)

