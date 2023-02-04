from django.shortcuts import render
from openai import Model
# Create your views here.
from crm.chatgpt.utils import ChatGpt

from django.http import HttpResponse
from django.views import View

class GptView(View):

    def get(self, request, *args, **kwargs):
        locals=ChatGpt.get_models()
        content={
            'data': locals
        }

        return render(request, 'gpt/gpt.html',content)