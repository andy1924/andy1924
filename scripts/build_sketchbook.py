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
 arrow(im,[(335,429),(410,470),(443,416),(465,391)])
 text(im,(110,508),'github.com/andy1924',25,fill=BLUE)
 # A notebook sketch of a laptop, with deliberately imperfect edges.
 polygon(im,[(725,95),(1091,108),(1080,338),(715,323)],'#e9efe9')
 line(im,[(713,94),(1097,103),(1083,340),(706,326),(713,94)],width=3,echo=True)
 line(im,[(730,116),(1077,124),(1066,313),(723,302),(730,116)],width=2,echo=True)
 line(im,[(706,326),(675,354),(1098,371),(1083,340)],width=3,echo=True)
 line(im,[(677,355),(686,369),(1089,386),(1098,371)],width=2)
 line(im,[(833,338),(820,352),(949,359),(945,342)],width=1.5)
 text(im,(759,150),'> python',29,fill=BLUE,angle=-2)
 text(im,(755,204),'building something',26,angle=-2)
 text(im,(751,252),'(or fixing it)',25,fill=RED,angle=-2)
 text(im,(793,41),'usually here',25,fill=BLUE,angle=-4)
 arrow(im,[(956,65),(1005,60),(1035,70),(1042,96)])
 # Headphones.
 curve(im,[(1002,466),(987,392),(1132,388),(1123,474)],width=4,echo=True)
 curve(im,[(1017,463),(1008,414),(1114,413),(1108,469)],width=2)
 line(im,[(1002,454),(991,476),(999,509),(1017,507),(1022,475),(1013,456)],width=3,echo=True)
 line(im,[(1112,456),(1128,460),(1135,492),(1120,507),(1108,497),(1105,472)],width=3,echo=True)
 curve(im,[(1125,507),(1134,550),(1071,535),(1079,559)],width=2)
 text(im,(766,512),'Daniel Caesar',25,fill=BLUE,angle=2)
 arrow(im,[(926,526),(965,538),(980,520),(995,507)])
 # Cricket ball, seam and a loose path.
 ellipse(im,(587,445,650,508),fill='#f2b5a6',outline=INK,width=2)
 curve(im,[(601,448),(633,457),(604,492),(637,504)],fill=RED,width=2,echo=True)
 for x,y in [(606,457),(611,468),(615,480),(623,491)]:line(im,[(x-4,y),(x+3,y-3)],RED,1)
 curve(im,[(518,494),(461,542),(581,561),(585,509)],fill=BLUE,width=1.5)
 star(im,540,112);star(im,1118,73,10,BLUE);star(im,695,438,7)
 save(im,'header.png')

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
