"""Render the profile's original notebook artwork using Pillow (no remote assets)."""
from pathlib import Path
import math, random
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'sketchbook'
OUT.mkdir(exist_ok=True)
S=2
INK='#243445'; BLUE='#3165a8'; PAPER='#fffdf6'; GRID='#e7e8df'; RED='#d4664e'
FONT='/System/Library/Fonts/Noteworthy.ttc'
BOLD='/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf'
rng=random.Random(1924)
THEME='dark'
DARK={
 '#243445':'#c7cfd8', '#3165a8':'#8daed0', '#e7e8df':'#202832',
 '#d4664e':'#ce927d', '#e9b4a4':'#48383d', '#e9e6dc':'#151c25',
 '#d6d2c8':'#303b48', '#dceba3':'#394b3c', '#e9efe9':'#19242d',
 '#f2b5a6':'#704b48', '#f5e6a5':'#514735', '#c5caca':'#34424f',
 '#f1d9a6':'#5a4d3c', '#f5d68c':'#b59767', '#f3c1b1':'#644b49',
 '#f0b4a6':'#704b48',
}
def color(value):
 return DARK.get(value,value) if THEME=='dark' else value


def canvas(w,h):
 im=Image.new('RGBA',(w*S,h*S),(0,0,0,0) if THEME=='dark' else PAPER)
 d=ImageDraw.Draw(im)
 for x in range(26,w,24):
  for y in range(18,h,24):
   d.ellipse((x*S,y*S,x*S+2,y*S+2),fill=color(GRID))
 return im

def line(im,pts,fill=INK,width=2,echo=False):
 d=ImageDraw.Draw(im)
 d.line([(int(x*S),int(y*S)) for x,y in pts], fill=color(fill),width=max(1,int(width*S)),joint='curve')
 if echo:
  d.line([(int((x+rng.uniform(-1.3,1.3))*S),int((y+rng.uniform(-1.3,1.3))*S)) for x,y in pts],fill=color(fill),width=max(1,int(S*.65)),joint='curve')

def curve(im,points,fill=INK,width=2,echo=False):
 # Cubic Bezier, sampled for clean pen strokes at export resolution.
 a,b,c,d=points
 pts=[]
 for i in range(65):
  t=i/64; u=1-t
  pts.append((u*u*u*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t*t*t*d[0],u*u*u*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t*t*t*d[1]))
 line(im,pts,fill,width,echo)

def ellipse(im,box,fill=None,outline=INK,width=2):
 d=ImageDraw.Draw(im); d.ellipse(tuple(int(v*S) for v in box),fill=color(fill),outline=color(outline),width=int(width*S))

def polygon(im,pts,fill):
 ImageDraw.Draw(im).polygon([(int(x*S),int(y*S)) for x,y in pts],fill=color(fill))

def text(im,xy,s,size=30,fill=INK,angle=0,bold=False):
 f=ImageFont.truetype(BOLD if bold else FONT,int(size*S))
 b=f.getbbox(s); pad=10*S
 stamp=Image.new('RGBA',(b[2]-b[0]+2*pad,b[3]-b[1]+2*pad))
 ImageDraw.Draw(stamp).text((pad-b[0],pad-b[1]),s,font=f,fill=color(fill))
 if angle:stamp=stamp.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True)
 im.alpha_composite(stamp,(int(xy[0]*S)-pad,int(xy[1]*S)-pad))

def arrow(im,pts,fill=BLUE):
 curve(im,pts,fill,2)
 x,y=pts[-1]; px,py=pts[-2]; a=math.atan2(y-py,x-px)
 for da in [-.55,.55]:line(im,[(x-12*math.cos(a+da),y-12*math.sin(a+da)),(x,y)],fill,2)

def star(im,x,y,r=9,fill=RED):
 for a in [0,math.pi/3,2*math.pi/3]:
  line(im,[(x-math.cos(a)*r,y-math.sin(a)*r),(x+math.cos(a)*r,y+math.sin(a)*r)],fill,2)

def save(im,name):
 suffix='-light.png' if THEME=='light' else '.png'
 im.save(OUT/(Path(name).stem+suffix),optimize=True)

def object_layer(w,h):
 return Image.new('RGBA',(w*S,h*S))

