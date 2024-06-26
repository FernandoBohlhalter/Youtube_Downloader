# Centralize the window on the middle of screen
def center_screen(root, app_width, app_height):
    screen_wid = root.winfo_screenwidth() # gets screen res x
    screen_hei = root.winfo_screenheight() #gets screen res y
    x_pos = int(screen_wid/2)
    y_pos = int((screen_hei/2) - (app_height/2))

    root.geometry(f'{app_width}x{app_height}+{x_pos}+{y_pos}')