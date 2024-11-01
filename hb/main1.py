from hitbox import Hitbox

box1 = Hitbox(0, 0, 100, 100)
box2 = Hitbox(75, 50, 100, 100)
box3 = Hitbox(200, 0, 100, 100)

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

