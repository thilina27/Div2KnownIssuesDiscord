# Division 2 Known Issues Discord Bot

Simple Discord bot to get informations from [Division 2 knows issues](https://trello.com/b/F2RU9ia9/the-division-2-known-issues]) and post 
them in to a specific channel within discord server. 

## Requirements ## 
1. Python 3
2. Discordpy
3. dotenv 

## How To ## 

1. Create discord bot and get a Token. [1](https://discordpy.readthedocs.io/en/stable/discord.html)
2. Add bot to the server. With nesessary permissions. [2](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#creating-and-using-your-invite-link)
3. Clone this repository. 
4. Get trello api key and token. [3](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)
5. Get channel id from discord. (bot will post meessages in to that channel)
6. Create a file named ``` .env ``` as the same folder that has the ``` main.py ```.
7. Add the following details to the ``` .env ``` file. 

``` 
DISCORD_TOKEN=<discord bot token>
KEY=<trello key>
DTOKEN=<trello token>
TARGET=<target channel ID> 
```

* If need to change posting time interval see [```line 21, main.py ```](https://github.com/thilina27/Div2KnownIssuesDiscord/blob/3201c0ecdf431d1b3cbee1a1e10931e7e17208a4/main.py#L21)
* Need a help, or any suggestions post an issue here. 

** NOTE : This code is not fully optimized **
