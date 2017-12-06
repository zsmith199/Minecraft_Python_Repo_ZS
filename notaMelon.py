from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 62
y = 3
z = 83

melon = 103
block = mc.getBlock(x, y, z)

noMelon = block == 0

mc.postToChat("You need to get some food: " + str(noMelon))
