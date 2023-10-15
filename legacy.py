import discord
from discord import message
import time
import random
import os

TOKEN = 'Nzc5MDAyNDA4MTAxNDc4NDAw.Gi8Vzx.5XCLixJB4dP3B-ZynLhfOChvfI-dCP8SokDM2c'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
    async def on_ready(self):
        await discord.TextChannel.message.send('logged')

        if message.content == 'ping':
            await message.channel.send('pong')

        mateusz1 = [
            "Rodowód Jezusa Chrystusa, syna Dawida, syna Abrahama."
            , "Abraham był ojcem Izaaka; Izaak ojcem Jakuba; Jakub ojcem Judy i jego braci;"
            , "Juda zaś był ojcem Faresa i Zary, których matką była Tamar. Fares był ojcem Ezrona; Ezron ojcem Arama;"
            , "Aram ojcem Aminadaba; Aminadab ojcem Naassona; Naasson ojcem Salmona;"
            , "Salmon ojcem Booza, a matką była Rachab. Booz był ojcem Obeda, a matką była Rut. Obed był ojcem Jessego,"
            , "a Jesse ojcem króla Dawida. Dawid był ojcem Salomona, a matką była [dawna] żona Uriasza."
            , "Salomon był ojcem Roboama; Roboam ojcem Abiasza; Abiasz ojcem Asy;"
            , "Asa ojcem Jozafata; Jozafat ojcem Jorama; Joram ojcem Ozjasza;"
            , "Ozjasz ojcem Joatama; Joatam ojcem Achaza; Achaz ojcem Ezechiasza;"
            , "Ezechiasz ojcem Manassesa; Manasses ojcem Amosa; Amos ojcem Jozjasza;"
            , "Jozjasz ojcem Jechoniasza i jego braci w czasie przesiedlenia babilońskiego."
            , "Po przesiedleniu babilońskim Jechoniasz był ojcem Salatiela; Salatiel ojcem Zorobabela;"
            , "Zorobabel ojcem Abiuda; Abiud ojcem Eliakima; Eliakim ojcem Azora;"
            , "Azor ojcem Sadoka; Sadok ojcem Achima; Achim ojcem Eliuda;"
            , " Eliud ojcem Eleazara; Eleazar ojcem Mattana; Mattan ojcem Jakuba;"
            , "Jakub ojcem Józefa, męża Maryi, z której narodził się Jezus, zwany Chrystusem."
            ,
            "Tak więc w całości od Abrahama do Dawida jest czternaście pokoleń; od Dawida do przesiedlenia babilońskiego czternaście pokoleń; od przesiedlenia babilońskiego do Chrystusa czternaście pokoleń."
        ]

        mateusz2 = [
            "Z narodzeniem Jezusa Chrystusa było tak. Po zaślubinach Matki Jego, Maryi, z Józefem, wpierw nim zamieszkali razem, znalazła się brzemienną za sprawą Ducha Świętego."
            ,
            "Mąż Jej, Józef, który był człowiekiem sprawiedliwym i nie chciał narazić Jej na zniesławienie, zamierzał oddalić Ją potajemnie."
            ,
            "Gdy powziął tę myśl, oto anioł Pański ukazał mu się we śnie i rzekł: «Józefie, synu Dawida, nie bój się wziąć do siebie Maryi, twej Małżonki; albowiem z Ducha Świętego jest to, co się w Niej poczęło."
            , "Porodzi Syna, któremu nadasz imię Jezus, On bowiem zbawi swój lud od jego grzechów»."
            , "A stało się to wszystko, aby się wypełniło słowo Pańskie powiedziane przez Proroka:"
            , "Oto Dziewica pocznie i porodzi Syna, któremu nadadzą imię Emmanuel, to znaczy: Bóg z nami."
            , "Zbudziwszy się ze snu, Józef uczynił tak, jak mu polecił anioł Pański: wziął swoją Małżonkę do siebie,"
            , "lecz nie zbliżał się do Niej, aż porodziła Syna, któremu nadał imię Jezus..."
        ]

        if message.content == 'amen':
            await message.channel.send('Amen')

        if message.content == 'Amen':
            await message.channel.send('Amen')

        if message.content == 'rip':
            await message.channel.send('Na wieki wieków...')
        if message.content == 'Rip':
            await message.channel.send('Na wieki wieków...')
        if message.content == 'durak':
            await message.channel.send('durak')

        if message.content == 'bot':
            await message.channel.send(file=discord.File('pies.jpg'))
        if message.content == 'bot co wyslal':
            await message.channel.send(file=discord.File('bot.jpg'))
        if message.content == 'chlop co wyslal':
            await message.channel.send(file=discord.File('chlop.jpg'))


        ruski1 = [ "ты охрыниел?", " похшанило чие?", "замкий руй педале-закрой свой рот пидорас", " пиердол сие суко в пыск йебана -иди на хуй сука ёбана в рот",
                   "ыбчией курво бо сие зайебие-быстрее шлюха или я тебя убийу", "Дурак", "Шельма??", "Болван!", "Идиот", "тупая башка", "Уже два года как мы расстались, а ты сука до сих пор празднуешь!?!",
                   "етить твою мать!!", "соси мой хуй"
        ]
        if message.content == '!':
            x = random.randrange(len(ruski1))
            await message.channel.send(ruski1[x])


        if message.content == 'mateusz1':
            i = 0
            for i in range(len(mateusz1)):
                await message.channel.send(mateusz1[i])
                time.sleep(1)
                print(i)
                i = i + 1

        if message.content == 'mateusz2':
            i = 0
            for i in range(len(mateusz2)):
                await message.channel.send(mateusz2[i])
                time.sleep(1)
                print(i)
                i = i + 1

                x = 0


client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)
# client.run('Nzc5MDAyNDA4MTAxNDc4NDAw.X7aMhw.j2yMiAsmOzuCnmr-ss9GCFNqyfw')