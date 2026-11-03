import os
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("rag-chatbot")


def retrieve_docs(question, k=5):
    query_vec = embeddings.embed_query(question)
    results = index.query(vector=query_vec, top_k=k, include_metadata=True)
    docs = []
    for match in results.matches:
        docs.append(match.metadata.get("text", ""))
    return docs


gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
    timeout=30,
)

groq_llm = ChatGroq(
    model="qwen/qwen3.8-27b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=500,
)

groq_backup_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=500,
)

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Use ONLY the context below to answer. "
    "Give a direct, clear answer. Do NOT say 'based on the context' or 'according to the provided text'. "
    "Just answer naturally as if you know the information.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}\n\n"
    "Answer:"
)

chain_tail = prompt | StrOutputParser()


def ask_llm(llm, context, question):
    messages = prompt.format_messages(context=context, question=question)
    response = llm.invoke(messages)
    return response.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question.strip():
        return jsonify({"error": "Please enter a question."}), 400

    preferred = data.get("model", "auto")

    docs = retrieve_docs(question)
    context = "\n\n".join(docs)

    answer = None
    used_model = None

    if preferred == "gemini":
        try:
            answer = ask_llm(gemini_llm, context, question)
            used_model = "Gemini 3.8 Flash"
        except Exception as e:
            return jsonify({"error": f"Gemini failed: {str(e)[:200]}"}), 500
    elif preferred == "groq":
        try:
            answer = ask_llm(groq_llm, context, question)
            used_model = "Groq (Qwen 27B)"
        except Exception:
            try:
                answer = ask_llm(groq_backup_llm, context, question)
                used_model = "Groq (GPT-OSS 20B)"
            except Exception as e:
                return jsonify({"error": f"Groq failed: {str(e)[:200]}"}), 500
    else:
        try:
            answer = ask_llm(gemini_llm, context, question)
            used_model = "Gemini 3.8 Flash"
        except Exception:
            pass
        if answer is None:
            try:
                answer = ask_llm(groq_llm, context, question)
                used_model = "Groq (Qwen 27B)"
            except Exception:
                pass
        if answer is None:
            try:
                answer = ask_llm(groq_backup_llm, context, question)
                used_model = "Groq (GPT-OSS 20B)"
            except Exception as e:
                return jsonify({"error": f"All APIs failed: {str(e)[:200]}"}), 500

    return jsonify({
        "answer": answer,
        "model": used_model
    })


if __name__ == "__main__":
    print("Starting RAG Chatbot on http://localhost:5000")
    print("Using Gemini 3.8 Flash (primary) + Groq Qwen 27B (fallback)")
    app.run(debug=False, port=5000)
