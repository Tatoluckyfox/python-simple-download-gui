import eel
import os
import requests

# tele2 speedtest     http://speedtest.tele2.net/1GB.zip

@eel.expose
def start_download(url):

	path = os.getenv('TEMP').replace("AppData\\Local\\Temp", "") + "Downloads\\"

	name_of_file = url[url.rfind("/")+1:]
	req = requests.get(url, stream=True)

	if req.headers.get("Content-Length"):
		total_length = float(req.headers.get("Content-Length"))
	else:
		return

	print total_length

	with open(path + name_of_file, "wb") as f:

		for chunk in req.iter_content(chunk_size=32768):
			if chunk:
				f.write(chunk)

			cs = float(os.stat(path + name_of_file).st_size)
			prog = (cs/total_length)*100
			print prog
			eel.update_progress(prog)
	print "successful"
	return

eel.init('web')
eel.start('index.html', size=(450, 200))
