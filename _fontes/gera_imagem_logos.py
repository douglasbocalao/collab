# -*- coding: utf-8 -*-
import sys, json, io, random

def lum(h):
    h=h.lstrip("#"); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def escurece(h,k=.55):
    h=h.lstrip("#"); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
    return "#%02X%02X%02X"%(int(r*k),int(g*k),int(b*k))

def build(path, W, H, fsize, baseline, cell, topy, boty, logos):
    random.seed(7)
    FUNDO="#12100E"; LETRA="#F5F2EC"
    pool=[]; 
    while len(pool) < 400:
        bloco=logos[:]; random.shuffle(bloco); pool+=bloco
    k=0; marcas=[]
    y=-cell*0.3
    while y < H+cell:
        x=-cell*0.3
        while x < W+cell:
            L=pool[k%len(pool)]; k+=1
            cor=L["hex"]
            if lum(cor) > .72: cor=escurece(cor,.62)          # claro demais sobre o creme
            s=cell*0.70/24.0
            ox=x+(cell-cell*0.70)/2; oy=y+(cell-cell*0.70)/2
            marcas.append(f'<g transform="translate({ox:.1f},{oy:.1f}) scale({s:.4f})">'
                          f'<path d="{L["d"]}" fill="{cor}"/></g>')
            x+=cell
        y+=cell
    marcas="".join(marcas)
    html=f"""<!doctype html><meta charset="utf-8">
<style>
 html,body{{margin:0;padding:0;background:{FUNDO}}}
 .c{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:{FUNDO}}}
 .rule{{position:absolute;left:0;top:0;width:100%;height:14px;background:#2DD4BF}}
 .top{{position:absolute;left:58px;top:{topy}px;font-family:"Courier New",monospace;font-size:19px;
      letter-spacing:.22em;text-transform:uppercase;color:#F5F2EC}}
 .meta{{position:absolute;left:58px;right:58px;bottom:{boty}px;display:flex;justify-content:space-between;
       align-items:flex-end;font-family:"Courier New",monospace;font-size:19px;letter-spacing:.13em;
       text-transform:uppercase;color:#F5F2EC}}
 .meta .r{{text-align:right;color:#A6A099;font-size:15px;line-height:1.65;letter-spacing:.1em}}
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
   <rect x="0" y="0" width="{W}" height="{H}" fill="{LETRA}"/>{marcas}
  </g>
 </svg>
 <div class="meta">
  <div>douglasbocalao.github.io/collab</div>
  <div class="r">Dissertação de mestrado<br>MPA FGV EAESP · 2026</div>
 </div>
</div>"""
    open(path,"w",encoding="utf-8").write(html)

logos=json.load(io.open(sys.argv[3],encoding="utf-8"))
build(sys.argv[1], 1080, 1080, 338, 660, 46, 54, 54, logos)
build(sys.argv[2], 1200, 630, 268, 408, 38, 42, 38, logos)
print("html gerado com", len(logos), "marcas")
