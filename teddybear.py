#This code prints out a teddy bear
#Created by Lena Weissman
from DrawingPanel import* #import DrawingPanel

p = DrawingPanel(500,500, background="lightsteelblue1") #background

def head():
    p.fill_oval(160, 70, 50, 50, "Navajowhite3") #left ear
    p.draw_oval(160, 70, 50, 50, "tan4") #left ear outline
    p.fill_oval(175, 83, 30, 30, "blanched almond") #left inner ear
    p.draw_oval(175, 83, 30, 30, "tan4") #left inner ear outline
    p.fill_oval(290, 70, 50, 50, "Navajowhite3") #right ear
    p.draw_oval(290, 70, 50, 50, "tan4") #right ear outline
    p.fill_oval(295, 83, 30, 30, "blanched almond") #right inner ear
    p.draw_oval(295, 83, 30, 30, "tan4") #right inner ear outline
    p.fill_oval(170, 80, 160, 150, "Navajowhite3") #head
    p.draw_oval(170, 80, 160, 150, "tan4") #head outline
    p.fill_polygon(253, 80, 243, 80, 260, 64, "Navajowhite3") #hair 1
    p.draw_polygon(253, 80, 243, 80, 260, 64, "tan4") #hair 1 outline
    p.fill_polygon(260, 80, 250, 80, 268, 70, "Navajowhite3") #hair 2
    p.draw_polygon(260, 80, 250, 80, 268, 70, "tan4") #hair 2 outline

def upper_face():
    p.fill_oval(212, 138, 26, 24, "white") #left eye outer white
    p.draw_oval(212, 138, 26, 24, "tan4") #left eye outline
    p.fill_oval(218, 139, 17, 19, "black") #left eye pupil
    p.fill_oval(226, 140, 4, 4, "white") #left eye inner white
    p.fill_oval(258, 138, 26, 24, "white") #right eye outer white
    p.draw_oval(258, 138, 26, 24, "tan4") #right eye outline
    p.fill_oval(263, 139, 17, 19, "black") #right eye pupil
    p.fill_oval(268, 140, 4, 4, "white") #right eye inner white
    p.draw_arc(208, 125, 30, 30, 45, 120, "tan4") #left eyebrow
    p.draw_arc(258, 125, 30, 30, 15, 120, "tan4") #right eyebrow
    p.draw_line(216, 141, 212, 136, "black") #right eye eyelash 1
    p.draw_line(223, 138, 222, 131, "black") #right eye eyelash 2
    p.draw_line(231, 139, 233, 133, "black") #right eye eyelash 3
    p.draw_line(264, 140, 261, 134, "black") #left eye eyelash 1
    p.draw_line(272, 138, 273, 131, "black") #left eye eyelash 2
    p.draw_line(279, 141, 283, 136, "black") #left eye eyelash 3

def lower_face():
    p.fill_oval(216, 162, 65, 50, "blanched almond") #snout
    p.draw_oval(216, 162, 65, 50, "tan4") #snout outline
    p.fill_oval(228, 162, 40, 30, "black") #nose
    p.draw_line(248, 180, 248, 205, "black") #nose line
    p.draw_arc(238, 185, 20, 20, 180, 180, "black") #smile line
    p.fill_oval(189, 156, 25, 20, "RosyBrown2") #right cheek blush
    p.fill_oval(283, 156, 25, 20, "RosyBrown2") #left cheek blush

def belly():
    p.fill_oval(140, 175, 215, 225, "Navajowhite3") #belly
    p.draw_oval(140, 175, 215, 225, "tan4") #belly outline

def arms():
    p.fill_oval(130, 220, 60, 90, "Navajowhite3") #right arm
    p.draw_oval(130, 220, 60, 90, "tan4")#right arm outline
    p.draw_arc(150, 227, 45, 30, 230, 90, "tan4") #top right paw line
    p.draw_arc(150, 250, 45, 30, 230, 90, "tan4") #lower right paw line
    p.fill_oval(308, 220, 60, 90, "Navajowhite3") #left arm
    p.draw_oval(308, 220, 60, 90, "tan4")#left arm outline
    p.draw_arc(300, 227, 45, 30, 230, 90, "tan4") #top left paw line
    p.draw_arc(300, 250, 45, 30, 230, 90, "tan4") #lower left paw line

def bow():
    p.fill_polygon(166, 118, 185, 143, 205, 110, "Indianred3") #left of bow
    p.fill_polygon(203, 110, 240, 110, 227, 80, "IndianRed3") #right of bow
    p.fill_oval(194, 101, 18, 18, "IndianRed1") #middle of bow
    
def feet():
    p.fill_oval(290, 310, 90, 100, "Navajowhite3") #left foot
    p.draw_oval(290, 310, 90, 100, "tan4") #left foot outline
    p.fill_oval(115, 310, 90, 100, "Navajowhite3") #right foot
    p.draw_oval(115, 310, 90, 100, "tan4") #right foot outline
    p.fill_oval(300, 330, 16, 25, "blanched almond") #left paw pad 1
    p.draw_oval(300, 330, 16, 25, "tan4") #left paw pad 1 outline
    p.fill_oval(328, 320, 16, 25, "blanched almond") #left paw pad 2
    p.draw_oval(328, 320, 16, 25, "tan4") #left paw pad 2 outline
    p.fill_oval(354, 330, 16, 25, "blanched almond") #left paw pad 3
    p.draw_oval(354, 330, 16, 25, "tan4") #left paw pad 3 outline
    p.fill_oval(123, 330, 16, 25, "blanched almond") #right paw pad 1
    p.draw_oval(123, 330, 16, 25, "tan4") #right paw pad 1 outline
    p.fill_oval(152, 320, 16, 25, "blanched almond") #right paw pad 2
    p.draw_oval(152, 320, 16, 25, "tan4") #right paw pad 2 outline
    p.fill_oval(179, 330, 16, 25, "blanched almond") #right paw pad 3
    p.draw_oval(179, 330, 16, 25, "tan4") #right paw pad 3 outline
    p.fill_oval(137, 352, 46, 40, "blanched almond") #middle right paw pad
    p.draw_oval(137, 352, 46, 40, "tan4") #middle right paw pad
    p.fill_oval(313, 352, 46, 40, "blanched almond") #middle left paw pad
    p.draw_oval(313, 352, 46, 40, "tan4") #middle left paw pad

