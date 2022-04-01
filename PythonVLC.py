import vlc
import pafy
from time import sleep

class Watch:

	def __init__(self, id):
		url = "https://www.youtube.com/watch?v="+str(id)

		try:
			video = pafy.new(url)
			best = video.getbest()
			media = vlc.MediaPlayer(best.url)

			media.play()
			while True:
				sleep(1)

		except:
			None
