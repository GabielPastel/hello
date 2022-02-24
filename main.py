def on_button_pressed_a():
    for index in range(1):
        music.set_tempo(200)
        music.play_tone(147, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
        music.play_tone(147, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.DOUBLE))
        music.play_tone(147, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(147, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.DOUBLE))
input.on_button_pressed(Button.A, on_button_pressed_a)
