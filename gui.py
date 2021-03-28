from tkinter import *

# Create 'num' array of 3^4 = 81 cells
a = set(['1','2','3'])
num = set()
for i in a:
    for j in a:
        for k in a:
            for l in a:
                '''for m in a:
                    for n in a:
                        for o in a:
                            for p in a:'''
                num.add(int(i+j+k+l))
# Draw a canvas
master = Tk()
canvas_width = 300
canvas_height = 300
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
offset = 10
size = 30
#w.create_rectangle(offset,canvas_height - offset,offset + size,canvas_height - offset - size, fill="#FFFFFF")
for i in num:
    i = str(i)
    w.create_rectangle(offset + 0 + (int(i[0])-1)*3*size + (int(i[2])-1)*size,
                       canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3])-1)*size,
                       offset + (int(i[0])-1)*3*size + int(i[2])*size,
                       canvas_height - offset - (int(i[1])-1)*3*size - (int(i[3]))*size,
                       fill="#FFFFFF")
mainloop()

'''def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(0,canvas_width,line_distance):
      canvas.create_line(x, 0+30, x, canvas_height-30, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(0,canvas_height,line_distance):
      canvas.create_line(0+30, y, canvas_width-30, y, fill="#476042")


master = Tk()
canvas_width = 330
canvas_height = 330
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w,30)

mainloop()'''
