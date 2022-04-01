#encoding: UTF-8

import requests
import urllib
import time

class start:

	def Search(self, query):
		query = urllib.quote_plus(query)

		html = requests.get("https://www.youtube.com/results?search_query="+query)

		if html.status_code == 200:
			videos = html.text.split('"videoRenderer":{')
			data = ""
			search_result = []
			for video in videos:
				info = {}
				try:
					title = video.split('"title":{')[1].split('"text":"')[1].split('"}')[0].replace("\\", "")
					thumb = video.split('"thumbnails":[{"url":"')[1].split('",')[0]
					durat = video.split('},"publishedTimeText":{')[1].split('"label":"')[1].split('"')[0]
					publish = video.split('},"publishedTimeText":{"simpleText":"')[1].split('"')[0]
					id = video.split('"videoId":"')[1].split('"')[0]
					channel = video.split('"longBylineText":{"runs":[{"text":"')[1].split('"')[0]
					views = video.split('},"viewCountText":{"simpleText":"')[1].split('"')[0]
				except:
					continue

				info["title"] = title.encode('UTF-8').encode("BASE64")
				info["thumb"] = thumb.encode('UTF-8').encode("BASE64")
				info["duration"] = durat.encode('UTF-8').encode("BASE64")
				info["posted"] = publish.encode('UTF-8').encode("BASE64")
				info["id"] = id.encode('UTF-8').encode("BASE64")
				info["channel"] = channel.encode('UTF-8').encode("BASE64")
				info["views"] = views.encode('UTF-8').encode("BASE64")

				if info not in search_result:
					search_result.append(info)

			return search_result


		else:
			print "[!] YouTube returned an unexpected error"
			print "Status code:",html.status_code
			time.sleep(0.5)


