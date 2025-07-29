from retrieval_qa import qa_chain
if __name__ == "__main__":
    #question = "who has the Power to Issue Regulations Ethiopia?"
    question="ethiopia allows any commodity to be traded freely, this is not true for two categories of goods what are they?"
    result = qa_chain.invoke({"query": question})

    print("\nAnswer:\n", result["result"])
    print("\nSources:\n", [doc.metadata["source"] for doc in result["source_documents"]])
