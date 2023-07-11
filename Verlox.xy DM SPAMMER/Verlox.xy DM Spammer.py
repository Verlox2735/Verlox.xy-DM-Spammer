import asyncio
import threading
import os
import time
import colorama
import discord
import random
from colorama import Fore, Back, Style
from discord.ext import commands

os.system("title MassDm - By Verlox.xy")

with open(r'PATH TO TOKENS.TXT', 'r', encoding='utf-8') as file:
    totaltokens = sum(1 for line in file)

print(Fore.BLUE + "You Got " + Fore.CYAN + str(totaltokens) + Fore.BLUE + " Bot Tokens.")

print(Fore.CYAN + "Type Help to get info about this tool.\n")

InvalidTokens = []
nickofbots = None

async def dmspam(token, prefix, nickofbots):
    bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Bot is working and fully functional! :D")
        if nickofbots is not None:
            await bot.user.edit(username=nickofbots)
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="ⱤɄⱠɆĐ ฿Ɏ VɆⱤⱠØӾ.ӾɎ#2735"))

    @bot.command()
    async def dm(ctx, times=None, user_id=None, *, args=None):
        aws = 0
        if times is not None and user_id is not None:
            if args is not None:
                try:
                    target = await bot.fetch_user(user_id)
                    await ctx.channel.send(f"'{args}' is getting sent to: {target.name}")
                    for i in range(int(times)):
                        await asyncio.sleep(random.uniform(0.2, 0.5))  # Add a random delay between messages
                        try:
                            await target.send(args)
                            aws += 1
                            print(Fore.LIGHTCYAN_EX + f"[+] {Fore.CYAN}Sent Message. | Messages that were Sent > {aws}")
                        except discord.HTTPException as e:
                            if e.code == 429:  # Rate limit exceeded
                                retry_after = e.retry_after
                                print(Fore.YELLOW + f"[/] Rate Limited: Waiting for {retry_after} seconds.")
                                await asyncio.sleep(retry_after)
                                await target.send(args)  # Retry sending the message after the delay
                                aws += 1
                                print(Fore.LIGHTCYAN_EX + f"[+] {Fore.CYAN}Sent Message. | Messages that were Sent > {aws}")
                            else:
                                print(Fore.YELLOW + f"[/] Error sending message: {e}")
                except discord.NotFound:
                    print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "Invalid user ID.")
                except discord.Forbidden:
                    print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "Missing permissions to send a message to the user.")
            else:
                print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "A message was not provided.")
        else:
            print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "A user_id and/or times were not included.")

    try:
        await bot.start(token)
    except discord.LoginFailure:
        print(Fore.RED + "[-] Failed to log in with token: " + token)
        InvalidTokens.append(token)


def cttest(token, askForChannelIDCT):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), loop=loop)

    @bot.event
    async def on_ready():
        await bot.change_presence(status=discord.Status.offline, activity=discord.Activity(type=discord.ActivityType.playing, name="₣Ʉ₵₭ɆĐ ฿Ɏ ₱4Ɽ4Đ0Ӿ"))
        channel = bot.get_channel(int(askForChannelIDCT))
        try:
            await channel.send("Message Sent.")
        except discord.Forbidden:
            print(Fore.RED + "Failed with token " + token + Fore.CYAN)
            InvalidTokens.append(token)

    bot.run(token)


