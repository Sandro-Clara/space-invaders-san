input.onButtonPressed(Button.A, function () {
    nave.move(-1)
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    shoot = game.createSprite(nave.get(LedSpriteProperty.X), nave.get(LedSpriteProperty.X))
    shoot.change(LedSpriteProperty.Brightness, 88)
    music.play(music.stringPlayable("C5 B A G F E D C ", 1500), music.PlaybackMode.UntilDone)
    for (let index = 0; index < 4; index++) {
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(150)
        if (shoot.isTouching(enemy)) {
            enemy.delete()
            music.play(music.stringPlayable("C D E F G A B C5 ", 3470), music.PlaybackMode.UntilDone)
            shoot.delete()
            game.addScore(1)
        }
    }
    if (shoot.get(LedSpriteProperty.Y) <= 0) {
        shoot.delete()
    }
})
input.onButtonPressed(Button.B, function () {
    nave.move(1)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
})
let enemy: game.LedSprite = null
let shoot: game.LedSprite = null
let nave: game.LedSprite = null
nave = game.createSprite(2, 4)
game.setScore(0)
basic.forever(function () {
    enemy = game.createSprite(randint(0, 4), 0)
    enemy.change(LedSpriteProperty.Brightness, 150)
    basic.pause(100)
    enemy.turn(Direction.Right, 90)
    for (let index = 0; index < 4; index++) {
        enemy.move(1)
        basic.pause(500)
        if (enemy.isTouching(nave)) {
            basic.showString("FIM")
            game.gameOver()
        }
        if (enemy.isTouchingEdge()) {
            enemy.delete()
        }
    }
})