def place(im,obj,xy,angle=0):
 if angle:
  obj=obj.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True)
 im.alpha_composite(obj,(int(xy[0]*S),int(xy[1]*S)))

def rounded(im,box,r=8,fill=None,outline=INK,width=2):
 ImageDraw.Draw(im).rounded_rectangle(tuple(int(v*S) for v in box),radius=int(r*S),fill=color(fill),outline=color(outline),width=int(width*S))

def racket():
 ob=object_layer(108,284)
 # Thin double hoop and strings clipped to the interior ellipse.
 ellipse(ob,(8,4,100,143),fill='#e9efe9',outline=INK,width=2.5)
 strings=object_layer(108,284)
 for x in range(17,97,8):line(strings,[(x,9),(x,140)],BLUE,.65)
 for y in range(12,140,9):line(strings,[(12,y),(97,y)],BLUE,.65)
 mask=Image.new('L',ob.size);ImageDraw.Draw(mask).ellipse((14*S,10*S,94*S,137*S),fill=255)
 strings.putalpha(Image.composite(strings.getchannel('A'),Image.new('L',ob.size),mask))
 ob.alpha_composite(strings)
 ellipse(ob,(13,9,95,138),outline=BLUE,width=1)
 curve(ob,[(40,140),(46,150),(50,157),(53,162)],width=2)
 curve(ob,[(66,140),(60,150),(56,157),(53,162)],width=2)
 line(ob,[(53,158),(53,231)],INK,3)
 line(ob,[(54,162),(54,229)],BLUE,.7)
 rounded(ob,(47,229,60,279),4,fill='#394b3c' if THEME=='dark' else '#dceba3',width=1.5)
 for y in range(235,275,6):line(ob,[(48,y+3),(58,y)],BLUE,.8)
 line(ob,[(45,279),(62,279)],INK,3)
 for y in [24,44,64,84,104,122]:
  # Small frame grommets.
  inset=4 if y in [24,122] else 0
  line(ob,[(9+inset,y),(14+inset,y)],INK,1)
  line(ob,[(94-inset,y),(99-inset,y)],INK,1)
 return ob

def headphones():
 ob=object_layer(159,147)
 # Padded headband in nested curves; separate metal sliders and ear cushions.
 curve(ob,[(22,85),(12,-8),(147,-8),(137,85)],INK,7)
 curve(ob,[(30,82),(24,10),(135,10),(129,82)],INK,2)
 curve(ob,[(24,56),(39,4),(121,4),(135,55)],BLUE,1)
 for x,slant in [(23,-1),(132,1)]:
  line(ob,[(x,66),(x+slant*6,100)],BLUE,3)
  line(ob,[(x+slant*5,65),(x+slant*10,98)],INK,1)
 # Angled oval earcups with cushion, shell and seam detail.
 for x,ang in [(11,12),(113,-12)]:
  cup=object_layer(37,61)
  rounded(cup,(3,2,32,57),12,fill='#e9efe9',width=2)
  rounded(cup,(8,7,28,52),9,outline=BLUE,width=1)
  curve(cup,[(12,12),(8,23),(8,38),(12,48)],INK,.8)
  line(cup,[(30,18),(34,19),(34,40),(30,42)],INK,1)
  place(ob,cup,(x,76),ang)
 curve(ob,[(134,135),(144,148),(114,140),(106,145)],BLUE,1)
 return ob

def weight():
 ob=object_layer(174,86)
 # Cylindrical grip, end caps and shaded hexagonal plates with thickness.
 rounded(ob,(42,35,132,48),5,fill='#e9efe9',width=1.5)
 for x in range(57,120,5):
  line(ob,[(x,38),(x+5,45)],BLUE,.7)
  line(ob,[(x,45),(x+5,38)],BLUE,.7)
 for x in [29,126]:
  back=[(x+6,7),(x+25,7),(x+34,20),(x+34,63),(x+25,77),(x+6,77),(x-2,63),(x-2,20),(x+6,7)]
  polygon(ob,back,'#e9efe9');line(ob,back,INK,1.7)
  front=[(x,5),(x+18,5),(x+26,18),(x+26,61),(x+18,75),(x,75),(x-8,61),(x-8,18),(x,5)]
  polygon(ob,front,'#e9efe9');line(ob,front,INK,2)
  for a,b in [((x+18,5),(x+25,7)),((x+26,18),(x+34,20)),((x+26,61),(x+34,63)),((x+18,75),(x+25,77))]:line(ob,[a,b],BLUE,1)
  line(ob,[(x-3,21),(x-3,58)],BLUE,1)
  line(ob,[(x+3,13),(x+14,13)],BLUE,.8)
 # Small collars attach the plates to the grip.
 line(ob,[(53,32),(53,51)],INK,3);line(ob,[(123,32),(123,51)],INK,3)
 return ob

