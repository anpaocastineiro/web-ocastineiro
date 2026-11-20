#!/usr/bin/env python3
"""Exportación de identidade da ANPA O Castiñeiro para Canva gratuíto.

Emprega exclusivamente os orixinais do repositorio: non emprega xeración de
imaxe nin altera a marca. Os PNG de maior tamaño son ampliacións de orixinais
rasterizados, non ficheiros vectoriais.
"""
from pathlib import Path
import shutil
import zipfile
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ROOT / "identidade-canva"
OUT.mkdir(exist_ok=True)
GREEN = (15, 61, 50)
WHITE = (255, 255, 255)
CREAM = (247, 239, 226)
OCHRE = (235, 178, 60)
FILES = []

def open_rgba(name):
    return Image.open(ASSETS/name).convert("RGBA")

def trim(image, threshold=20, border=14):
    image = image.convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda v: 255 if v >= threshold else 0).getbbox()
    if not bbox:
        return image
    x0,y0,x1,y1 = bbox
    x0,y0 = max(0,x0-border),max(0,y0-border)
    x1,y1 = min(image.width,x1+border),min(image.height,y1+border)
    return image.crop((x0,y0,x1,y1))

def scale_width(img, width):
    height = max(1,round(width*img.height/img.width))
    return img.resize((width,height), Image.Resampling.LANCZOS)

def tint(im, color):
    result=Image.new("RGBA",im.size,color+(0,))
    result.putalpha(im.getchannel("A"))
    return result

