# Quixotibot

## General Information
Discord bot to react with rolled results using the [Quixotic SRD](https://wuderpg.itch.io/quixotic) by [wuderpg](https://wuderpg.itch.io/)

Built with Python 3.10.2, requires discord.py library (See [documentation](https://discordpy.readthedocs.io/en/stable/))

Use the code at your own risk

## How to install
Use the [Discord Developer Portal](https://discord.com/developers/applications) to add a new application, generate a OAuth2 Token, enter the OAuth2 token in the config/Botconfig.ini and use the generated bot-URL to invite the bot to your server. 
The Application currently needs to be able to read and send messages

## Features
Once the bot has been invited to your Discord Server you can use the following commands to trigger a response containing your detailed roll (because lets be honest, while it's not as great to here the dice go clickety-clack at least you can see your huge number of dice rolls) and the sum of all rolls. The bot includes configuration of a role, that is allowed to use the commands, check for this roll can also be disabled. 

Use !qd followed by your action to roll the preconfigured default die with the Quixotic SRD ruleset. 

`!qd I try to convince the guard, that I am not worth searching, describing in detail, how I am the heir to a rich king and he absolutely has to let me into the throne room right now.`

Result: 

`Rolled: 4 + 1 + 3 + 2 + 4 + 3 + 4 + 5 + 6 + 4 + 6 + 5 + 6 + 3 + 3 + 2 + 2 + 1 + 1 + 5 + 2 + 2 + 3 + 4 + 6 + 6 + 1 + 6 + 2 + 2 + 4 + 6 + 1 + 5 + 3 + 5 + 1 + 3 + 3 + 2 + 5 + 1 + 1 + 2 + 5 + 4 + 1 + 3 + 5 + 1 + 4 + 2 + 3 + 1 + 4 + 3 + 3 + 3 + 5 + 1 + 1 + 4 + 1 + 6 + 1 + 4 + 2 + 1 + 4 + 3 + 6 + 5 + 2 + 6 + 2 + 2 + 1 + 4 + 5 + 3 + 3 + 5 + 4 + 1 + 5 + 1 + 1 + 4 + 6 + 2 + 4 + 4 + 6 + 6 + 1 + 4 + 2 + 4 + 1 + 2 + 1 + 2 + 5 + 1 + 2 + 2 + 1 + 5 + 6 + 2 + 4 + 6 + 2 + 4 + 5 + 6 + 4 + 5 + 4 + 4 + 5 + 6 + 6 + 6 + 1 + 6 + 4 + 5 + 4 + 3 + 1 + 3 + 1 + 2 + 2 + 3 + 2 + 3 = 457`

Use !qdx (with x being a number) to roll a specific die 

`!qd20 I run down the hallway, firing both of my blasters at the drones, making my way towards the closing hatch.`

Result: 

`Rolled: 1 + 4 + 10 + 5 + 6 + 3 + 20 + 17 + 12 + 20 + 10 + 16 + 16 + 19 + 15 + 10 + 10 + 19 + 20 + 8 + 16 + 4 + 10 + 16 + 2 + 5 + 16 + 14 + 20 + 14 + 19 + 2 + 11 + 5 + 7 + 16 + 5 + 9 + 6 + 7 + 13 + 14 + 11 + 17 + 16 + 13 + 20 + 1 + 1 + 3 + 7 + 13 + 9 + 3 + 2 + 4 + 20 + 15 + 2 + 6 + 6 + 18 + 2 + 7 + 5 + 6 + 5 + 11 + 19 + 17 + 14 + 17 + 11 + 4 + 17 + 17 + 13 + 1 + 7 + 6 + 7 + 18 + 12 + 13 = 888`
