# coding: utf-8
import sys
convertop = "convert %s -resize x48 +dither -map woolp.png tiny.png" % (sys.argv[1])
import os
os.system(convertop)

from PIL import Image
im=Image.open('woolp.png')
imp=im.convert("RGB")
colors=["white","light_gray","gray",
"black","brown","red","orange","yellow",
"lime","green","cyan","light_blue",
"blue","purple","magenta","pink"]
lookup={}
for i in range(16):
    lookup[imp.getpixel((i,0))] = colors[i]+'_wool'
    lookup[imp.getpixel((i,1))] = colors[i]+'_wool'
    lookup[imp.getpixel((i,2))] = colors[i]+'_wool'

imml = Image.open('tiny.png')
imm=imml.convert("RGB")
items = []
for c in range(imm.width):
    for r in range(imm.height-1,-1,-1):
        items.append([c+1,imm.height - r,lookup[imm.getpixel((c,r))]])

pages = []
for triplet in items:
    pages.append('"/setblock ~%d ~%d ~-5 minecraft:%s"' % (15-triplet[0], triplet[1], triplet[2]))

chunks = []
running = 0
temp = []
for page in pages:
    running += len(page)
    temp.append(page)
    if running > 30000:
        chunks.append(temp)
        running = 0
        temp = []
chunks.append(temp)

for chunk in chunks:
    cmd = '/give @p minecraft:writable_book{pages:[%s]}' % (",".join(chunk))
    print(cmd)
