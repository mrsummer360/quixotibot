import discord
import random
import configparser

class MyClient(discord.Client):
    
    async def on_ready(self):
        # Starts bot and set Activity message
        print('Logged on as {0}'.format(self.user))
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!qd or !qd<diceSize>'))

        
    async def on_message(self,message):
        # Reads incoming messages and rolls lots of dice
        text = '{0.content}'.format(message)

        # print('Message from {0.author}: {0.content}'.format(message))

        # Check if command should be listened to
        # Currently checks for the role specified in Botconfig.ini, if Checkrole flag is set
        execqd = False
        if config['DiscordConfig']['CheckRole'] != 'yes':
            execqd = True
        else:
            rolename = config['DiscordConfig']['Quixotic_Role']
            role = discord.utils.get(message.guild.roles, name = rolename)
            user = message.author
            if role in user.roles:
                execqd = True            

        # Listener for !qd command
        if text.startswith('!qd') and execqd:            
            # Check for end of command
            cmdEnd = text.find(" ")
            cmd = '{0.content}'.format(message)[3:cmdEnd]

            # Set Default Die and get additional command details             
            useDie = int(config['Defaults']['defaultDie'])
            cmdarg = '{0.content}'.format(message)[cmdEnd+1:]

            # Execute rolling routines, see routine definition for further information
            if cmd == 'rnd':
                sendmessage = self.rollrandom(cmdarg)  
            elif cmd == 'rlm':
                sendmessage = self.rlmroll(cmdarg)              
            else:
                # Default roll, use one sort of dice, either specified by the command or the default die
                if cmd.isdigit(): useDie = int(cmd)
               
                respText = ''
                rollresult = 0
                numberOfDies = 0
                for c in cmdarg:
                    if c.isalpha():                    
                        if len(respText) > 0: 
                            respText += " + "
                        numberOfDies += 1
                        singleresult = random.randrange(1,useDie+1)
                        rollresult += singleresult
                        respText += str(singleresult)
                sendmessage = '_Rolled ' + str(numberOfDies) + 'd' + str(useDie) + ': ' + respText + " = " + str(rollresult) + '_'

            # Send message to the channel, the request was sent to
            await message.channel.send(sendmessage)

    def rollrandom(self, text):
        #Rolling routine to use a random die for each role        
        randomdice = [4,6,8,10,12,20]        # Add or remove values to add other dice-face values
        counts = [0,0,0,0,0,0]               # Dicecounters for the result text, length must be the same as randomdice above
        respText = ''
        numberOfDies = 0
        rollresult = 0
        for c in text:
            if c.isalpha():          
                useDie = random.choice(randomdice)          
                if len(respText) > 0: 
                    respText += " + "
                numberOfDies += 1
                singleresult = random.randrange(1,useDie+1)
                counts[randomdice.index(useDie)] += 1
                rollresult += singleresult
                respText += str(singleresult)


        result = ''
        result += result.join("{}d{}, ".format(x,y) for x, y in zip(counts,randomdice))
        result = '_Rolled ' + result[:-2] + ': ' + respText + ' = ' + str(rollresult) + '_'
        return result

    def rlmroll(self, text):
        # Special rolling routine for "Revenge of the Lettermasters" 
        # Each letter is assigned a dice-size value. Values can be edited using this dictionary
        letterdict = {
            "a":4,
            "b":12,
            "c":-8,
            "d":-6,
            "e":4,
            "f":10,
            "g":10,
            "h":6,
            "i":4,
            "j":-20,
            "k":12,
            "l":8,
            "m":8,
            "n":-4,
            "o":4,
            "p":10,
            "q":-20,
            "r":6,
            "s":-4,
            "t":-4,
            "u":-8,
            "v":-12,
            "w":-10,
            "x":20,
            "y":10,
            "z":20
        }

        respText = ''
        numberOfDies = 0
        rollresult = 0
        
        for c in text:
            if c.isalpha():                          
                useDie = letterdict[c.casefold()]          
                if len(respText) == 0 and useDie < 0:
                    respText = " - "
                elif len(respText) > 0 and useDie < 0: 
                    respText += " - "
                elif len(respText) > 0 and useDie > 0:
                    respText += " + "
                numberOfDies += 1
                if useDie > 0:
                    singleresult = random.randrange(1,useDie+1)
                    rollresult += singleresult
                else:  
                    singleresult = random.randrange(1,abs(useDie)+1)
                    rollresult -= singleresult
                respText += str(singleresult)

        respText = "_Roll Result: " + respText + " = " + str(rollresult) + "_"

        return respText





        
# Initialize Bot Client
client = MyClient()
config = configparser.ConfigParser()
# TODO Make configlocation call parameter
config.read('config\Botconfig.ini')
client.run(config['Security']['oauth2'])
