from telethon import events , TelegramClient
from asyncio import sleep as zzz
from random import randint
from re import match

#dont edit else gay this constant
api_id = 2282111
api_hash = 'da58a1841a16c352a2a999171bbabcad'
bot = TelegramClient('session' , api_id , api_hash)
chat = 572621020

#edit the list
list = ["Eternatus", "Zacian", "Shaymin", "Dialga", "Palkia", "Mewtwo", "Arceus", "Zamazenta", "Glastrier", "Kyurem", "Lunala", "Necrozma", "Shiny", "✨", "Rayquaza", "Cosmoem", "Yveltal", "Kyogre", "Xerneas", "Cosmog", "Groudon", "Giratina", "Zeraora", "Marshadow", "Buzzwole", "Solgaleo", "Zygarde", "Regigigas", "Mew", "Ho-oh", "Lugia", "Raikou", "Entei", "Celebi", "Deoxys", "Jirachi", "Darkrai", "Reshiram", "Zekrom", "Victini", "Hoopa", "Diancie", "Volcanion", "Pheromosa", "Magearna", "Regieleki", "Spectrier", "Mewtwo", "Beldum", "Darumaka", "Terrakion", "Kartana",  "Vigoroth", "Slakoth", "Treecko", "Mudkip"]
@bot.on(events.NewMessage(outgoing=True,pattern='.go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(2,3)
       await bot.send_message(chat , "/hunt")
    for i in range(1,10000):
      await zzz(randint(1000, 1020))
      await bot.send_message(chat , "/hunt")


@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
     if ("A shiny" in event.message.text):
        bot.disconnect()
     elif("TM" in event.message.text):
        print(event.message.text)
        await zzz(randint(2,3))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(2,3)
           await bot.send_message(chat , "/hunt")
     elif any(item in event.message.text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in event.text or "An expert" in event.message.text):
      if hun == False:
       pass
      else:
       await zzz(randint(2,5))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(2,3)
          await bot.send_message(chat , "/hunt")
      

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(2)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      


@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
      await zzz(2)
      await message.click(text = "Repeat")
      await message.click(text = "Repeat")
      await message.click(text = "Repeat")
   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(2,5))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(2,3)
         await bot.send_message(chat , "/hunt")



@bot.on(events.NewMessage(outgoing=True,pattern='.stop'))
async def stop(event):
    global hunt
    hunt = False


bot.start()
bot.run_until_disconnected()
