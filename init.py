#encoding: UTF-8
import requests, re, sys, warnings, youtube_dl
warnings.filterwarnings("ignore")
def erros():
	global help_erro, help_download, help_listing, help_name, help_search

	help_erro = "[!] Help [!]\n\nUsage: Python3 "+str(sys.argv[0])+" <OPTIONS> <ARGS> <Result limit>\n\n[!]OPTIONS[!]\n\n-u\tChannel URL\n-n\tChannel name\n-d\tDownload a video\n-s\tSearch a video\n\n[!]MORE HELP[!]\n\nUse: python3 "+str(sys.argv[0])+" <OPTION> \n\n[!] END [!]\n\n"
	help_download = "[DOWNLOAD MODE HELP - 1]\n\n[WARNING] You need to specify the download link\n\nUsege: python3 "+str(sys.argv[0])+" -d <LINK DOWNLOAD>\n"
	help_listing = "[LISTING LINKS VIA URL HELP - 1]\n\n[WARNING] You need to specify the desired channel URL\n\nExemple: python3 "+sys.argv[0]+" -u https://youtube.com/user/tseries/videos/\n"
	help_name = "[LISTING LINKS VIA NAME HELP - 1]\n\n[WARNING] You need to especify the desired channel name\n\nExemple: python3 "+sys.argv[0]+" -n dossiedofelile\n"
	help_search = "[YOUTUBE SEARCH MODE HELP - 1]\n\n[WARNING] You need to specify the keyword to perform the search\n\nExemple: python3 "+sys.argv[0]+" -s \"Minecraft gameplay\"\n"



def pythonversion():
        try:
                version = 199/2*2

                if version == 198:
                        print ("[WARNING] Run with python3")
                        exit(0)

        except Exception as error:
#               print(error)
                exit(0)


def init():

	erros()

	try:
		global mode, req
		mode = sys.argv[1]

		if mode == "-h" or mode == "--help":
		        sys.stdout.write(help_erro)
		        exit(0)
	except Exception as erro:
		#print (erro)
		sys.stdout.write(help_erro)
		exit(0)


	try:
		channel = sys.argv[2]
	except:
		if mode == "-d":
		        print (help_download)
		        exit(0)

		elif mode == "-u":
		        print (help_listing)
		        exit(0)

		elif mode == "-n":
		        print (help_name)
		        exit(0)

		elif mode == "-s":
		        print (help_search)
		        exit(0)

		else:
		        print ("\n\n[X] Erro: Mode ["+str(mode)+"] not found !!. Try --help or -h\n")
		        exit(0)

		exit(0)

	try:
		if mode == "-d":
		        ydl_opts = {}
		        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		                ydl.download([channel])
		        exit(0)

	except Exception as erro:
		print ("[X] Erro:",erro)

	nonumber = "[NUMBER FOR OUTPUT NOT FOUND]\n[WARNING] You need to specify the limit number for the output\n\nExemple python3 "+str(sys.argv[0])+" <MODE> <ARGS> <NUMBER LIMIT OUTPUT>"
	try:
		global limit
		limit = int(sys.argv[3])
		if limit < 0:
			print (nonumber)
			exit(0)

	except Exception as erro:
	#               print (erro)
		print(nonumber)
		exit(0)



	sys.stdout.write("[INFO] trying to connect - wait ...\n")
	if mode == "-u":
		try:
			req = requests.get(str(channel))
			print ("[!] Status Code:",req.status_code)

			invalid_url = "[X] invalid URL or was not passed as it should [X]\nthe URL should look like this https://youtube.com/user/thechannel/videos/"

			if req.status_code != 200:
				print (invalid_url)
				exit(0)

		except Exception as erro:
			print ("[X] Erro:",erro)
			exit(0)

	elif mode == "-n":
		try:
		        name = "https://youtube.com/user/"+str(channel.lower().replace(" ", ""))
		        req = requests.get(str(name))
		        print ("[!] Channel name mode[!]\n[!] Status Code:",req.status_code)

		        if req.status_code != 200:
		                print ("[X] Username ["+str(channel.lower())+"] does not exist [X]")
		                exit(0)

		        url = name+str("/videos/")
		        req = requests.get(url)

		except Exception as erro:
		        print ("[X] Erro:",erro)
		        exit(0)

	elif mode == "-s":
		try:
		       	search = str(channel).replace(" ","+")
		        name = "https://www.youtube.com/results?search_query="+str(search)+"&disable_polymer=true"
		        req = requests.get(str(name))
		        print ("[!] Search mode [!]\n[!] Status Code:",req.status_code)

		        if req.status_code != 200:
		                print ("[X] Unexpected Error [X]")
		                exit(0)
		except Exception as erro:
		        print ("[X] Erro:",erro,"\n[WARNING] CHECK YOUR CONNECTION WITH INTERNET")
		        exit(0)


def getlinks():
	init()

	global link

	html = req.text
	link = re.findall("v=\S+", html)



def getname(link):
	links = {"a", "b"}
	for i in link:

		i = (str(i[0])+str(i[1])+str(i[2])+str(i[3])+str(i[4])+str(i[5])+str(i[6])+str(i[7])+str(i[8])+str(i[9])+str(i[10])+str(i[11])+str(i[12]))

		url = "https://www.youtube.com/watch?"+i
		links.add(url)

	id = 0
	limite = limit

	videourl = []
	videotit = []

	print ("[INFO] Getting video list")

	for i in links:

		try:
			req = requests.get(i)
			html = req.text
			raw_title = re.findall("<title>[\S]+[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?[\s]?[[\S]+]?", html)
			chan = re.findall('ownerChannelName\S\S\S\S\S(\w+[\s]?[[\w]+]?[\s]?[[\w]+]?[\s]?[[\w]+]?)',html)

			title = raw_title[0][7:]

			t1 = 0
			t2 = 1
			t3 = 2
			t4 = 3
			t5 = 4
			t6 = 5
			t7 = 6

			url = i

			for i in range(len(title)):
				if str(title[t1])+str(title[t2])+str(title[t3])+str(title[t4])+str(title[t5])+str(title[t6])+str(title[t7]) == "YouTube":
					print ("\n","-"*70,"\n ID: "+str(id)+" #",title[:t1],"\n Link:",url,"\n Channel:", chan[0],"-"*70,"\n")

					videourl.append(url)
					videotit.append(title[:t1])

					id += 1
					limite -= 1
					if limite <= 0:
						while True:
							try:
								option = input("Enter the video ID to download | Type [quit] to exit | Press enter for more results :  ")
							except:
								exit(0)

							if option.lower() == "quit":
								exit(0)

							else:
								limite = 5
								try:
									dow = input(videotit[int(option)]+"\nIs correct ? N/y ")
									if dow == "Y" or dow == "y":
										ydl_opts = {}
										with youtube_dl.YoutubeDL(ydl_opts) as ydl:
											ydl.download([videourl[int(option)]])

									else:
										limite = 5
										pass

								except Exeption as erro:
									print (erro)
									print ("\n################\n[X] ID not exist\n################\n")

				t1 += 1
				t2 += 1
				t3 += 1
				t4 += 1
				t5 += 1
				t6 += 1
				t7 += 1


		except Exception as erro:
			None



pythonversion()
getlinks()
getname(link)

