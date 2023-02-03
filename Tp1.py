from cng import cng
#Ex1
def create_rectangle(x1,y1,lo,la):
    """
    Creates a rectangle at x1,y1
    with a width of la and a height of lo
    """
    id_box=cng.rectangle(x1,y1,x1+la,y1+lo,pep=1)
    return id_box

def move_rectangle(id_box,mx,my):
    """
    Moves the rectangle by mx on x axis and my on y axis
    """
    currentx=cng.obj_get_coord(id_box)[0] #coordinate x of object
    currenty=cng.obj_get_coord(id_box)[1] #coordinate y of object
    cng.obj_move(id_box,mx-currentx,my-currenty)

def affich_coord():
    """
    Prints current mouse coordinates
    """
    print(cng.get_mouse_x(),cng.get_mouse_y())

#Ex2
def projection_DC(pt,window,viewport):
    """
    Does the projection between WorldCoordinates and DisplayCoordinates
    """

    pass
cng.init_window(pnom='Test',pla=720,pha=480,color="white")
x=int(input("Enter the x coordinate of the window :"))
y=int(input("Enter the y coordinate of the window :"))
lo=int(input("Enter the height of the window :"))
la=int(input("Entrez the width of the window :"))
px=int(input("Enter the x coordinate of the point :"))
py=int(input("Enter the y coordinate of the point :"))
vx=int(input("Enter the x coordinate of the viewport :"))
vy=int(input("Enter the y coordinate of the viewport :"))
vlo=int(input("Enter the height of the viewport :"))
vla=int(input("Enter the width of the viewport :"))
pt=cng.point(px,py)
window=create_rectangle(x,y,lo,la)
viewport=create_rectangle(x,y,lo,la)
viewport=create_rectangle(x,y,lo,la)
cng.assoc_button(1,lambda:move_rectangle(viewport,cng.get_mouse_x(),cng.get_mouse_y()))
cng.main_loop()
