import streamlit as st
from streamlit_chat import message
from chatbot import Chatbot

class Dashboard():
    def __init__(self) -> None:
        self.chat_context = ""
        self.dashboard_title = 'Chatbot POC'
        st.title(self.dashboard_title)

        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []

        if 'user_input' not in st.session_state:
            st.session_state['user_input'] = ''

    def submit_user_input_handler(self) -> None:
        st.session_state['user_input'] = st.session_state['input_widget']
        st.session_state['input_widget'] = ''
        st.session_state.past.append(st.session_state['user_input'])
    
    def get_user_input(self) -> str | None:
        input_text = st.text_input('You: ', key='input_widget', on_change=self.submit_user_input_handler)
        print(f"input_text: {st.session_state['user_input']}")
        return st.session_state['user_input']
    
    def get_chat_context_input(self) -> None:
        with st.form(key="form_chat_context"):
            input_context = st.text_area(
                label='Enter context for the chat here in 1000 chars or less', max_chars=1000)
            st.form_submit_button(on_click=self.set_chat_context, args=(input_context,))

    def set_chat_context(self, input_context: str) -> None:
        self.chat_context = input_context

    def get_chat_context(self) -> str:
        return self.chat_context

    def set_generated_message_state(self, generated_text: str) -> None:
        st.session_state.generated.append(generated_text)

    def create_chat_component(self) -> None:
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i],
                        is_user=True, key=str(i) + '_user')