def drink():
 ob=object_layer(84,154)
 # Highball glass on an elliptical coaster, with a curved lip and double base.
 ellipse(ob,(7,132,76,151),fill='#e9efe9',outline=BLUE,width=1)
 polygon(ob,[(20,56),(63,56),(59,133),(25,133)],'#f1d9a6')
 ellipse(ob,(20,51,63,62),fill='#f1d9a6',outline=RED,width=1)
 curve(ob,[(15,25),(16,61),(20,109),(23,136)],INK,1.8)
 curve(ob,[(68,25),(66,63),(63,112),(61,136)],INK,1.8)
 ellipse(ob,(15,19,68,32),outline=INK,width=1.5)
 curve(ob,[(23,136),(34,143),(51,143),(61,136)],INK,2)
 curve(ob,[(25,131),(38,137),(49,137),(59,132)],BLUE,.8)
 line(ob,[(28,40),(31,114)],INK,.7)
 # Straw, ice and citrus garnish, without a label.
 line(ob,[(43,93),(55,7),(73,2)],BLUE,2)
 line(ob,[(47,93),(59,9),(74,5)],BLUE,.7)
 for pts in [[(25,41),(36,36),(44,48),(32,54),(25,41)],[(45,65),(57,68),(53,82),(41,77),(45,65)]]:
  polygon(ob,pts,'#e9efe9');line(ob,pts,INK,.8)
 ellipse(ob,(2,14,30,42),fill='#dceba3',outline=BLUE,width=1.2)
 ellipse(ob,(5,17,27,39),outline=BLUE,width=.6)
 for x,y in [(8,21),(23,20),(24,34),(9,35)]:line(ob,[(16,28),(x,y)],BLUE,.6)
 return ob

