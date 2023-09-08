import openai
import json
from types import SimpleNamespace

class GptConnect():

    def __init__(self):

        openai.api_key = "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"

    def response(self, user_input):
        models = {
            'text': {
                'best': 'text-davinci-003',
                'better': 'text-curie-001',
                'good': 'text-babbage-001',
                'base': 'text-ada-001'
            },
            'code': {
                'best': 'code-davinci-002',
                'base': 'code-cushman-001'
            }
        }
        models = json.loads(json.dumps(models), object_hook=lambda item: SimpleNamespace(**item))

        response = openai.Completion.create(
            model=models.text.best,
            prompt=user_input,
            temperature=1,  # if top_p is not 1.0, this should be 1.0
            max_tokens=100,
            top_p=1.0,  # if temperature is not 0, this should be 1.0
            frequency_penalty=0.2,
            presence_penalty=0.0,
            suffix=None,
            n=1,
            stop=None
        )
        return response



if __name__ == '__main__':

    chat = GptConnect()
    response = chat.response("where does magic mushrooms grow in kodaikanal.")
    print(response['choices'][0]['text'])


