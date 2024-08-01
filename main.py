import json
import re
import requests
import os
import schedule
import threading
import asyncio
import time
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext, ChatJoinRequestHandler

chat_id = -1001410722926
chinese_pattern = re.compile(u'[\u4e00-\u9fff]+')

# Token del bot proporcionado por @BotFather
TOKEN = '7453182687:AAEN1zgb7hdzDCaNjGy4-u-teDAcXVrFUmY'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('您好！使用 /create_link 来生成一个邀请链接。\n使用 /my_link 查询人数\n\n温馨提示 人数每天凌晨12点清空/n12点前联系 @dilei87 结账')

async def create_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    
    if update.message.from_user.username:
        name = f'@{update.message.from_user.username}'
    elif update.message.from_user.last_name:
        name = f'{update.message.from_user.first_name} {update.message.from_user.last_name}'
    else:
        name = update.message.from_user.first_name
    
    with open('Users.txt', 'r') as file:
        users = json.load(file)
    
    if f'{update.message.from_user.id}' not in users:
        # Crear un enlace de invitación
        invite_link = await bot.create_chat_invite_link(chat_id, creates_join_request=True, name=f"{update.message.from_user.id}")
        link = invite_link.invite_link
        
        users[f'{update.message.from_user.id}'] = {}
        users[f'{update.message.from_user.id}']['name'] = name
        users[f'{update.message.from_user.id}']['link'] = link
        
        with open('Users.txt', 'w') as file:
            json.dump(users, file)
        
        # Enviar el enlace al usuario
        await update.message.reply_text(f'已创建邀请链接 {link}')
    else:
        link = users[f'{update.message.from_user.id}']['link']
    
    await update.message.reply_text(f'〖您的昵称〗{name}\n〖您的账号〗{update.message.from_user.id}\n〖邀请链接〗点击复制⬇️\n<code>{link}</code>', 'HTML')

async def my_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('Users Inviters.txt', 'r') as file:
        users_inviters = json.load(file)
    if f'{update.message.from_user.id}' in users_inviters:
        await update.message.reply_text(f'您已邀请{users_inviters[f'{update.message.from_user.id}']['amount']}人')
    else:
        await update.message.reply_text('您已邀请0人')

async def recount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    await update.message.reply_text(f'Recounting... Please wait')

    try:
        with open('Users Inviters.txt', 'r') as file:
            users_inviters = json.load(file)
    
        with open('IDS.txt', 'r') as file:
            IDS = json.load(file)
        
        IDScopy = IDS.copy()

        for ID in IDScopy:
            url = f"https://api.telegram.org/bot{TOKEN}/getChatMember"
            params = {
                'chat_id': chat_id,
                'user_id': ID
            }
            response = requests.get(url, params=params)
            data = response.json()
            print(f'{data}')
            if data['ok']:
                if data['result']['status'] == 'left':
                    print(f'{data['result']['user']['username']} NO es miembro\n\n')
                    users_inviters[f'{IDS[f'{ID}']}']['amount'] -= 1

                    del users_inviters[f'{IDS[f'{ID}']}']['users'][f'{ID}']
                    del IDS[f'{ID}']
            else:
                print(f'Problema con {ID}: {data['description']}\n\n')
        
        with open('Users Inviters.txt', 'w') as file:
            json.dump(users_inviters, file)
            
        with open('IDS.txt', 'w') as file:
            json.dump(IDS, file)

        await update.message.reply_text("Recount completed ✅")
        
    except Exception as e:
        await update.message.reply_text(f"An error occurred during the recount\n\nError: {e}")

