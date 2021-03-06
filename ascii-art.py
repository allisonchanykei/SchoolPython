#create ascii art from picture
#usage: python program.py	image.jpg	art.txt
import Image, sys

img=Image.open(sys.argv[1],'r')
w,h=img.size #returns a tuple
w=int((120.0/h)*w) #120 vertical lines for 2 point font in gedit
h=120
w=2*w #widen pic since most fonts are about twice as high as wide
img=img.resize((w,h),Image.BILINEAR) #or BICUBIC
img=img.convert('L') #greyscale
scale = ['@','#','A','%','S','<','*','+',':','.']

f=open(sys.argv[2],'w')
for y in range(h):
	for x in range(w):
		lum=img.getpixel((x,y)) #int form 0-255
		step=int(256/(len(scale)-1)) #int(256/9)=28
		index=lum//step
		f.write(scale[index])
	f.write('\n')
	
f.close()
