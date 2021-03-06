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
        
        self.challenge_sent = False
        
        for i in client.get_all_channels():
            self.text_channel_names.append(str(i))
            self.text_channels.append(i)
        
        users = client.users
        await client.change_presence(activity=discord.Game(name="with scissors"))
        
        self.challenger_choice = ""
        self.challenged_choice = ""
        
    async def on_message(self, message):
        print("-------------------------")
        print('Message from {0.author} from {0.channel}: {0.content}'.format(message))
        text = message.content
        words = text.split(" ")
        
        
        if self.challenge_sent == False:
            self.challenge_sent = len(words) >= 3 and words[0] == "rps" and words[1] == "challenge"
        
        print(len(words) >= 3)
        
        print(words[0] == "rps")
        print(words[1] == "challenge")
        print()
        
        if self.challenge_sent:
            self.challenged = client.get_user(int(words[2][3:-1]))
            self.challenger = message.author
            
        
        print(message.author == self.challenger)
        print(str(message.author == str(self.challenger)))
        print(self.challenge_sent)
        
        """
        if self.challenge_sent and message.author == self.challenger:
            print("Challenger has messaged Me ---------------------------")
        else:
            print("Challenger has not messaged me")
        
        if self.challenge_sent and message.author == self.challenged:
            print("Challenged has messaged Me ---------------------------")
        else:
            print("Challenged has not messaged me")
        """
        
        print(message.author)
        print(self.challenger)
        print()
        print(str(message.author))
        print(str(self.challenger))
        
        if message.author == self.challenger:
            print("challenger sent")
            if len(words) > 2 and words[0].lower() == "choice:": 
                self.challenger_choice = words[1]
                self.challenger_chosen = True
        elif message.author == self.challenger:
            print("challenged sent")
            if len(words) > 2 and words[0].lower() == "choice:": 
                self.challenged_choice = words[1]
                self.challenged_chosen = True    
        
        if self.challenged_chosen and self.challenger_chosen:
            rps.resolve(self.challenger_choice, self.challenged_choice)
           
           
        if self.challenge_sent:
            
            self.challenged = client.get_user(int(words[2][3:-1]))
            self.challenger = message.author
            
            print("challenged: " , type(self.challenged))
            print("challenger: " , type(self.challenger))
            
            print("Challenge sent from " , self.challenger , "to" , self.challenged)
            print("field: " , self.challenged)
            
            await asyncio.sleep(0.5)
            
            await message.channel.send("'{} just challenged {} to a game of Rock Paper Scissors'".format(self.challenger, self.challenged))
         
            await self.challenged.send("You've been challenged by: {}".format(self.challenger))
            await self.challenged.send("Send me your choice:")
            await self.challenged.send("Rock, paper, or scissors?")
            
            await message.author.send("You've challenged: {}".format(self.challenged))
            await message.author.send("Send me your choice:")
            await message.author.send("Rock, paper, or scissors?")
            
            
            
        
client = MyClient()

key = key_retriever.get_key() #Insert your key retriever here

client.run(key)