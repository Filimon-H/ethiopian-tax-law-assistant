# src/pipeline/test_llm_connection.py
from llm_chain import llm
response = llm.invoke("Who is required to pay VAT in Ethiopia?")
print(response.content)
