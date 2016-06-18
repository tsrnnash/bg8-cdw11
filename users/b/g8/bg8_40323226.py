<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
 
</head>
<body>
 
<script>
window.onload=function(){
brython(1);
}
</script>
 
<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import alert
from browser import window
import math
 
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
 
cgo.setWorldCoords(-250, -250, 500, 500) 
 
# 畫軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
 
deg = math.pi/180  
 
# 將繪製鏈條輪廓的內容寫成 class 物件
class chain():
    # 輪廓的外型設為 class variable
    chamber = "M -6.8397, -1.4894             A 7, 7, 0, 1, 0, 6.8397, -1.4894             A 40, 40, 0, 0, 1, 6.8397, -18.511             A 7, 7, 0, 1, 0, -6.8397, -18.511             A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    #chamber = "M 0, 0 L 0, -20 z"
    cgoChamber = window.svgToCgoSVG(chamber)
 
    def __init__(self, fillcolor="green", border=True, strokecolor= "tan", linewidth=2, scale=1):
        self.fillcolor = fillcolor
        self.border = border
        self.strokecolor = strokecolor
        self.linewidth = linewidth
        self.scale = scale
 
    # 利用鏈條起點與終點定義繪圖
    def basic(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # 注意, cgo.Chamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(math.atan2(y2-y1, x2-x1)/deg+90)
 
        # 放大 scale 倍
        cgo.render(basic1, x1, y1, self.scale, 0)
 
    # 利用鏈條起點與旋轉角度定義繪圖, 使用內定的 color, border 與 linewidth 變數
    def basic_rot(self, x1, y1, rot, v=False):
        # 若 v 為 True 則為虛擬 chain, 不 render
        self.x1 = x1
        self.y1 = y1
        self.rot = rot
        self.v = v
        # 注意, cgoChamber 為成員變數
        cmbr = cobj(self.cgoChamber, "SHAPE", {
                "fillColor": self.fillcolor,
                "border": self.border,
                "strokeColor": self.strokecolor,
                "lineWidth": self.linewidth })
 
        # hole0 為原點位置
        hole = cobj(shapedefs.circle(4*self.scale), "PATH")
        cmbr.appendPath(hole)
        # 根據旋轉角度, 計算 x2 與 y2
        x2 = x1 + 20*math.cos(rot*deg)*self.scale
        y2 = y1 + 20*math.sin(rot*deg)*self.scale
 
        # 複製 cmbr, 然後命名為 basic1
        basic1 = cmbr.dup()
        # 因為鏈條的角度由原點向下垂直, 所以必須轉 90 度, 再考量 atan2 的轉角
        basic1.rotate(rot+90)
 
        # 放大 scale 倍
        if v == False:
            cgo.render(basic1, x1, y1, self.scale, 0)
 
        return x2, y2

mychain = chain()
 
x1, y1 = mychain.basic_rot(44.0532,-165.17, 110.78)
 
x2, y2=mychain.basic_rot(x1, y1,90.78, True) 
x3, y3=mychain.basic_rot(x2, y2,70.78, True) 
x4, y4=mychain.basic_rot(x3, y3,50.78, True) 
x5, y5=mychain.basic_rot(x4, y4,30.78, True) 
x6, y6=mychain.basic_rot(x5, y5,10.780000000000001, True) 
x7, y7=mychain.basic_rot(x6, y6,-9.219999999999999, True) 
x8, y8=mychain.basic_rot(x7, y7,-29.22, True) 
x9, y9=mychain.basic_rot(x8, y8,-49.22, True) 
x10, y10=mychain.basic_rot(x9, y9,-69.22, True) 
x11, y11=mychain.basic_rot(x10, y10,-89.22, True) 
x12, y12=mychain.basic_rot(x11, y11,-109.22) 
x13, y13=mychain.basic_rot(x12, y12,-129.22) 
x14, y14=mychain.basic_rot(x13, y13,-149.22) 
x15, y15=mychain.basic_rot(x14, y14,-169.22) 
x16, y16=mychain.basic_rot(x15, y15,-189.22) 
x17, y17=mychain.basic_rot(x16, y16,-209.22) 
x18, y18=mychain.basic_rot(x17, y17,-229.22) 

#mychain = chain()
 
p1, k1 = mychain.basic_rot(0,50, 94.78)
p2, k2=mychain.basic_rot(p1, k1,82.78) 
p3, k3=mychain.basic_rot(p2, k2,70.78) 
p4, k4=mychain.basic_rot(p3, k3,58.78) 
p5, k5=mychain.basic_rot(p4, k4,46.78) 
p6, k6=mychain.basic_rot(p5, k5,34.78) 
p7, k7=mychain.basic_rot(p6, k6,22.78) 
p8, k8=mychain.basic_rot(p7, k7,10.780000000000001) 
p9, k9=mychain.basic_rot(p8, k8,-1.2199999999999989) 
p10, k10=mychain.basic_rot(p9, k9,-13.219999999999999) 
p11, k11=mychain.basic_rot(p10, k10,-25.22) 
p12, k12=mychain.basic_rot(p11, k11,-37.22) 
p13, k13=mychain.basic_rot(p12, k12,-49.22) 
p14, k14=mychain.basic_rot(p13, k13,-61.22) 
p15, k15=mychain.basic_rot(p14, k14,-73.22) 
p16, k16=mychain.basic_rot(p15, k15,-85.22) 
p17, k17=mychain.basic_rot(p16, k16,-97.22) 
p18, k18=mychain.basic_rot(p17, k17,-109.22, True) 
p19, k19=mychain.basic_rot(p18, k18,-121.22, True) 
p20, k20=mychain.basic_rot(p19, k19,-133.22, True) 
p21, k21=mychain.basic_rot(p20, k20,-145.22, True) 
p22, k22=mychain.basic_rot(p21, k21,-157.22, True) 
p23, k23=mychain.basic_rot(p22, k22,-169.22, True) 
p24, k24=mychain.basic_rot(p23, k23,-181.22, True) 
p25, k25=mychain.basic_rot(p24, k24,-193.22, True) 
p26, k26=mychain.basic_rot(p25, k25,-205.22, True) 
p27, k27=mychain.basic_rot(p26, k26,-217.22, True) 
p28, k28=mychain.basic_rot(p27, k27,-229.22, True) 
p29, k29=mychain.basic_rot(p28, k28,-241.22, True) 
p30, k30=mychain.basic_rot(p29, k29,-253.22, True) 

m1, n1 = mychain.basic_rot(x1, y1, 100.78)
m2, n2=mychain.basic_rot(m1, n1, 100.78)
m3, n3=mychain.basic_rot(m2, n2, 100.78)
m4, n4=mychain.basic_rot(m3, n3, 100.78)
m5, n5=mychain.basic_rot(m4, n4, 100.78)
m6, n6=mychain.basic_rot(m5, n5, 100.78)
m7, n7=mychain.basic_rot(m6, n6, 100.78)
m8, n8=mychain.basic_rot(m7, n7, 100.78)
m9, n9=mychain.basic_rot(m8, n8, 100.78)
m10, n10=mychain.basic_rot(m9, n9, 100.78)

r1, s1 = mychain.basic_rot(x11, y11, 79.22)
r2, s2=mychain.basic_rot(r1, s1, 79.22)
r3, s3=mychain.basic_rot(r2, s2, 79.22)
r4, s4=mychain.basic_rot(r3, s3, 79.22)
r5, s5=mychain.basic_rot(r4, s4, 79.22)
r6, s6=mychain.basic_rot(r5, s5, 79.22)
r7, s7=mychain.basic_rot(r6, s6, 79.22)
r8, s8=mychain.basic_rot(r7, s7, 79.22)
r9, s9=mychain.basic_rot(r8, s8, 79.22)
r10, s10=mychain.basic_rot(r9, s9, 79.22)

</script>
