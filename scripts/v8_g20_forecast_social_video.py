"""Day20 independent original forecast uncertainty explainers; not a product interface."""
from PIL import Image,ImageDraw,ImageFont
import pathlib,subprocess,math,json
R=pathlib.Path("assets/media/g20");R.mkdir(parents=True,exist_ok=True)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
NAVY=(4,17,29);WHITE=(234,246,253);MUTED=(182,204,217);CYAN=(88,230,214);GOLD=(240,194,130)
def fit(d,t,width,size,bold=True):
 while size>16:
  f=ImageFont.truetype(BOLD if bold else FONT,size)
  if d.textbbox((0,0),t,font=f)[2]<width:return f
  size-=2
 return ImageFont.truetype(BOLD if bold else FONT,size)
def draw_wrap(d,t,x,y,width,size,lineh,color):
 font=fit(d,t,width,size,False)
 words=t.split();rows=[];line=""
 for word in words:
  cand=(line+" "+word).strip()
  if line and d.textbbox((0,0),cand,font=font)[2]>width:rows.append(line);line=word
  else:line=cand
 if line:rows.append(line)
 for i,row in enumerate(rows[:3]):d.text((x,y+i*lineh),row,font=font,fill=color)
def run(vertical):
 W,H=(1080,1920) if vertical else (1920,1080)
 fps=12;seconds=30 if vertical else 36;scene_secs=6
 scenes=[
 ("GÖRÜLEN SATIŞ","TALEP Mİ?","Satışın sıfır olduğu gün, stokta yokluk olup olmadığına bakın."),
 ("VERİ KONTROLÜ","EKSİK DÖNEM","Tarihli kayıt ve ürün kimliği olmadan tahmin güvencesi verilmez."),
 ("BAĞLAM KONTROLÜ","KAMPANYA","Özel dönemlerin etkisini temel talepten ayırmayı planlayın."),
 ("KARŞILAŞTIRMA","REFERANS MODEL","Basit yöntemle zaman içinde, gelecek görmeyen test gerekir."),
 ("BELİRSİZLİK","TEK SAYI DEĞİL","Aralık ve sınır raporlanır, sipariş kararı insanda kalır."),
 ("SYNAPSE AUTOMATE","KARAR İNSANDA","Kavramsal yöntem ve ön koşulları inceleyin.")
 ]
 logo_file=pathlib.Path("assets/brand/synapse-logo-clean.png")
 if not logo_file.exists():raise RuntimeError("Verified source brand logo file missing")
 logo=Image.open(logo_file).convert("RGBA");logo.thumbnail((290 if not vertical else 300,90),Image.Resampling.LANCZOS)
 p=R/("SYNAPSE_G20_TALEP_TAHMINI_DIKEY.mp4" if vertical else "SYNAPSE_G20_TALEP_TAHMINI_YATAY.mp4")
 cmd=["ffmpeg","-loglevel","error","-y","-f","rawvideo","-pixel_format","rgb24","-video_size",f"{W}x{H}","-framerate",str(fps),"-i","pipe:0","-f","lavfi","-i","anullsrc=channel_layout=stereo:sample_rate=44100","-shortest","-c:v","libx264","-preset","veryfast","-crf","22","-pix_fmt","yuv420p","-r","24","-c:a","aac","-b:a","96k","-t",str(seconds),"-movflags","+faststart",str(p)]
 process=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 mx=78 if vertical else 98
 # Uniform high-contrast master with carefully measured inset safe zones.
 base=Image.new("RGB",(W,H),NAVY);gd=ImageDraw.Draw(base)
 for y in range(H):
  k=y/H;gd.line((0,y,W,y),fill=(5,17+int(12*k),29+int(15*k)))
 for f in range(seconds*fps):
  t=f/fps;i=min(5,int(t/6));phase=(t%6)/6
  eyebrow,title,copy=scenes[i]
  im=base.copy();d=ImageDraw.Draw(im);im.paste(logo,(mx,28 if not vertical else 76),logo)
  d=ImageDraw.Draw(im);rule=150 if not vertical else 239;d.line((mx,rule,W-mx,rule),fill=(52,96,113),width=3)
  ytitle=207 if not vertical else 335
  d.text((mx,ytitle),eyebrow,font=fit(d,eyebrow,W-2*mx,30),fill=CYAN)
  hsize=98 if not vertical else 87
  d.text((mx,ytitle+69),title,font=fit(d,title,W-2*mx,hsize),fill=WHITE)
  draw_wrap(d,copy,mx,ytitle+(202 if vertical else 198),W-2*mx,32 if vertical else 34,52,MUTED)
  # Interpolated light paths imply possible trajectories, not measured numeric forecasts.
  y0=int(H*.67 if vertical else H*.7)
  panel=(mx,int(H*.49 if vertical else H*.53),W-mx,int(H*.81 if vertical else H*.85))
  d.rounded_rectangle(panel,radius=28,fill=(10,35,49),outline=(54,106,117),width=3)
  start=mx+34;end=W-mx-34
  for n in [1,2,3]:
   gy=panel[1]+n*(panel[3]-panel[1])//4
   d.line((start,gy,end,gy),fill=(35,67,77),width=2)
  for n in [1,2,3]:
   gx=start+n*(end-start)//4
   d.line((gx,panel[1]+30,gx,panel[3]-30),fill=(32,65,76),width=2)
  main=[];upper=[];lower=[]
  for q in range(0,101):
   ratio=q/100
   x=start+(end-start)*ratio
   mid=panel[1]+(panel[3]-panel[1])*.52+math.sin(ratio*7+t*.45)*((panel[3]-panel[1])*.08)
   spread=max(0,ratio-.34)**1.55*(panel[3]-panel[1])*.75
   main.append((int(x),int(mid)))
   upper.append((int(x),int(mid-spread)));lower.append((int(x),int(mid+spread)))
  d.line(upper,fill=GOLD,width=6);d.line(lower,fill=GOLD,width=6);d.line(main,fill=CYAN,width=10)
  dot=main[min(100,int(100*phase))];d.ellipse((dot[0]-11,dot[1]-11,dot[0]+11,dot[1]+11),fill=WHITE,outline=CYAN,width=4)
  # Presentational disclosure on every frame; this cannot be mistaken for live application evidence.
  foot=int(H*.867 if vertical else H*.895)
  d.line((mx,foot-22,W-mx,foot-22),fill=(51,91,107),width=2)
  label="SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL"
  if vertical:
   d.text((mx,foot), "SENTETİK ÖRNEK /",font=fit(d,"SENTETİK ÖRNEK /",W-2*mx,33),fill=WHITE)
   d.text((mx,foot+46),"GERÇEK MÜŞTERİ VERİSİ DEĞİL",font=fit(d,"GERÇEK MÜŞTERİ VERİSİ DEĞİL",W-2*mx,33),fill=WHITE)
  else:d.text((mx,foot),label,font=fit(d,label,W-2*mx,41),fill=WHITE)
  d.rectangle((0,0,int(W*(f+1)/(seconds*fps)),8),fill=CYAN)
  try:process.stdin.write(im.tobytes())
  except BrokenPipeError:raise RuntimeError("Video encoder broken pipe")
 process.stdin.close()
 if process.wait():raise RuntimeError("ffmpeg enc failed")
 s=[]
 for j,(ey,ti,cap) in enumerate(scenes[:seconds//scene_secs]):
  def stamp(v):return f"00:00:{v:02d},000"
  a=j*6;h=(j+1)*6
  s.append(f"{j+1}\n{stamp(a)} --> {stamp(h)}\n{ey}. {ti}. {cap}\n")
 p.with_suffix(".srt").write_text("\n".join(s),encoding="utf-8")
 print("VIDEO",str(p),p.stat().st_size)
if __name__=="__main__":run(False);run(True)
