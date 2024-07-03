import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from prompt import system_prompt


generation_config = {
    "max_output_tokens": 2048,
    "temperature": 1,
    "top_p": 1,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

vertexai.init(project="247572588539", location="us-central1")
model = GenerativeModel(model_name="projects/247572588539/locations/us-central1/endpoints/1034858145039515648", system_instruction=[system_prompt])

chat = model.start_chat()


def multiturn_generate_content(input_message):
    response = chat.send_message(content=input_message,generation_config=generation_config, safety_settings=safety_settings)
    return response.text        


# while True:
#     user = input("Enter message : ")
#     if user != "quit":
#         res = multiturn_generate_content(user)
#         print(res)
#     else:
#         break



