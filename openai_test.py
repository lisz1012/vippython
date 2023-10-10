import openai
import os

openai.api_key = "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"
COMPLETION_MODEL = "text-davinci-003"

prompt = """
Consideration proudct : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readable product title used on Amazon in english within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a suggested price range for this product in U.S.
4. Provide the competitor product name, url and price for 3 candidates in Amazon

Output the result in json format with three properties called title, selling_points and price_range
"""

def get_response(prompt):
    completions = openai.Completion.create (
        engine=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt))