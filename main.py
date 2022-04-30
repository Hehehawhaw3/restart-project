def on_overlap_tile(sprite4, location4):
    mySprite.set_velocity(0, 0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile)

def on_up_pressed():
    if not_true:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(0, -100)
    else:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(0, -100)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite, location):
    mySprite.set_velocity(0, 0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile2)

def on_b_pressed():
    if controller.left.is_pressed():
        mySprite.set_velocity(-150, 0)
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        pause(5000)
        mySprite.set_velocity(0, 0)
    elif controller.up.is_pressed():
        mySprite.set_velocity(0, -150)
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        pause(5000)
        mySprite.set_velocity(0, 0)
    elif controller.down.is_pressed():
        mySprite.set_velocity(0, 150)
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        pause(5000)
        mySprite.set_velocity(0, 0)
    elif controller.right.is_pressed():
        mySprite.set_velocity(150, 0)
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        pause(5000)
        mySprite.set_velocity(0, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    mySprite.set_flag(SpriteFlag.GHOST, True)
    mySprite.set_flag(SpriteFlag.INVISIBLE, True)
    myEnemy.follow(mySprite, 0)
    info.start_countdown(10)
    pause(9950)
    info.stop_countdown()
    mySprite.set_flag(SpriteFlag.GHOST, False)
    mySprite.set_flag(SpriteFlag.INVISIBLE, False)
    myEnemy.follow(mySprite, speed)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite3, location3):
    info.change_life_by(-1)
    mySprite.set_velocity(0, 0)
    mySprite.set_velocity(50, 50)
    pause(100)
    mySprite.set_velocity(50, 50)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile3)

def on_down_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_velocity(0, 0)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    if not_true:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(-100, 0)
    else:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(-100, 0)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_velocity(0, 0)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_velocity(0, 0)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    if not_true:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(100, 0)
    else:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(100, 0)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_velocity(0, 0)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    if not_true:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(0, 100)
    else:
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            100,
            True)
        mySprite.set_velocity(0, 100)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile4(sprite2, location2):
    mySprite.set_velocity(0, 0)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile7
    """),
    on_overlap_tile4)

enemy_y = 0
enemy_x = 0
sprite_y = 0
sprite_x = 0
opp_x = 0
opp_y = 0
loop1 = 0
index = 0
myEnemy: Sprite = None
mySprite: Sprite = None
not_true = False
speed = 0
speed = 25
not_true = True
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(mySprite)
mySprite.set_bounce_on_wall(True)
list2 = [3, 1, 2]
info.set_life(1)
mySprite2 = sprites.create(img("""
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
    """),
    SpriteKind.player)
myEnemy = sprites.create(img("""
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
    """),
    SpriteKind.enemy)
if list2._pick_random() == 1:
    myEnemy.set_position(120, 80)
elif list2._pick_random() == 2:
    myEnemy.set_position(100, 60)
elif list2._pick_random() == 3:
    myEnemy.set_position(70, 80)

def on_forever():
    global speed
    myEnemy.follow(mySprite, speed)
    speed += 25
    pause(25000)
forever(on_forever)

def on_forever2():
    global loop1, index, opp_y, opp_x
    while index <= loop1:
        if mySprite.x == scene.screen_width():
            mySprite.set_velocity(0, 0)
            loop1 = loop1 + 1
        index += 1
        opp_y = opp_y - opp_y * 2
        opp_x = opp_x - opp_x * 2
forever(on_forever2)

def on_forever3():
    global sprite_x, sprite_y, enemy_x, enemy_y
    sprite_x = mySprite.x
    sprite_y = mySprite.y
    enemy_x = myEnemy.x
    enemy_y = myEnemy.y
forever(on_forever3)

def on_forever4():
    global not_true, myEnemy, mySprite
    mySprite2.set_position(opp_x, opp_y)
    if mySprite.overlaps_with(myEnemy):
        not_true = False
        animation.run_image_animation(myEnemy,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            200,
            False)
        info.change_life_by(-1)
        mySprite.set_kind(SpriteKind.enemy)
        myEnemy.set_kind(SpriteKind.player)
        myEnemy = sprites.create(img("""
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
            """),
            SpriteKind.enemy)
        mySprite = sprites.create(img("""
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
            """),
            SpriteKind.player)
        myEnemy.follow(mySprite2)
        mySprite.set_position(sprite_x - 10, sprite_y - 10)
forever(on_forever4)
