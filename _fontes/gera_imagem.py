# -*- coding: utf-8 -*-
import sys, random
def build(path, W, H, fsize, G, baseline, topy, boty):
    random.seed(1912)
    CORES=["#E8452C","#FBBA00","#2DD4BF","#1F6FEB","#E0318C","#5C7A47","#8B5CF6","#F97316",
           "#0EA5E9","#DC2626","#16A34A","#EAB308","#DB2777","#14B8A6","#4F46E5","#F43F5E",
           "#65A30D","#0891B2","#C2410C","#7C3AED","#FF6B6B","#1D4ED8"]
    def tile(x,y,s):
        c=random.choice(CORES); c2=random.choice(CORES); t=random.random()
        if t<.28: return f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*.46:.1f}" fill="{c}"/>'
        if t<.44: return (f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*.46:.1f}" fill="{c}"/>'
                          f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*.24:.1f}" fill="#F5F2EC"/>')
        if t<.60: return f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s*.22:.1f}" fill="{c}"/>'
        if t<.74: return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" fill="{c}"/>'
                          f'<rect x="{x:.1f}" y="{y+s*.38:.1f}" width="{s:.1f}" height="{s*.24:.1f}" fill="{c2}"/>')
        if t<.86: return f'<rect x="{x:.1f}" y="{y+s*.22:.1f}" width="{s:.1f}" height="{s*.56:.1f}" rx="{s*.28:.1f}" fill="{c}"/>'
        if t<.94: return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" fill="{c}"/>'
                          f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*.19:.1f}" fill="#F5F2EC"/>')
        return (f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*.46:.1f}" fill="{c}"/>'
                f'<rect x="{x:.1f}" y="{y+s*.4:.1f}" width="{s:.1f}" height="{s*.2:.1f}" fill="{c2}"/>')
    m=[]; y=-G
    while y<H+G:
        x=-G
        while x<W+G:
            m.append(tile(x+random.uniform(-2,2), y+random.uniform(-2,2), G*random.uniform(.76,.99)))
            x+=G
        y+=G
    m="".join(m)
    html=f"""<!doctype html><meta charset="utf-8">
<style>
 html,body{{margin:0;padding:0;background:#F5F2EC}}
 .c{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#F5F2EC}}
 .rule{{position:absolute;left:0;top:0;width:100%;height:14px;background:#2DD4BF}}
 .top{{position:absolute;left:58px;top:{topy}px;font-family:"Courier New",monospace;font-size:19px;
      letter-spacing:.22em;text-transform:uppercase;color:#0E0D0B}}
 .meta{{position:absolute;left:58px;right:58px;bottom:{boty}px;display:flex;justify-content:space-between;
       align-items:flex-end;font-family:"Courier New",monospace;font-size:19px;letter-spacing:.13em;
       text-transform:uppercase;color:#0E0D0B}}
 .meta .r{{text-align:right;color:#5D574E;font-size:15px;line-height:1.65;letter-spacing:.1em}}
</style>
<div class="c">
 <div class="rule"></div>
 <div class="top">Toolkit de collabs</div>
 <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
  <defs><clipPath id="L">
   <text x="{W/2}" y="{baseline}" text-anchor="middle" font-family="Impact,'Arial Black',sans-serif"
         font-size="{fsize}" letter-spacing="-10">COLLAB</text>
  </clipPath></defs>
  <g clip-path="url(#L)">
   <rect x="0" y="0" width="{W}" height="{H}" fill="#12100E"/>{m}
  </g>
 </svg>
 <div class="meta">
  <div>douglasbocalao.github.io/collab</div>
  <div class="r">Dissertação de mestrado<br>MPA FGV EAESP · 2026</div>
 </div>
</div>"""
    open(path,"w",encoding="utf-8").write(html)

build(sys.argv[1], 1080, 1080, 338, 19, 660, 54, 54)     # feed
build(sys.argv[2], 1200, 630, 268, 16, 408, 42, 38)      # preview de link
print("ok")
