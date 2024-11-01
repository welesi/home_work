from tank import Tank
from tkinter import*
import world



KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 60
def update():
    player.update()
    enemy.update()
    check_collision()
    w.after(1000//FPS, update)

def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)

def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()

w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.WIDTH, height = world.HEIGHT, bg = 'alice blue')
canv.pack()

player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed=1, bot = False)
enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100, bot = True)

enemy.set_target(player)


w.bind('<KeyPress>', key_press)



update()
w.mainloop()