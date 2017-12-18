from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 37
y = 5
z = -7
gift = mc.getBlock(x, y, z) 
if gift == 57:
    Block == 0
    mc.setBlock(36, 4, -5)
    mc.setBlock(36, 5, -5)

        
    
else:
    mc.postToChat("Place an offering on the pedestal.") 
