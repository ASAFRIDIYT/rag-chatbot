import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PDF_PATH = "./data/your_document.pdf"
INDEX_NAME = "rag-chatbot"

# Step 1: Load PDF
print("[1/5] Loading PDF...")
loader = PyPDFLoader(PDF_PATH)
pages = loader.load()
print(f"[1/5] Done! {len(pages)} pages loaded.")

# Step 2: Create chunks
print("[2/5] Creating chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(pages)
print(f"[2/5] Done! {len(chunks)} chunks created.")

# Step 3: Load embedding model
print("[3/5] Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print("[3/5] Done! Embedding model ready.")

# Step 4: Create Pinecone index if not exists
print("[4/5] Setting up Pinecone index...")
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

existing_indexes = [idx.name for idx in pc.list_indexes()]
if INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print(f"[4/5] Created new index '{INDEX_NAME}'.")
else:
    print(f"[4/5] Index '{INDEX_NAME}' already exists.")

# Step 5: Store in Pinecone
print("[5/5] Storing chunks in Pinecone...")
vectorstore = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name=INDEX_NAME,
)
print(f"[5/5] Done! {len(chunks)} chunks stored in Pinecone.")
print("Ingestion complete! Run app.py to start the chatbot.")
