#pip install discord.py
# Para o bot funcionar normalmente, ative as intents do seu bot.
import discord
from discord.ext import commands
import asyncio
import random
intents = discord.Intents.all() 


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Opa ! {bot.user} acordou agora !")
  

#Mensagem de Boas-Vindas e saída básica:
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(id_do_canal) # ID do canal em que você quer que o bot envie a mensagem da entrada de algum membro.
    
    await channel.send(f'👉 {member.mention} entrou e agora estamos com **{len(member.guild.members)}** membros !')
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(id_do_canal) # ID do canal em que você quer que o bot envie a mensagem da saída de algum membro.
    
    await channel.send(f'😔 {member.mention} infelizmente saiu do servidor, espero que ele volte um dia...')

#Mensagens de Boas-Vindas e saída avançada: 
#Lembrando que não é permitido ter dois async def com o mesmo nome. Por exemplo nesse caso, não pode ter dois on_member_join ou on_member_remove, infelizmente você só pode escolher um. Caso contrário, o seu bot não enviará nada.
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(id_do_canal) # ID do canal em que você quer que o bot envie a mensagem da entrada de algum membro.
        
    WelcomeEmbed = discord.Embed(title=f'{member.name} | Bem vindo(a)!', color=0xfafafa)
    WelcomeEmbed.set_thumbnail(url = f'{member.avatar_url}')
    WelcomeEmbed.description = f'Olá, seja bem vindo(a) ao {member.guild.name} !'
    WelcomeEmbed.add_field(name="Leia as nossas diretrizes.", value="<#id_do_canal>")
    WelcomeEmbed.add_field(name="Converse com a gente ! ", value="<#id_do_canal>", inline=False)
    WelcomeEmbed.add_field(name=f"Atualmente estamos com:", value=f'**{len(member.guild.members)}** membros !')
    WelcomeEmbed.add_field(name="Precisando de ajuda?", value='Caso você tenha alguma dúvida ou problema aqui no servidor, fale com um dos nossos staffs !', inline=False)
    WelcomeEmbed.set_footer(text=f"ID do usuário: {member.id}")
        
    await channel.send(embed=WelcomeEmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(id_do_canal) # ID do canal em que você quer que o bot envie a mensagem da saída de algum membro.
        
    LeaveEmbed = discord.Embed(title=f'👋 | Até mais amigo!', description=f"😔 | **{member.name}** infelizmente saiu do servidor ", color=0xfafafa)
    LeaveEmbed.set_footer(text=f"ID do usuário: {member.id}")
        
    await channel.send(embed=LeaveEmbed)

#Comando "calcular":
@bot.command(name="calcular", help="Calcule uma expressão")
async def calculate_expression(ctx, *, expressão): 
    expressão= "".join (expressão) # Calcula a expressão.
    
    response = eval(expressão)
    
    await ctx.send("A resposta é: "  + str (response))

#Comando "ban":
@bot.command(name="ban", help="Bane um usuário")
async def ban(ctx, member : discord.Member, reason=None):
    if (not ctx.author.guild_permissions.ban_members): # Caso a pessoa não tenha a permissão para banir membros, ele enviará a mensagem abaixo.
        await ctx.send(f"{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Banir membros´´!")# Envia a mensagem de erro.

    if reason == None: # Caso o motivo do banimento seja nada.
        await ctx.send(f"Você precisa colocar um motivo!")
    else:
        embed_ban = discord.Embed(title="Usuário banido !", description=f"{ctx.author.mention} baniu {member.mention} por {reason} !", color=0x00FF00)
        await ctx.send(embed=embed_ban) # Envia a embed no canal onde você usou o comando para banir o membro.
        embed1 = discord.Embed(title="Você foi banido de um servidor !", description=f"Você foi banido de **{ctx.guild.name}** por **{reason}**", color=0xFF0000) 
        await member.send(embed=embed1) # Envia a embed1 para o membro que foi banido.
        await member.ban(reason=reason) # Bane o membro.

#Comando "ping":
@bot.command(name="ping", help="Mostra a latência do bot")
async def ping(self, ctx):
        
    pingEmbed = discord.Embed(title=':ping_pong: | Pong !', color=0xfafafa)
    pingEmbed.description = f'Meu ping é de ``{round(self.bot.latency * 1000)}ms`` !'
        
    await ctx.send(embed=pingEmbed)
    
#Comando "clear":
@bot.command(name="clear", help="Limpa uma certa quantidade de mensagens do chat")
async def clear(ctx, quantia=0):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(f'{ctx.author.mention} Você não tem permissão para utilizar este comando! Para utilizá-lo, você precisa ter permissão para ``Gerenciar Mensagens`` !')
        return
    await ctx.channel.purge(limit=quantia) # Limpa o chat.
    clearEmbed = discord.Embed(title='Chat limpo!', description=f'Chat limpo por: {ctx.author.mention}', color=0xfafafa)
    clearEmbed.set_footer(text='Já podem conversar novamente !')
    await ctx.send(embed=clearEmbed) 

    await asyncio.sleep(10)

#Comando "coinflip":
@bot.command(name="coinflip", help="Gire uma moeda !")
async def coinflip(ctx):
    choices = ["Deu **cara!** ", "Deu **coroa!**"]
    rancoin = random.choice(choices) # Aleatoriza as respostas do da variável choices.
    await ctx.send(rancoin)
   
#Comando "say":
@bot.command(name="say", help="Faça eu falar algo!")
async def say(ctx, *, mensagem):    
    await ctx.send(mensagem)
        
 
#Comando "oi":
@bot.command(name="oi", help="Oi?")
async def send_hello(ctx):
    choices = [f"Olá {ctx.author.mention} !", f"Opa! tudo bem?", "Oi!"]
    ranchoice = random.choice(choices) # Aleatoriza as respostas do da variável choices.
    
    response = f"{ranchoice}"

    await ctx.send(response)
    
#Caso você falar a palavra "palavrão" o bot irá enviar a mensagem da linha 131 e depois apagar a mensagem que contém o "palavrão". Caso queira mudar isso, só substituir "palavrão" por outra palavra na linha 132.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "palavrão" in message.content:
        await message.channel.send(f"Por favor {message.author.mention}, evite palavras de alto calão !")  
    await message.delete()
    await bot.process_commands(message)

# Lembrando que dá para melhorar bastante esse bot, em algum dia eu irei atualizar e melhorar algumas coisas!

bot.run('token_do_seu_bot_aqui')