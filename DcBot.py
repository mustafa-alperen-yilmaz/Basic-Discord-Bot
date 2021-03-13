import discord
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents(messages = True , guilds = True , members = True , reactions = True , presences = True)#botumuzun erişmesi gerekn bir kaç bilgi
client = commands.Bot(command_prefix="!!" , intents = intents) #botun nasıl çalışacağını bize söyler yada gösterir

#botun çalışıp çalışmadığını terminale yazdırır
@client.event
async def on_ready():
    print("hazır")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels , name ="yeni-gelenler")
    await channel.send(f"{member} aramıza hoş geldi ^^")# yeni gelenler kanalına kişinin idsi ve kendine has numarasını yazdırır
    print(f"{member} aramıza hoş geldi ^^")# teminale kişinin idsi ve kendine has numarasını yazdırır

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels , name = "aramızdan-ayrılanlar")
    await channel.send(f"{member} aramızadan atrıldı :(")# aramızdan ayrılanlar kanalına kişinin idsi ve kendine has numarasını yazdırır
    print(f"{member} aramızdan ayrıldı :(")# teminale kişinin idsi ve kendine has numarasını yazdırır

#serverin ping durumu
@client.command()
async def ping(ctx):
    await ctx.send(f' serverde {client.latency * 1000} Ms ping var')

#yönetim rolüne sahip kullanıcıların diğer kullanıcılara kicklemesini sağlar
@client.command()
@commands.has_role("yönetim")
async def kick(ctx , member : discord.Member, *args , reason=""):
    await member.kick(reason = reason)

#yönetim rolüne sahip kullanıcıların diğer kullanıcılara ban atmasını sağlar
@client.command()
@commands.has_role("yönetim")
async def ban(ctx , member : discord.Member , *args , reason = ""):
    await member.ban(reason = reason)

#yönetim rolüne sahip kullanıcıların o yazı kanalındaki son 10 mesajı silmesini sağlar
@client.command()
@commands.has_role("yönetim")
async def clear(ctx , amount = 10):
    await ctx.channel.purge(limit = amount)

#serverin bilgisini yazıldığı kanala gönderir ve yazar
@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(
        title=name + " Server Bilgisi",
        description = "HOŞGELDİNİZ",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name = "sunucunun sahibi" , value=owner , inline=True)
    embed.add_field(name = "server id" , value= id , inline= True)
    embed.add_field(name = "server bölgesi" , value=region, inline= True)
    embed.add_field(name = "kaç kişiyiz" , value=memberCount,inline=True)
    await ctx.send(embed = embed)

#botun çalışması için kendi tokeninizi ('') içine yazın
client.run('discord bot token')