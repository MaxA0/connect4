from discord.ext import commands
import discord

class connect4(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.players = []
        self.row = []
        self.sented = []
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def startgame(self, ctx, member: discord.User):
      self.row.clear()
      for i in range(6):
          self.row.append(["x","x","x","x","x","x","x"])
      
      await self.output(ctx.channel)
      await ctx.send(f"{ctx.author.mention} you are player 1 and {member.mention} is player 2")
      self.players.append(ctx.author)
      self.players.append(member)
      self.go = 1
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      guild = discord.utils.find(lambda g : g.id == payload.guild_id, self.client.guilds)
      author = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if author in self.players:
        if str(payload.emoji) == "1️⃣":
          await self.turn(1)

        if str(payload.emoji) == "2️⃣":
          await self.turn(2)
        
        if str(payload.emoji) == "3️⃣":
          await self.turn(3)

        if str(payload.emoji) == "4️⃣":
          await self.turn(4)
        
        if str(payload.emoji) == "5️⃣":
          await self.turn(5)
        
        if str(payload.emoji) == "6️⃣":
          await self.turn(6)
        if str(payload.emoji) == "7️⃣":
          await self.turn(7)

    async def turn(self, column:int):
        column -=1
        empty = -1
        for i in range(6):
            if self.row[i][column] == "x":
                empty = i
                break
        if empty == -1:
            print("not valid!")
        else:
            if self.go == 1:
                self.row[empty][column] = "z"
                self.go = 0
            else:
                self.row[empty][column] = "y"
                self.go =1
        
        toprint = self.row[empty].copy()
        print(toprint)
        for i in range(len(toprint)):
          if toprint[i] == "x":
            toprint[i] = ":white_large_square:"
          if toprint[i] =="z":
            toprint[i] = ":red_square:"
          if toprint[i] == "y":
            toprint[i] = ":blue_square:"
        tosend = " ".join(str(x) for x in toprint)
        await self.sented[empty].edit(content=f"{tosend}")
        


        ##await self.output(message.channel)
        check = await self.checkw()
        if check != None:
            if check == "z":
                check = self.players[0].name
            else:
                check = self.players[1].name
            await self.sented[empty].channel.send(f"player {check} won!")

    async def checkw(self):
        checks = [self.diagleft, self.diagright, self.horwin, self.verwin]
        for i in range(len(checks)):
            if await checks[i]() != None:
                return await checks[i]()
        return None
        
    async def horwin(self):
        for i in range(len(self.row)):
            z=0
            y=0
            for j in range(len(self.row[i])):
                if self.row[i][j] == "z":
                    z+=1
                    y = 0
                elif self.row[i][j] == "y":
                    y+=1
                    z=0
                if z==4:
                    return("z")
                if y==4:
                    return("y")
        return None

    async def verwin(self):
        for i in range(len(self.row[0])):
            z = 0
            y = 0
            for j in range(len(self.row)):
                if self.row[j][i] == "z":
                    z+=1
                    y =0
                elif self.row[j][i] =="y":
                    y+=1
                if z==4:
                    return("z")
                if y==4:
                    return("y")
        return None


    async def diagright(self):
        for z in range(3):
            y = z
            for i in range(len(self.row[0])):
                x = i
                keyi = 1
                start = self.row[y][x]
                
                if (start == "x"):
                    continue
                while True: 
                    try:
                        if self.row[y+1][x+1] == start:
                            keyi+=1
                            print(keyi)
                            print(x,y)
                        x+=1
                        y+=1
                        
                        if ((keyi == 4) and (start != "x")):
                            return start
                    except:
                        break
                    
    
    async def diagleft(self):
        for z in range(3):
            y=z
            for i in range(len(self.row[0])-1, -1, -1):
                x = i
                keyi = 1
                start = self.row[y][x]
                if (start == "x"):
                    continue
                while True: 
                    try:
                        if self.row[y+1][x-1] == start:
                            keyi+=1
                        else:
                            start = self.row[y+1][x-1]
                        x-=1
                        y+=1
                        if ((keyi == 4) and (start != "x")):
                            return start
                    except:
                        break
        
    async def output(self,chan: discord.TextChannel):
        for i in range(6):
            tosend = self.row[5-i].copy()
            for i in range(len(tosend)):
              if tosend[i] == "x":
                tosend[i] = ":white_large_square:"
            ("x", ":white_large_square:")
            tosend = " ".join(str(x) for x in tosend)
            sent = await chan.send(tosend)
            self.sented.append(sent)
        self.sented.reverse()
        await sent.add_reaction("1️⃣")
        await sent.add_reaction("2️⃣")
        await sent.add_reaction("3️⃣")
        await sent.add_reaction("4️⃣")
        await sent.add_reaction("5️⃣")
        await sent.add_reaction("6️⃣")
        await sent.add_reaction("7️⃣")
        print(self.row)

def setup(client):
    client.add_cog(connect4(client))
