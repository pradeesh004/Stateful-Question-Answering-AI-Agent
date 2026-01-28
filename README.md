# Stateful-Question-Answering-AI-Agent
Stateful Question-Answering AI Agent

This project demonstrates how to build a stateful AI agent using Google ADK that can answer user questions based on stored session history and user context.

The agent remembers user information using an in-memory session service and responds intelligently using that context.

🚀 Features

Maintains user session state

Stores user profile and background information

Answers questions based on conversation history

Uses Google ADK Runner for agent execution

Powered by Gemini 2.5 Flash Lite model

🧠 How It Works

User details and background are stored in a session state.

An InMemorySessionService manages session data.

A unique session is created using:

App name

User ID

Session ID

The Runner executes the agent with access to session history.

The agent uses stored user context to answer questions meaningfully.

📂 Project Structure
project/
│
├── agent_1.py          # Agent definition
├── main.py             # Runner and session setup
├── .env                # Environment variables

📌 Code Overview
🔹 Session State Initialization
initial_state = {
    "user_name": "Pradeesh kumar",
    "user_content": """
    Pradeesh is good at acquiring technical and scientific knowledge.
    He loves science, math, computer science, AI, ML, and DL.
    He is also interested in dance, singing, and drawing.
    """
}

🔹 Session Creation
session_state_full = session_service_state.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

🔹 Agent Definition
root_agent = Agent(
    name="agent_1",
    model="gemini-2.5-flash-lite",
    description="Question-answering agent",
    instruction="""
    Answer the user's questions based on the provided user history.
    user_name: {user_name}
    user_content: {user_content}
    """
)

🔹 Runner Setup
runner = Runner(
    agent=agent,
    session_service=session_state_full,
    app_name=APP_NAME,
)

▶️ Usage

Define the user profile and background in initial_state

Start a session using InMemorySessionService

Run the agent using Runner

Ask questions — the agent responds using stored context

🛠 Requirements

Python 3.8+

Google ADK

python-dotenv

Valid Gemini model access

pip install python-dotenv

📌 Example Use Cases

Personalized question-answering systems

AI assistants with memory

Student or profile-based AI agents

Conversational AI with session awareness

📄 Notes

Session data is stored in memory (not persistent).

Suitable for demos, prototypes, and learning projects.

For production use, a persistent session store is recommended.

✨ Author

Built as a state-aware conversational AI agent using Google ADK.
