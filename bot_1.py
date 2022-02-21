import discord
import random
import configparser

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

        
    async def on_message(self,message):
        text = '{0.content}'.format(message)
        print('Message from {0.author}: {0.content}'.format(message))

        execqd = False
        if config['DiscordConfig']['CheckRole'] != 'yes':
            execqd = True
        else:
            rolename = config['DiscordConfig']['Quixotic_Role']
            role = discord.utils.get(message.guild.roles, name = rolename)
            user = message.author
            if role in user.roles:
                execqd = True            


        if text.startswith('!qd') and execqd:            
            cmdEnd = text.find(" ")
            cmd = '{0.content}'.format(message)[3:cmdEnd]
            useDie = int(config['Defaults']['defaultDie'])
            if cmd.isdigit(): useDie = int(cmd)
            cmdarg = '{0.content}'.format(message)[cmdEnd+1:]
            respText = ''
            rollresult = 0
            for c in cmdarg:
                if c.isalpha():                    
                    if len(respText) > 0: 
                        respText += " + "
                    singleresult = random.randrange(1,useDie+1)
                    rollresult += singleresult
                    respText += str(singleresult)
            await message.channel.send('Rolled: ' + respText + " = " + str(rollresult))

client = MyClient()
config = configparser.ConfigParser()
config.read('config\Botconfig.ini')
client.run(config['Security']['oauth2'])