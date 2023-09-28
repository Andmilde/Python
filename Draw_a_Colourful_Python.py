import turtle as t
i,j,k=0,0,0
t.setup(650,350,200,200)
t.speed(99999)
t.pu()
t.fd(-250)
t.pd()
t.pensize(25)
t.seth(-40)
for i in range(2):
    for j in range(80):
        t.circle(40,1)
        t.pencolor(0,0,j/80)
    for k in range(80):
        t.circle(-40,1)
        t.pencolor(0,k/80,(80-k)/80)
    for a in range(80):
        t.circle(40,1)
        t.pencolor(a/80,(80-a)/80,0)
    for b in range(80):
        t.circle(-40,1)
        t.pencolor((80-b)/80,0,0)
for m in range(40):
    t.circle(40,1)
    t.pencolor(m/40,m/40,m/40)
for n in range(40):
    t.fd(1)
    t.pencolor((40-n)/40,(40-n)/40,(40-n)/40)
for o in range(180):
    t.circle(30,1)
    t.pencolor(o/180,0,o/180)
for p in range(30):
    t.fd(1)
    t.pencolor(1,p/30,1)
t.done()
