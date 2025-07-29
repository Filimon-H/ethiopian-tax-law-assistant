import streamlit as st
import httpx

st.set_page_config(page_title="Ethiopian Tax Assistant", page_icon="🇪🇹", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>🤖 Ethiopian Tax Law Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Ask any question related to Ethiopian tax law and get reliable answers based on legal documents.</p>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("📚 Instructions")
    st.markdown("""
    - Type your tax-related question below
    - Click "Ask"
    - The assistant will answer and cite sources
    """)

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = "user" if msg["is_user"] else "assistant"
    with st.chat_message(role):
        st.markdown(msg["text"])

# Input box
query = st.chat_input("Ask about VAT, Turnover Tax, or Income Tax...")

if query:
    st.session_state.messages.append({"is_user": True, "text": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = httpx.post(
                    #"http://localhost:8000/ask", 
                     "http://fastapi:8000/ask",
                     # FastAPI must be running
                    json={"query": query},
                    timeout=30.0
                )
                result = response.json()
                answer = result["answer"]
                sources = result.get("sources", [])
                source_display = "\n".join(f"- {src}" for src in sources)
                full_response = f"{answer}\n\n📚 **Sources:**\n{source_display}"
            except Exception as e:
                full_response = f"❌ Error: {e}"

        st.markdown(full_response)
        st.session_state.messages.append({"is_user": False, "text": full_response})
