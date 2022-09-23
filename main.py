import requests, json, os, discord;from discord.ext import commands


client = commands.Bot(command_prefix ='<', self_bot = True)
token = ""


@client.command()
async def cs(ctx,server_id, channel_id):
    await ctx.message.delete()
    
    with open(f'{channel_id}.txt', 'w+') as file:
        headers = {'authorization' : f'{token}'}
        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
        messages = json.loads(response.text)
        for value in messages:
            format = f"""==================================\nDate: {str(value['timestamp'][0:10])}\n
            Author: {str(value['author']['username'])}#{str(value['author']['discriminator'])}\n\t
            Content: \"{str(value['content'])}\"\n\n\n\t
            Message Link: https://discordapp.com/channels/{server_id}/{str(value['channel_id'])}/{str(value['id'])}\n=================================="""
            file.write(format)
            await ctx.send(format)
    os.unlink(f"{channel_id}")
    
client.run(token, bot=False)
