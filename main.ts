scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile5`, function (sprite4, location4) {
    if (!(controller.B.isPressed())) {
        mySprite.setVelocity(0, 0)
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (not_true) {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d c f . . . . . . . 
            . . f d d e d c d f . . . . . . 
            . f d f f 4 d c d f . f f f f . 
            f e d d d d d c d f f e e d d f 
            f e d d d d c d d f 4 f f b d f 
            f 4 d f f d d d d f 4 f f f c f 
            f e e d d d d d 4 4 e e e d d f 
            f e e 4 e 4 4 4 e e e f f b d f 
            . f 4 4 e e e e f e 4 e e f b f 
            . . f f d b b f f e 4 e e f b f 
            . . . f d d d c . f e 4 4 e d f 
            . . . . f c c . . . f 4 e f f f 
            . . . . . . . f f f f f f . . . 
            . . . . . . f e 4 4 e f . . . . 
            . . . . . . f f f f f . . . . . 
            `,img`
            . . . . . c c c . . . f f f . . 
            . . . c c d d c f f f d d f . . 
            . . f d d 4 d c d f f d b f . . 
            . f d f f e d c d f f f f f . . 
            f e d d d d d c d f f d d f . . 
            f 4 d d d d c d d f e d b f . . 
            f e d f f d d d e 4 4 f f f . . 
            f 4 e d d d d 4 4 4 e e e f . . 
            f 4 4 e 4 e e 4 4 e 4 f f f . . 
            . f e 4 e 4 e e f 4 4 4 e f f . 
            . . f f f d b b f e e 4 e f c f 
            . . . . f d d d c f e e e f d f 
            . . . . . f c c . . f e 4 e d f 
            . . . . . . . . f f f f f f f f 
            . . . . . . . f e 4 e f . . . . 
            . . . . . . . f f f f . . . . . 
            `,img`
            . . . . . c c c . . . . . f f . 
            . . . c c d d d f . . . f d d f 
            . . f d d d 4 d c f . f e d d f 
            . f d d f f e d c f . f f b c f 
            f e d d d d d d c f f e f d d f 
            f e d d d d d c d f e f e d d f 
            f 4 d d f f d d e f 4 4 e c d f 
            f 4 4 d d d d e e 4 4 e f f f f 
            f e e 4 4 4 e 4 4 e 4 4 f f . . 
            . f e 4 e e e e f e e 4 f f . . 
            . . f d b b f f f e e 4 e f f . 
            . . f d d d c . . f 4 4 e f c f 
            . . . f c c . . . . f 4 e f d f 
            . . . . . . f f f f f f f b d f 
            . . . . . f e 4 4 e f . . f f . 
            . . . . . f f f f f . . . . . . 
            `,img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d d f . . . . . . . 
            . . f d d d d e d f . . . f f . 
            . f d d d f f 4 d f . . f d d f 
            f e d d d d d d d f f f e d d f 
            f e d d d d d d c d e f f b c f 
            f 4 e d d f f d d e e e f d d f 
            f e 4 e d d d d 4 e e 4 e d d f 
            f e 4 4 e e e 4 e 4 4 4 e c d f 
            . f e e e 4 4 e f 4 4 e c f f f 
            . f d b b f f f f e 4 e d f f . 
            . f d d d c . . . f e b d f . . 
            . . f c c . . . . . f f f . . . 
            . . . . . f f f f f f f f . . . 
            . . . . . f e e e e f . . . . . 
            . . . . . . f f f f . . . . . . 
            `,img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d c f . . . . f f . 
            . . f d d 4 d c d f . . f b d f 
            . f d f f e d c d f . f e d d f 
            f e d d d d d c d f f 4 4 f f f 
            f 4 d d d d c d d f f e f d d f 
            f e d f f d d d e f e f 4 b d f 
            f 4 4 d d d d e 4 e e 4 e f f f 
            f e 4 e e 4 4 4 4 e 4 4 f b d f 
            . f e e 4 e e e f e 4 f e b d f 
            . . f f d b b f f e 4 4 e f b f 
            . . . f d d d c . f e 4 4 e e f 
            . . . . f c c . . . f f f f f f 
            . . . . . . . . . . . . . f f f 
            . . . . . . . . . . f e 4 4 f f 
            . . . . . . . . . . f f f f f . 
            `],
        100,
        true
        )
        mySprite.setVelocity(0, -100)
    } else {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d c f . . . . . . . 
            . . f d d e d c d f . . . . . . 
            . f d f f e d c d f . f f f f . 
            f e d d d d d c d f f e e d d f 
            f e d d d d c d d f e f f b d f 
            f e d f f d d d d f e f f f c f 
            f e e d d d d d e e e e e d d f 
            f e e e e e e e e e e f f b d f 
            . f e e e e e e f e e e e f b f 
            . . f f d b b f f e e e e f b f 
            . . . f d d d c . f e e e e d f 
            . . . . f c c . . . f e e f f f 
            . . . . . . . f f f f f f . . . 
            . . . . . . f e e e e f . . . . 
            . . . . . . f f f f f . . . . . 
            `,img`
            . . . . . c c c . . . f f f . . 
            . . . c c d d c f f f d d f . . 
            . . f d d e d c d f f d b f . . 
            . f d f f e d c d f f f f f . . 
            f e d d d d d c d f f d d f . . 
            f e d d d d c d d f e d b f . . 
            f e d f f d d d e f e f f f . . 
            f e e d d d d e e e e e e f . . 
            f e e e e e e e e e e f f f . . 
            . f e e e e e e f e e e e f f . 
            . . f f f d b b f e e e e f c f 
            . . . . f d d d c f e e e f d f 
            . . . . . f c c . . f e e e d f 
            . . . . . . . . f f f f f f f f 
            . . . . . . . f e e e f . . . . 
            . . . . . . . f f f f . . . . . 
            `,img`
            . . . . . c c c . . . . . f f . 
            . . . c c d d d f . . . f d d f 
            . . f d d d e d c f . f e d d f 
            . f d d f f e d c f . f f b c f 
            f e d d d d d d c f f e f d d f 
            f e d d d d d c d f e f e d d f 
            f e d d f f d d e f e e e c d f 
            f e e d d d d e e e e e f f f f 
            f e e e e e e e e e e f f f . . 
            . f e e e e e e f e e e f f . . 
            . . f d b b f f f e e e e f f . 
            . . f d d d c . . f e e e f c f 
            . . . f c c . . . . f e e f d f 
            . . . . . . f f f f f f f b d f 
            . . . . . f e e e e f . . f f . 
            . . . . . f f f f f . . . . . . 
            `,img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d d f . . . . . . . 
            . . f d d d d e d f . . . f f . 
            . f d d d f f e d f . . f d d f 
            f e d d d d d d d f f f e d d f 
            f e d d d d d d c d e f f b c f 
            f e e d d f f d d e e e f d d f 
            f e e e d d d d e e e e e d d f 
            f e e e e e e e e e e e e c d f 
            . f e e e e e e f e e e c f f f 
            . f d b b f f f f e e e d f f . 
            . f d d d c . . . f e b d f . . 
            . . f c c . . . . . f f f . . . 
            . . . . . f f f f f f f f . . . 
            . . . . . f e e e e f . . . . . 
            . . . . . . f f f f . . . . . . 
            `,img`
            . . . . . c c c . . . . . . . . 
            . . . c c d d c f . . . . f f . 
            . . f d d e d c d f . . f b d f 
            . f d f f e d c d f . f e d d f 
            f e d d d d d c d f f e e f f f 
            f e d d d d c d d f f e f d d f 
            f e d f f d d d e f e f e b d f 
            f e e d d d d e e e e e e f f f 
            f e e e e e e e e e e e f b d f 
            . f e e e e e e f e e f e b d f 
            . . f f d b b f f e e e e f b f 
            . . . f d d d c . f e e e e e f 
            . . . . f c c . . . f f f f f f 
            . . . . . . . . . . . . . f f f 
            . . . . . . . . . . f e e e f f 
            . . . . . . . . . . f f f f f . 
            `],
        100,
        true
        )
        mySprite.setVelocity(0, -100)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile6`, function (sprite, location) {
    if (!(controller.B.isPressed())) {
        mySprite.setVelocity(0, 0)
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.left.isPressed()) {
        mySprite.setVelocity(-150, 0)
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . f f f f f . . . . . . . 
            . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d 1 1 e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c 1 1 1 1 1 1 c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f 1 f f e e e e f . f e f 
            . . . . f 1 1 1 1 1 1 1 f f e f 
            1 1 1 1 1 1 1 1 1 e e e e f f . 
            . . . f e f f e f 1 1 e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d 1 1 1 1 1 1 1 
            . . . . f f f f f f f f f . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d 1 1 1 1 1 1 1 1 1 1 1 
            . c d f d d f d e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            c d e e d 1 1 1 1 1 1 1 f . . . 
            c 1 1 d d c d d 1 1 1 1 1 1 1 . 
            c c c 1 1 d d e e e b d c . f f 
            . f d d d 1 1 e e f f c . f e f 
            . f f f 1 1 1 1 1 1 1 f . f e f 
            . f f f f e e e e e e 1 1 1 1 1 
            f d d f d d f e f e e e e f f . 
            f d b f d 1 f e f e e e e f . . 
            f f f f f f 1 1 1 f f f e f . . 
            . . . . . . . . . f c d d f . . 
            . . . . . . . . . . f f f f . . 
            `,img`
            . . . . 1 1 f f f . . . . . . . 
            . . . f e e 1 e e f . . . . . . 
            . . f d d d d 1 1 e f f . . . . 
            . c d d d d d d e 1 1 d f . . . 
            . c d f d d 1 1 1 1 1 1 c . . . 
            1 1 1 1 1 d f d e e b d c . 1 1 
            c d e e d d d d e e f 1 1 1 e f 
            c d d d d c d e 1 1 1 . . f e f 
            . f c c c d e e e f f . . f e f 
            . . 1 1 1 1 1 1 1 1 1 1 1 f e f 
            . . . . f e e e e e e e f f f . 
            . . f f e f e e f e e e e f . . 
            . f e 1 1 1 1 1 1 1 1 1 1 1 . . 
            f d d b d d c f f f f f f b f . 
            f d d c d d d f . . f c d d f . 
            . f f f f f f f . . . f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 1 1 1 f . . . . 
            . . f d 1 1 1 e e e d d f . . . 
            . c d d d d d 1 1 e b d c . . . 
            . c d d d d d d e 1 1 1 1 1 1 1 
            c d d f d d f d e e f c . f f . 
            1 1 1 1 1 1 1 d e e f . . f e f 
            c d e e d d d d e e f . . f e f 
            . f d d d c d e e f f . . f e f 
            . . f f f 1 1 1 1 1 1 1 . f e f 
            . . . . f e e e e e e e f f f . 
            . . . . f f e e e e e b f f . . 
            . . . f e f f 1 1 1 1 1 1 1 . . 
            . . f d d b d d c f f f . . . . 
            . . f d d c d d d f f . . . . . 
            . . . f f f f f f f . . . . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d 1 1 1 1 1 1 1 1 1 . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c 1 1 1 1 1 1 1 1 1 1 d c . . . 
            c d d d d c d d e e b d c . . . 
            c c c c c d d e e e f c . . . . 
            . f d d d d e e e f f . . . . . 
            . . f f f f f e 1 1 1 1 1 1 1 . 
            . . . . f f e e 1 e e e f . f f 
            . . . f e e f e e 1 e e f . e f 
            . . f e e f e e f e 1 1 f . e f 
            . f b d 1 1 1 1 1 1 1 1 1 1 1 f 
            . f d d f d d f d d b e f f f f 
            . . f f f f f f f f f f f f f . 
            `],
        100,
        true
        )
        pause(5000)
        mySprite.setVelocity(0, 0)
    } else if (controller.up.isPressed()) {
        mySprite.setVelocity(0, -150)
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . 1 . . . c c c . . . . . 
            . . . . 1 . . f c d d c c . . . 
            . . . . 1 . f d c d e d d f 1 . 
            . f f f 1 . f d c d e f f d 1 . 
            f d d e 1 f 1 d c d d d d d 1 f 
            f d b f 1 1 f d 1 c d d d d 1 f 
            f c f f 1 1 f d 1 d d 1 f d 1 f 
            f d d e 1 1 e e 1 d d 1 d e 1 f 
            f d b f 1 1 e e 1 e e e e e 1 f 
            f 1 f 1 e 1 e f 1 e e e e e 1 . 
            f 1 f 1 e 1 e f 1 b b d f f 1 . 
            f 1 e e e 1 f . c d d d f . 1 . 
            f 1 f e e f . . . c c f . . 1 . 
            . 1 . f f f f f f . . . . . 1 . 
            . 1 . . f e e e e f . . . . 1 . 
            . 1 . . . f f f f f . . . . 1 . 
            `,img`
            . . f f f . . . c c c . . . . . 
            . . f d d f f f c 1 d c c . . . 
            . . f b d f f d c 1 e d d f . . 
            . . f f f f f d 1 d e f f d f . 
            . . f d d f 1 d 1 d d d d d e f 
            . . f 1 d e 1 1 d c 1 d d 1 e f 
            . . 1 f f e 1 1 d d 1 f f 1 e f 
            . . 1 e e e 1 e e d 1 d d 1 e f 
            . . 1 f f e 1 e e 1 1 e e 1 e f 
            . f f e e e 1 f e 1 1 e e 1 f . 
            f c f e e e 1 f b 1 1 f f 1 . . 
            f d f e e 1 f c d 1 1 f . 1 . . 
            f d e e e 1 . . c 1 f . . 1 . . 
            f f f f f 1 f f . 1 . . . 1 . . 
            . . . . f 1 e e f 1 . . . 1 . . 
            . . . . . 1 f f f . . . . 1 . . 
            `,img`
            . f f . . . . . c c 1 . . . . . 
            f d d f . . . f d d 1 c c . . . 
            f d d e f . 1 c d e 1 d d f . . 
            f c b 1 f . 1 c d e 1 f d d f . 
            f d d 1 e f 1 c d d 1 d d d e 1 
            f d d 1 f e 1 d c d d d d d e 1 
            f d c 1 e e 1 e d d f 1 d d 1 f 
            f f f 1 e e 1 e e d d 1 d 1 e f 
            . . f 1 f e 1 e 1 e e 1 e 1 e f 
            . . f 1 e e 1 f 1 e e 1 1 e f . 
            . f f 1 e e 1 f 1 f b 1 1 f . . 
            f c f 1 e e 1 . . 1 d 1 d f . . 
            f d f 1 e f 1 . . 1 c c f . . . 
            f d b 1 f f f f f 1 . . . . . . 
            . f f . . f e e e e 1 . . . . . 
            . . . . . . f f f f 1 . . . . . 
            `,img`
            . . . . . . . . c 1 c . . . . . 
            . . . . . . . f d 1 d c c . . . 
            . f f . . . f d e 1 d d d f . . 
            f d d f . . f d e 1 f d d d f . 
            f d d e f f f d d 1 d d d 1 e f 
            f c b f f e 1 c d 1 d d d 1 e f 
            f d d f e e 1 d d 1 f d d 1 e f 
            f d d 1 e e 1 e d d d d 1 e 1 f 
            f d c 1 e e 1 e e e e e 1 e 1 f 
            f f f 1 e e 1 f e e e 1 e e 1 . 
            . f f 1 e e 1 f f f f 1 b d 1 . 
            . . f 1 b e 1 . . . c 1 d d f . 
            . . . 1 f f . . . . . 1 c f . . 
            . . . 1 f f f f f f f 1 . . . . 
            . . . . . f e e e e f 1 . . . . 
            . . . . . . f f f f . 1 . . . . 
            `,img`
            . . . . . . . . c c c . . . . . 
            . f f . . . . f c d 1 c c . . . 
            f d b f . . f d c d 1 d d f . . 
            f d d e f . f d c d 1 f f d f . 
            f f 1 e e f f d c d 1 d d d e f 
            f d 1 f e f f d d c 1 d d 1 e f 
            f d 1 e f e f e d d 1 f f 1 e f 
            f f 1 e e e e e e d 1 d d 1 e f 
            f d 1 f e 1 1 e e e 1 e e 1 e f 
            f d 1 e 1 e 1 f e e 1 e e 1 f . 
            f b 1 1 e e 1 f f b 1 d f 1 . . 
            f e 1 1 e e 1 . c d d d f 1 . . 
            f f 1 f f f 1 . . c c f . 1 . . 
            f f 1 . . . 1 . . . . . . 1 . . 
            f f 1 e e f 1 . . . . . . . . . 
            . f f f f f . . . . . . . . . . 
            `],
        100,
        true
        )
        pause(5000)
        mySprite.setVelocity(0, 0)
    } else if (controller.down.isPressed()) {
        mySprite.setVelocity(0, 150)
        animation.runImageAnimation(
        mySprite,
        [img`
            . 1 . . . f f f f f . . . . 1 . 
            . 1 . . f e e e e f . . . . 1 . 
            . 1 . f f f f f f . . . . . 1 . 
            f 1 f e e f . . . c c f . . 1 . 
            f 1 e e e 1 f . c d d d f . 1 . 
            f 1 f 1 e 1 e f 1 b b d f f 1 . 
            f 1 f 1 e 1 e f 1 e e e e e 1 . 
            f d b f 1 1 e e 1 e e e e e 1 f 
            f d d e 1 1 e e 1 d d 1 d e 1 f 
            f c f f 1 1 f d 1 d d 1 f d 1 f 
            f d b f 1 1 f d 1 c d d d d 1 f 
            f d d e 1 f 1 d c d d d d d 1 f 
            . f f f 1 . f d c d e f f d 1 . 
            . . . . 1 . f d c d e d d f 1 . 
            . . . . 1 . . f c d d c c . . . 
            . . . . 1 . . . c c c . . . . . 
            `,img`
            . . . . . 1 f f f . . . . 1 . . 
            . . . . f 1 e e f 1 . . . 1 . . 
            f f f f f 1 f f . 1 . . . 1 . . 
            f d e e e 1 . . c 1 f . . 1 . . 
            f d f e e 1 f c d 1 1 f . 1 . . 
            f c f e e e 1 f b 1 1 f f 1 . . 
            . f f e e e 1 f e 1 1 e e 1 f . 
            . . 1 f f e 1 e e 1 1 e e 1 e f 
            . . 1 e e e 1 e e d 1 d d 1 e f 
            . . 1 f f e 1 1 d d 1 f f 1 e f 
            . . f 1 d e 1 1 d c 1 d d 1 e f 
            . . f d d f 1 d 1 d d d d d e f 
            . . f f f f f d 1 d e f f d f . 
            . . f b d f f d c 1 e d d f . . 
            . . f d d f f f c 1 d c c . . . 
            . . f f f . . . c c c . . . . . 
            `,img`
            . . . . . . f f f f 1 . . . . . 
            . f f . . f e e e e 1 . . . . . 
            f d b 1 f f f f f 1 . . . . . . 
            f d f 1 e f 1 . . 1 c c f . . . 
            f c f 1 e e 1 . . 1 d 1 d f . . 
            . f f 1 e e 1 f 1 f b 1 1 f . . 
            . . f 1 e e 1 f 1 e e 1 1 e f . 
            . . f 1 f e 1 e 1 e e 1 e 1 e f 
            f f f 1 e e 1 e e d d 1 d 1 e f 
            f d c 1 e e 1 e d d f 1 d d 1 f 
            f d d 1 f e 1 d c d d d d d e 1 
            f d d 1 e f 1 c d d 1 d d d e 1 
            f c b 1 f . 1 c d e 1 f d d f . 
            f d d e f . 1 c d e 1 d d f . . 
            f d d f . . . f d d 1 c c . . . 
            . f f . . . . . c c 1 . . . . . 
            `,img`
            . . . . . . f f f f . 1 . . . . 
            . . . . . f e e e e f 1 . . . . 
            . . . 1 f f f f f f f 1 . . . . 
            . . . 1 f f . . . . . 1 c f . . 
            . . f 1 b e 1 . . . c 1 d d f . 
            . f f 1 e e 1 f f f f 1 b d 1 . 
            f f f 1 e e 1 f e e e 1 e e 1 . 
            f d c 1 e e 1 e e e e e 1 e 1 f 
            f d d 1 e e 1 e d d d d 1 e 1 f 
            f d d f e e 1 d d 1 f d d 1 e f 
            f c b f f e 1 c d 1 d d d 1 e f 
            f d d e f f f d d 1 d d d 1 e f 
            f d d f . . f d e 1 f d d d f . 
            . f f . . . f d e 1 d d d f . . 
            . . . . . . . f d 1 d c c . . . 
            . . . . . . . . c 1 c . . . . . 
            `,img`
            . f f f f f . . . . . . . . . . 
            f f 1 e e f 1 . . . . . . . . . 
            f f 1 . . . 1 . . . . . . 1 . . 
            f f 1 f f f 1 . . c c f . 1 . . 
            f e 1 1 e e 1 . c d d d f 1 . . 
            f b 1 1 e e 1 f f b 1 d f 1 . . 
            f d 1 e 1 e 1 f e e 1 e e 1 f . 
            f d 1 f e 1 1 e e e 1 e e 1 e f 
            f f 1 e e e e e e d 1 d d 1 e f 
            f d 1 e f e f e d d 1 f f 1 e f 
            f d 1 f e f f d d c 1 d d 1 e f 
            f f 1 e e f f d c d 1 d d d e f 
            f d d e f . f d c d 1 f f d f . 
            f d b f . . f d c d 1 d d f . . 
            . f f . . . . f c d 1 c c . . . 
            . . . . . . . . c c c . . . . . 
            `],
        100,
        true
        )
        pause(5000)
        mySprite.setVelocity(0, 0)
    } else if (controller.right.isPressed()) {
        mySprite.setVelocity(150, 0)
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . . . f f f f f . . . . 
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 . . 
            . . . . . f e e e d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e 1 1 d d f d c . 
            . . . c d b e e d d d d e e d c 
            f f . c d b e e d d c d d d d c 
            f e f . c 1 1 1 1 1 1 c c c c c 
            f e f . . f f e e d d d d d f . 
            f e f . f e e e e f f 1 f f . . 
            f e f f 1 1 1 1 1 1 1 f . . . . 
            . f f e e e e 1 1 1 1 1 1 1 1 1 
            . . f e e 1 1 f e f f e f . . . 
            . . . f e f f b d f b d f . . . 
            1 1 1 1 1 1 1 d d c d d f . . . 
            . . . f f f f f f f f f . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            1 1 1 1 1 1 1 1 1 1 1 d d f . . 
            . . . . . f e e d f d d f d c . 
            . . . . f f e e d f d d f d c . 
            . . . f 1 1 1 1 1 1 1 d e e d c 
            . 1 1 1 1 1 1 1 d d c d d 1 1 c 
            f f . c d b e e e d d 1 1 c c c 
            f e f . c f f e e 1 1 d d d f . 
            f e f . f 1 1 1 1 1 1 1 f f f . 
            1 1 1 1 1 e e e e e e f f f f . 
            . f f e e e e f e f d d f d d f 
            . . f e e e e f e f 1 d f b d f 
            . . f e f f f 1 1 1 f f f f f f 
            . . f d d c f . . . . . . . . . 
            . . f f f f . . . . . . . . . . 
            `,img`
            . . . . . . . f f f 1 1 . . . . 
            . . . . . . f e e 1 e e f . . . 
            . . . . f f e 1 1 d d d d f . . 
            . . . f d 1 1 e d d d d d d c . 
            . . . c 1 1 1 1 1 1 d d f d c . 
            1 1 . c d b e e d f d 1 1 1 1 1 
            f e 1 1 1 f e e d d d d e e d c 
            f e f . . 1 1 1 e d c d d d d c 
            f e f . . f f e e e d c c c f . 
            f e f 1 1 1 1 1 1 1 1 1 1 1 . . 
            . f f f e e e e e e e f . . . . 
            . . f e e e e f e e f e f f . . 
            . . 1 1 1 1 1 1 1 1 1 1 1 e f . 
            . f b f f f f f f c d d b d d f 
            . f d d c f . . f d d d c d d f 
            . . f f f . . . f f f f f f f . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . f 1 1 1 1 e e e f . . . 
            . . . f d d e e e 1 1 1 d f . . 
            . . . c d b e 1 1 d d d d d c . 
            1 1 1 1 1 1 1 e d d d d d d c . 
            . f f . c f e e d f d d f d d c 
            f e f . . f e e d 1 1 1 1 1 1 1 
            f e f . . f e e d d d d e e d c 
            f e f . . f f e e d c d d d f . 
            f e f . 1 1 1 1 1 1 1 f f f . . 
            . f f f e e e e e e e f . . . . 
            . . f f b e e e e e f f . . . . 
            . . 1 1 1 1 1 1 1 f f e f . . . 
            . . . . f f f c d d b d d f . . 
            . . . . . f f d d d c d d f . . 
            . . . . . . f f f f f f f . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . 1 1 1 1 1 1 1 1 1 d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d 1 1 1 1 1 1 1 1 1 1 c 
            . . . c d b e e d d c d d d d c 
            . . . . c f e e e d d c c c c c 
            . . . . . f f e e e d d d d f . 
            . 1 1 1 1 1 1 1 e f f f f f . . 
            f f . f e e e 1 e e f f . . . . 
            f e . f e e 1 e e f e e f . . . 
            f e . f 1 1 e f e e f e e f . . 
            f 1 1 1 1 1 1 1 1 1 1 1 d b f . 
            f f f f e b d d f d d f d d f . 
            . f f f f f f f f f f f f f . . 
            `],
        100,
        true
        )
        pause(5000)
        mySprite.setVelocity(0, 0)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setFlag(SpriteFlag.Ghost, true)
    mySprite.setImage(img`
        . . . . . . . f f f f f . . . . 
        . . . . . . f . . . . . f . . . 
        . . . . . f . . . . . . . f . . 
        . . . . f f . . . . . . . . c . 
        . . . f . . . . . . . . . . c . 
        . . . c . . . . . . . . . . . c 
        f f . c . . . . . . c . . . . c 
        f . f . c f . . . . . c c c c c 
        f . f . . f f . . . . . . . f . 
        f . f . f . . . . f f f f f . . 
        f . f f . . . . . . . f . . . . 
        . f f . . . . f . f f . f . . . 
        . . f . . . . f . f f . f . . . 
        . . . f . f f . . f . . f . . . 
        . . . f d b b . . c . . f . . . 
        . . . f f f f f f f f f . . . . 
        `)
    myEnemy.follow(mySprite, 0)
    info.startCountdown(10)
    pause(9950)
    info.stopCountdown()
    mySprite.setFlag(SpriteFlag.Ghost, false)
    mySprite.setImage(img`
        . . . . f f f f f . . . . . . . 
        . . . f e e e e 4 f . . . . . . 
        . . f d d d d e e e f . . . . . 
        . c d f d d f d 4 e f f . . . . 
        . c d f d d f d e 4 d d f . . . 
        c d e 4 d d d d e 4 b d c . . . 
        c d d d d c d d e e b d c . f f 
        c c c c c d d d e e f c . f e f 
        . f d d d d d 4 4 f f . . f 4 f 
        . . f f f f f 4 e e e f . f e f 
        . . . . f e 4 4 e e e 4 f f e f 
        . . . f e f f 4 f e 4 e e f f . 
        . . . f e f f e f e e 4 e f . . 
        . . . f d b f d b f f 4 f . . . 
        . . . f d d c d d b b d f . . . 
        . . . . f f f f f f f f f . . . 
        `)
    myEnemy.follow(mySprite, speed)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava1, function (sprite3, location3) {
    info.changeLifeBy(-1)
    mySprite.setVelocity(0, 0)
    mySprite.setVelocity(50, 50)
    pause(100)
    mySprite.setVelocity(50, 50)
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setVelocity(0, 0)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (not_true) {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . f f f f f . . . . . . . 
            . . . f e e 4 e e f . . . . . . 
            . . f d d d d e e 4 f . . . . . 
            . c d f d d f d 4 4 f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e 4 d d d d 4 e b d c . . . 
            c d d d d c d d 4 e b d c . f f 
            c c c c c d d d 4 e f c . f e f 
            . f d d d d d 4 e f f . . f 4 f 
            . . f f f f f 4 e e e f . f 4 f 
            . . . . f 4 4 e e 4 4 e f f e f 
            . . . f e f f e f e e 4 4 f f . 
            . . . f e f f e f e e 4 e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e 4 e 4 4 f . . . . . . 
            . . f d d d d e 4 e f . . . . . 
            . c d f d d f d e 4 f . . . . . 
            . c d f d d f d 4 e f f . . . . 
            c d 4 e d d d d e 4 d d f . . . 
            c d d d d c d d e e b d c . . . 
            c c c c c d d 4 4 e b d c . f f 
            . f d d d d e 4 4 f f c . f e f 
            . f f f f f 4 4 e 4 e f . f 4 f 
            . f f f f e 4 e 4 4 e e f f e f 
            f d d f d d f e f 4 4 e e f f . 
            f d b f d b f e f e e e 4 f . . 
            f f f f f f f f f f f f e f . . 
            . . . . . . . . . f c d d f . . 
            . . . . . . . . . . f f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e 4 4 e f . . . . . . 
            . . f d d d d 4 e e f f . . . . 
            . c d d d d d d 4 4 d d f . . . 
            . c d f d d f d 4 e b d c . . . 
            c d d f d d f d 4 e b d c . f f 
            c d 4 e d d d d e e f c . f e f 
            c d d d d c d e 4 e f . . f 4 f 
            . f c c c d e e 4 f f . . f 4 f 
            . . f f f f f 4 e e e f . f e f 
            . . . . f e 4 4 4 e e 4 f f f . 
            . . f f e f 4 e 4 4 4 4 4 f . . 
            . f e f f e e f f f e e e f . . 
            f d d b d d c f f f f f f b f . 
            f d d c d d d f . . f c d d f . 
            . f f f f f f f . . . f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e 4 e e f f f . . . . 
            . . f d d d e 4 4 e d d f . . . 
            . c d d d d d e 4 e b d c . . . 
            . c d d d d d d e e b d c . . . 
            c d d f d d f d e 4 f c . f f . 
            c d d f d d f d e 4 f . . f e f 
            c d e 4 d d d d 4 e f . . f e f 
            . f d d d c d 4 e f f . . f e f 
            . . f f f d e e 4 4 e f . f e f 
            . . . . f e e e 4 4 4 e f f f . 
            . . . . f f e 4 4 e e b f f . . 
            . . . f e f f e e c d d f f . . 
            . . f d d b d d c f f f . . . . 
            . . f d d c d d d f f . . . . . 
            . . . f f f f f f f . . . . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e 4 e 4 e f . . . . . . 
            . . f d d d d 4 4 e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e 4 d d f . . . 
            c d 4 e d d d d 4 e b d c . . . 
            c d d d d c d d 4 e b d c . . . 
            c c c c c d d e 4 e f c . . . . 
            . f d d d d e 4 4 f f . . . . . 
            . . f f f f f e e e e f . . . . 
            . . . . f f e e 4 4 4 e f . f f 
            . . . f 4 e f 4 4 f 4 4 f . e f 
            . . f e 4 f 4 e f e e 4 f . 4 f 
            . f b d f d b f b b f e f f 4 f 
            . f d d f d d f d d b e f f f f 
            . . f f f f f f f f f f f f f . 
            `],
        100,
        true
        )
        mySprite.setVelocity(-100, 0)
    } else {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f e f 
            . . . f e f f e f e e e e f f . 
            . . . f e f f e f e e e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            c d e e d d d d e e d d f . . . 
            c d d d d c d d e e b d c . . . 
            c c c c c d d e e e b d c . f f 
            . f d d d d e e e f f c . f e f 
            . f f f f f f e e e e f . f e f 
            . f f f f e e e e e e e f f e f 
            f d d f d d f e f e e e e f f . 
            f d b f d b f e f e e e e f . . 
            f f f f f f f f f f f f e f . . 
            . . . . . . . . . f c d d f . . 
            . . . . . . . . . . f f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f f . . . . 
            . c d d d d d d e e d d f . . . 
            . c d f d d f d e e b d c . . . 
            c d d f d d f d e e b d c . f f 
            c d e e d d d d e e f c . f e f 
            c d d d d c d e e e f . . f e f 
            . f c c c d e e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f f . 
            . . f f e f e e f e e e e f . . 
            . f e f f e e f f f e e e f . . 
            f d d b d d c f f f f f f b f . 
            f d d c d d d f . . f c d d f . 
            . f f f f f f f . . . f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f f f . . . . 
            . . f d d d e e e e d d f . . . 
            . c d d d d d e e e b d c . . . 
            . c d d d d d d e e b d c . . . 
            c d d f d d f d e e f c . f f . 
            c d d f d d f d e e f . . f e f 
            c d e e d d d d e e f . . f e f 
            . f d d d c d e e f f . . f e f 
            . . f f f d e e e e e f . f e f 
            . . . . f e e e e e e e f f f . 
            . . . . f f e e e e e b f f . . 
            . . . f e f f e e c d d f f . . 
            . . f d d b d d c f f f . . . . 
            . . f d d c d d d f f . . . . . 
            . . . f f f f f f f . . . . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . . . 
            c c c c c d d e e e f c . . . . 
            . f d d d d e e e f f . . . . . 
            . . f f f f f e e e e f . . . . 
            . . . . f f e e e e e e f . f f 
            . . . f e e f e e f e e f . e f 
            . . f e e f e e f e e e f . e f 
            . f b d f d b f b b f e f f e f 
            . f d d f d d f d d b e f f f f 
            . . f f f f f f f f f f f f f . 
            `],
        100,
        true
        )
        mySprite.setVelocity(-100, 0)
    }
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setVelocity(0, 0)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setVelocity(0, 0)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (not_true) {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e 4 e e f . . . 
            . . . . . f 4 e e d d d d f . . 
            . . . . f f 4 4 d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d b e 4 d d d d 4 e d c 
            f f . c d b e 4 d d c d d d d c 
            f e f . c f e 4 d d d c c c c c 
            f 4 f . . f f e 4 d d d d d f . 
            f 4 f . f e e e 4 f f f f f . . 
            f e f f e 4 4 e e 4 4 f . . . . 
            . f f 4 4 e e f e f f e f . . . 
            . . f e 4 e e f e f f e f . . . 
            . . . f e f f b d f b d f . . . 
            . . . f d b b d d c d d f . . . 
            . . . f f f f f f f f f . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f 4 4 e 4 e f . . . 
            . . . . . f e 4 e d d d d f . . 
            . . . . . f 4 e d f d d f d c . 
            . . . . f f e 4 d f d d f d c . 
            . . . f d d 4 e d d d d e 4 d c 
            . . . c d b e e d d c d d d d c 
            f f . c d b e 4 4 d d c c c c c 
            f e f . c f f 4 4 e d d d d f . 
            f 4 f . f e 4 e 4 4 f f f f f . 
            f e f f e e 4 4 e 4 e f f f f . 
            . f f e e 4 4 f e f d d f d d f 
            . . f 4 e e e f e f b d f b d f 
            . . f e f f f f f f f f f f f f 
            . . f d d c f . . . . . . . . . 
            . . f f f f . . . . . . . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e 4 4 e e f . . . 
            . . . . f f e e 4 d d d d f . . 
            . . . f d d 4 4 d d d d d d c . 
            . . . c d b e 4 d f d d f d c . 
            f f . c d b e 4 d f d d f d d c 
            f e f . c f e e d d d d e 4 d c 
            f 4 f . . f e 4 e d c d d d d c 
            f 4 f . . f f 4 e e d c c c f . 
            f e f . f e e e 4 f f f f f . . 
            . f f f 4 e e 4 4 4 e f . . . . 
            . . f 4 4 4 4 4 e 4 f e f f . . 
            . . f e e e f f f e e f f e f . 
            . f b f f f f f f c d d b d d f 
            . f d d c f . . f d d d c d d f 
            . . f f f . . . f f f f f f f . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . f f f e e 4 e e f . . . 
            . . . f d d e 4 4 e d d d f . . 
            . . . c d b e 4 e d d d d d c . 
            . . . c d b e e d d d d d d c . 
            . f f . c f 4 e d f d d f d d c 
            f e f . . f 4 e d f d d f d d c 
            f e f . . f e 4 d d d d 4 e d c 
            f e f . . f f e 4 d c d d d f . 
            f e f . f e 4 4 e e d f f f . . 
            . f f f e 4 4 4 e e e f . . . . 
            . . f f b e e 4 4 e f f . . . . 
            . . f f d d c e e f f e f . . . 
            . . . . f f f c d d b d d f . . 
            . . . . . f f d d d c d d f . . 
            . . . . . . f f f f f f f . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e 4 e 4 e f . . . 
            . . . . . f e 4 4 d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d 4 e d f d d f d c . 
            . . . c d b e 4 d d d d e 4 d c 
            . . . c d b e 4 d d c d d d d c 
            . . . . c f e 4 e d d c c c c c 
            . . . . . f f 4 4 e d d d d f . 
            . . . . f e e e e f f f f f . . 
            f f . f e 4 4 4 e e f f . . . . 
            f e . f 4 4 f 4 4 f e 4 f . . . 
            f 4 . f 4 e e f e 4 f 4 e f . . 
            f 4 f f e f b b f b d f d b f . 
            f f f f e b d d f d d f d d f . 
            . f f f f f f f f f f f f f . . 
            `],
        100,
        true
        )
        mySprite.setVelocity(100, 0)
    } else {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . . f e e e d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d b e e d d d d e e d c 
            f f . c d b e e d d c d d d d c 
            f e f . c f e e d d d c c c c c 
            f e f . . f f e e d d d d d f . 
            f e f . f e e e e f f f f f . . 
            f e f f e e e e e e e f . . . . 
            . f f e e e e f e f f e f . . . 
            . . f e e e e f e f f e f . . . 
            . . . f e f f b d f b d f . . . 
            . . . f d b b d d c d d f . . . 
            . . . f f f f f f f f f . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . . f e e e d d d d f . . 
            . . . . . f e e d f d d f d c . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d d d d e e d c 
            . . . c d b e e d d c d d d d c 
            f f . c d b e e e d d c c c c c 
            f e f . c f f e e e d d d d f . 
            f e f . f e e e e f f f f f f . 
            f e f f e e e e e e e f f f f . 
            . f f e e e e f e f d d f d d f 
            . . f e e e e f e f b d f b d f 
            . . f e f f f f f f f f f f f f 
            . . f d d c f . . . . . . . . . 
            . . f f f f . . . . . . . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . f f e e e d d d d f . . 
            . . . f d d e e d d d d d d c . 
            . . . c d b e e d f d d f d c . 
            f f . c d b e e d f d d f d d c 
            f e f . c f e e d d d d e e d c 
            f e f . . f e e e d c d d d d c 
            f e f . . f f e e e d c c c f . 
            f e f . f e e e e f f f f f . . 
            . f f f e e e e e e e f . . . . 
            . . f e e e e f e e f e f f . . 
            . . f e e e f f f e e f f e f . 
            . f b f f f f f f c d d b d d f 
            . f d d c f . . f d d d c d d f 
            . . f f f . . . f f f f f f f . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . f f f e e e e e f . . . 
            . . . f d d e e e e d d d f . . 
            . . . c d b e e e d d d d d c . 
            . . . c d b e e d d d d d d c . 
            . f f . c f e e d f d d f d d c 
            f e f . . f e e d f d d f d d c 
            f e f . . f e e d d d d e e d c 
            f e f . . f f e e d c d d d f . 
            f e f . f e e e e e d f f f . . 
            . f f f e e e e e e e f . . . . 
            . . f f b e e e e e f f . . . . 
            . . f f d d c e e f f e f . . . 
            . . . . f f f c d d b d d f . . 
            . . . . . f f d d d c d d f . . 
            . . . . . . f f f f f f f . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . . f e e e d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d b e e d d d d e e d c 
            . . . c d b e e d d c d d d d c 
            . . . . c f e e e d d c c c c c 
            . . . . . f f e e e d d d d f . 
            . . . . f e e e e f f f f f . . 
            f f . f e e e e e e f f . . . . 
            f e . f e e f e e f e e f . . . 
            f e . f e e e f e e f e e f . . 
            f e f f e f b b f b d f d b f . 
            f f f f e b d d f d d f d d f . 
            . f f f f f f f f f f f f f . . 
            `],
        100,
        true
        )
        mySprite.setVelocity(100, 0)
    }
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setVelocity(0, 0)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (not_true) {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . . f f f f f . . . . . 
            . . . . . . f e 4 4 e f . . . . 
            . . . . . . . f f f f f f . . . 
            . . . . f c c . . . f 4 e f f f 
            . . . f d d d c . f e 4 4 e d f 
            . . f f d b b f f e 4 e e f b f 
            . f 4 4 e e e e f e 4 e e f b f 
            f e e 4 e 4 4 4 e e e f f b d f 
            f e e d d d d d 4 4 e e e d d f 
            f 4 d f f d d d d f 4 f f f c f 
            f e d d d d c d d f 4 f f b d f 
            f e d d d d d c d f f e e d d f 
            . f d f f 4 d c d f . f f f f . 
            . . f d d e d c d f . . . . . . 
            . . . c c d d c f . . . . . . . 
            . . . . . c c c . . . . . . . . 
            `,img`
            . . . . . . . f f f f . . . . . 
            . . . . . . . f e 4 e f . . . . 
            . . . . . . . . f f f f f f f f 
            . . . . . f c c . . f e 4 e d f 
            . . . . f d d d c f e e e f d f 
            . . f f f d b b f e e 4 e f c f 
            . f e 4 e 4 e e f 4 4 4 e f f . 
            f 4 4 e 4 e e 4 4 e 4 f f f . . 
            f 4 e d d d d 4 4 4 e e e f . . 
            f e d f f d d d e 4 4 f f f . . 
            f 4 d d d d c d d f e d b f . . 
            f e d d d d d c d f f d d f . . 
            . f d f f e d c d f f f f f . . 
            . . f d d 4 d c d f f d b f . . 
            . . . c c d d c f f f d d f . . 
            . . . . . c c c . . . f f f . . 
            `,img`
            . . . . . f f f f f . . . . . . 
            . . . . . f e 4 4 e f . . f f . 
            . . . . . . f f f f f f f b d f 
            . . . f c c . . . . f 4 e f d f 
            . . f d d d c . . f 4 4 e f c f 
            . . f d b b f f f e e 4 e f f . 
            . f e 4 e e e e f e e 4 f f . . 
            f e e 4 4 4 e 4 4 e 4 4 f f . . 
            f 4 4 d d d d e e 4 4 e f f f f 
            f 4 d d f f d d e f 4 4 e c d f 
            f e d d d d d c d f e f e d d f 
            f e d d d d d d c f f e f d d f 
            . f d d f f e d c f . f f b c f 
            . . f d d d 4 d c f . f e d d f 
            . . . c c d d d f . . . f d d f 
            . . . . . c c c . . . . . f f . 
            `,img`
            . . . . . . f f f f . . . . . . 
            . . . . . f e e e e f . . . . . 
            . . . . . f f f f f f f f . . . 
            . . f c c . . . . . f f f . . . 
            . f d d d c . . . f e b d f . . 
            . f d b b f f f f e 4 e d f f . 
            . f e e e 4 4 e f 4 4 e c f f f 
            f e 4 4 e e e 4 e 4 4 4 e c d f 
            f e 4 e d d d d 4 e e 4 e d d f 
            f 4 e d d f f d d e e e f d d f 
            f e d d d d d d c d e f f b c f 
            f e d d d d d d d f f f e d d f 
            . f d d d f f 4 d f . . f d d f 
            . . f d d d d e d f . . . f f . 
            . . . c c d d d f . . . . . . . 
            . . . . . c c c . . . . . . . . 
            `,img`
            . . . . . . . . . . f f f f f . 
            . . . . . . . . . . f e 4 4 f f 
            . . . . . . . . . . . . . f f f 
            . . . . f c c . . . f f f f f f 
            . . . f d d d c . f e 4 4 e e f 
            . . f f d b b f f e 4 4 e f b f 
            . f e e 4 e e e f e 4 f e b d f 
            f e 4 e e 4 4 4 4 e 4 4 f b d f 
            f 4 4 d d d d e 4 e e 4 e f f f 
            f e d f f d d d e f e f 4 b d f 
            f 4 d d d d c d d f f e f d d f 
            f e d d d d d c d f f 4 4 f f f 
            . f d f f e d c d f . f e d d f 
            . . f d d 4 d c d f . . f b d f 
            . . . c c d d c f . . . . f f . 
            . . . . . c c c . . . . . . . . 
            `],
        100,
        true
        )
        mySprite.setVelocity(0, 100)
    } else {
        animation.runImageAnimation(
        mySprite,
        [img`
            . . . . . . f f f f f . . . . . 
            . . . . . . f e 4 4 e f . . . . 
            . . . . . . . f f f f f f . . . 
            . . . . f c c . . . f 4 e f f f 
            . . . f d d d c . f e 4 4 e d f 
            . . f f d b b f f e 4 e e f b f 
            . f 4 4 e e e e f e 4 e e f b f 
            f e e 4 e 4 4 4 e e e f f b d f 
            f e e d d d d d 4 4 e e e d d f 
            f 4 d f f d d d d f 4 f f f c f 
            f e d d d d c d d f 4 f f b d f 
            f e d d d d d c d f f e e d d f 
            . f d f f 4 d c d f . f f f f . 
            . . f d d e d c d f . . . . . . 
            . . . c c d d c f . . . . . . . 
            . . . . . c c c . . . . . . . . 
            `,img`
            . . . . . . . f f f f . . . . . 
            . . . . . . . f e 4 e f . . . . 
            . . . . . . . . f f f f f f f f 
            . . . . . f c c . . f e 4 e d f 
            . . . . f d d d c f e e e f d f 
            . . f f f d b b f e e 4 e f c f 
            . f e 4 e 4 e e f 4 4 4 e f f . 
            f 4 4 e 4 e e 4 4 e 4 f f f . . 
            f 4 e d d d d 4 4 4 e e e f . . 
            f e d f f d d d e 4 4 f f f . . 
            f 4 d d d d c d d f e d b f . . 
            f e d d d d d c d f f d d f . . 
            . f d f f e d c d f f f f f . . 
            . . f d d 4 d c d f f d b f . . 
            . . . c c d d c f f f d d f . . 
            . . . . . c c c . . . f f f . . 
            `,img`
            . . . . . f f f f f . . . . . . 
            . . . . . f e 4 4 e f . . f f . 
            . . . . . . f f f f f f f b d f 
            . . . f c c . . . . f 4 e f d f 
            . . f d d d c . . f 4 4 e f c f 
            . . f d b b f f f e e 4 e f f . 
            . f e 4 e e e e f e e 4 f f . . 
            f e e 4 4 4 e 4 4 e 4 4 f f . . 
            f 4 4 d d d d e e 4 4 e f f f f 
            f 4 d d f f d d e f 4 4 e c d f 
            f e d d d d d c d f e f e d d f 
            f e d d d d d d c f f e f d d f 
            . f d d f f e d c f . f f b c f 
            . . f d d d 4 d c f . f e d d f 
            . . . c c d d d f . . . f d d f 
            . . . . . c c c . . . . . f f . 
            `,img`
            . . . . . . f f f f . . . . . . 
            . . . . . f e e e e f . . . . . 
            . . . . . f f f f f f f f . . . 
            . . f c c . . . . . f f f . . . 
            . f d d d c . . . f e b d f . . 
            . f d b b f f f f e 4 e d f f . 
            . f e e e 4 4 e f 4 4 e c f f f 
            f e 4 4 e e e 4 e 4 4 4 e c d f 
            f e 4 e d d d d 4 e e 4 e d d f 
            f 4 e d d f f d d e e e f d d f 
            f e d d d d d d c d e f f b c f 
            f e d d d d d d d f f f e d d f 
            . f d d d f f 4 d f . . f d d f 
            . . f d d d d e d f . . . f f . 
            . . . c c d d d f . . . . . . . 
            . . . . . c c c . . . . . . . . 
            `,img`
            . . . . . . . . . . f f f f f . 
            . . . . . . . . . . f e 4 4 f f 
            . . . . . . . . . . . . . f f f 
            . . . . f c c . . . f f f f f f 
            . . . f d d d c . f e 4 4 e e f 
            . . f f d b b f f e 4 4 e f b f 
            . f e e 4 e e e f e 4 f e b d f 
            f e 4 e e 4 4 4 4 e 4 4 f b d f 
            f 4 4 d d d d e 4 e e 4 e f f f 
            f e d f f d d d e f e f 4 b d f 
            f 4 d d d d c d d f f e f d d f 
            f e d d d d d c d f f 4 4 f f f 
            . f d f f e d c d f . f e d d f 
            . . f d d 4 d c d f . . f b d f 
            . . . c c d d c f . . . . f f . 
            . . . . . c c c . . . . . . . . 
            `],
        100,
        true
        )
        mySprite.setVelocity(0, 100)
    }
})
function spawn (sprite: Sprite, pos_x: number, pos_y: number) {
    sprite.setPosition(pos_x, pos_y)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile7`, function (sprite2, location2) {
    if (!(controller.B.isPressed())) {
        mySprite.setVelocity(0, 0)
    }
})
info.player1.onLifeZero(function () {
    game.splash("You survived " + time + " seconds")
    game.over(false)
})
let enemy_y = 0
let enemy_x = 0
let loop1 = 0
let index = 0
let sprite_y = 0
let sprite_x = 0
let opp_y = 0
let opp_x = 0
let myEnemy: Sprite = null
let mySprite: Sprite = null
let not_true = false
let speed = 0
let time = 0
time = 0
speed = 25
not_true = true
mySprite = sprites.create(img`
    . . . . . . . f f f f f . . . . 
    . . . . . . f e e e e e f . . . 
    . . . . . f e e e d d d d f . . 
    . . . . f f e e d f d d f d c . 
    . . . f d d e e d f d d f d c . 
    . . . c d b e e d d d d e e d c 
    f f . c d b e e d d c d d d d c 
    f e f . c f e e d d d c c c c c 
    f e f . . f f e e d d d d d f . 
    f e f . f e e e e f f f f f . . 
    f e f f e e e e e e e f . . . . 
    . f f e e e e f e f f e f . . . 
    . . f e e e e f e f f e f . . . 
    . . . f e f f b d f b d f . . . 
    . . . f d b b d d c d d f . . . 
    . . . f f f f f f f f f . . . . 
    `, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`level1`)
