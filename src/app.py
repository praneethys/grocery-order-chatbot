from openai import api_key
from dotenv import load_dotenv, find_dotenv
from os import getenv

from chatbot import Chatbot
from dashboard import Dashboard

_ = load_dotenv(find_dotenv())  # read local .env file
api_key = getenv('OPENAI_API_KEY')

if __name__ == '__main__':
    print('-----------------------------------------')
    chatbot = Chatbot()
    dashboard = Dashboard() 
    
    # print(f'get chat context input from user')
    # dashboard.get_chat_context_input()

    # chat_context = dashboard.get_chat_context()
    # chatbot.set_context(chat_context)
    
    user_input = dashboard.get_user_input()
    if user_input:
        output = chatbot.get_completion(user_input)
        dashboard.set_generated_message_state(output)
    
    dashboard.create_chat_component()