def heart():
    p.fill_oval(170, 225, 80, 80, "dark red")   # Left of heart
    p.fill_oval(245, 225, 80, 80, "dark red")   # Right of heart 
    p.fill_polygon(172, 279, 245, 388, 325, 278, "dark red") #bottom of heart
    p.draw_string("   I love\n Python", 210, 263, "white", "Papyrus 21")#I love Python text

def table():
    p.fill_rect(95, 360, 30, 140, "tan4") #table leg 1
    p.draw_rect(95, 360, 30, 140, "saddle brown") #table leg 1 outline
    p.fill_rect(235, 360, 30, 140, "tan4") #table leg 2
    p.draw_rect(235, 360, 30, 140, "saddle brown") #table leg 2 outline
    p.fill_rect(370, 360, 30, 140, "tan4") #table leg 3
    p.draw_rect(370, 360, 30, 140, "saddle brown") #table leg 3 outline
    p.fill_oval(73, 310, 350, 150, "burlywood3") #table top shadow
    p.draw_oval(73, 310, 350, 150, "saddle brown") #table top shadow outline
    p.fill_oval(73, 300, 350, 150, "tan4") #table top
    p.draw_oval(73, 300, 350, 150, "saddle brown") #table top outline
    
def floor():
    p.fill_rect(0, 300, 50, 50, "pink1") #floor tile 1
    p.fill_rect(0, 350, 50, 50, "pink2") #floor tile 2
    p.fill_rect(0, 400, 50, 50, "pink1") #floor tile 3
    p.fill_rect(0, 450, 50, 50, "pink2") #floor tile 4
    p.fill_rect(50, 300, 50, 50, "pink2") #floor tile 5
    p.fill_rect(50, 350, 50, 50, "pink1") #floor tile 6
    p.fill_rect(50, 400, 50, 50, "pink2") #floor tile 7
    p.fill_rect(50, 450, 50, 50, "pink1") #floor tile 8
    p.fill_rect(100, 300, 50, 50, "pink1") #floor tile 9
    p.fill_rect(100, 350, 50, 50, "pink2") #floor tile 10
    p.fill_rect(100, 400, 50, 50, "pink1") #floor tile 11
    p.fill_rect(100, 450, 50, 50, "pink2") #floor tile 12
    p.fill_rect(150, 400, 50, 50, "pink2") #floor tile 13
    p.fill_rect(150, 450, 50, 50, "pink1") #floor tile 14
    p.fill_rect(200, 450, 50, 50, "pink2") #floor tile 15
    p.fill_rect(250, 450, 50, 50, "pink1") #floor tile 16
    p.fill_rect(300, 400, 50, 50, "pink1") #floor tile 17
    p.fill_rect(300, 450, 50, 50, "pink2") #floor tile 18
    p.fill_rect(350, 300, 50, 50, "pink2") #floor tile 10
    p.fill_rect(350, 400, 50, 50, "pink2") #floor tile 20
    p.fill_rect(350, 450, 50, 50, "pink1") #floor tile 21
    p.fill_rect(400, 300, 50, 50, "pink1") #floor tile 22
    p.fill_rect(400, 350, 50, 50, "pink2") #floor tile 23
    p.fill_rect(400, 400, 50, 50, "pink1") #floor tile 24
    p.fill_rect(400, 450, 50, 50, "pink2") #floor tile 25
    p.fill_rect(450, 300, 50, 50, "pink2") #floor tile 26
    p.fill_rect(450, 350, 50, 50, "pink1") #floor tile 27
    p.fill_rect(450, 400, 50, 50, "pink2") #floor tile 28
    p.fill_rect(450, 450, 50, 50, "pink1") #floor tile 29

def frame():
    p.fill_rect(35, 100, 100, 80, "plum4") #frame 
    p.fill_rect(45, 110, 80, 60, "lightblue1") #picture background
    p.fill_oval(60, 120, 10, 10, "yellow") #sun
    p.fill_rect(45, 155, 80, 15, "light green") #grass
    p.fill_rect(90, 140, 20, 25, "IndianRed1") #house
    p.fill_polygon(88, 140, 113, 140, 101, 128, "IndianRed4") #house top
    p.fill_rect(365, 100, 100, 80, "plum4") #frame 2
    p.fill_rect(375, 110, 80, 60, "skyblue3") #picture background 2
    p.fill_oval(407, 133, 15, 15, "gold") #sun
    p.fill_rect(375, 145, 80, 25, "RoyalBlue2") #ocean
    p.draw_line(390, 144, 410, 144, "gold") #sunlight
    p.draw_line(420, 144, 440, 144, "gold") #sunlight
    p.draw_line(395, 146, 435, 146, "orange") #sunlight
    p.draw_line(400, 148, 430, 148, "orange") #sunlight
    
def main(): #calls the functions
    frame()
    floor()
    table()
    belly()
    head()
    upper_face()
    lower_face()
    heart()
    arms()
    feet()
    bow()
    
main()