scene.cameraFollowSprite(mySprite)
mySprite.setBounceOnWall(true)
let list2 = [3, 1, 2]
info.setLife(1)
let mySprite2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
myEnemy = sprites.create(img`
    . . . . f f f f f . . . . . . . 
    . . . f e e e e 4 f . . . . . . 
    . . f d d d d e e e f . . . . . 
    . c d f d d f d 4 e f f . . . . 
    . c d f d d f d e 4 d d f . . . 
    c d e 4 d d d d e 4 b d c . . . 
    c d d d d c d d e e b d c . f f 
    c c c c c d d d e e f c . f e f 
    . f d d d d d 4 4 f f . . f 4 f 
    . . f f f f f 4 e e e f . f e f 
    . . . . f e 4 4 e e e 4 f f e f 
    . . . f e f f 4 f e 4 e e f f . 
    . . . f e f f e f e e 4 e f . . 
    . . . f d b f d b f f 4 f . . . 
    . . . f d d c d d b b d f . . . 
    . . . . f f f f f f f f f . . . 
    `, SpriteKind.Enemy)
if (list2._pickRandom() == 1) {
    spawn(myEnemy, 120, 80)
} else if (list2._pickRandom() == 2) {
    spawn(myEnemy, 100, 60)
} else if (list2._pickRandom() == 3) {
    spawn(myEnemy, 70, 80)
} else {
    spawn(myEnemy, randint(60, 90), randint(90, 120))
}
forever(function () {
    mySprite2.setPosition(opp_x, opp_y)
    if (mySprite.overlapsWith(myEnemy)) {
        not_true = false
        animation.runImageAnimation(
        myEnemy,
        [img`
            . . . . f f f f f . . . . . . . 
            . . . f e 4 e e 4 f . . . . . . 
            . . f d d d d e 4 e f . . . . . 
            . c d f d d f d e 4 f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e 4 d d d d 4 e b d c . . . 
            c d d d d c d d e 4 b d c . . . 
            c c c c c d d e 4 e f c . . . . 
            . f d d d d e 4 e f f . . . . . 
            . . f f f f f 4 e e 4 f . . . . 
            . . . . f f e e e e 4 e f . f f 
            . . . f e 4 f e e f e 4 f . 4 f 
            . . f e 4 f 4 e f e e e f . e f 
            . f b d f d b f b b f e f f e f 
            . f d d f d d f d d b e f f f f 
            . . f f f f f f f f f f f f f . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e 4 e e 4 f . . . . . . 
            . . f d d d d 4 4 4 f . . . . . 
            . c d f d d f d 4 e f f . . . . 
            . c d f d d f d 4 e d d f . . . 
            c d e 4 d d d d 4 e b d c . . . 
            c d d d d c d d 4 e b d c . . . 
            c c c c c d d e e e f c . . . . 
            . f d d d d 4 e e 4 f . . . . . 
            . . f 4 e 4 f f e e 4 f . . . . 
            . . f f f f f e 4 e 4 e f . f f 
            . . f d b f 4 4 f f 4 e f . e f 
            . f f d d f e f f e e 4 f . 4 f 
            . f f f f f f 4 b b f e f f e f 
            . f d d f 4 e e d d b e f f f f 
            . . f f f f f f f f f f f f f . 
            `,img`
            . . . . . f f f f f . . . . . . 
            . . . . f 4 e e 4 e f . . . . . 
            . . . f d d d d d e 4 f . . . . 
            . . f f f d d f f d 4 f f . . . 
            . c d d e 4 d d d d e d d f . . 
            . c c d d d d c d d e d f f f . 
            . c d c c c c d d d e d f b d f 
            . . c d d d d d d 4 e f f d d f 
            . . . c d d d d 4 e f f e f f f 
            . . . . f f f e 4 f e e 4 f . . 
            . . . . f e e e 4 4 e 4 f f f . 
            . . . f e 4 4 4 e e f f f 4 f . 
            . . f f e e e 4 f f f f f 4 f . 
            . f b d f e e f b b f f f e f . 
            . f d d f e e f d d b f f f f . 
            . f f f f f f f f f f f f f . . 
            `,img`
            . . . . . f f f f f . . . . . . 
            . . . . f e 4 e 4 e f . . . . . 
            . . . f d d d d d d e f . . . . 
            . . f d f f d d f f d f f . . . 
            . c d d d 4 e d d d d 4 d f . . 
            . c d c d d d d c d d 4 f f . . 
            . c d d c c c c d d d 4 f f f f 
            . . c d d d d d d d e f f b d f 
            . . . c d d d d 4 e f f f d d f 
            . . . . f f f e e f e 4 e f f f 
            . . . . f e e 4 4 e e 4 f f f . 
            . . . f e e 4 e 4 e f f f e f . 
            . . f f e 4 e e f f f f f 4 f . 
            . f b d f e e f b b f f f e f . 
            . f d d f f f f d d b f f f f . 
            . f f f f f f f f f f f f f . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f . . . . . . . 
            . . . f e e 4 4 4 f . . . . . . 
            . . f d d d d e 4 4 f . . . . . 
            . . f d d d d d 4 e f f . . . . 
            . c d d d f f d 4 e d d f . . . 
            c d e 4 d d d d e e b d c . . . 
            c f f d d c d d e 4 b d c . . . 
            f d d f e f f f e e e f . . . . 
            f d d f e 4 e f f f f f . . . . 
            f f f f f e 4 4 e e f f . f f . 
            . f f f e 4 f e 4 e f f . 4 f . 
            . f b d f 4 f f b b f f f e f . 
            . f d d f e e f d d b f f e f . 
            . f f f f f f f f f f f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d 4 4 e f . . . . . 
            . . f d d f d d 4 e f f . . . . 
            . c d d d f d d 4 e d d f . . . 
            c d e 4 d d d d 4 e b d c . . . 
            c d d d d c d d e e b d c . . . 
            c f f f f d d d e 4 f c f . . . 
            . f b d f f f e e 4 e f . . . . 
            . f d d f e f f f e 4 f . . . . 
            . . f f f e 4 e 4 f f f . f f . 
            . . f e e f e 4 e e f f . 4 f . 
            . f f e 4 e f f f f f f f e f . 
            . f b d f 4 e f b b f f f e f . 
            . f d d f f e 4 d d b f f f f . 
            . f f f f f f f f f f f f f . . 
            `],
        200,
        false
        )
        info.changeLifeBy(-1)
        mySprite.setKind(SpriteKind.Enemy)
        myEnemy.setKind(SpriteKind.Player)
        myEnemy = sprites.create(img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f e f 
            . . . f e f f e f e e e e f f . 
            . . . f e f f e f e e e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . . 
            `, SpriteKind.Enemy)
        mySprite = sprites.create(img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e e 4 f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d 4 e f f . . . . 
            . c d f d d f d e 4 d d f . . . 
            c d e 4 d d d d e 4 b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d 4 4 f f . . f 4 f 
            . . f f f f f 4 e e e f . f e f 
            . . . . f e 4 4 e e e 4 f f e f 
            . . . f e f f 4 f e 4 e e f f . 
            . . . f e f f e f e e 4 e f . . 
            . . . f d b f d b f f 4 f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . . 
            `, SpriteKind.Player)
        myEnemy.follow(mySprite2)
        mySprite.setPosition(sprite_x - 10, sprite_y - 10)
    }
})
forever(function () {
    time += 1
    pause(1000)
})
forever(function () {
    myEnemy.follow(mySprite, speed)
    speed += 25
    pause(25000)
})
forever(function () {
    while (index <= loop1) {
        if (mySprite.x == scene.screenWidth()) {
            mySprite.setVelocity(0, 0)
            loop1 = loop1 + 1
        }
        index += 1
        opp_y = opp_y - opp_y * 2
        opp_x = opp_x - opp_x * 2
    }
})
forever(function () {
    sprite_x = mySprite.x
    sprite_y = mySprite.y
    enemy_x = myEnemy.x
    enemy_y = myEnemy.y
})
