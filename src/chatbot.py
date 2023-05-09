from openai import ChatCompletion
from typing import List, TypedDict
import streamlit as st

class ContextType(TypedDict):
    role: str
    content: str
        
class Chatbot():
    def __init__(self) -> None:
        print(f'{__name__} called')
        self.context: List[ContextType] = []

    def get_completion(self, prompt: str, model='gpt-3.5-turbo') -> str:
        print(f'{self.get_completion.__name__} called')
        messages = [{'role': 'user', 'content': prompt}]
        # response = ChatCompletion.create(
        #     model=model,
        #     messages=messages,
        #     temperature=0,  # this is the degree of randomness of the model's output
        # )
        # return response.choices[0].message['content']
        return f'*sample ChatGPT response*'

    def get_completion_from_messages(self, messages: List[str], model='gpt-3.5-turbo', temperature=0) -> str:
        print(f'{self.get_completion_from_messages.__name__} called')
        # response = ChatCompletion.create(
        #     model=model,
        #     messages=messages,
        #     temperature=temperature,  # this is the degree of randomness of the model's output
        # )
        # # print(str(response.choices[0].message))
        # return response.choices[0].message['content']
        return f'*sample ChatGPT response*'
    
    def set_context(self, input_context: str) -> None:
        print(f'{self.set_context.__name__} called')
        current_context = {'role': 'system',
                            'content': f'{input_context}'}
        self.context.append(current_context)
        response = self.get_completion_from_messages([current_context])
        self.context.append(
            {'role': 'assistant', 'content': f'{response}'})