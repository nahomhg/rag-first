from rag_pipeline import build_rag_chain
from vector import get_retriever

def interactive_rag():
    retriever = get_retriever()
    chain = build_rag_chain()

    print("\n--- RAG QA System: Pizza Reviews ---\n")

    while True:
        question = input("Ask a question (q to quit): ").strip()
        if question.lower() == "q":
            print("Exiting. Goodbye!")
            break

        documents = retriever.invoke(question)
        response = chain.invoke({
            "reviews": documents,
            "question": question
        })

        print("\nResponse:\n", response)
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    interactive_rag()
