import pyxel

pyxel.init(128, 128, title="Carre errant")
carre_pos = [60, 60]


def carre_deplacement(pos):
    """Déplace le carré en fonction des touches appuyées."""
    x, y = pos

    if pyxel.btn(pyxel.KEY_RIGHT):
        x += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        x -= 1
    if pyxel.btn(pyxel.KEY_UP):
        y -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        y += 1

    return [x, y]


def update():
    """Met à jour la position du carré à chaque frame."""
    carre_pos[:] = carre_deplacement(carre_pos)


def draw():
    """Dessine le carré à l'écran."""
    pyxel.cls(0)
    pyxel.rect(carre_pos[0], carre_pos[1], 8, 8, 1)


pyxel.run(update, draw)
