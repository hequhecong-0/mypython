


#��������
��="�¿���"
�¿���="˧��"
print("����",�¿���)


#���ʺ磬��ʧ����
from turtle import *


def HSB2RGB(hues):
    hues=hues*3.59
    rgb=[0.0,0.0,0.0]
    i=int(hues/60)%6
    f=hues/60-i
    if i==0:
        rgb[0]=1;rgb[1]=f;rgb[2]=0
    elif i==1:
        rgb[0]=1-f;rgb[1]=1;rgb[2]=0
    elif i==2:
        rgb[0]=0;rgb[1]=1;rgb[2]=f
    elif i==3:
        rgb[0]=0;rgb[1]=1-f;rgb[2]=1
    elif i==4:
        rgb[0]=f;rgb[1]=0;rgb[2]=1
    elif i==5:
        rgb[0]=1;rgb[1]=0;rgb[2]=1-f
    return rgb


def rainbow():
    hues=0.0
    color(1,0,0)
    hideturtle()
    speed(5)
    pensize(3)
    penup()
    goto(-650,-150)
    pendown()
    right(110)
    for i in range(100):
        circle(600)
        right(0.23)
        hues=hues+1
        rgb=HSB2RGB(hues)
        color(rgb[0],rgb[1],rgb[2])
    penup()

def main():
            setup(1200,800,0,0)
            bgcolor((64/255,64/255,1))
            tracer(False)
            rainbow()
            tracer(False)
            goto(0,0)
            pendown()
            color('yellow')
            write('�ʺ�',align="center",
                   font=("Script MT Bold", 80, "bold"))
            tracer(True)


            mainloop()


if __name__=="_main__":
              main()


















#������
import turtle
import time

def hart_arc():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

def move_pen_position(x,y):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.showturtle()

turtle.setup(width=800,height=500)
turtle.color('red', 'pink')
turtle.pensize(3)
turtle.speed(3)
move_pen_position(x=0,y=-180)
turtle.left(140)
turtle.begin_fill()
turtle.forward(224)
hart_arc()
turtle.left(120)
hart_arc()
turtle.forward(224)
turtle.end_fill()
window=turtle.Screen()
window.exitonclick()


#��������
def main():
    PM=eval(input("�����������Σ�\n"))

    if PM>250:
        print("������Ⱦ")
    elif PM>150:
        print("�����Ⱦ")
    elif PM>115:
        print("�е���Ⱦ")
    elif PM>75:
        print("��������")
    elif PM>35:
        print("��������")
    else:
        print("��������")
main()

#�򵥴�����κ����Ĵ���
import math
def main():
    print("������������κ���զ����")
    a,b,c = eval(input("���������ϵ�� (a,b,c ):  "))
    delta=b*b-4*a*c
    if a==0:
        x=-b/c
        print("\n��һ����",x)
    elif delta<0:
        print("\nû��ʵ����")
    elif delta==0:
        x=-b/(2*a)
        print("\n��˫��",x)
    else:
        discRoot=math.sqrt(delta)
        x1=(-b+discRoot)/(2*a)
        x2=(-b-discRoot)/(2*a)
        print("��������һ���ĸ�: ",x1,x2)
main()





#�ڱ�ѭ����ʼ��
def main():
    sum=0.0
    count=0
    xStr=input("��������������һ�����֣� >>")
    while xStr !="":
        x=eval(xStr)
        sum=sum+x
        count=count+1
        xStr=input("����������������һ�����֣�>>")
    print("���ǵ�ƽ��������",sum/count)
main()

#�ڱ�ѭ�������ļ����ݰ汾
def main():
    fileName=input("�����������ĸ��ļ��������أ��ϴ�")
    infile=open(fileName,'r')
    sum=0.0
    count=0
    line=infile.readline()
    while line !="":
        for xStr in line.split(","):
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print("���ǵ�ƽ��������",sum/count)
main()




#�ڱ�ѭ�������ļ����ݰ汾
def main():
    fileName=input("�����������ĸ��ļ��������أ��ϴ�")
    infile=open(fileName,'r')
    sum=0.0
    count=0
    line=infile.readline()
    while line !="":
        for xStr in line.split(","):
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print("���ǵ�ƽ��������",sum/count)
main()



#��С�������Ĵ���
from turtle import*
def nose(x,y):
    penup()
    goto(x,y)
    pendown()
    setheading(-30)
    begin_fill()
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            left(3)
            forward(a)
        else:
            a=a-0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,85,45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,255,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()
def head(x,y):
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3)
            fd(a)
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()
def ears(x,y):
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()
def eyes(x,y):
    color((255,155,192),"white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255,155,192),"white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
def cheek(x,y):
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()
def mouth(x,y):
    color(255,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)
def setting():
    pensize(4)
    hideturtle()
    colormode(255)
    color((255,155,192),"pink")
    setup(840,500)
    speed(10)
def main():
    setting()
    nose(-100,100)
    head(-69,167)
    ears(0,160)
    eyes(0,140)
    cheek(80,10)
    mouth(-20,30)
    done()
if __name__ == '__main__':
    main()


#��ת���ӵĳ���
def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]
def main():
    a=input("������Ҫ��ת�ľ���\n")
    print(reverse(a))
main()






# in ���÷�
list1 = [1, 2, 3, 4, 5]
a = 10
if a in list1:
    print("a��list1�ĳ�Ա֮һ")
else:
    print("a����list1�ĳ�Ա֮һ")




def main():
    a=eval(input("������һ������"))
    i=1
    b=0
    while i<=a:
        if i%2==0:
            b=i+b
        i=i+1
    print("1��%d�����е�ż����Ϊ%d"%(a,b))
main()


