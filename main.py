def on_button_pressed_a():
    nave.move(-1)
    music.play(music.tone_playable(523, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(nave.get(LedSpriteProperty.X), nave.get(LedSpriteProperty.X))
    shoot.change(LedSpriteProperty.BRIGHTNESS, 88)
    music.play(music.string_playable("C5 B A G F E D C ", 1500),
        music.PlaybackMode.UNTIL_DONE)
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if shoot.is_touching(enemy):
            enemy.delete()
            music.play(music.string_playable("C D E F G A B C5 ", 3470),
                music.PlaybackMode.UNTIL_DONE)
            shoot.delete()
            game.add_score(1)
    if shoot.get(LedSpriteProperty.Y) <= 0:
        shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    nave.move(1)
    music.play(music.tone_playable(988, music.beat(BeatFraction.SIXTEENTH)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemy: game.LedSprite = None
shoot: game.LedSprite = None
nave: game.LedSprite = None
nave = game.create_sprite(2, 4)
game.set_score(0)

def on_forever():
    global enemy
    enemy = game.create_sprite(randint(0, 4), 0)
    enemy.change(LedSpriteProperty.BRIGHTNESS, 150)
    basic.pause(100)
    enemy.turn(Direction.RIGHT, 90)
    for index2 in range(4):
        enemy.move(1)
        basic.pause(500)
        if enemy.is_touching(nave):
            basic.show_string("FIM")
            game.game_over()
        if enemy.is_touching_edge():
            enemy.delete()
basic.forever(on_forever)
