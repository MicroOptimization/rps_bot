"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import discord
import key_retriever
import asyncio

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        self.challenges = []
        
        self.text_channel_names = []
        self.text_channels = []
        
        for i in client.get_all_channels():
            self.text_channel_names.append(str(i))
            self.text_channels.append(i)
        
        users = client.users
        await client.change_presence(activity=discord.Game(name="with scissors"))
    
    async def on_message(self, message):
        print("-------------------------")
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")
        
        challenge_sent = len(words) >= 3 and words[0] == "rps" and words[1] == "challenge"
        
        if challenge_sent:
            
            self.challenged = client.get_user(int(words[2][3:-1]))
            self.challenger = message.author
            
            print("challenged: " , type(self.challenged))
            print("challenger: " , type(self.challenger))
            
            print("Challenge sent from " , self.challenger , "to" , self.challenged)
            print("field: " , self.challenged)
            await asyncio.sleep(0.5)
            
            
            await self.challenged.send("You've been challenged by: {}".format(self.challenger))
            await self.challenged.send("Send me your choice:")
            await self.challenged.send("Rock, paper, or scissors?")
            
            await message.author.send("You've challenged: {}".format(self.challenged))
            await message.author.send("Send me your choice:")
            await message.author.send("Rock, paper, or scissors?")
        

client = MyClient()

key = key_retriever.get_key() #Insert your key here

client.run(key)