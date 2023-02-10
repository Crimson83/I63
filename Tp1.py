from cng import cng
#Ex1
def create_rectangle(x1,y1,lo,la):
    """
    Creates a rectangle at x1,y1
    with a width of la and a height of lo
    """
    cng.current_color('Blue')
    id_box=cng.rectangle(x1,y1,x1+la,y1+lo,pep=1) #create a box at coordinates x1 y1, width of x1+la and height of y1+lo
    cng.current_color('Black')
    return id_box

def move_viewport(id_box,point,window,viewport_stat):
    """
    Moves the rectangle by mx on x axis and my on y axis
    and then does projects the point in the new viewport
    """
    mx,my=cng.get_mouse_x(),cng.get_mouse_y()
    currentx=cng.obj_get_coord(id_box)[0] #coordinate x of object
    currenty=cng.obj_get_coord(id_box)[1] #coordinate y of object
    cng.obj_move(id_box,mx-currentx,my-currenty)
    viewport_stat[0]=cng.obj_get_coord(id_box)[0]
    viewport_stat[1]=cng.obj_get_coord(id_box)[1]
    x1,y1=projection(point,window,viewport_stat)
    print(x1,y1)
    cng.point(x1,y1)

def print_mouse_coord():
    """
    Prints current mouse coordinates
    """
    print(cng.get_mouse_x(),cng.get_mouse_y()) #print of mouse x coordinate and y coordinate

#Ex2
def projection(point,window,viewport):
    """
    Does the projection between WorldCoordinates and DisplayCoordinates
    """
    xw1=window[0]
    yw1=window[1]
    a=xw1
    b=yw1
    xw2=xw1+window[3]
    c=xw2
    yw2=yw1+window[2]
    d=yw2
    e=viewport[0]
    f=viewport[1]
    xv2=xv1+viewport[3]
    g=xv2
    yv2=yv1+viewport[2]
    h=yv2
    print(a,b,c,d,e,f,g,h)
    point_x=(point[0]*((g-e)/(c-a)))+(e-((a*(g-e))/(c-a)))
    point_y=(point[1]*((h-f)/(d-h)))+(f-((b*(h-f))/(d-b)))
    return point_x,point_y

cng.init_window(pnom='Test',pla=720,pha=480,color="white")
"""
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
"""
xw1=-25 #x coordinate of window
yw1=-25 #y coordinate of window
lo=50 #height of window
la=50 #width of window
window=[xw1,yw1,lo,la]
px=0 #x coordinateste of point
py=0 #y coordinate of point
point=[px,py]
xv1=0 #starting x coordinate of viewport
yv1=0 #starting y coordinate of viewport
vlo=250 #height of viewport
vla=250 #width of viewport
viewport_stat=[xv1,yv1,vlo,vla]
viewport=create_rectangle(xv1,yv1,vlo,vla)
xv1=cng.obj_get_coord(viewport)[0]
yv1=cng.obj_get_coord(viewport)[1]
print(xv1,yv1)
cng.assoc_button(1,lambda:move_viewport(viewport,point,window,viewport_stat))
cng.main_loop()
