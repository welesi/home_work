from tank import Tank
import world

_tanks = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv
    player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
    enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
    neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=False)
    neutral.stop()
    enemy.set_target(player)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.inersects(other_tank):
            return True
        return False