def process_command(cmd):
    global nickofbots

    if cmd == "Help" or cmd == "help":
        print(Fore.CYAN + r"""
This is a Discord MassDM Tool coded by Verlox.xy. Here are the commands you can use:

SetID [SI] - Sets your user ID so that you are the only one who can spam.
CheckTokens [CT] - Checks if the tokens in the Tokens.txt file are valid.
StartBots [SB] - Starts the bots.
Stop - Stops the bot and exits the program.
        """)

    elif cmd == "SI" or cmd == "si" or cmd == "sI" or cmd == "Si":
        keyword = input(Fore.CYAN + "USERID: " + Fore.MAGENTA)
        time.sleep(0.5)
        print(Fore.CYAN + "Setting UserID...")
        with open("user_id.txt", "w") as keyfile:
            keyfile.write(keyword)
            time.sleep(1)
            print(Fore.CYAN + "UserID Set!")

    elif cmd == "SB" or cmd == "sb" or cmd == "sB" or cmd == "Sb":
        prefix = input(Fore.CYAN + "Prefix: " + Fore.MAGENTA)
        askifchangenick = input(Fore.CYAN + "Change name of all Bots?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askifchangenick == "Y" or askifchangenick == "y":
            nickofbots = input(Fore.CYAN + "Name: " + Fore.MAGENTA)

        with open(r"C:\Users\islam\Desktop\Verlox.xy DM SPAMMER\Verlox.xy DM SPAMMER\tokens.txt", 'r') as file:
            lines = file.readlines()

        loop = asyncio.get_event_loop()
        for line in lines:
            token = line.strip()
            if nickofbots is not None:
                loop.create_task(dmspam(token, prefix, nickofbots))
            else:
                loop.create_task(dmspam(token, prefix, None))

        loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop=loop)))
        loop.close()

        for line in lines:
            token = line.strip()
            if nickofbots is not None:
                asyncio.create_task(dmspam(token, prefix, nickofbots))
            else:
                asyncio.create_task(dmspam(token, prefix, None))


while True:
    cmd = input(Fore.GREEN + "$ Input $ : " + Fore.MAGENTA)
    process_command(cmd)

    if cmd == "CT" or cmd == "ct" or cmd == "cT" or cmd == "Ct":
        askiftokensinserver = input(Fore.CYAN + "[REMINDER] Did you get all bots into the server?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askiftokensinserver == "n" or askiftokensinserver == "N":
            pass
        if askiftokensinserver == "y" or askiftokensinserver == "Y":
            askForChannelIDCT = input(Fore.CYAN + "all bots need to write a test message into a server, ChannelID: " + Fore.MAGENTA)
            print(Fore.CYAN + "Checking all Lines...")
            file1 = open('tokens.txt', 'r')
            Lines = file1.readlines()
            print(Fore.CYAN + "Checked all Lines.")
            time.sleep(0.5)

            for line in Lines:
                cttoken = line
                time.sleep(0.1)
                threading.Thread(target=cttest, args=(cttoken, askForChannelIDCT)).start()
            
            time.sleep(10)
            print(Fore.LIGHTRED_EX + "INVALID TOKENS: \n" + Fore.RED)
            print(*InvalidTokens, sep="\n")
            askifcleartokens = input(Fore.CYAN + "Delete Invalid Tokens?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)

            if askifcleartokens == "Y" or askifcleartokens == "y":
                with open("tokens.txt", "r") as file:
                    lines = file.readlines()
                with open("tokens.txt", "w") as file:
                    for line in lines:
                        if not any(word in line for word in InvalidTokens):
                            file.write(line)

                print(Fore.CYAN + "Finished.")

            if askifcleartokens == "N" or askifcleartokens == "n":
                pass

    if cmd == "SB" or cmd == "sb" or cmd == "sB" or cmd == "Sb":
        runned = 0
        prefix = input(Fore.CYAN + "Prefix: " + Fore.MAGENTA)
        askifchangenick = input(Fore.CYAN + "Change name of all Bots?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askifchangenick == "Y" or askifchangenick == "y":
            nickofbots = input(Fore.CYAN + "Name: " + Fore.MAGENTA)

        file1 = open('tokens.txt', 'r')
        Lines = file1.readlines()
        
        with open("user_id.txt", "r") as readuserid:
            userid = readuserid.readline()

        for line in Lines:
            print(Fore.CYAN)
            dmtoken = line
            dmthread = threading.Thread(target=dmspam, args=(dmtoken, prefix, nickofbots))
            dmthread.start()