async def handle_chat_join_request(update: Update, context: CallbackContext):
    # Obtener la solicitud de unión al chat
    chat_join_request = update.chat_join_request

    # Obtener información sobre el chat al que se le está solicitando unirse
    chat = chat_join_request.chat
    if chat.id == chat_id:
        # Obtener información sobre el usuario que envió la solicitud
        user = chat_join_request.from_user
        
        if user.last_name:
            name = f'{user.first_name} {user.last_name}'
        else:
            name = user.first_name
        
        # La expresión regular para detectar caracteres chinos
        match = chinese_pattern.search(name)
        
        if match:
            with open('IDS.txt', 'r') as file:
                IDS = json.load(file)
        
            if user.id not in IDS:
                IDS[f'{user.id}'] = chat_join_request.invite_link.name
                with open('IDS.txt', 'w') as file:
                    json.dump(IDS, file)
                        
                if f'{user.id}' != chat_join_request.invite_link.name:
                    with open('Users Inviters.txt', 'r') as file:
                        users_inviters = json.load(file)
                    
                    # Obtener información sobre el chat al que se le está solicitando unirse
                    if f'{chat_join_request.invite_link.name}' not in users_inviters:
                        with open('Users.txt', 'r') as file:
                            users = json.load(file)
                        users_inviters[f'{chat_join_request.invite_link.name}'] = {}
                        users_inviters[f'{chat_join_request.invite_link.name}']['name'] = users[f'{chat_join_request.invite_link.name}']['name']
                        users_inviters[f'{chat_join_request.invite_link.name}']['amount'] = 0
                        users_inviters[f'{chat_join_request.invite_link.name}']['users'] = {}

                    if user.username:
                        name = f'@{user.username}'
                    
                    users_inviters[f'{chat_join_request.invite_link.name}']['users'][f'{user.id}'] = name
                    users_inviters[f'{chat_join_request.invite_link.name}']['amount'] += 1

                    with open('Users Inviters.txt', 'w') as file:
                        json.dump(users_inviters, file)
                    
            await chat_join_request.approve()
        
        else:
            await chat_join_request.decline()
            await context.bot.send_message(chat_id = user.id, text = "您必須有中文名字才能加入我們的頻道")

def reset():
    print("Starting reset")

    # Abrir la lista del archivo IDS.txt
    with open('IDS.txt', 'r') as file:
        ids = json.load(file)

    # Abrir la lista del archivo Users Inviters.txt
    with open('Users Inviters.txt', 'r') as file:
        users_inviters = json.load(file)
    
    # Limpio la lista de IDS
    ids_new = {
        "28323": 5419769,
        "48322": 99999
    }

    # Limpio la lista de participantes
    users_inviters_new = {
        "231": {
            "name": "@psdaso",
            "amount": 2,
            "users": {
                "384572": "Naza",
                "834752": "Leo"
            }
        },
        "123": {
            "name": "@NazaCarp",
            "amount": 1,
            "users": {
                "3899129": "Saturnino"
            }
        }
    }

    # Reviso el nombre de carpeta disponible para un backup
    now = datetime.now()
    now = now.strftime("%m - %d")

    # Creo una carpeta con el nombre disponible
    os.makedirs(f'Backups/Backup {now}')
            
    # Respaldar la lista de IDs en un archivo .txt y resetearla
    with open(f'Backups/Backup {now}/IDS.txt', 'w') as file:
        json.dump(ids, file)

    with open(f'IDS.txt', 'w') as file:
        json.dump(ids_new, file)
        
    # Respaldar la lista de usuarios invitadores en un archivo .txt y resetearla
    with open(f'Backups/Backup {now}/Users Inviters.txt', 'w') as file:
        json.dump(users_inviters, file)

    with open(f'Users Inviters.txt', 'w') as file:
        json.dump(users_inviters_new, file)

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('create_link', create_link))
    application.add_handler(CommandHandler('my_link', my_link))
    application.add_handler(CommandHandler('recount', recount))

    # Agregar el manejador para las solicitudes de unión al chat
    chat_join_request_handler = ChatJoinRequestHandler(handle_chat_join_request)
    application.add_handler(chat_join_request_handler)

    # Ejecutar el método run_polling en un hilo separado
    threading.Thread(target=asyncio.run, args=(application.run_polling(),)).start()

    schedule.every().day.at("13:00").do(reset)

    while True:
        schedule.run_pending()
        time.sleep(55)

if __name__ == "__main__":
    main()