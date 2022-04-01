#encoding: UTF-8

import RequestsVideos
import json
import ast
import os
import PythonVLC
import pafy

youtube = RequestsVideos.start()



help = """

Search to videos:
> search Minecraft videos

Watch video:
> watch <video id>

Download video:
> download <video id>

Type exit to exit.

"""


menu = '''

██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                               By: https://github.com/them3x
                                                             ██████╗██╗     ██╗
                                                            ██╔════╝██║     ██║
                                                            ██║     ██║     ██║
           Type: help to see options                        ██║     ██║     ██║
                                                            ╚██████╗███████╗██║
                                                             ╚═════╝╚══════╝╚═╝

'''


print menu

none_search = True
while True:
	command = raw_input("\n> ")


	if command == "help":
		print help

	elif command == "exit":
		exit(0)

	try:

		if command[:6] == "search":

			search = command.replace("search ", "")
			videos_json = youtube.Search(search)
			id = 0
			for_watch = {}
			for video in videos_json:
				video = ast.literal_eval(json.dumps(video))

				print "\nId:",id
				print "Title:",video["title"].decode("BASE64")
				print "Duration:",video["duration"].decode("BASE64")
				print "Channel:",video["channel"].decode("BASE64")
				print "Link: https://www.youtube.com/watch?v=" + str(video["id"].decode("BASE64"))
				print "Views:",video["views"].decode("BASE64")
				print "________________________________________________"
				for_watch[str(id)] = str(video["id"].decode("BASE64"))

				id +=1

			none_search = False

		elif command[:5] == "watch":
			if none_search:
				print "[!] No research has been carried out"

			else:
				watch = command.replace("watch ", "")
				PythonVLC.Watch(for_watch[watch])


		elif command[:8] == "download":
			if none_search:
				print "[!] No research has been carried out"
			else:
				id_down = for_watch[command.replace("download ", "")]
				info = pafy.new("https://www.youtube.com/watch?v="+id_down)
				title = str(info).split('Title: ')[1].split("\n")[0]
				video = info.getbest()
				os.system('wget "' + str(video.url) + '"' + ' -O "/home/messias/Desktop/' + title + '"')

	except Exception as erro:
		print erro
		None
