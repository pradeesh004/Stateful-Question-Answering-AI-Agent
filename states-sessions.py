import uuid

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv
from agent_1 import agent
load_dotenv()

session_service_state = InMemorySessionService()

initial_State = {
    "user_name":"Pradeesh kumar",
    "user_content":"""
    Pradeesh good at aquire more knowledge in technical and science.
    Pradeesh loves science,math,computer science,ai,ml,dl subjects.
    Pradeesh kumar also intrested in dance,singing and drawing too.
    Pradeesh always wish to be a good person and he recognized as a good person by everyone who knows him.
    
    """
}

APP_NAME = "fifth-agent"
USER_ID = "Pradeesh Kumar"
SESSION_ID = str(uuid.uuid4())
session_state_full = session_service_state.create_session(
    app_name = APP_NAME,
    user_id = USER_ID,
    session_id= SESSION_ID,
    state = initial_state,
)

runner = Runner(
    agent = agent,
    session_service = session_state_full,
    app_name = APP_NAME,
)
