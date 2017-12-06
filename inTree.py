from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y - 1, z)
inTree = blockType == 18
mc.postToChat("You are in a tree: " + str (inTree)) 