def render(theme):
 global THEME
 THEME=theme
 rng.seed(1924)
 im=canvas(1200,590)
 line(im,[(61,0),(60,590)],'#e9b4a4',1)
 for y in [68,210,352,494]:ellipse(im,(17,y,35,y+18),fill='#e9e6dc',outline='#d6d2c8',width=1)
 text(im,(103,40),"hi, i'm",36,angle=3)
 polygon(im,[(101,130),(491,119),(495,205),(103,216)],'#dceba3')
 text(im,(100,93),'arnav.',132,bold=True,angle=2)
 line(im,[(105,234),(265,239),(423,232),(491,235)],INK,2,True)
 text(im,(105,269),'Computer engineering student.',34)
 text(im,(105,320),'AI + backend development.',31)
 text(im,(105,404),'NMIMS / Mumbai',28,fill=BLUE,angle=-3)
 line(im,[(111,445),(202,448),(303,443)],BLUE,.8)
 text(im,(110,508),'github.com/andy1924',25,fill=BLUE)
 # A single composition: racket behind the laptop, small personal objects in front.
 place(im,racket(),(987,25),-17)
 place(im,drink(),(1090,241),-5)
 # Laptop body, hinge, deck, keyboard, and trackpad.
 polygon(im,[(731,127),(1080,137),(1069,346),(720,334)],'#e9efe9')
 line(im,[(731,127),(1080,137),(1069,346),(720,334),(731,127)],INK,2.6)
 line(im,[(741,139),(1068,149),(1058,331),(731,320),(741,139)],INK,1.3)
 line(im,[(725,338),(1066,350)],BLUE,2)
 ellipse(im,(901,133,904,136),fill=BLUE,outline=BLUE,width=1)
 polygon(im,[(720,334),(1069,346),(1102,390),(681,376)],'#e9efe9')
 line(im,[(720,334),(1069,346),(1102,390),(681,376),(720,334)],INK,2.3)
 line(im,[(681,376),(687,383),(1097,397),(1102,390)],INK,1.3)
 for row in range(3):
  for col in range(15):
   x=738+col*19-row*4;y=342+row*7+col*.035
   line(im,[(x,y),(x+13,y+.4)],BLUE,.65)
 line(im,[(851,367),(929,369),(935,380),(843,377),(851,367)],INK,.8)
 text(im,(767,178),'> python',28,fill=BLUE,angle=-2)
 text(im,(762,230),'building something',25,angle=-2)
 text(im,(759,275),'(or fixing it)',24,fill=RED,angle=-2)
 text(im,(769,64),'usually here',25,fill=BLUE,angle=-5)
 arrow(im,[(924,94),(971,75),(1008,88),(1002,129)])
 # A pair of objects overlap the main drawing instead of forming an icon row.
 place(im,headphones(),(1002,333),-15)
 place(im,weight(),(687,438),-17)
 text(im,(1009,518),'always on',23,fill=BLUE,angle=3)
 arrow(im,[(1084,515),(1064,486),(1096,487),(1114,473)])
 # A small landscape study, with the mountains and coast sharing a baseline.
 study=object_layer(245,103)
 line(study,[(7,56),(30,38),(43,42),(69,13),(85,31),(100,20),(132,57)],BLUE,1.6)
 line(study,[(58,29),(69,37),(76,28)],INK,.8)
 line(study,[(91,30),(99,36),(106,30)],INK,.8)
 curve(study,[(12,61),(53,54),(78,72),(120,62)],BLUE,1)
 curve(study,[(120,62),(157,51),(181,67),(217,54)],BLUE,1)
 for y in [72,81,90]:
  curve(study,[(97,y),(119,y-7),(132,y+7),(157,y-1)],BLUE,.9)
  curve(study,[(157,y-1),(178,y-8),(192,y+6),(219,y-3)],BLUE,.9)
 ellipse(study,(169,35,188,54),outline=RED,width=1)
 # Brief contour strokes read as rock and sand instead of a separate shell icon.
 line(study,[(29,82),(35,76),(42,79),(47,86)],INK,1)
 line(study,[(51,87),(57,83),(65,88)],INK,.8)
 for x,y in [(73,91),(28,94),(86,87)]:line(study,[(x,y),(x+4,y-1)],BLUE,.6)
 place(im,study,(407,467),4)
 text(im,(427,415),'or here',23,fill=BLUE,angle=5)
 arrow(im,[(509,429),(545,418),(565,446),(529,472)])
 # Small side-profile Formula 1 car: slick tires, low chassis, wings, halo.
 car=object_layer(150,63)
 # Body silhouette stays inside the tires, with a high rear wing and long nose.
 polygon(car,[(13,37),(39,33),(56,22),(77,22),(94,33),(122,40),(139,43),(139,48),(24,48)],'#e9efe9')
 line(car,[(13,37),(39,33),(56,22),(77,22),(94,33),(122,40),(139,43),(139,48),(24,48)],INK,1.3)
 polygon(car,[(44,36),(62,27),(78,29),(86,37),(44,36)],'#f3c1b1')
 line(car,[(44,36),(62,27),(78,29),(86,37)],RED,1)
 # Halo and cockpit.
 curve(car,[(66,25),(64,12),(83,13),(86,29)],INK,1.3)
 line(car,[(76,17),(77,28)],INK,1)
 ellipse(car,(68,24,77,32),fill=BLUE,outline=BLUE,width=1)
 # Rear and front aero elements.
 line(car,[(12,19),(31,19),(32,24),(13,24),(12,19)],BLUE,1.4)
 line(car,[(20,24),(21,37)],INK,1)
 line(car,[(130,47),(147,47),(147,51),(129,51)],BLUE,1.4)
 for x in [32,114]:
  ellipse(car,(x-12,35,x+12,59),fill='#e9efe9',outline=INK,width=2)
  ellipse(car,(x-7,40,x+7,54),outline=BLUE,width=.8)
  ellipse(car,(x-2,45,x+2,49),fill=INK,outline=INK,width=1)
 line(car,[(50,45),(94,45)],BLUE,.8)
 place(im,car,(519,46),7)
 # A few quick pen tests in the margin, with the central area left open.
 for pts in [[(500,165),(506,157)],[(513,161),(515,151)]]:
  line(im,pts,RED,1)
 curve(im,[(117,475),(128,478),(135,470),(145,475)],BLUE,.8)
 save(im,'header.png')

 rng.seed(1924)
 # The project sketches use actual objects from each project, rather than decorative badges.
 for key,title,subtitle in [('carrick','CARRICK','field report to schedule'),('udyog','UdyogSaarthi','from idea to business plan'),('graph','Graph-RAG','following the connections'),('cricket','The First Six Overs','1,227 IPL matches')]:
  im=canvas(560,300)
  end=min(530,48+ImageFont.truetype(BOLD,32*S).getlength(title)/S)
  polygon(im,[(22,28),(end,23),(end+1,56),(24,61)],'#f5e6a5' if key in ['carrick','cricket'] else '#dceba3')
  text(im,(28,24),title,32,bold=True,angle=1)
  text(im,(28,254),subtitle,24,fill=BLUE,angle=-1)
  if key=='carrick':
   line(im,[(87,218),(88,94),(240,102),(88,77),(88,94)],width=2.5,echo=True)
   line(im,[(110,98),(109,219),(87,197),(110,174),(88,153),(110,130),(88,108)],width=2)
   line(im,[(66,221),(129,221)],width=3)
   line(im,[(203,101),(202,155),(190,165),(201,175),(211,165)],width=2)
   line(im,[(292,109),(512,113),(508,215),(289,211),(292,109)],width=2,echo=True)
   for x in [325,363,401,439,477]:line(im,[(x,114),(x-2,210)],'#c5caca',1)
   for y in [142,175]:line(im,[(291,y),(508,y+3)],'#c5caca',1)
   line(im,[(305,128),(369,130)],BLUE,8);line(im,[(349,159),(425,161)],RED,8);line(im,[(401,192),(491,194)],BLUE,8)
   arrow(im,[(221,198),(242,222),(258,211),(279,186)])
  elif key=='udyog':
   line(im,[(145,217),(148,123),(389,128),(386,222),(145,217)],width=2.5,echo=True)
   polygon(im,[(132,124),(162,88),(380,94),(405,133)],'#f1d9a6')
   line(im,[(132,124),(162,88),(380,94),(405,133),(132,124)],width=2.5,echo=True)
   for x in range(158,393,30):line(im,[(x,128),(x-4,149)],BLUE,4)
   line(im,[(239,219),(240,163),(290,165),(289,221)],width=2)
   line(im,[(167,164),(213,166),(212,197),(166,196),(167,164)],width=2)
   line(im,[(312,166),(365,168),(363,201),(311,199),(312,166)],width=2)
   ellipse(im,(415,80,443,108),fill='#f5d68c',outline=RED)
   star(im,426,65,5,RED)
   curve(im,[(99,206),(62,167),(83,141),(111,174)],fill=BLUE,width=2)
  elif key=='graph':
   nodes=[(105,151),(191,98),(264,162),(351,105),(447,159),(351,219),(186,219)]
   edges=[(0,1),(0,6),(1,2),(1,3),(2,3),(2,5),(2,6),(3,4),(4,5),(5,6)]
   for a,b in edges:line(im,[nodes[a],nodes[b]],width=2,echo=True)
   for i,(x,y) in enumerate(nodes):ellipse(im,(x-15,y-15,x+15,y+15),fill=['#dceba3','#f3c1b1','#f5e6a5'][i%3],outline=INK)
   ellipse(im,(239,137,289,187),outline=BLUE,width=2)
   line(im,[(284,182),(307,205)],BLUE,5)
  elif key=='cricket':
   ellipse(im,(179,79,318,218),fill='#f0b4a6',outline=INK,width=2)
   curve(im,[(224,84),(294,119),(208,177),(281,211)],fill=RED,width=3,echo=True)
   for x,y in [(237,102),(245,123),(245,144),(246,165),(257,185),(268,201)]:line(im,[(x-7,y+3),(x+7,y-5)],RED,2)
   curve(im,[(169,185),(60,225),(89,92),(152,118)],fill=BLUE,width=2)
   arrow(im,[(352,184),(409,170),(409,117),(466,97)])
   text(im,(376,202),'6?',30,fill=BLUE,angle=-8)
  save(im,key+'.png')

for theme in ['dark','light']:
 render(theme)
print('Rendered dark and light notebook artwork to',OUT)
