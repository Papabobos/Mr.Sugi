#!/usr/bin/env python3
import struct, zlib, base64

def make_png(size):
    w = h = size
    # Draw a simple icon: dark bg + "MS" pixel art
    pixels = []
    for y in range(h):
        row = []
        for x in range(w):
            # Background
            r,g,b,a = 5,2,20,255
            # Blue circle bg
            cx,cy = w//2,h//2
            dist = ((x-cx)**2+(y-cy)**2)**0.5
            if dist < w*0.46:
                r,g,b = 26,82,160
            if dist < w*0.42:
                r,g,b = 30,74,144
            # Hat (dark blue top)
            hx1,hx2 = int(w*0.28),int(w*0.72)
            hy1,hy2 = int(h*0.12),int(h*0.30)
            if hx1<=x<=hx2 and hy1<=y<=hy2:
                r,g,b = 10,48,112
            # Hat brim
            bx1,bx2 = int(w*0.22),int(w*0.78)
            by1,by2 = int(h*0.27),int(h*0.34)
            if bx1<=x<=bx2 and by1<=y<=by2:
                r,g,b = 26,74,144
            # Head (skin)
            fx1,fx2 = int(w*0.30),int(w*0.70)
            fy1,fy2 = int(h*0.30),int(h*0.55)
            if fx1<=x<=fx2 and fy1<=y<=fy2:
                r,g,b = 232,184,120
            # Eyes
            ex1,ex2 = int(w*0.36),int(w*0.44)
            ex3,ex4 = int(w*0.56),int(w*0.64)
            ey1,ey2 = int(h*0.37),int(h*0.44)
            if (ex1<=x<=ex2 or ex3<=x<=ex4) and ey1<=y<=ey2:
                r,g,b = 26,16,32
            # Body (shirt blue)
            sx1,sx2 = int(w*0.24),int(w*0.76)
            sy1,sy2 = int(h*0.55),int(h*0.78)
            if sx1<=x<=sx2 and sy1<=y<=sy2:
                r,g,b = 26,80,144
            # Name tag
            ntx1,ntx2 = int(w*0.44),int(w*0.60)
            nty1,nty2 = int(h*0.60),int(h*0.67)
            if ntx1<=x<=ntx2 and nty1<=y<=nty2:
                r,g,b = 255,255,255
            row.extend([r,g,b,a])
        pixels.append(bytes(row))
    
    def chunk(tag, data):
        c = zlib.crc32(tag+data) & 0xffffffff
        return struct.pack('>I',len(data))+tag+data+struct.pack('>I',c)
    
    raw = b''
    for row in pixels:
        raw += b'\x00' + row
    compressed = zlib.compress(raw, 9)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    png += chunk(b'IDAT', compressed)
    png += chunk(b'IEND', b'')
    return png

for size in [192, 512]:
    with open(f'icon-{size}.png','wb') as f:
        f.write(make_png(size))
    print(f'icon-{size}.png created')
