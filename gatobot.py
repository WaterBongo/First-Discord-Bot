import discord
import os
import urllib.error
from urllib.request import Request, urlopen
import time
from discord.colour import Color
from discord.member import Member
import requests
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^
url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"
client = discord.Client()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)
client = commands.Bot(command_prefix = '.', case_insensitive=True, intents = intents) #prefix
client.remove_command('help')
client.members=True
@client.event
async def on_ready():
    activity = discord.Game(name="Sub to Pog hacking")
    await client.change_presence(status=discord.Status.online, activity=activity)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\

   ______      __           __          __ 
  / ____/___ _/ /_____     / /_  ____  / /_
 / / __/ __ `/ __/ __ \   / __ \/ __ \/ __/
/ /_/ / /_/ / /_/ /_/ /  / /_/ / /_/ / /_  
\____/\__,_/\__/\____/  /_.___/\____/\__/  
                                           

""")
    print("Launching Gato Bot....")
    print("Gato Bot has loaded have a good day!")#will print "online message" in the console when the bot is online
    print("-----------------------------------Logs start here-----------------------------------")  
    
    
@client.command()
async def Floppa(ctx):
    await ctx.message.delete()
    await ctx.send("Floppa the Cat!" + " https://tenor.com/view/floppa-hahaahah-big-floppa-gif-20097912") #floppa owns all
    print(str(ctx.message.author) + " Just ran Floppa!")

@client.command()
async def Kick(ctx, member : discord.Member):
    if ctx.message.author.guild_permissions.manage_channels:
        try:
            await member.kick(reason=None)
            await ctx.send("kicked " +member.mention) #kick command
            print(str(ctx.message.author)+" Kicked "+member.mention)
        except:
                print(str(ctx.message.author) + " just tried to kick! " + member.mention + " and failed!")
                embed=discord.Embed(title ="Command has failed!", description="It seems that you do not have enough permissions to kick "+member.mention, color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def Roll(ctx):
  await ctx.message.delete()
  await ctx.send(" https://media1.tenor.com/images/23aeaaa34afd591deee6c163c96cb0ee/tenor.gif") #dk!"
  print(str(ctx.message.author) + " Just got rick rolled lmao")


@client.command()
async def ban(ctx, member : discord.Member, *, reason):
    author = ctx.message.author
    if ctx.message.author.guild_permissions.manage_channels:
        try:
            await member.ban(reason=reason)
            embed=discord.Embed(title="Banned User!",description=str(author) + " Just Banned " + str(member) + " for | " + str(reason), color=0xff00f6)
            await ctx.send(embed=embed) #ban command
            print(str(ctx.message.author) + " Just Banned " + member.mention)
        except:
            await ctx.send("Give yourself 3 seconds to think about this")
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def unban(ctx, *, member):#unbans
  banned_users = await ctx.guild.bans()
  member_name, member_discriniator = member.split('#')
  if ctx.message.author.guild_permissions.manage_channels:
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriniator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return
  else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def Nuke(ctx):
    if ctx.message.author.guild_permissions.manage_channels:
        channel = ctx.channel
        channel_position = channel.position
        new_channel = await channel.clone()
        await channel.delete()
        await new_channel.edit(position=channel_position, sync_permissions=True)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)
    


@client.command()
async def Dog(ctx):
    await ctx.message.delete()
    r = requests.get    ("https://api.thedogapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    await ctx.send(link)
    print(str(ctx.message.author) + " asked for a Dog!")


@client.command()
async def gato(ctx):
    await ctx.message.delete()
    r = requests.get    ("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    await ctx.send(link)
    print(str(ctx.message.author) + " Asked for a Gato!")



@client.command()
async def Shutdown(ctx):
  if ctx.message.author.guild_permissions.manage_channels:
    await ctx.message.delete()
    embed=discord.Embed(title="**Thank you for using Gato Bot!**", description="Shutting down...", color=0xff00f6)
    await ctx.send(embed=embed)
    time.sleep(3)
    exit()
  else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)



@client.command()
async def spam(ctx, y, v):
  if ctx.message.author.guild_permissions.manage_channels:
    print(str(ctx.message.author) + " spammed "+ v,  y + " times!")
    for i in range(int(y)):
        await ctx.send(v)
  else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)





@client.command()
async def mute(ctx, member : discord.Member,*, reason="Not specified"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if ctx.message.author.guild_permissions.manage_channels:

        if not mutedRole:
            await guild.create_role(name="Muted")

        if member == ctx.author:
            await ctx.send("You cannot mute yourself.")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title=str(member) + " has been muted!", description=f"{member} was muted ", color=0xff00f6)
        embed.add_field(name="reason:", value=reason, inline=False)
        memberRole = discord.utils.get(guild.roles, name="Member")   
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.remove_roles(memberRole)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)
@client.command()
async def unmute(ctx, member : discord.Member,*, reason="Not specified"):
    guild = ctx.guild
    memberRole = discord.utils.get(guild.roles, name="Member")    
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    embed = discord.Embed(title="Un-Mute", description=f"{member.mention} was un-muted ", color=0xff00f6)
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.remove_roles(mutedRole, reason=reason)
    await member.add_roles(memberRole, reason=reason)
    await member.send(f" you have been Unmuted from: {guild.name} reason: {reason}")


@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')


@client.command()
async def friday(ctx):
    if ctx.message.author.guild_permissions.manage_channels:
        await ctx.message.delete()
        await ctx.send("@everyone Have a happy floppa friday and i wish @takeru#0001 and @antihak#1549 Happy fish friday" + "https://tenor.com/view/floppa-pet-big-floppa-allah-gif-18720385")
        print(str(ctx.message.author) + " Has run Friday!")
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def accept(ctx, member : discord.Member):
    guild = ctx.guild
    channel = ctx.message.channel
    BetaRole = discord.utils.get(guild.roles, name="Beta")
    newcate = discord.utils.get(ctx.guild.categories, name="appy")
    dl_channel = discord.utils.get(guild.channels, name="beta-downloads")
    dl_chat = discord.utils.get(guild.channels, name="beta-access")
    if ctx.message.author.guild_permissions.manage_channels:
        await member.add_roles(BetaRole)
        await channel.edit(name="accepted", category=newcate)
        print(str(ctx.message.author)+" has just accepted " +str(member))
        embed=discord.Embed(title="Congrats " + str(member) + " you've accepted into Hummus Beta!", description="Congratulations! Youve been accepted for Hummus beta!\nTo get beta builds go to," + dl_channel.mention + "and to talk to others goto " + dl_chat.mention + "!", color=0xff00f6)
        await ctx.send(embed=embed)
        await ctx.send("Please Close This Ticket Now If You Dont Have Any Questions :)")
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def denied(ctx):
    channel = ctx.message.channel
    newcate = discord.utils.get(ctx.guild.categories, name="appy")
    print(str(ctx.message.author)+" has just denied somebody!")
    await ctx.message.delete()
    await channel.edit(name="denied", category=newcate)
    embed=discord.Embed(title="Sorry, Unfortunatley you've been denied for hummus beta", description="Unfortunatley we've reviewed your application and have decided that you are not suited for this beta\nYou may reapply for beta in 1 month\nGood luck next time :D", color=0xff00f6)
    await ctx.send(embed=embed)



@client.command()
async def download(ctx, Version=None):
    guild = ctx.guild
    user = ctx.message.author
    role = discord.utils.get(guild.roles, name="Beta")
    role2 = discord.utils.get(guild.roles, name="Paid")
    if Version == "beta":
        if role in user.roles or role2 in user.roles:
            url = "https://hummusclient.info/api/account/login"
            payload = {'email': 'astriogamer@riseup.net', 'password': '_Bananapopcorn22_', 'beta' : 'False'}
            response = requests.post(url, params=payload)
            dl=response.json()
            url = " https://hummusclient.info/api/admin/createDownloadLink"
            payload = {'token': dl["responseObject"]["token"], 'beta': "True"}
            rhala = requests.post(url, params=payload)
            realink = rhala.json()
            embed=discord.Embed(title="Download Succesful!", description="**Download link**\n" + 
            realink["statusText"] + "\nThis link will expire in 5 minutes", color=0xff00f6)
            await user.send(embed=embed)
            alalh=discord.Embed(title="Download Successful!", description="Look in Dms! " + str(user), color=0xff00f6)
            await ctx.send(embed=alalh)
            print(str(user) + " generated a " + str(Version) + " download!")


        else:
            embed=discord.Embed(title="Download Error!", description="You Dont have beta!\nThat means you cant download it just yet", color=0xff00f6)
            await ctx.send(embed=embed)
    elif Version == "release":
            embed=discord.Embed(title="Pulic Version Has not been released yet!", description="Please Apply for beta at\n<#868007168669024328>", color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="What Version?", description="**Beta**\nBeta Download for Beta users only\n**Release**\nPublic build for everybody to use!", color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def purge(ctx, amount : int):
    if ctx.message.author.guild_permissions.manage_channels:
        await ctx.channel.purge(limit=amount)
        msg = await ctx.send("Purged " + str(amount) + " messages!")
        print(str(ctx.message.author)+" Purged " + str(amount) + " messages!")
        time.sleep(10)
        await msg.delete()
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


    



@client.command()
async def hummus(ctx, person=None):
    if person == "shiv":
        embed=discord.Embed(title="Shivs Hummus Recipe", description="**Ingredients for this Hummus**\n2 cloves garlic, divided\n1 (19 ounce) can garbanzo beans, half the liquid reserved\n4 tablespoons lemon juice\n2 tablespoons tahini\n1 teaspoon salt\nblack pepper to taste\n2 tablespoons olive oil\n\n **Instructions**\nStep 1\n\nIn a blender, chop garlic. Pour garbanzo beans into the blender, reserving about 1 tablespoon for garnish. Add reserved liquid, lemon juice, tahini, and salt to the blender. Blend until creamy and well mixed.\n\nStep 2\n\nTransfer the mixture to a medium serving bowl. Sprinkle with pepper and pour olive oil over the top. Garnish with reserved garbanzo beans.", color=0xff00f6)
        await ctx.send(embed=embed)
    elif person == "noodler":
        embed=discord.Embed(title="Noodler's Hummus Recipe", description="**Ingredients**\n\n1 (30-ounce) can chickpeas\n½  cup (120 ml) fresh lemon juice (2 large lemons)\n½  cup (120 ml) well-stirred tahini,\n2 medium garlic cloves, minced\n4 tablespoons (60 ml) extra-virgin olive oil, plus more for serving\n1 teaspoon ground cumin\nSalt to taste\nAbout ½  cup of ice cubes\nCayenne pepper, for serving\n\n**Instructions**\n\n1. Pour tahini, lemon juice in the blender/food processor then blend for about 30 seconds or until it looks uniform and whipped.\n2. Add garlic, oil, cumin and 1 teaspoon of salt to the whipped tahini, then blend for another 30 seconds or until uniform. Scrape the bowl so that the mixture blends evenly when the chickpeas are added.\n3. Add about a ¼ cup of ice cubes to the blender (this will help keep the hummus cool so you can serve and eat it as soon as it's ready)\n4. Open the can of chickpeas, drain and rinse the peas with cold water.\n5. Add half the can of chickpeas to the blender and blend for about 1 minute, do your best safely to mix it so that the peas are blended evenly.\n6. The mixture will likely be too thick and there will still be solid chunks of peas so this is when you can add more chunks of ice to loosen the mixture up until it’s the consistency you want.\n7. Add the rest of the chickpeas to the blender and process until the mixture is uniform, you can blend for less time if you want it chunky or more time if you like it smooth.\n8. Add salt to taste\n\n**Tips**\nFeel free to add more/larger garlic cloves if you like a stronger garlic taste.\nYou can experiment with your recipe and make different flavours of hummus by adding ingredients such as dried tomato, fresh jalapenos, or basil\nServe with a dash of olive oil and cayenne pepper in the bowl to make the hummus look fancy", color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Real Hummus recipes", description="**Shivs**\n Shiv's recipe its ok i guess\n**Noodler**\nLITTERLY THE BEST HUMMUS IN THE WORLD MUST TRY NOW", color=0xff00f6)
        await ctx.send(embed=embed)



@client.command()
async def give(ctx, role, member : discord.Member):
    guild=ctx.guild
    ranrole = discord.utils.get(guild.roles, name = role)
    if ctx.message.author.guild_permissions.manage_channels:
        try:
            await member.add_roles(ranrole)
            await ctx.send("Given " + member.mention + " "+ str(ranrole) + "!")
        except:
            embed=discord.Embed(title="Give Role Error!", description="There was a issue With giving \n" + str(member) + " " + str(ranrole), color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def remove(ctx, thingtoremove, member : discord.Member):
    guild=ctx.guild
    ranrole = discord.utils.get(guild.roles, name = thingtoremove)
    if ctx.message.author.guild_permissions.manage_channels:
        if ranrole in member.roles:
            await member.remove_roles(ranrole)
            embed=discord.Embed(title="Role Removal successful!", description=str(ranrole) + " has been removed from " + str(member), color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(tite="There was a error!",description="This bot doesnt have sufficent permissions\nor The person doesnt have" + str(ranrole) + " to remove!", color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)



@client.command()
async def paybeta(ctx, payment=None):
    await ctx.message.delete()
    if payment == "eth":
        embed=discord.Embed(title="Pay via ETH for beta!", description="Send 8$ to \n0xD21247D7C743e3e08c0D9001b3DBEAA449805044\nWith proof of payment!", color=0xff00f6)
        await ctx.send(embed=embed)
    if payment == "btc":
        embed=discord.Embed(title="Pay for Beta via BTC", description="Send 8$ to\nbc1qrn2twdpkf5jma982rjxev2yvagqd0es5qv33qy\n With proof of Payment :)", color=0xff00f6)
    elif payment == "paypal":
        embed=discord.Embed(title="Pay Paypal for beta!", description="Send 5$ f&f to https://paypal.me/lavaflowglow/7\8\nPlease show proof in ticket :)", color=0xff00f6)
        await ctx.send(embed=embed)
    elif payment == "nitro":
        embed=discord.Embed(title="Gift Nitro for beta!", description="Please Gift Cutecat#0604 10$ Nitro\nbeta will only be given after\nbeing verified by Cutecat#0604", color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Payment methods for Hummus Beta!", description="**Nitro(prefered way of payment)**\nGift 10$ Nitro to Cutecat#0604\n**BTC crypto**\nRun the command to learn more\n**ETH Crypto**\n Send Crypto to Cutecat#0604\n**Paypal**\nBuy beta with paypal!", color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def help(ctx, panel=None):
    await ctx.message.delete()
    if panel == "admin":
        embed=discord.Embed(title ="Admin Commands!", description="**Ban**\nUse this to ban people\n**Kick**\nUse this to kick people\n**Nuke**\nThis command Nukes Whatever channel you need\n**Friday**\nTry it out ;)\n**Purge**\nPurge chat messages!", color=0xff00f6)
        await ctx.send(embed=embed)
    elif panel == "fun":
        embed=discord.Embed(title ="Fun Commands!", description="**Gato**\nGet a gato pic :D\n**Dog**\nGet a dog pic :D\n**Roll**\nTest it out ;)\n**Spam**\nspam to your hearts desire(admin only)\n**Ping**\nCheck bot ping!\n**Masschannel**\nCreated a seperate category with 5 channels!\n**Dele**\nDelete all chambers with a simple command", color=0xff00f6)
        await ctx.send(embed=embed)
    elif panel == "moderation":
        embed=discord.Embed(title="Moderation stuff!", description="**Kick**\nThis is the Kick command. obviously...\n**Ban**\n Use this to ban people\n**Unban**\nUnban people that have been banned\n**Mute**\nThis is used to mute people\n**unmute**\nUnmute people right after muting them\n**Give**\nGive somebody a role by using this command!\n**Remove**\nRemove Somebodies role with this command", color=0xff00f6)
        await ctx.send(embed=embed)
    elif panel == "Dev stuff":
        embed=discord.Embed(title="Developer stuff", description="**Dev Mode**\nShuts down the bot for development", color=0xff00f6)
        await ctx.send(embed=embed)
    elif panel == "all":
         embed=discord.Embed(title="Gato Bot Commands", description="**ban**\nThis is used to ban players\n**Ban**\nBan Is A Ban very hard understand?\n**Dog**\nDOGGGGGGGGGGGGGG\n**Floppa**\nhappy floppa everyday\n**Gato**\nWe all love gatos\n**Help**\n What your looking at\n**Kick**\n Kick players from a discord\n**Nuke**\n Nuke a discord channel(delete all msgs)\n**Roll**\nTest it out!\n**Unban**\n unban people\n**Shutdown**\Shutdown the whole bot \n**Spam**\nSpam with the bot\n**Event**\n Hmm? a event? well test the cmd already!\n**Ping**\nCheck bot Ping!\n**Friday**\nFinally, Its friday again Run this cmd to finish your week off :)\n**Purge**\nPurge messages", color=0xff00f6)
         await ctx.send(embed=embed)
    elif panel == "hummus":
        embed=discord.Embed(title="Hummus Commands!",description="**Accept**\nAccept people for hummus beta\n**Denied**\nuseful for denying children is all im saying\n**download**\nRun This command to get Hummus Client downloads\n**Verify**\nverify Hummus beta users\n**Unverify**\nRemoves Hummus Beta users completely")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Commands!", description="**Admin**\n These are all the admin commands!\n**fun**\nThis is where all the usless.. but fun commands are stored!\n**Moderation**\nall boring stuff nothing to see here\n**All**\nShow all bot commands", color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def masschannel(ctx):
  if ctx.message.author.guild_permissions.manage_channels:
    msg = await ctx.send("Creating Chamber Channels....")
    
    z = 0
    await ctx.guild.create_category("Welcome_to_the_chambers")
    await msg.edit(content="New Category has been made!")
    time.sleep(1)
    await msg.edit(content="Starting to create Chambers...")
    for i in range(50):
        category = discord.utils.get(ctx.guild.categories, name="Welcome_to_the_chambers")
        z = z + 1   
        await ctx.guild.create_text_channel('chamber ' + str(z),    category=category)
    await msg.edit(content="Finished putting as many channels as it can!")
  else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def dele(ctx):
  x = 0
  msg2 = await ctx.send("Chamber deletion in Progress...")
  category = discord.utils.get(ctx.guild.categories, name="Welcome_to_the_chambers")
  guild = ctx.message.guild
  channel = ctx.message.channel
  embed=discord.Embed(title="All channels have been deleted!",description="All the Chamber channels have been deleted!", color=0xff00f6)
  if ctx.message.author.guild_permissions.manage_channels:
    for i in range(50):
        try:
            x = x + 1
            existing_channel = discord.utils.get(guild.channels, name="chamber-" + str(x))
            await existing_channel.delete()
        except:
            pass
    await category.delete()
    msg = await ctx.send(embed=embed)
    time.sleep(5)
    await msg.delete()
    await msg2.delete()
  else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def verify(ctx, acc):
    if ctx.message.author.guild_permissions.manage_channels:
        url = "https://hummusclient.info/api/account/login"
        payload = {'email': 'astriogamer@riseup.net', 'password': '_Bananapopcorn22_'}
        response = requests.post(url, params=payload)
        req = response.json()
        url = "https://hummusclient.info/api/admin/addBeta"
        payload = {'token': req["responseObject"]["token"], 'username': str(acc)}
        response2 = requests.post(url, params=payload)
        if response2.status_code == 200:
            embed=discord.Embed(title="Success!", description="User " + str(acc) + " Has been whitelisted!",color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(time="Whitelist failed!",description="Trying to Whitelist " + str(acc) + " has failed!",color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)
    
@client.command()
async def unverify(ctx, acc):
    if ctx.message.author.guild_permissions.manage_channels:
        url = "https://hummusclient.info/api/account/login"
        payload = {'email': 'astriogamer@riseup.net', 'password': '_Bananapopcorn22_'}
        response = requests.post(url, params=payload)
        req = response.json()
        url = " https://hummusclient.info/api/admin/removeBeta"
        payload = {'token': req["responseObject"]["token"], 'username': str(acc)}
        response2 = requests.post(url, params=payload)
        if response2.status_code == 200:
            embed=discord.Embed(title="Success!", description="User " + str(acc) + " Has been Banned!",color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(time="Ban failed!",description="Trying to Ban " + str(acc) + " has failed!",color=0xff00f6)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Command error!",description="It seems that you do not have permissions to run this command!",color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
async def furryporn(ctx):
  author = ctx.message.author
  await ctx.message.delete()
  r = requests.get("https://sheri.bot/api/yiff/?format=json")
  res = r.json()
  em = discord.Embed()
  em.set_image(url=res['url'])
  await ctx.send(embed=em)
  for i in range(500):
    msg = await ctx.send(author.mention)
    await msg.delete()
  print(str(author) + " Generated Porn!")

@client.command()
async def gping(ctx, Amount, User):
    await ctx.message.delete()
    for i in range(int(Amount)):
        msg = await ctx.send(str(User))
        await msg.delete()

@client.event
async def on_member_join(member):
  channel = client.get_channel(906385411356655656)
  await channel.send("Welcome to Hummus appreciation " + member.mention + " !, go to <#906385495104307201> To start verification!")

client.run('token')