import os,re
from PIL import Image
dir = input('请输入需要设置启动图的路径：')
list_land = []
list_port = []
list_mipmap = []
for root,dirs,files in os.walk(dir):
        for file in files:
            if(re.match('.*drawable-land.*',root)):
                list_land.append(os.path.join(root,file))
            if (re.match('.*drawable-port.*', root)):
                list_port.append(os.path.join(root, file))
            if (re.match('.*ic_launcher_foreground\.png', file)):
                list_mipmap.append(os.path.join(root, file))
for i in range(len(list_land)):
    im = Image.open(list_land[i])
    im = Image.new('RGBA', im.size, color=0xffffffff)
    icon = Image.open(list_mipmap[i])
    im.paste(icon, box=(int(im.size[0] / 2 - icon.size[0] / 2), int(im.size[1] / 2 - icon.size[1] / 2)))
    im.save(list_land[i])
for i in range(len(list_port)):
    im = Image.open(list_port[i])
    im = Image.new('RGBA', im.size, color=0xffffffff)
    icon = Image.open(list_mipmap[i])
    im.paste(icon, box=(int(im.size[0] / 2 - icon.size[0] / 2), int(im.size[1] / 2 - icon.size[1] / 2)))
    im.save(list_port[i])
im = Image.open(r'%s\drawable\splash.png'%dir)
im = Image.new('RGBA', im.size, color=0xffffffff)
icon = Image.open(list_mipmap[0])
im.paste(icon, box=(int(im.size[0] / 2 - icon.size[0] / 2), int(im.size[1] / 2 - icon.size[1] / 2)))
im.save(r'%s\drawable\splash.png'%dir)