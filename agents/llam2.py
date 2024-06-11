from langchain_community.llms import Ollama
llm=Ollama(model="llama2")
op=llm.invoke("Tell me About Machince Learning")
print(op)