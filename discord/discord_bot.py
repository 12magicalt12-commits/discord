import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime, timedelta
import random
load_dotenv()
TOKEN = os.getenv('discord_token')
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='+', intents=intents)
ACCESS_ROLE_ID = 1401588306730291230
ability_cooldown = {
    'mist':604800,
    'amaterasu':172800,
    'arrow':345600,
    'blood':172800,
    'ragnarok':86400,
    'heal':86400,
    'paralyse':259200,
    'laser':172800,
    'phoenix':86400,
    'phoenix2':259200,
    'cursed':604800,
    'poison':432000,
    'saturn':86400,
    'volcan':86400,
    'angel':86400,
    'clef':86400,
    'judgement':1296000,
    'ombre':259200
}
# Helper function (place this outside any command)
def _set_cooldown_logic(member_id, ability_name, cooldown_duration):
    """
    Handles the core database logic for setting and checking a cooldown.
    Returns: (is_on_cooldown, expiration_timestamp)
    """
    global conn, cursor
    current_time = datetime.now().timestamp()
    
    # Check for existing cooldown
    cursor.execute(
        "SELECT cooldown_until FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member_id, ability_name)
    )
    result = cursor.fetchone()
    
    # If active cooldown found, return it
    if result is not None:
        expiration_timestamp = result[0]
        if expiration_timestamp > current_time:
            return True, expiration_timestamp # is_on_cooldown=True
            
    # If no active cooldown, set a new one
    expiration_dt = datetime.now() + timedelta(seconds=cooldown_duration)
    new_expiration_timestamp = expiration_dt.timestamp()

    cursor.execute(
        """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
           VALUES (?, ?, ?)""",
        (member_id, ability_name, new_expiration_timestamp)
    )
    conn.commit()
    return False, new_expiration_timestamp 
@bot.command(name='mist')
async def mist_cd_command(ctx):
    ability_name = "mist"
    cooldown_duration = ability_cooldown[ability_name]
    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='paralyse')
async def mist_cd_command(ctx):
    ability_name = "paralyse"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ta **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='blood')
async def mist_cd_command(ctx):
    ability_name = "blood"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='laser')
async def mist_cd_command(ctx):
    ability_name = "laser"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='amaterasu')
async def mist_cd_command(ctx):
    ability_name = "amaterasu"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='phoenix')
async def mist_cd_command(ctx):
    ability_name = "phoenix"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='phoenix2')
async def mist_cd_command(ctx):
    ability_name = "phoenix2"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='cursed')
async def mist_cd_command(ctx):
    ability_name = "cursed"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='poison')
async def mist_cd_command(ctx):
    ability_name = "poison"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='saturn')
async def mist_cd_command(ctx):
    ability_name = "saturn"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='ragnarok')
async def mist_cd_command(ctx):
    ability_name = "ragnarok"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='clef')
async def mist_cd_command(ctx):
    ability_name = "clef"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ta **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='judgment')
async def mist_cd_command(ctx):
    ability_name = "judgement"
    cooldown_duration = ability_cooldown[ability_name]

    is_on_cooldown, timestamp = _set_cooldown_logic(
        ctx.author.id, 
        ability_name, 
        cooldown_duration
    )
    if is_on_cooldown:
        await ctx.send(
            f"❌ **{ctx.author.display_name}**, ton **{ability_name}** est toujours sous cooldown ! "
            f"Pret: <t:{int(timestamp)}:R>"
        )
    else:
        await ctx.send(
            f"✅ Ton **{ability_name}** est sous cooldown. "
            f"Pret a nouveau: <t:{int(timestamp)}:R> (<t:{int(timestamp)}:T>)"
        )
