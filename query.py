"""
PHASE 2: QUERY TIME
User sawal poochhe -> ChromaDB se search -> Gemini se jawab

Usage: python query.py
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

load_dotenv()

# ============================================
# STEP 1: Embedding model load karo (same as ingest)
# ============================================
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# ============================================
# STEP 2: ChromaDB se connect karo
# ============================================
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

# ============================================
# STEP 3: Gemini LLM connect karo (FREE)
# ============================================
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# ============================================
# STEP 4: RAG Chain banao
# ============================================
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

# ============================================
# STEP 5: Chat loop
# ============================================
print("🤖 RAG Chatbot Ready!")
print("Type 'quit' to exit.\n")

while True:
    question = input("👤 Tumhara sawal: ")

    if question.lower() in ["quit", "exit", "q"]:
        print("Bye! 👋")
        break

    result = qa_chain.invoke({"query": question})

    print(f"\n🤖 Jawab: {result['result']}")
    print(f"\n📄 Sources: {len(result['source_documents'])} chunks se jawab aaya")
    print("-" * 50)
