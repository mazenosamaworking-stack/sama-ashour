import random, os
random.seed(7)
A='public/assets/'
def save(n,s): open(A+n,'w').write(s)
def stars(w,h,n):
    return ''.join(f'<circle cx="{random.uniform(0,w):.0f}" cy="{random.uniform(0,h):.0f}" r="{random.choice([.5,.7,1,1.3])}" fill="#fff" opacity="{random.uniform(.3,1):.2f}"/>' for _ in range(n))
def svg(w,h,body,defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"><defs>{defs}</defs>{body}</svg>'
SPACE='<linearGradient id="sp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#030816"/><stop offset="1" stop-color="#0a1a44"/></linearGradient>'
EARTH_DEFS='''<radialGradient id="eg" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#3f9bff"/><stop offset=".45" stop-color="#0f4cc0"/><stop offset="1" stop-color="#030f3a"/></radialGradient>
<radialGradient id="atm" cx=".5" cy=".5" r=".5"><stop offset=".92" stop-color="#4fc3ff" stop-opacity="0"/><stop offset=".985" stop-color="#6fd4ff" stop-opacity=".9"/><stop offset="1" stop-color="#6fd4ff" stop-opacity="0"/></radialGradient>'''
def clouds(cx,cy,r,n):
    o=''
    for _ in range(n):
        import math
        a=random.uniform(0,6.28);d=random.uniform(0,r*.85)
        x=cx+d*math.cos(a);y=cy+d*math.sin(a)
        o+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{random.uniform(15,70):.0f}" ry="{random.uniform(4,12):.0f}" fill="#fff" opacity="{random.uniform(.08,.3):.2f}" transform="rotate({random.uniform(-30,30):.0f} {x:.0f} {y:.0f})"/>'
    return o
def lights(cx,cy,r,n):
    import math
    o=''
    for _ in range(n):
        a=random.uniform(0,6.28);d=random.uniform(0,r*.9)
        o+=f'<circle cx="{cx+d*math.cos(a):.0f}" cy="{cy+d*math.sin(a):.0f}" r="{random.uniform(.6,1.6):.1f}" fill="#ffb347" opacity="{random.uniform(.4,.9):.2f}"/>'
    return o
# hero
W,H=1340,250
body=f'<rect width="{W}" height="{H}" fill="url(#sp)"/>{stars(W,H,220)}'
body+=f'<circle cx="650" cy="560" r="520" fill="url(#atm)"/><clipPath id="c"><circle cx="650" cy="560" r="500"/></clipPath><circle cx="650" cy="560" r="500" fill="url(#eg)"/><g clip-path="url(#c)">{clouds(650,560,500,160)}{lights(650,560,500,120)}</g>'
body+='<rect width="1340" height="250" fill="url(#fade)"/>'
fade='<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#030816" stop-opacity=".85"/><stop offset=".5" stop-color="#030816" stop-opacity="0"/></linearGradient>'
save('hero-earth.svg',svg(W,H,body,SPACE+EARTH_DEFS+fade))
# astronaut
astro='''<g transform="rotate(-18 100 130)"><rect x="55" y="70" width="50" height="95" rx="18" fill="#cfd6e4"/><rect x="62" y="80" width="76" height="90" rx="26" fill="#f2f5fb"/><rect x="82" y="105" width="38" height="22" rx="4" fill="#2b5fd9"/><circle cx="100" cy="52" r="34" fill="#eef2f9"/><ellipse cx="104" cy="54" rx="24" ry="20" fill="url(#vz)"/><path d="M135 100 L178 70 L186 86 L148 120Z" fill="#e6ebf5"/><circle cx="184" cy="76" r="9" fill="#9aa6bd"/><path d="M70 100 L24 128 L32 146 L80 124Z" fill="#e6ebf5"/><circle cx="28" cy="138" r="9" fill="#9aa6bd"/><path d="M80 165 L58 232 L84 240 L104 172Z" fill="#e6ebf5"/><path d="M114 168 L130 230 L156 222 L136 162Z" fill="#dfe5f1"/><rect x="52" y="230" width="38" height="16" rx="6" fill="#8e9ab3"/><rect x="124" y="222" width="38" height="16" rx="6" fill="#8e9ab3"/></g>'''
save('astronaut.svg',svg(200,260,astro,'<radialGradient id="vz" cx=".3" cy=".3"><stop offset="0" stop-color="#5aa7ff"/><stop offset="1" stop-color="#06122e"/></radialGradient>').replace('slice','meet'))
# ISS group
def panel(x,y,w,h,r=0):
    return f'<g transform="rotate({r} {x+w/2} {y+h/2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#pn)" stroke="#9fc2ff" stroke-width="1.5"/><path d="M{x} {y+h/2}H{x+w}" stroke="#9fc2ff" stroke-width=".8"/>' + ''.join(f'<path d="M{x+w*i/6} {y}V{y+h}" stroke="#9fc2ff" stroke-width=".8"/>' for i in range(1,6))+'</g>'
def iss():
    g=''
    g+='<rect x="60" y="165" width="480" height="8" fill="#9aa4b8"/>'
    for (x,y,w,h,r) in [(40,20,150,80,-8),(40,215,150,80,-8),(410,20,150,80,-8),(410,215,150,80,-8)]:
        g+=panel(x,y,w,h,r)
    g+='<rect x="230" y="130" width="140" height="80" rx="10" fill="#d9dde6"/><rect x="250" y="118" width="100" height="22" rx="6" fill="#bfc6d6"/><rect x="250" y="200" width="100" height="22" rx="6" fill="#bfc6d6"/><rect x="170" y="148" width="64" height="44" rx="8" fill="#e9ecf2"/><rect x="366" y="148" width="64" height="44" rx="8" fill="#e9ecf2"/><circle cx="300" cy="170" r="12" fill="#6b7a99"/><rect x="290" y="60" width="20" height="60" fill="#aab3c7"/><rect x="290" y="220" width="20" height="60" fill="#aab3c7"/><rect x="460" y="155" width="50" height="30" rx="6" fill="#f2f4f8"/>'
    return g
PN='<pattern id="pn" width="25" height="40" patternUnits="userSpaceOnUse"><rect width="25" height="40" fill="#1a49b8"/><rect x="1" y="1" width="23" height="38" fill="#2a6bff" opacity=".7"/></pattern>'
save('iss.svg',svg(600,340,f'<rect width="600" height="340" fill="url(#sp)"/>{stars(600,340,60)}<g transform="rotate(-12 300 170)">{iss()}</g>',SPACE+PN))
save('iss-clear.svg',svg(600,340,f'<g transform="rotate(-12 300 170)">{iss()}</g>',PN))
# scenes
def moonscene(sky,ground1,ground2,dome,extra=''):
    d=f'<linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ground1}"/><stop offset="1" stop-color="{ground2}"/></linearGradient><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky[0]}"/><stop offset="1" stop-color="{sky[1]}"/></linearGradient>'
    b=f'<rect width="800" height="200" fill="url(#sk)"/>{stars(800,90,70) if sky[0]!="#c9703a" else ""}<path d="M0 95 Q200 80 400 92 T800 88 V200H0Z" fill="url(#gr)"/>'
    for i,x in enumerate([90,300,520,700]):
        s=1.3-.15*(i%2)
        b+=f'<g transform="translate({x} {108+ (i%2)*8}) scale({s})"><ellipse cx="0" cy="26" rx="62" ry="8" fill="#000" opacity=".3"/><path d="M-55 24 A55 50 0 0 1 55 24Z" fill="{dome}" stroke="#fff" stroke-opacity=".6"/><path d="M-30 24 V-8 M0 24 V-24 M30 24 V-8" stroke="#fff" stroke-opacity=".4"/><rect x="-18" y="8" width="36" height="16" fill="#8892a6"/><circle cx="20" cy="-10" r="3" fill="#ffd86b"/></g>'
    for _ in range(60):
        x=random.uniform(0,800);y=random.uniform(125,195)
        b+=f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{random.uniform(2,10):.0f}" ry="{random.uniform(1,4):.0f}" fill="#000" opacity=".25"/>'
    return svg(800,200,b+extra,d)
save('env-lunar.svg',moonscene(('#02040c','#0b1330'),'#8d919c','#3c4050','#dfe6f5'))
save('env-mars.svg',moonscene(('#c9703a','#f0b183'),'#b4562f','#5c2a17','#e9d7cc'))
save('mars-habitat.svg',moonscene(('#c9703a','#f0b183'),'#b4562f','#5c2a17','#e9d7cc'))
save('env-rover.svg',moonscene(('#02040c','#0b1330'),'#8d919c','#3c4050','#dfe6f5','<g transform="translate(330 130)"><rect x="0" y="20" width="140" height="30" rx="6" fill="#d5d9e2"/><rect x="40" y="0" width="60" height="26" rx="4" fill="#9aa6bd"/><rect x="100" y="-30" width="4" height="34" fill="#aab"/><circle cx="20" cy="56" r="15" fill="#222"/><circle cx="70" cy="56" r="15" fill="#222"/><circle cx="120" cy="56" r="15" fill="#222"/></g>'))
save('env-iss.svg',svg(800,200,f'<rect width="800" height="200" fill="url(#sp)"/>{stars(800,200,120)}<circle cx="400" cy="420" r="300" fill="url(#eg)"/><g transform="translate(250 15) scale(.55)">{iss()}</g>',SPACE+EARTH_DEFS+PN))
save('env-spacecraft.svg',svg(800,200,f'<rect width="800" height="200" fill="url(#sp)"/>{stars(800,200,120)}<g transform="translate(180 30)"><path d="M0 70 L120 40 L420 40 L440 70 L420 100 L120 100Z" fill="#dfe4ee"/><rect x="420" y="50" width="120" height="40" rx="10" fill="#b9c1d3"/><circle cx="150" cy="70" r="14" fill="#2a6bff"/><circle cx="210" cy="70" r="14" fill="#2a6bff"/><path d="M200 40 L260 -10 L300 -10 L280 40Z M200 100 L260 150 L300 150 L280 100Z" fill="#1a49b8"/><path d="M540 55 L610 40 L610 100 L540 85Z" fill="#ff8a30"/></g>',SPACE))
# fire
def fire(n,c1,c2,seed):
    random.seed(seed)
    b='<rect width="130" height="100" fill="#0a0a12"/><rect y="78" width="130" height="22" fill="#25262e"/>'
    for i in range(7):
        x=random.uniform(30,100);h=random.uniform(40,75);w=random.uniform(14,28)
        b+=f'<path d="M{x} 82 C{x-w} {82-h*.4} {x-w*.3} {82-h*.7} {x} {82-h} C{x+w*.2} {82-h*.6} {x+w} {82-h*.4} {x} 82Z" fill="url(#f{i%2})" opacity=".85"/>'
    return svg(130,100,b+'<circle cx="65" cy="70" r="30" fill="url(#gl)"/>',f'<linearGradient id="f0" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}" stop-opacity=".2"/></linearGradient><linearGradient id="f1" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#fff2b0"/><stop offset=".5" stop-color="{c1}"/><stop offset="1" stop-color="{c2}" stop-opacity=".1"/></linearGradient><radialGradient id="gl"><stop offset="0" stop-color="{c1}" stop-opacity=".6"/><stop offset="1" stop-color="{c1}" stop-opacity="0"/></radialGradient>')
save('fire-saffire.svg',fire(1,'#ff8a1f','#ff3b1f',1));save('fire-flex.svg',fire(2,'#ff6a1f','#7a3cff',2));save('fire-bass.svg',fire(3,'#ffb020','#ff2a1a',3))
save('fire-viz.svg',svg(140,140,'<rect width="140" height="140" fill="#06102a"/><circle cx="70" cy="75" r="60" fill="none" stroke="#2a6bff" stroke-opacity=".5"/><circle cx="70" cy="75" r="50" fill="url(#o)"/><path d="M70 30 C50 55 40 70 55 95 C62 108 78 108 85 95 C100 72 85 55 70 30Z" fill="#ffd36b" opacity=".9"/><path d="M70 55 C60 72 58 85 66 96 C72 100 78 96 78 88 C80 76 74 68 70 55Z" fill="#fff"/>','<radialGradient id="o"><stop offset="0" stop-color="#ff7a1a"/><stop offset=".6" stop-color="#c4281c"/><stop offset="1" stop-color="#2a0c4a"/></radialGradient>'))
# sidebar planet, earth sphere, bottom earth
save('side-planet.svg',svg(148,360,f'<rect width="148" height="360" fill="#030816"/>{stars(148,360,40)}<circle cx="30" cy="330" r="150" fill="url(#atm)"/><circle cx="30" cy="330" r="135" fill="url(#eg)"/><clipPath id="c"><circle cx="30" cy="330" r="135"/></clipPath><g clip-path="url(#c)">{clouds(30,330,135,40)}{lights(30,330,135,30)}</g>',EARTH_DEFS))
save('earth-sphere.svg',svg(200,200,f'<rect width="200" height="200" fill="#030816"/><circle cx="100" cy="100" r="95" fill="url(#atm)"/><circle cx="100" cy="100" r="80" fill="url(#eg)"/><clipPath id="c"><circle cx="100" cy="100" r="80"/></clipPath><g clip-path="url(#c)"><path d="M60 60 Q90 40 110 70 Q90 100 70 110 Q50 90 60 60Z M120 110 Q150 100 155 130 Q140 155 120 140Z" fill="#2c8a5c" opacity=".7"/>{clouds(100,100,80,25)}</g><circle cx="120" cy="85" r="4" fill="#ff3b30"/><circle cx="85" cy="120" r="3" fill="#ff9f1c"/><circle cx="140" cy="115" r="3" fill="#ff3b30"/><path d="M20 125 Q100 40 180 90" fill="none" stroke="#ff4a3a" stroke-width="1" opacity=".7"/>',EARTH_DEFS))
save('bottom-earth.svg',svg(300,220,f'<rect width="300" height="220" fill="url(#sp)"/>{stars(300,220,50)}<circle cx="150" cy="330" r="250" fill="url(#atm)"/><circle cx="150" cy="330" r="235" fill="url(#eg)"/><clipPath id="c"><circle cx="150" cy="330" r="235"/></clipPath><g clip-path="url(#c)">{clouds(150,330,235,80)}</g>',SPACE+EARTH_DEFS))
print(os.listdir(A))
