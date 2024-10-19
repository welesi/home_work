from hitbox import Hitbox

box1 = Hitbox(0, 0, 50, 50)
box2 = Hitbox(50, 50, 50, 50)
box3 = Hitbox(100, 100, 50, 50)

if box1.intersects(box2):
    print("box1 и box2 пересекаются")
else:
    print("box1 и box2 не пересекаются")

if box1.intersects(box3):
    print("box1 и box3 пересекаются")
else:
    print("box1 и box3 не пересекаются")

if box2.intersects(box3):
    print("box2 и box3 пересекаются")
else:
    print("box2 и box3 не пересекаются")

