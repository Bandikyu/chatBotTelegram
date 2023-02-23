from env import *
EMAIL = os.environ.get('EMAIL')
PASS = os.environ.get('PASS')
# from revChatGPT.V2 import Chatbot

# async def main():
#     chatbot = Chatbot(email=EMAIL, password=PASS)
#     async for line in chatbot.ask("Buenas buenas"):
#         print(line["choices"][0]["text"].replace("<|im_end|>", ""), end="", flush = True)
#     print()

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
#-------------------------
# from revChatGPT.V1 import Chatbot

# chatbot = Chatbot(config={
#   "email": EMAIL,
#   "password": PASS
# })

# print("Chatbot: ")
# prev_text = ""
# for data in chatbot.ask(
#     "Como estas?", 
#     gen_title= True,
# ):
#     message = data["message"][len(prev_text) :]
#     print(message, end="", flush=True)
#     prev_text = data["message"]
# print()


# --- otra forma


from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": EMAIL,
  "password": PASS
})

prompt = "capital de Uruguay?"
response = ""

for data in chatbot.ask(
  prompt, False,
):
    response = data["message"]
    responseID = data["conversation_id"]

print(chatbot)
print(response)