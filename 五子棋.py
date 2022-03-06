# coding=utf-8
import turtle as t
#turtle库
import keyboard as k
#左键黑棋，右键白棋，黑棋先下





t.ht()
t.pensize(3)
t.tracer(0)




a=0
b=0
c=0
d=0
线x=-270
线y=-324
xb=30
yb=36
x0=线x-xb
y0=线y-yb
xa=-70
ya=y0-10
角1x=线x+xb*3
角1y=线y+yb*3
角2x=线x+xb*3
角2y=-线y-yb*3
角3x=-线x-xb*3
角3y=-线y-yb*3
角4x=-线x-xb*3
角4y=线y+yb*3
边1x=线x+xb*9
边1y=线y+yb*3
边2x=-线x-xb*9
边2y=-线y-yb*3
边3x=线x+xb*3
边3y=线y+yb*9
边4x=-线x-xb*3
边4y=-线y-yb*9
腹x=线x+xb*9
腹y=线y+yb*9
#变量




list0=[]
list1=[]
list2=[]
#列表




def 棋盘():
    global 线x,线y
    t.fillcolor('gold')
    t.pu()
    t.goto(x0,y0)
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(-x0*2)
        t.lt(90)
        t.fd(-y0*2)
        t.lt(90)
    t.end_fill()

    t.pencolor('goldenrod')
    t.pu()
    t.goto(线x,线y)
    t.pd()
    t.seth(90)
    for i in range(19):
        线x=线x+xb
        t.fd(-线y*2)
        t.pu()
        t.goto(线x,线y)
        t.pd()
    线x=-270

    t.pu()
    t.goto(线x,线y)
    t.pd()
    t.rt(90)
    for i in range(19):
        线y=线y+yb
        t.fd(-线x*2)
        t.pu()
        t.goto(线x,线y)
        t.pd()
    线y=-324

    t.pu()
    t.goto(角1x,角1y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(角2x,角2y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(角3x,角3y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(角4x,角4y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(边1x,边1y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(边2x,边2y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(边3x,边3y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(边4x,边4y)
    t.pd()
    t.dot(15,'goldenrod')
    t.pu()
    t.goto(腹x,腹y)
    t.pd()
    t.dot(15,'goldenrod')

def 下黑子(x,y):
    global a,b
    if a!=0:
        return
    t.pu()
    if x%30<15:
        x=x-x%30
    elif x%30>15:
        x=x-x%30+30
    else:
        return
    if y%36<18:
        y=y-y%36
    elif y%36>18:
        y=y-y%36+36
    else:
        return
    t.goto(x,y)
    t.pd()
    if 线x<=x<=-线x and 线y<=y<=-线y and str(int(x/30+10))+'，'+str(int(y/36+10)) not in list0:
        t.dot(25,'black')
        x=x/30+10
        y=y/36+10
        a=a+1
        b=b+1

        t.pencolor('white')
        t.fillcolor('white')
        t.pu()
        t.goto(x0-1,0)
        t.seth(90)
        t.begin_fill()
        for i in range(2):
            t.fd(55)
            t.lt(90)
            t.fd(295)
            t.lt(90)
        t.end_fill()

        t.pu()
        t.goto(x0-140,0)
        t.pd()
        t.pencolor('black')
        t.write('黑棋第'+str(int(b))+'步的位置在：\n第'+str(int(x))+'行，第'+str(int(y))+'列',font=('楷体',20),align='center')

        z=str(int(x))+'，'+str(int(y))

        w0=str(int(x+1))+'，'+str(int(y+1))
        w1=str(int(x+2))+'，'+str(int(y+2))
        w2=str(int(x+3))+'，'+str(int(y+3))
        w3=str(int(x+4))+'，'+str(int(y+4))

        w4=str(int(x-1))+'，'+str(int(y-1))
        w5=str(int(x-2))+'，'+str(int(y-2))
        w6=str(int(x-3))+'，'+str(int(y-3))
        w7=str(int(x-4))+'，'+str(int(y-4))

        w8=str(int(x+1))+'，'+str(int(y))
        w9=str(int(x+2))+'，'+str(int(y))
        w10=str(int(x+3))+'，'+str(int(y))
        w11=str(int(x+4))+'，'+str(int(y))

        w12=str(int(x-1))+'，'+str(int(y))
        w13=str(int(x-2))+'，'+str(int(y))
        w14=str(int(x-3))+'，'+str(int(y))
        w15=str(int(x-4))+'，'+str(int(y))

        w16=str(int(x))+'，'+str(int(y+1))
        w17=str(int(x))+'，'+str(int(y+2))
        w18=str(int(x))+'，'+str(int(y+3))
        w19=str(int(x))+'，'+str(int(y+4))

        w20=str(int(x))+'，'+str(int(y-1))
        w21=str(int(x))+'，'+str(int(y-2))
        w22=str(int(x))+'，'+str(int(y-3))
        w23=str(int(x))+'，'+str(int(y-4))

        w24=str(int(x+1))+'，'+str(int(y-1))
        w25=str(int(x+2))+'，'+str(int(y-2))
        w26=str(int(x+3))+'，'+str(int(y-3))
        w27=str(int(x+4))+'，'+str(int(y-4))

        w28=str(int(x-1))+'，'+str(int(y+1))
        w29=str(int(x-2))+'，'+str(int(y+2))
        w30=str(int(x-3))+'，'+str(int(y+3))
        w31=str(int(x-4))+'，'+str(int(y+4))

        if w0 in list1 and w1 in list1 and w2 in list1 and w3 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list1 and w1 in list1 and w2 in list1 and w4 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list1 and w1 in list1 and w4 in list1 and w5 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list1 and w4 in list1 and w5 in list1 and w6 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w4 in list1 and w5 in list1 and w6 in list1 and w7 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w8 in list1 and w9 in list1 and w10 in list1 and w11 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list1 and w9 in list1 and w10 in list1 and w12 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list1 and w10 in list1 and w12 in list1 and w13 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list1 and w12 in list1 and w13 in list1 and w14 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w12 in list1 and w13 in list1 and w14 in list1 and w15 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w16 in list1 and w17 in list1 and w18 in list1 and w19 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list1 and w18 in list1 and w19 in list1 and w20 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list1 and w19 in list1 and w20 in list1 and w21 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list1 and w20 in list1 and w21 in list1 and w22 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w20 in list1 and w21 in list1 and w22 in list1 and w23 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w24 in list1 and w25 in list1 and w26 in list1 and w27 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list1 and w26 in list1 and w27 in list1 and w28 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list1 and w27 in list1 and w28 in list1 and w29 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list1 and w28 in list1 and w29 in list1 and w30 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w28 in list1 and w29 in list1 and w30 in list1 and w31 in list1:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，黑胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        list0.append(z)
        list1.append(z)
    else:
        return

def 下白子(x,y):
    global a,c
    if a!=1:
        return
    t.pu()
    if x%30<15:
        x=x-x%30
    elif x%30>15:
        x=x-x%30+30
    else:
        return
    if y%36<18:
        y=y-y%36
    elif y%36>18:
        y=y-y%36+36
    else:
        return
    t.goto(x,y)
    t.pd()
    if 线x<=x<=-线x and 线y<=y<=-线y and str(int(x/30+10))+'，'+str(int(y/36+10)) not in list0:
        t.dot(25,'snow')
        x=x/30+10
        y=y/36+10

        a=a-1
        c=c+1

        t.pencolor('white')
        t.fillcolor('white')
        t.pu()
        t.goto(-x0+2,0)
        t.seth(90)
        t.begin_fill()
        for i in range(2):
            t.fd(55)
            t.rt(90)
            t.fd(295)
            t.rt(90)
        t.end_fill()

        t.pu()
        t.goto(-x0+140,0)
        t.pd()
        t.pencolor('black')
        t.write('白棋第'+str(int(c))+'步的位置在：\n第'+str(int(x))+'行，第'+str(int(y))+'列',font=('楷体',20),align='center')

        z=str(int(x))+'，'+str(int(y))

        w0=str(int(x+1))+'，'+str(int(y+1))
        w1=str(int(x+2))+'，'+str(int(y+2))
        w2=str(int(x+3))+'，'+str(int(y+3))
        w3=str(int(x+4))+'，'+str(int(y+4))

        w4=str(int(x-1))+'，'+str(int(y-1))
        w5=str(int(x-2))+'，'+str(int(y-2))
        w6=str(int(x-3))+'，'+str(int(y-3))
        w7=str(int(x-4))+'，'+str(int(y-4))

        w8=str(int(x+1))+'，'+str(int(y))
        w9=str(int(x+2))+'，'+str(int(y))
        w10=str(int(x+3))+'，'+str(int(y))
        w11=str(int(x+4))+'，'+str(int(y))

        w12=str(int(x-1))+'，'+str(int(y))
        w13=str(int(x-2))+'，'+str(int(y))
        w14=str(int(x-3))+'，'+str(int(y))
        w15=str(int(x-4))+'，'+str(int(y))

        w16=str(int(x))+'，'+str(int(y+1))
        w17=str(int(x))+'，'+str(int(y+2))
        w18=str(int(x))+'，'+str(int(y+3))
        w19=str(int(x))+'，'+str(int(y+4))

        w20=str(int(x))+'，'+str(int(y-1))
        w21=str(int(x))+'，'+str(int(y-2))
        w22=str(int(x))+'，'+str(int(y-3))
        w23=str(int(x))+'，'+str(int(y-4))

        w24=str(int(x+1))+'，'+str(int(y-1))
        w25=str(int(x+2))+'，'+str(int(y-2))
        w26=str(int(x+3))+'，'+str(int(y-3))
        w27=str(int(x+4))+'，'+str(int(y-4))

        w28=str(int(x-1))+'，'+str(int(y+1))
        w29=str(int(x-2))+'，'+str(int(y+2))
        w30=str(int(x-3))+'，'+str(int(y+3))
        w31=str(int(x-4))+'，'+str(int(y+4))

        if w0 in list2 and w1 in list2 and w2 in list2 and w3 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list2 and w1 in list2 and w2 in list2 and w4 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list2 and w1 in list2 and w4 in list2 and w5 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w0 in list2 and w4 in list2 and w5 in list2 and w6 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w4 in list2 and w5 in list2 and w6 in list2 and w7 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w8 in list2 and w9 in list2 and w10 in list2 and w11 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list2 and w9 in list2 and w10 in list2 and w12 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list2 and w10 in list2 and w12 in list2 and w13 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w8 in list2 and w12 in list2 and w13 in list2 and w14 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w12 in list2 and w13 in list2 and w14 in list2 and w15 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w16 in list2 and w17 in list2 and w18 in list2 and w19 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list2 and w18 in list2 and w19 in list2 and w20 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list2 and w19 in list2 and w20 in list2 and w21 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w16 in list2 and w20 in list2 and w21 in list2 and w22 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w20 in list2 and w21 in list2 and w22 in list2 and w23 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        elif  w24 in list2 and w25 in list2 and w26 in list2 and w27 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list2 and w26 in list2 and w27 in list2 and w28 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list2 and w27 in list2 and w28 in list2 and w29 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w24 in list2 and w28 in list2 and w29 in list2 and w30 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()
        elif  w28 in list2 and w29 in list2 and w30 in list2 and w31 in list2:
            t.clear()
            t.goto(0,0)
            t.write('游戏结束，白胜',font=('楷体',20),align='center')
            t.goto(0,-35)
            t.write('点击任意地方退出',font=('楷体',20),align='center')
            t.exitonclick()

        list0.append(z)
        list2.append(z)

    else:
        return

#函数




棋盘()




t.pencolor('black')
t.onscreenclick(下黑子)
t.onscreenclick(下白子,btn=3)

print(1)
#执行函数



t.done()