#!/usr/bin/env python3
"""Original conceptual voice AI explainer. No customer voice, app interface or live demo."""
from PIL import Image, ImageDraw, ImageFont
import pathlib,math,subprocess,sys
FPS=24; BG=(5,16,28); PANEL=(15,37,54); CYAN=(101,233,228); WHITE=(238,249,252); MUTED=(188,210,222); GREEN=(122,230,170)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
OUT=pathlib.Path("assets/media/g19"); OUT.mkdir(parents=True,exist_ok=True)
SCENES=[
("RANDEVU","KESİNLEŞTİ Mİ?","Bir konuşmayı anlamak, randevuyu onaylamak değildir."),
("01 / RANDEVU","“Yarın 10.00 uygun mu?”","Takvim doğrulanmadıysa saat sözü verilmez."),
("02 / YÖNLENDİRME","“Destek ekibiyle görüşebilir miyim?”","Talep sınıflandırılır. Yetkili ekibe devir önerilir."),
("03 / İNSAN DEVRİ","“Hassas bir sorum var.”","Belirsizlikte bot durur; sorumlu insan devralır."),
("ONAY SINIRI","Önce doğrulama. Sonra karar.","Canlı çağrı, müşteri kaydı ve otomatik rezervasyon yok."),
("SYNAPSE AUTOMATE","Karar hakkı sizde.","Yöntemi ve kapsamı inceleyin: synapseautomate.github.io")]
def fontfit(t,maxw,size,bold=False):
 path=BOLD if bold else FONT
 while size>13:
  f=ImageFont.truetype(path,size)
  if ImageDraw.Draw(Image.new("RGB",(2,2))).textbbox((0,0),t,font=f)[2]<maxw:return f
  size-=2
 return ImageFont.truetype(path,size)
def getlogo(vertical):
 path=pathlib.Path("assets/brand/synapse-logo-clean.png")
 if not path.exists():raise RuntimeError("Official site brand asset missing. Stop.")
 im=Image.open(path).convert("RGBA")
 # preserve original aspect ratio; use original alpha and no shape editing
 im.thumbnail((235 if vertical else 205,85 if vertical else 69),Image.Resampling.LANCZOS)
 return im
def make(vertical):
 W,H=(720,1280) if vertical else (1280,720)
 duration=(30 if vertical else 36);unit=duration/6
 logo=getlogo(vertical)
 dest=OUT/("synapse-voice-human-handoff-vertical.mp4" if vertical else "synapse-voice-human-handoff-horizontal.mp4")
 command=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo","-pixel_format","rgb24","-video_size",f"{W}x{H}","-framerate",str(FPS),"-i","pipe:0","-f","lavfi","-i","anullsrc=channel_layout=stereo:sample_rate=48000","-shortest","-c:v","libx264","-preset","veryfast","-crf","22","-pix_fmt","yuv420p","-r",str(FPS),"-profile:v","high","-level","4.1","-movflags","+faststart","-c:a","aac","-b:a","96k","-t",str(duration),str(dest)]
 p=subprocess.Popen(command,stdin=subprocess.PIPE)
 for frame in range(duration*FPS):
  t=frame/FPS;scene=min(5,int(t/unit));local=(t-scene*unit)/unit
  eyebrow,title,explain=SCENES[scene]
  im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im);margin=44 if vertical else 72;right=W-margin
  d.rectangle((0,0,W,7),fill=CYAN)
  im.paste(logo,(margin,22 if vertical else 17),logo)
  d.line((margin,122 if vertical else 94,right,122 if vertical else 94),fill=(37,68,85),width=2)
  d.text((right-205,91 if vertical else 66),"KAVRAMSAL ANLATIM",fill=CYAN,font=ImageFont.truetype(BOLD,14 if vertical else 12))
  top=180 if vertical else 137
  d.text((margin,top),eyebrow,fill=CYAN,font=fontfit(eyebrow,W-2*margin,31 if vertical else 29,True))
  headfont=fontfit(title,W-2*margin,54 if vertical else 55,True)
  lines=[title]
  if vertical and d.textbbox((0,0),title,font=headfont)[2]>W-2*margin:
   words=title.split();lines=[];line=""
   for word in words:
    nexttext=(line+" "+word).strip()
    if d.textbbox((0,0),nexttext,font=headfont)[2]>W-2*margin and line:
     lines.append(line);line=word
    else:line=nexttext
   if line:lines.append(line)
  for j,line in enumerate(lines[:3]):d.text((margin,top+59+j*80 if vertical else top+54+j*62),line,font=headfont,fill=WHITE)
  small=fontfit(explain,W-2*margin,25 if vertical else 26)
  rows=[explain]
  if vertical and d.textbbox((0,0),explain,font=small)[2]>W-2*margin:
   rows=[];line=""
   for word in explain.split():
    v=(line+" "+word).strip()
    if d.textbbox((0,0),v,font=small)[2]>W-2*margin and line:rows.append(line);line=word
    else:line=v
   if line:rows.append(line)
  for j,row in enumerate(rows[:3]):d.text((margin,(top+300 if vertical else top+154)+j*42),row,fill=MUTED,font=small)
  py=668 if vertical else 395;ph=300 if vertical else 205
  d.rounded_rectangle((margin,py,right,py+ph),radius=24,fill=PANEL,outline=(51,97,111),width=2)
  cx=margin+90;cy=py+(90 if vertical else 85);rx=right-87
  d.line((cx,cy,rx,cy),fill=(60,109,121),width=7)
  progress=max(0,min(1,local*1.23));d.line((cx,cy,cx+(rx-cx)*progress,cy),fill=CYAN,width=8)
  for i,x in enumerate([cx,(cx+rx)//2,rx]):
   active=progress>=i/2-.02;rad=25 if active else 20
   d.ellipse((x-rad,cy-rad,x+rad,cy+rad),fill=CYAN if active else (56,90,108),outline=WHITE if active else (88,125,141),width=2)
   d.ellipse((x-7,cy-7,x+7,cy+7),fill=BG if active else WHITE)
   label=["TALEP","KONTROL","İNSAN ONAYI"][i]
   f=fontfit(label,160,17 if vertical else 16,True)
   bounds=d.textbbox((0,0),label,font=f);d.text((x-(bounds[2]-bounds[0])/2,cy+38),label,font=f,fill=WHITE)
  d.text((margin+20,py+ph-56),"Kesinleştirme yalnız yetkili teyidiyle.",font=fontfit("Kesinleştirme yalnız yetkili teyidiyle.",W-2*margin-40,20 if vertical else 21),fill=GREEN)
  fy=H-140 if vertical else H-74
  d.line((margin,fy-24,right,fy-24),fill=(43,73,87),width=2)
  flag="SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL"
  d.text((margin,fy),flag,font=fontfit(flag,W-2*margin,18 if vertical else 19,True),fill=WHITE)
  d.text((margin,fy+(36 if vertical else 29)),"Gerçek telefon görüşmesi veya çalışan ürün ekranı değildir.",font=fontfit("Gerçek telefon görüşmesi veya çalışan ürün ekranı değildir.",W-2*margin,17 if vertical else 15),fill=MUTED)
  try:p.stdin.write(im.tobytes())
  except BrokenPipeError:break
 p.stdin.close();rc=p.wait()
 if rc!=0:raise RuntimeError(f"ffmpeg exit {rc}")
 print(dest,dest.stat().st_size)
 return dest
if __name__=="__main__":
 make(False);make(True)
