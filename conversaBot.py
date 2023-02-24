from revChatGPT.V1 import Chatbot
import telebot
from env import *
from generateMD import saveMarkDown
TOKEN = os.environ.get('TOKEN')
EMAIL = os.environ.get('EMAIL')
PASS = os.environ.get('PASS')

chatbot = ""
while True:
    print("iniciando codigo")
    try:
        def generateResponse(prompt):
            response = ""
            try:
                for data in chatbot.ask(
                prompt,
                ):
                    response = data["message"]
            except Exception as e:
                print(f"error al procesar el mensaje {e}")
                response = "error al procesar el mensaje"
            return response
                #return response = data["message"]
                #responseID = data["conversation_id"]

        bot = telebot.TeleBot(TOKEN)

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(message, "Aca va el id del mensaje y el unico texto del mensaje va a ser el id del chat de chatGPT")

        @bot.message_handler(commands=['clean'])
        def send_buenas(message):
            chatbot.clear_conversations()
            bot.reply_to(message, "Creo que se limpio")

        @bot.message_handler(func=lambda message: True, content_types=['text']) # all content_types > ['audio', 'photo', 'voice', 'video', 'document','text', 'location', 'contact', 'sticker']
        def default_command(message):
            global chatbot
            request = message.text
            print(message.chat.first_name)
            print(message.chat.id)
            print(request)
            response = ""
            if chatbot == "":
                bot.send_message(message.chat.id, "Iniciando bot...")
                try:
                    chatbot = Chatbot(config={
                    "email": EMAIL,
                    "password": PASS
                    })
                    print("Bot iniciado")
                    bot.send_message(message.chat.id, "pensando respuesta...")
                    response = generateResponse(request)
                except Exception as e:
                    print(dir(e))
                    print(e.args)
                    print("status code:" , e.status_code)
                    print("getAttribute" , e.__getattribute__)
                    print("detalles" , e.details)

                    print("Error de autenticación")
                    response = "Error de autenticación"
            else:
                bot.send_message(message.chat.id, "pensando respuesta...")
                response = generateResponse(request)
            print(response)
            """ Podria mejorarlo usando el decorador del modulo generateMD """
            saveMarkDown(f"{message.chat.first_name}-{message.chat.id}.md", f"{message.chat.first_name}: {request} \n\nBot: {response}\n___\n" , "a")
            bot.send_message(message.chat.id, response)

        bot.polling()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        print("Reiniciando programa...")
        continue