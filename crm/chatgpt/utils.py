import os
import openai
# openai.organization = "org-80oV8m7voYA4OmMwkXdfklqI"
# openai.api_key = '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'
# res=openai.Model.list()
# print(dir(openai.Model))



class ChatGpt:
    def __init__(self):
        self.organization="org-80oV8m7voYA4OmMwkXdfklqI"
        self.api_key='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'
        
        openai.organization = self.organization
        openai.api_key = self.api_key


    # def openAi(self):
                
    #     openai.organization = self.organization
    #     openai.api_key = self.api_key
    #     return openai





    def get_models():
        data=[]
        res=openai.Model.list()
        
        
        return res       
    
    def say_hello(self):
        print("Hello, my name is " + self.name)



