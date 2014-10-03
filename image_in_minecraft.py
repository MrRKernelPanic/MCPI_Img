from mcpi import minecraft
import Image
import sys
import math

mc = minecraft.Minecraft.create()
mc.postToChat("Hello World")

mcPalette = [ 
    221,221,221, # White 
    219,125,62,  # Orange 
    179,80,188,  # Magenta 
    107,138,201, # Light Blue 
    177,166,39,  # Yellow 
    65,174,56,   # Lime Green 
    208,132,153, # Pink 
    64,64,64,    # Dark Grey 
    154,161,161, # Light Grey 
    46,110,137,  # Cyan 
    126,61,181,  # Purple 
    46,56,141,   # Blue 
    79,50,31,    # Brown 
    53,70,27,    # Green 
    150,52,48,   # Red 
    25,22,22,    # Black 
] 

mcPalette.extend((0,0,0) * 256 - len(mcPalette)/3)
mcImagePal = Image.new("P", (1,1)) 
mcImagePal.putpalette(mcPalette)

mcImage = Image.open("dude.gif").convert('RGB') 
width = mcImage.size[0] 
height = mcImage.size[1] 
ratio = height / float(width) 
maxsize = 64

if width > height: 
    rwidth = maxsize 
    rheight = int(rwidth * ratio) 
else: 
    rheight = maxsize 
    rwidth = int(rheight / ratio)

#mcImage = mcImage.convert("RGB") 
mcImage = mcImage.quantize(palette = mcImagePal) 
mcImage = mcImage.resize((rwidth,rheight))

playerPos = mc.player.getPos() 
x = playerPos.x 
y = playerPos.y 
z = playerPos.z

for j in range(rwidth): 
    for k in range(rheight): 
	pixel = mcImage.getpixel((j,k)) 
        if pixel < 16:
		mc.setBlock(j + x + 5, rheight - k + y, z, 35, pixel)