def canvas_square(img, size=1600, fraction=0.78):
    canvas=Image.new("RGBA",(size,size),(0,0,0,0))
    avail=int(size*fraction)
    ratio=min(avail/img.width,avail/img.height)
    w,h=round(img.width*ratio),round(img.height*ratio)
    resized=img.resize((w,h),Image.Resampling.LANCZOS)
    canvas.alpha_composite(resized,((size-w)//2,(size-h)//2))
    return canvas

def save(im, filename):
    im.save(OUT/filename,"PNG",compress_level=9,optimize=True)
    FILES.append(filename)

horizontal=trim(open_rgba("logo.webp"), threshold=20, border=12)
favicon=trim(open_rgba("favicon.png"), threshold=22, border=4)
mark=trim(open_rgba("castineiro.webp"), threshold=20, border=8)
# O primeiro orixinal é o logotipo completo co seu lettering e texturas.
h=scale_width(horizontal,2400)
save(h,"01_logo_horizontal_cor_alpha.png")
save(tint(h,GREEN),"02_logo_horizontal_verde_alpha.png")
save(tint(h,WHITE),"03_logo_horizontal_branco_alpha.png")

# O favicon é a versión a toda cor e separada da tipografía do símbolo.
ic=scale_width(favicon,1400)
save(ic,"04_isotipo_cor_alpha.png")
hi=scale_width(mark,1600)
save(tint(hi,GREEN),"05_isotipo_verde_alpha.png")
save(tint(hi,WHITE),"06_isotipo_branco_alpha.png")

# Versión cadrada con marxes, cómoda para redes sociais e para Canva.
save(canvas_square(favicon,1600,.80),"07_isotipo_cadrado_alpha.png")
save(canvas_square(tint(mark,WHITE),1600,.80),"08_isotipo_cadrado_branco_alpha.png")
square_bg=Image.new("RGBA",(1600,1600),GREEN+(255,))
white_symbol=canvas_square(tint(mark,WHITE),1600,.73)
square_bg.alpha_composite(white_symbol)
save(square_bg,"09_avatar_fondo_verde.png")

# A icona orixinal conservase sen ampliar, para uso en tamaños pequenos.
save(favicon,"10_isotipo_cor_tamano_orixinal_alpha.png")

# Identidade horizontal centrada nun lenzo amplo, útil para cabeceiras.
banner=Image.new("RGBA",(2800,1200),(0,0,0,0))
ratio=min(2400/horizontal.width,800/horizontal.height)
bw,bh=round(horizontal.width*ratio),round(horizontal.height*ratio)
centered=horizontal.resize((bw,bh),Image.Resampling.LANCZOS)
banner.alpha_composite(centered,((2800-bw)//2,(1200-bh)//2))
save(banner,"11_logo_cabeceira_2800x1200_alpha.png")

# Os ficheiros WebP e PNG de partida viaxan tamén no paquete.
ORIGINALS=[("logo.webp","ORIXINAL_logo.webp"),
           ("castineiro.webp","ORIXINAL_isotipo_monocromo.webp"),
           ("favicon.png","ORIXINAL_isotipo_color_pequeno.png")]
for source,target in ORIGINALS:
    shutil.copy2(ASSETS/source, OUT/target)
    FILES.append(target)

instructions = """O CASTIÑEIRO · PAQUETE DE IDENTIDADE PARA CANVA GRATUÍTO
========================================================

Todos os PNG co sufixo _alpha teñen transparencia real.
Podes subilos a Canva gratuíto en «Subidos / Cargar ficheiros».

01  Logo horizontal en cor, para fondos claros.
02  Logo horizontal verde, unha tinta.
03  Logo horizontal branco, para fondos escuros.
04  Isotipo en cor, sen o nome.
05  Isotipo verde, sen o nome.
06  Isotipo branco, sen o nome.
07  Isotipo en cor cadrado e centrado, fondo transparente.
08  Isotipo branco cadrado e centrado, fondo transparente.
09  Avatar cadrado sobre verde (sen transparencia), para perfís.
10  Isotipo en cor no tamaño de partida, sen interpolación.
11  Logo horizontal centrado en lenzo 2800×1200 transparente.

O ficheiro ZIP inclúe tamén os tres orixinais extraídos da web.

IMPORTANTE SOBRE A RESOLUCIÓN:
Os orixinais da web son rasterizados (WebP e PNG). Os ficheiros
ampliados teñen máis píxeles para facilitar o traballo en Canva,
pero non son vectores nin gañan o detalle dun SVG mestre.
O isotipo a cor procede do favicon pequeno da web; para pezas
moi grandes recoméndase recuperar o orixinal vectorial se existe.

SOBRE O USO:
- Fondos claros: logo ou isotipo en cor.
- Fondos escuros: versión branca.
- Perfil de redes: 09 ou 07.
- Non deformes a proporción nin superpoñas texto sobre a marca.
- Non son necesarios Canva Pro nin plugins para importar PNG.
"""
(OUT/"LEME_CANVA.txt").write_text(instructions,encoding="utf-8")
FILES.append("LEME_CANVA.txt")

# Vista previa para comprobar con xente da ANPA; fondo branco e verde.
thumbs=[
("Logo · cor", "01_logo_horizontal_cor_alpha.png",CREAM),
("Logo · verde", "02_logo_horizontal_verde_alpha.png",CREAM),
("Logo · branco", "03_logo_horizontal_branco_alpha.png",GREEN),
("Isotipo · cor","04_isotipo_cor_alpha.png",CREAM),
("Isotipo · verde","05_isotipo_verde_alpha.png",CREAM),
("Isotipo · branco","06_isotipo_branco_alpha.png",GREEN),
("Cadrado · alfa","07_isotipo_cadrado_alpha.png",CREAM),
("Cadrado · branco","08_isotipo_cadrado_branco_alpha.png",GREEN),
("Avatar","09_avatar_fondo_verde.png",CREAM),
("Icona · orixinal","10_isotipo_cor_tamano_orixinal_alpha.png",CREAM),
("Cabeceira","11_logo_cabeceira_2800x1200_alpha.png",CREAM),
]
W,H=1500,1200
contact=Image.new("RGB",(W,H),(247,239,226))
draw=ImageDraw.Draw(contact)
wcell,hcell=500,300
for index,(label,filename,bg) in enumerate(thumbs):
    col,row=index%3,index//3
    x,y=col*wcell,row*hcell
    draw.rectangle([x+8,y+8,x+wcell-8,y+hcell-8],fill=bg,outline=(197,203,188),width=2)
    a=Image.open(OUT/filename).convert("RGBA")
    maxw,maxh=wcell-42,hcell-72
    m=min(maxw/a.width,maxh/a.height)
    a=a.resize((round(a.width*m),round(a.height*m)),Image.Resampling.LANCZOS)
    contact.paste(a,(x+(wcell-a.width)//2,y+20+(maxh-a.height)//2),a)
    font_color=WHITE if bg==GREEN else GREEN
    draw.text((x+24,y+hcell-39),label,fill=font_color)
contact.save(OUT/"VISTA_PREVIA.png",optimize=True)
FILES.append("VISTA_PREVIA.png")
zip_path=OUT/"O_Castineiro_Paquete_Canva.zip"
with zipfile.ZipFile(zip_path,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for file in FILES:z.write(OUT/file,arcname=file)

for n in ["logo.webp","castineiro.webp","favicon.png"]:
    i=Image.open(ASSETS/n).convert("RGBA")
    alpha=i.getchannel("A")
    print(f"ORIXINAL {n}: {i.size}, alpha_minmax={alpha.getextrema()}, bbox20={alpha.point(lambda v: 255 if v>=20 else 0).getbbox()}")
print("Creáronse",len(FILES),"ficheiros e",zip_path)
