screen obj_screen(current, obj_prop={}):
    layer "master"
    $ img_col = ["#FF0000", "#808000", "#00FF00", "#008080", "#0000FF", "#800080"]
    draggroup:
        for i, item in enumerate(current):
            drag:
                drag_name item
                if renpy.can_show(item.lower()):
                    add item.lower()
                else:
                    add SampleImage(item, 150, 150, img_col[i % 6])
                draggable False
                droppable False
                clicked Event("obj_clicked", objname=item)
                if item in obj_prop:
                    properties obj_prop[item]
                else:
                    properties default_obj_prop[item]

screen obj_screen_pos_obj(current,x_pos,y_pos):
    layer "master"
    $ img_col = ["#FF0000", "#808000", "#00FF00", "#008080", "#0000FF", "#800080"]
    draggroup:
        for i, item in enumerate(current):
            drag:
                drag_name item
                if renpy.can_show(item.lower()):
                    add item.lower()
                else:
                    add SampleImage(item, 150, 150, img_col[i % 6])
                draggable False
                droppable False
                clicked Event("obj_clicked", objname=item)
                anchor (0.5,0.5)
                pos (x_pos,y_pos)
                
                
