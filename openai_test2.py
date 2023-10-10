import openai
import os

from openai_test import get_response

prompt = """
Man Utd must win trophies, says Ten Hag ahead of League Cup final

请将上面这句话的人名提取出来，并用json的方式展示出来
"""

print(get_response(prompt))