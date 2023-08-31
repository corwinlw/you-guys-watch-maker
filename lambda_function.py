from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io
import shutil

outfilename = f'ygw_{"star wars shows"}.gif'
# shutil.copy('ygw_blank.gif', outfilename)
im = Image.open('ygw_blank.gif')

fnt = ImageFont.truetype("impact.ttf", 20)

personyouwatch = "STAR WARS SHOWS"
xoff = 180 - (len(personyouwatch) * 5)

frames = []
for frame in ImageSequence.Iterator(im):
	frame = frame.convert('RGBA')
	
	d = ImageDraw.Draw(frame)
	d.text((105,140), "YOU GUYS AREN'T", align="center", font=fnt, fill=(255,255,255))
	d.text((xoff,160), "BLAMING JOHN", align="center", font=fnt, fill=(255,255,255))
	d.text((140,180), "MOSTLY?", align="center", font=fnt, fill=(255,255,255))
	 
	del d
	
	frames.append(frame)

my_bytes = io.BytesIO()
frames[0].save(my_bytes, format="GIF", save_all=True, append_images=frames[1:])

with open(outfilename, "wb") as f:
    f.write(my_bytes.getbuffer())