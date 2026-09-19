from PIL import Image, ImageDraw, ImageFilter
import math, random

S = 4                      # supersampling
W, H = 800*S, 450*S
NAVY_T, NAVY_B = (12, 36, 64), (6, 18, 36)
TRACE      = (27, 58, 99)
ICE        = (232, 241, 250)
STEEL      = (128, 176, 224)
ORANGE     = (215, 63, 9)
ORANGE_HI  = (255, 138, 61)

img = Image.new("RGB", (W, H), NAVY_B)
d = ImageDraw.Draw(img)

# --- background: diagonal gradient -------------------------------------------
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)],
           fill=tuple(int(NAVY_T[i] + (NAVY_B[i]-NAVY_T[i])*t) for i in range(3)))

# --- background circuit traces (left field, like the sibling course images) ----
random.seed(11)
tr = Image.new("RGB", (W, H)); td = ImageDraw.Draw(tr); td.rectangle([0,0,W,H], fill=(0,0,0))
for _ in range(34):
    x, y = random.randrange(0, int(W*0.55)), random.randrange(0, H)
    pts = [(x, y)]
    for _ in range(random.randint(2, 4)):
        step = random.randint(60, 220)*S//2
        if random.random() < .5: x += step * random.choice([-1, 1])
        else:                    y += step * random.choice([-1, 1])
        x, y = max(8*S, min(W-8*S, x)), max(8*S, min(H-8*S, y))
        pts.append((x, y))
    td.line(pts, fill=TRACE, width=2*S, joint="curve")
    r = 5*S
    td.ellipse([pts[-1][0]-r, pts[-1][1]-r, pts[-1][0]+r, pts[-1][1]+r], fill=TRACE)
img = Image.blend(img, Image.blend(img, tr, 0.0), 0.0)
img.paste(Image.composite(Image.new("RGB",(W,H),TRACE), img, tr.convert("L").point(lambda v: 255 if v>10 else 0)))
d = ImageDraw.Draw(img)

CX, CY = int(W*0.565), H//2
R_LOOP  = int(H*0.34)      # the agent loop
glow = Image.new("RGB", (W, H), (0,0,0)); gd = ImageDraw.Draw(glow)

# --- peripheral nodes: tool / memory / web / peer agent -----------------------
nodes = [(-146, 0.92, STEEL), (-72, 1.06, STEEL), (32, 1.04, ORANGE),
         (116, 1.02, STEEL), (178, 0.92, STEEL)]
placed = []
for ang, dist, col in nodes:
    a = math.radians(ang)
    nx = CX + math.cos(a) * R_LOOP * dist * 1.50
    ny = CY + math.sin(a) * R_LOOP * dist * 1.12
    placed.append((nx, ny, col))
    lw = 5*S if col is STEEL else 8*S
    d.line([(CX + math.cos(a)*R_LOOP, CY + math.sin(a)*R_LOOP), (nx, ny)],
           fill=col if col is ORANGE else TRACE, width=lw)
    if col is ORANGE:
        gd.line([(CX + math.cos(a)*R_LOOP, CY + math.sin(a)*R_LOOP), (nx, ny)],
                fill=ORANGE, width=lw)

# --- the agent loop ring ------------------------------------------------------
d.ellipse([CX-R_LOOP, CY-R_LOOP, CX+R_LOOP, CY+R_LOOP], outline=STEEL, width=4*S)
for a0 in (200, 320, 80):
    d.arc([CX-R_LOOP, CY-R_LOOP, CX+R_LOOP, CY+R_LOOP], a0, a0+58, fill=ICE, width=7*S)
    gd.arc([CX-R_LOOP, CY-R_LOOP, CX+R_LOOP, CY+R_LOOP], a0, a0+58, fill=ICE, width=7*S)
    ar = math.radians(a0+58)
    tipx, tipy = CX+math.cos(ar)*R_LOOP, CY+math.sin(ar)*R_LOOP
    per = ar + math.pi/2
    h = 15*S
    d.polygon([(tipx+math.cos(per)*h*1.5, tipy+math.sin(per)*h*1.5),
               (tipx+math.cos(ar-math.pi/2)*h + math.cos(ar)*0, tipy+math.sin(ar-math.pi/2)*h),
               (tipx-math.cos(ar-math.pi/2)*h, tipy-math.sin(ar-math.pi/2)*h)], fill=ICE)

# --- nodes on top -------------------------------------------------------------
for nx, ny, col in placed:
    r = 19*S if col is STEEL else 24*S
    d.ellipse([nx-r-4*S, ny-r-4*S, nx+r+4*S, ny+r+4*S], fill=NAVY_B)
    d.ellipse([nx-r, ny-r, nx+r, ny+r], fill=col)
    if col is ORANGE:
        gd.ellipse([nx-r, ny-r, nx+r, ny+r], fill=ORANGE_HI)
        for k in range(3):
            rr = r + (16+k*18)*S
            d.ellipse([nx-rr, ny-rr, nx+rr, ny+rr], outline=ORANGE, width=max(1, (3-k)*S))

# --- agent core ---------------------------------------------------------------
CR = int(R_LOOP*0.40)
d.ellipse([CX-CR-6*S, CY-CR-6*S, CX+CR+6*S, CY+CR+6*S], fill=NAVY_B)
d.ellipse([CX-CR, CY-CR, CX+CR, CY+CR], fill=ICE)
gd.ellipse([CX-CR, CY-CR, CX+CR, CY+CR], fill=ICE)
hx = [(CX+math.cos(math.radians(60*i-90))*CR*0.55, CY+math.sin(math.radians(60*i-90))*CR*0.55) for i in range(6)]
d.polygon(hx, fill=(12, 36, 64))

# --- composite glow -----------------------------------------------------------
img = Image.blend(img, Image.blend(img, glow.filter(ImageFilter.GaussianBlur(26*S)), 0.0), 0.0)
g = glow.filter(ImageFilter.GaussianBlur(22*S))
img = Image.eval(Image.merge("RGB", [
    Image.eval(c, lambda v: v) for c in img.split()]), lambda v: v)
img = Image.blend(img, Image.new("RGB",(W,H),(0,0,0)), 0.0)
base = img.copy()
img = Image.blend(base, Image.eval(base, lambda v: v), 0.0)
# additive-ish screen blend of the glow
px_b, px_g = base.load(), g.load()
for y in range(0, H, 1):
    for x in range(0, W, 1):
        b, gg = px_b[x, y], px_g[x, y]
        px_b[x, y] = (min(255, b[0]+gg[0]//3), min(255, b[1]+gg[1]//3), min(255, b[2]+gg[2]//3))

out = base.resize((800, 450), Image.LANCZOS)
out.save("/Users/sanghyun/Desktop/Websites/TRUE-Lab/assets/images/courses/course-sais.jpg",
         "JPEG", quality=92, optimize=True)
print("written 800x450")
