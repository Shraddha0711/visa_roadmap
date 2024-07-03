import chainlit as cl
from model import multiturn_generate_content

@cl.on_message
async def main(message: cl.Message):

    # output = ""
    # response = multiturn_generate_content(message.content)
    # for i in response:
    #     print(i.text)
    #     j = str(i.text)
    #     output += j
    # async for part in list(output):
    #     if token := part.choices[0].delta.content.strip():
    #         await cl.Message(content="").stream_token(token)



    # print(message)
    response = multiturn_generate_content(message.content)
    await cl.Message(content=response).send()
