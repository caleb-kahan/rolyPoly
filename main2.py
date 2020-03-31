f = open("my_script", "w")
f.write("ident\n")
f.write("clear\n")
height = 150
t = 0
while height > -500:
    f.write("ident\n")
    f.write("clear\n")
    y = -335
    while y<0:
        f.write("torus\n-30 " + str(y) + " 0 25 75\n")
        y+=100
    f.write("sphere\n-30 "+str(height)+" 0 20\n")
    f.write('''rotate
    x 30
    move
    250 400 0
    apply
    save
    pic'''+str(t)+".png\n")
    t+=1
    height-=(t*t*0.01)
f.close()
