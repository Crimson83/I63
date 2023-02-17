from cng import cng
#Ex1
def create_rectangle(x1,y1,lx,ly):
    """
    Creates a rectangle at x1,y1
    with a width of lx and a height of ly
    """
    cng.current_color('Blue')
    id_box=cng.rectangle(x1,y1,x1+lx,y1+ly,pep=1) #create a box at coordinates x1 y1, width of x1+lx and height of y1+ly
    cng.current_color('Black')
    return id_box

def move_viewport(id_box,pt_list,wd_list,vp_stat,id_point):
    """
    Moves the rectangle by mx on x axis and my on y axis
    and then does projects the point in the new viewport
    """
    global vly,vlx
    mx,my=cng.get_mouse_x(),cng.get_mouse_y()
    currentx=cng.obj_get_coord(id_box)[0] #coordinate x of object
    currenty=cng.obj_get_coord(id_box)[1] #coordinate y of object
    cng.obj_move(id_box,mx-currentx,my-currenty)
    print("stat viewport :",vp_stat)
    vp_stat[2]=mx+vlx
    vp_stat[3]=my+vly
    mouvement(id_box,id_point,pt_list,wd_list,vp_stat)

def mouvement(id_b,id_pt,pt_lt,wd_lt,vp_st):
    """
    projections due to the movement of the viewport
    """
    vp_st[0]=cng.obj_get_coord(id_b)[0]
    vp_st[1]=cng.obj_get_coord(id_b)[1]
    x1,y1=projection(pt_lt,wd_lt,vp_st)
    x_point=cng.obj_get_coord(id_pt)[0]
    y_point=cng.obj_get_coord(id_pt)[1]
    #print("ON BOUGE")
    #print(x1,y1)
    cng.obj_move(id_pt,x1-x_point,y1-y_point)
    #print("coord point après mouv :", cng.obj_get_coord(id_pt))

def print_mouse_coord():
    """
    Prints current mouse coordinates
    """
    print(cng.get_mouse_x(),cng.get_mouse_y()) #print of mouse x coordinate and y coordinate

#Ex2
def projection(pt_list,wd_list,vp_list):
    """
    Does the projection between WorldCoordinates and DisplayCoordinates
    """
    print("pt_list :",pt_list)
    print("wd_list :",wd_list)
    print("vp_list :",vp_list)
    a=wd_list[0]
    b=wd_list[1]
    c=a+wd_list[2]
    d=b+wd_list[3]
    e=vp_list[0]
    f=vp_list[1]
    g=vp_list[2]
    h=vp_list[3]

    print(a,b,c,d,e,f,g,h)
    print("coordonnée point avant projection :",pt_list[0],pt_list[1])
    point_x=pt_list[0]*((g-e)/(c-a))+e-((a*(g-e))/(c-a))
    point_y=pt_list[1]*((h-f)/(d-b))+f-((b*(h-f))/(d-b))
    print("Fonction projection coordonnée x :",point_x,"coordonnée y :",point_y)
    return point_x,point_y

cng.init_window(pnom='Test',pla=720,pha=480,color="white")
"""
    x=int(input("Enter the x coordinate of the window :"))
    y=int(input("Enter the y coordinate of the window :"))
    ly=int(input("Enter the height of the window :"))
    lx=int(input("Entrez the width of the window :"))
    px=int(input("Enter the x coordinate of the point :"))
    py=int(input("Enter the y coordinate of the point :"))
    vx=int(input("Enter the x coordinate of the viewport :"))
    vy=int(input("Enter the y coordinate of the viewport :"))
    vly=int(input("Enter the height of the viewport :"))
    vlx=int(input("Enter the width of the viewport :"))
"""
xw1=-10 #x coordinate of window
yw1=-10 #y coordinate of window
lx=40 #height of window
ly=40 #width of window
window_list=[xw1,yw1,lx,ly]
px=0 #x coordinateste of point
py=0 #y coordinate of point
point_list=[px,py]
xv1=100 #starting x coordinate of viewport
yv1=100 #starting y coordinate of viewport
global vly,vlx
vly=200 #height of viewport
vlx=200 #width of viewport
viewport_stat=[xv1,yv1,vlx,vly]
print("Stat Viewport :",viewport_stat)
viewport_id=create_rectangle(xv1,yv1,vlx,vly)
xv1=cng.obj_get_coord(viewport_id)[0]
yv1=cng.obj_get_coord(viewport_id)[1]
point_id=cng.rectangle(px,py,px,py,pep=5)
cng.assoc_button(1,lambda:move_viewport(viewport_id,point_list,window_list,viewport_stat,point_id))
cng.main_loop()