@bot.command(name='volcan')
# @commands.has_role(ROLE_ID) # Add permission decorator if needed
async def combo_ability_command(ctx):
    member = ctx.author
    ability_name = "volcan" 
    final_cooldown_duration = ability_cooldown[ability_name]
    current_time = datetime.now().timestamp()

    # 1. RETRIEVE CURRENT STATUS (Count or Cooldown Time)
    cursor.execute(
        "SELECT cooldown_until FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    result = cursor.fetchone()
    
    # Check 1: If the entry exists
    if result is not None:
        stored_value = result[0] # This could be a timestamp (cooldown) or an integer (count)
        
        # Check 1a: Is it an active COOLDOWN (i.e., the value is a future timestamp)?
        if stored_value > current_time:
            # Still on cooldown
            return await ctx.send(
                f"❌ **{member.display_name}**, ton **{ability_name}** est sous cooldown. "
                f"Pret: <t:{int(stored_value)}:R>"
            )

        # Check 1b: Is it a USAGE COUNT (i.e., the value is 1, and the cooldown expired)?
        elif stored_value == 2:
            # Second use! Start the final cooldown.
            
            # Calculate the final expiration time
            expiration_dt = datetime.now() + timedelta(seconds=final_cooldown_duration)
            new_expiration_timestamp = expiration_dt.timestamp()

            # Update database with the new, long cooldown time
            cursor.execute(
                """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
                   VALUES (?, ?, ?)""",
                (member.id, ability_name, new_expiration_timestamp)
            )
            conn.commit()
            
            return await ctx.send(
                f"✅ Ton {ability_name} est sous cooldown ! "
                f"Pret a nouveau: <t:{int(new_expiration_timestamp)}:R>"
            )

    # 2. FIRST USE (or Cooldown expired and deleted via +cd)
    
    # Set the usage count to 1 (or reset the count if it expired)
    usage_count = 2
    cursor.execute(
        """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
           VALUES (?, ?, ?)""",
        (member.id, ability_name, usage_count)
    )
    conn.commit()
    
    await ctx.send(
        f"⏳ **{ability_name.upper()}** use (1/2)"
    )
@bot.command(name='heal')
async def combo_ability_command(ctx):
    member = ctx.author
    ability_name = "heal"
    final_cooldown_duration = ability_cooldown[ability_name]
    current_time = datetime.now().timestamp()
    cursor.execute(
        "SELECT cooldown_until FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    result = cursor.fetchone()
    if result is not None:
        stored_value = result[0] 
        if stored_value > current_time:
            return await ctx.send(
                f"❌ **{member.display_name}**, ton **{ability_name}** est sous cooldown. "
                f"Pret a nouveau: <t:{int(stored_value)}:R>"
            )
        elif stored_value == 2:
            expiration_dt = datetime.now() + timedelta(seconds=final_cooldown_duration)
            new_expiration_timestamp = expiration_dt.timestamp()
            cursor.execute(
                """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
                   VALUES (?, ?, ?)""",
                (member.id, ability_name, new_expiration_timestamp)
            )
            conn.commit()
            return await ctx.send(
                f"✅ Ton {ability_name.upper()} est sous cooldown ! "
                f"Pret a nouveau: <t:{int(new_expiration_timestamp)}:R>"
            )
    usage_count = 2
    cursor.execute(
        """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
           VALUES (?, ?, ?)""",
        (member.id, ability_name, usage_count)
    )
    conn.commit()
    await ctx.send(
        f"⏳ **{ability_name.upper()}** use (1/2)"
    )
@bot.command(name='arrow')
async def combo_ability_command(ctx):
    member = ctx.author
    ability_name = "arrow"
    final_cooldown_duration = ability_cooldown[ability_name]
    current_time = datetime.now().timestamp()
    cursor.execute(
        "SELECT cooldown_until FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    result = cursor.fetchone()
    if result is not None:
        stored_value = result[0] 
        if stored_value > current_time:
            return await ctx.send(
                f"❌ **{member.display_name}**, ton **{ability_name}** est sous cooldown. "
                f"Pret a nouveau: <t:{int(stored_value)}:R>"
            )
        elif stored_value == 2:
            expiration_dt = datetime.now() + timedelta(seconds=final_cooldown_duration)
            new_expiration_timestamp = expiration_dt.timestamp()
            cursor.execute(
                """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
                   VALUES (?, ?, ?)""",
                (member.id, ability_name, new_expiration_timestamp)
            )
            conn.commit()
            return await ctx.send(
                f"✅ Ton {ability_name} est sous cooldown ! "
                f"Pret: <t:{int(new_expiration_timestamp)}:R>"
            )
    usage_count = 2
    cursor.execute(
        """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
           VALUES (?, ?, ?)""",
        (member.id, ability_name, usage_count)
    )
    conn.commit()
    await ctx.send(
        f"⏳ **{ability_name.upper()}** use (1/2)"
    )
@bot.command(name='ombre')
async def quad_ability_command(ctx):
    member = ctx.author
    ability_name = "ombre"
    MAX_USES = 4 # Total uses required
    FINAL_CD_DURATION = 180 # 3 minutes after the 4th use
    
    current_time = datetime.now().timestamp()
    
    # Retrieve current state from the database
    cursor.execute(
        "SELECT cooldown_until FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    result = cursor.fetchone()
    
    # stored_value will be the timestamp, a small integer (1-3), or 0 if not found
    stored_value = result[0] if result is not None else 0

    # 1. Active Cooldown Check (Value is a future timestamp)
    if stored_value > current_time:
        return await ctx.send(
            f"❌ **{member.display_name}**, ton **{ability_name}** est sous cooldown! Pret a nouveau: <t:{int(stored_value)}:R>"
        )
    
    # 2. Determine Current Count (Reset expired timestamp to 0)
    if stored_value < MAX_USES:
        # Value is 0, 1, 2, or 3 (a usage count)
        current_count = int(stored_value)
    else:
        # Value is an expired timestamp (large number), so we reset the count to 0.
        current_count = 0
        
    new_count = current_count + 1

    # 3. Handle Final Use (Count hits 4)
    if new_count == MAX_USES:
        expiration_dt = datetime.now() + timedelta(seconds=FINAL_CD_DURATION)
        new_expiration_timestamp = expiration_dt.timestamp()

        # Update database with the new, final cooldown timestamp
        cursor.execute(
            """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
               VALUES (?, ?, ?)""",
            (member.id, ability_name, new_expiration_timestamp)
        )
        conn.commit()
        return await ctx.send(
            f"✅ ton **{ability_name}** est sous cooldown ! Pret: <t:{int(new_expiration_timestamp)}:R>"
        )

    # 4. Handle Incremental Use (Count is 1, 2, or 3)
    else:
        uses_remaining = MAX_USES - new_count
        
        # Update database with the new usage count (small integer)
        cursor.execute(
            """INSERT OR REPLACE INTO cooldowns (user_id, ability, cooldown_until) 
               VALUES (?, ?, ?)""",
            (member.id, ability_name, new_count)
        )
        conn.commit()
        
        await ctx.send(
            f"⏳ **{ability_name}** : use restant {uses_remaining}"
        )
@bot.event
async def on_ready():
    global conn, cursor
    conn = sqlite3.connect('team_cds.db')   
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cooldowns (
        user_id INTEGER NOT NULL,
        ability TEXT NOT NULL,
        cooldown_until REAL NOT NULL, 
        PRIMARY KEY (user_id, ability)
    )""")
    conn.commit()
    print(f'🥳 Logged in as {bot.user} (ID: {bot.user.id})')
    print('------------------------------------------------')

@bot.command()
async def ping(ctx):
    """Responds with the bot's latency."""
    # ctx (context) contains info about the command invocation (user, channel, guild)
    await ctx.send(f'Pong! 🏓 Latency is {round(bot.latency * 1000)}ms')

@bot.command()
async def hello(ctx):
    """Greets the user who called the command."""
    await ctx.send(f'👋 Hello there, {ctx.author.display_name}!')
@bot.event
async def on_message(message):
    # This code runs every time a message is sent
    
    # 1. Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # 2. Check for a specific action/command
    if message.content.lower().strip() == "magic":
        await message.channel.send("Sous vodka ")
    elif message.content.lower().strip() == "zeo":
        await message.channel.send("Ze zuis ze chef")
    elif message.content.lower().strip() == "limule":
        rdm = random.randint(1,2)
        if rdm == 1:
            await message.channel.send("Viens rr tgm")
        if rdm == 2:
            await message.channel.send("CV: 19 ans chomeur")
    elif message.content.lower().strip() == "omar":
        await message.channel.send("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    elif message.content.lower().strip() == "cirzzox":
        rdm = random.randint(1,2)
        if rdm == 1:
            await message.channel.send("Actuellement en train de cultivée du coton")
        if rdm == 2:
            await message.channel.send("Afoumame le foutou")
    elif message.content.lower().strip() == "nizar":
        await message.channel.send("Nn j'ai pas 12 ans")
    elif message.content.lower().strip() == "ignir":
        await message.channel.send("Le grand singe")
    elif message.content.lower().strip() == "espada":
        await message.channel.send("Les goats")
    await bot.process_commands(message)

@bot.command(name='cd')
async def show_cooldowns(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    
    # ... (Database retrieval is the same) ...
    cursor.execute(
        "SELECT ability, cooldown_until FROM cooldowns WHERE user_id = ?", 
        (member.id,)
    )
    results = cursor.fetchall()
    
    # ... (No results check is the same) ...
    if not results:
        return await ctx.send(f"✅ {member.display_name} n'a pas encore de cooldown enregistré")

    current_time = datetime.now().timestamp()
    output_lines = []

    for ability_name, expiration_timestamp in results:
        MAX_USES_FOR_CHECK = 4
        if expiration_timestamp > current_time:
            status = f"**{ability_name.capitalize()}: ⏳ Pret a nouveau <t:{int(expiration_timestamp)}:R>**"
        elif int(expiration_timestamp) == 2 and ability_name.lower() == "arrow":
            uses_left = 3 - int(expiration_timestamp) 
            status = f"**{ability_name.capitalize()}: 🔄 {uses_left} use restant**"
        elif int(expiration_timestamp) == 2 and ability_name.lower() == "heal":
            uses_left = 3 - int(expiration_timestamp) 
            status = f"**{ability_name.capitalize()}: 🔄 {uses_left} use restant**"
        elif int(expiration_timestamp) == 2 and ability_name.lower() == "volcan":
            uses_left = 3 - int(expiration_timestamp) 
            status = f"**{ability_name.capitalize()}: 🔄 {uses_left} use restant**"
        if ability_name.lower() == "ombre" and expiration_timestamp >= 1 and expiration_timestamp < MAX_USES_FOR_CHECK:
            current_count = int(expiration_timestamp)
            uses_left = MAX_USES_FOR_CHECK - current_count
            status = f"**{ability_name.capitalize()}: 🔄 {uses_left} use restant{''if uses_left == 1 else 's'}**"
        else:
            status = f"**{ability_name.capitalize()}: ✅ Pret**"            
        # Add the generated status line to the list
        output_lines.append(status)

    conn.commit() # Commit the deletions of ready abilities

    # 3. Build and Send the Embed
    embed = discord.Embed(
        title=f"Cooldowns de {member.display_name}",
        description="\n".join(output_lines),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)
# Define the channel ID you want to restrict
@bot.command(name='reset')
async def reset_cooldown(ctx, ability_name: str):
    member = ctx.author
    ability_name = ability_name.lower()
    cursor.execute(
        "SELECT ability FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    result = cursor.fetchone()

    if result is None:
        return await ctx.send(
            f"⚠️ {ctx.author.display_name} tu n'as pas de cooldown enregistré pour **{ability_name}**."
        )
    cursor.execute(
        "DELETE FROM cooldowns WHERE user_id = ? AND ability = ?", 
        (member.id, ability_name)
    )
    conn.commit()
    await ctx.send(f"✅ Ton cooldown: **{ability_name}** a été reset.")
TARGET_CHANNEL_ID = 1429941293353795654
ROLE_ID = 1401636885033521183
@bot.command(name='setup_access_role')
@commands.has_permissions(administrator=True)
@commands.has_role(ROLE_ID) 
async def setup_access_role_command(ctx, role_name: str):
    """Creates a role and restricts a specific channel to only that role."""
    
    guild = ctx.guild
    
    # 1. Check Bot Permissions and Hierarchy
    if not guild.me.guild_permissions.manage_roles or not guild.me.guild_permissions.manage_channels:
        return await ctx.send("❌ I need both the 'Manage Roles' and 'Manage Channels' permissions.")

    # 2. CREATE THE NEW ROLE
    try:
        new_role = await guild.create_role(
            name=role_name,
            reason=f"Created by {ctx.author} to restrict channel access."
        )
        await ctx.send(f"✅ Role **{new_role.name}** created.")
    except discord.Forbidden:
        return await ctx.send("🚫 I cannot create that role. Check my role hierarchy.")

    # 3. GET THE TARGET CHANNEL
    target_channel = guild.get_channel(TARGET_CHANNEL_ID)
    if not target_channel:
        # This occurs if the ID is wrong or the channel was deleted
        return await ctx.send(f"⚠️ Error: Could not find channel with ID {TARGET_CHANNEL_ID}.")

    # 4. SET CHANNEL PERMISSION OVERWRITES

    # --- A. Restrict @everyone (Default Role) ---
    # Deny VIEW_CHANNEL permission for the default @everyone role.
    # This locks the channel for everyone who doesn't have a specific grant.
    everyone_role = guild.default_role
    try:
        await target_channel.set_permissions(
            everyone_role,
            view_channel=False
        )
    except discord.Forbidden:
        return await ctx.send("🚫 Failed to update @everyone permissions. Channel may be locked to me.")


    # --- B. Grant Access to the New Role ---
    # Explicitly allow VIEW_CHANNEL permission for the new role.
    try:
        await target_channel.set_permissions(
            new_role,
            view_channel=True,
            send_messages=True
        )
        await ctx.send(
            f"🔒 Channel **#{target_channel.name}** is now restricted. "
            f"Only members with the **{new_role.name}** role can see and access it."
        )
    except discord.Forbidden:
        await ctx.send("🚫 Failed to grant permissions to the new role. Check my channel permission overrides.")
ROLE_ID = 1401636885033521183
@bot.command(name='globalreset')
@commands.has_role(ROLE_ID) 
async def global_reset_cooldowns(ctx, ability_name: str = None):
    """
    Resets all cooldowns globally, or resets a specific ability globally.
    Usage: +globalreset [ability_name]
    Example 1: +globalreset (Resets EVERYTHING)
    Example 2: +globalreset mist (Resets only the 'mist' cooldown for all users)
    """
    
    if ability_name is None:
        # Case 1: No ability name provided -> Reset ALL cooldowns globally
        
        # DELETE ALL entries from the entire table
        cursor.execute("DELETE FROM cooldowns")
        conn.commit()

        await ctx.send(
            f"🚨 **GLOBAL RESET ** Tout les cooldowns on été reset par {ctx.author.display_name}."
        )
    
    else:
        # Case 2: An ability name is provided -> Reset that specific ability globally
        
        # Ensure the ability name is lowercase for consistency
        ability_name = ability_name.lower()
        
        # DELETE entries where the ability matches the provided name
        cursor.execute(
            "DELETE FROM cooldowns WHERE ability = ?",
            (ability_name,)
        )
        conn.commit()
        
        await ctx.send(
            f"⚡ **LOCAL RESET!** Le cooldown de :**{ability_name}** a été reset par {ctx.author.display_name}."
        )
@bot.command(name='addrole')
@commands.has_role(ROLE_ID)
@commands.has_permissions(manage_roles=True) 
async def add_access_role(ctx, member: discord.Member):
    """
    Adds the designated ACCESS_ROLE_ID to the specified member.
    Usage: +addrole @TargetMember
    """
    
    # 1. Check Bot Permissions
    if not ctx.guild.me.guild_permissions.manage_roles:
        return await ctx.send("❌ Pas la permission necessaire du bot")

    # 2. Find the Role Object by ID (More reliable than by name!)
    target_role = ctx.guild.get_role(ACCESS_ROLE_ID) # Use get_role() with the ID
    
    if not target_role:
        return await ctx.send(f"⚠️ Error: aucun role :  {ACCESS_ROLE_ID}.")

    # 3. Check Role Hierarchy (Same logic)
    if target_role >= ctx.guild.me.top_role:
        return await ctx.send("🚫 I cannot assign that role because it is higher or equal to my highest role in the hierarchy.")

    # 4. Add the Role
    try:
        await member.add_roles(target_role, reason=f" role donne par {ctx.author.name}")
        await ctx.send(f"✅ The **{target_role.name}** role a ete ajouter a {member.mention}.")

    except discord.Forbidden:
        await ctx.send("🚫 Permission error")
    except Exception as e:
        await ctx.send(f"Error : {e}")
# 6. Run the bot
if __name__ == '__main__':
    bot.run(TOKEN)