import vlc
import time
instance=vlc.Instance()
player = instance.media_player_new()
media = instance.media_new('/usr/bin/end.mp3')
player.set_media(media)
player.audio_set_volume(50)
for i in range(3):
	player.play()
	time.sleep(1)
	player.stop()
