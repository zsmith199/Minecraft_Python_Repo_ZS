from mpi.minecraft import Minecraft

mc = Minecraft.create ()

x = -4.6
y = 12
z = -1.3

mc.player.setPos(x, y+100, z)
