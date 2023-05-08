import os
import openai
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from streamlit_chat import message
from typing import List, TypedDict

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


class ContextType(TypedDict):
    role: str
    content: str


class Chatbot():
    def __init__(self) -> None:
        self.context: List[ContextType] = []

        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []

    def get_completion(self, prompt: str, model='gpt-3.5-turbo') -> str:
        messages = [{'role': 'user', 'content': prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message['content']

    def get_completion_from_messages(self, messages: List[str], model='gpt-3.5-turbo', temperature=0) -> str:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        # print(str(response.choices[0].message))
        return response.choices[0].message['content']

    def setup_streamlit_dashboard(self, title: str) -> None:
        """ Creating the chatbot interface """
        st.title(title)

    def get_user_input(self) -> str:
        input_text = st.text_input('You: ', 'Hello, how are you?', key='input')
        return input_text

    def set_chat_context(self) -> None:
        input_context = st.text_area(
            label='Enter context for the chat here in 1000 chars or less', max_chars=1000)
        current_context = {'role': 'system',
                           'content': f'{input_context}'}
        self.context.append(current_context)
        response = self.get_completion_from_messages([current_context])
        self.context.append(
            {'role': 'assistant', 'content': f'{response}'})


if __name__ == '__main__':

    chatbot = Chatbot()
    system_context = chatbot.set_chat_context()
    user_input = chatbot.get_user_input()

    if user_input:
        output = chatbot.get_completion(user_input)
        # store the output
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i],
                    is_user=True, key=str(i) + '_user')

