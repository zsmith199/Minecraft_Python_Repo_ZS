from mcpi.minecraft import Minecraft

mc = Minecraft.create()

wood = 17

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, wood)

