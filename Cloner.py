import discord

# - Download discord.py https://pypi.org/project/discord.py/ #

client = discord.Client()
input_guild_id = "id"  # <-- input guild id
output_guild_id = "id"  # <-- output guild id
token = "token"  # <-- your token


print("""\


███████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄▀███─▄▄▄─█▄─▄███─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█
██─██─██─██▄▄▄▄─█─███▀█─██─██─▄─▄██─██─███─███▀██─██▀█─██─██─█▄▀─███─▄█▀██─▄─▄█
▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
                                                         
   Edited by: Darkky.
   Original: Bytewitch                                                                            
        """)


print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("Log:")
@client.event
async def on_connect():
    extrem_map = {}
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))
    for role in new_guild.roles:
        try:
            await role.delete()
        except:
            continue
    list_roles = []
    for role in guild.roles:
        list_roles.insert(0, role)
    for role in list_roles:
        await new_guild.create_role(name=role.name, permissions=role.permissions, colour=role.colour, hoist=role.hoist,
                                    mentionable=role.mentionable)

    for channel in new_guild.categories:
        await channel.delete()

    for channel in new_guild.voice_channels:
        await channel.delete()

    for channel in new_guild.text_channels:
        await channel.delete()

    for cat in guild.categories:
        new_cat = await new_guild.create_category_channel(name=cat.name, overwrites=cat.overwrites)
        await new_cat.edit(position=int(cat.position), nsfw=cat.is_nsfw())
        extrem_map[str(cat.id)] = new_cat.id

    for channel in guild.text_channels:
        print(channel)
        if channel.category_id is not None:
            new_cat_id = extrem_map.get(str(channel.category_id))

            new_txt_chan = await client.fetch_channel(int(new_cat_id))
            await new_txt_chan.create_text_channel(name=channel.name, topic=channel.topic, position=channel.position,
                                                   slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(),
                                                   overwrites=channel.overwrites)
        else:
            await new_guild.create_text_channel(name=channel.name, topic=channel.topic, position=channel.position,
                                                slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(),
                                                overwrites=channel.overwrites)

    for channel in guild.voice_channels:
        if channel.category_id is not None:
            new_cat_id = extrem_map.get(str(channel.category_id))
            new_voc_chan = await client.fetch_channel(int(new_cat_id))
            await new_voc_chan.create_voice_channel(name=channel.name, position=channel.position,
                                                    user_limit=channel.user_limit, overwrites=channel.overwrites)
        else:
            await new_guild.create_voice_channel(name=channel.name, position=channel.position,
                                                 user_limit=channel.user_limit, overwrites=channel.overwrites)
    await client.close()


client.run(token, bot=False)
