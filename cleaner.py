import os
from datetime import datetime
import io
import shutil
# cleans up files and puts them in the right places

username = os.getlogin()

mydirs = [
	f"/home/{username}", 
	f"/home/{username}/Desktop/", 
	f"/home/{username}/Pictures", 
	f"/home/{username}/Documents", 
	f"/home/{username}/Templates", 
	f"/home/{username}/Downloads", 
	f"/home/{username}/Music", 
	f"/home/{username}/projects", 
	f"/home/{username}/Pictures/jpg",
	f"/home/{username}/Pictures/jpeg",
	f"/home/{username}/Pictures/png",
	f"/home/{username}/Pictures/BMP",
	f"/home/{username}/Pictures/gif",
	f"/home/{username}/Documents/text",
	f"/home/{username}/Documents/docx",
	f"/home/{username}/Documents/pdf",
	f"/home/{username}/projects/python",
	f"/home/{username}/projects/rust",
	f"/home/{username}/projects/cpp",
	f"/home/{username}/projects/go",
	f"/home/{username}/Music/wav",
	f"/home/{username}/Music/mpg",
	f"/home/{username}/Music/mpeg",
	f"/home/{username}/Music/mp4",
	f"/home/{username}/Music/mp3",
	f"/home/{username}/Misc/zip",
	f"/home/{username}/Misc/exe",
	f"/home/{username}/Misc/run",
	f"/home/{username}/Misc/iso",
	f"/home/{username}/Misc/ini",
	f"/home/{username}/Misc/web",
	f"/home/{username}/Misc/bin",
	]
zip_filter = [".7z", ".zip", ".xz", ".tar"]
misc_filter = ["zip", "iso", "exe", "ini", 'bin']
music_filter = [".wav", ".mpg", ".mpeg", ".mp4", ".mp3"]
allexts = [".txt", ".docx", ".pdf",".jpg", ".png", ".jpeg", ".heif", ".py", ".rs", ".cpp", ".go", ".wav", ".mpg", ".mpeg", ".mp4", ".mp3" ]
document_filter = [".txt", ".docx", ".pdf"]
picture_extensions = [".jpg", ".png", ".jpeg", ".heif"]
projects_filter = [".py", ".rs", ".cpp", ".go"]
misc_python_scripts = f"/home/{username}/python/misc"
tools = f"/home/{username}/tools"
commands = f"/home/{username}/.commands"


class Lister:
	def home(self):
		return os.listdir(mydirs[0])
	def desktop(self):
		return os.listdir(mydirs[1])
	def pictures(self):
		return os.listdir(mydirs[2])
	def documents(self):
		return os.listdir(mydirs[3])
	def templates(self):
		return os.listdir(mydirs[4])
	def downloads(self):
		return os.listdir(mydirs[5])
	def music(self):
		return os.listdir(mydirs[6])
	def projects(self):
		return os.listdir(mydirs[7])
	def jpegPictures(self):
		return os.listdir(mydirs[8])
	def pngPictures(self):
		return os.listdir(mydirs[9])
	def heifPictures(self):
		return os.listdir(mydirs[10])
	def txtDocuments(self):
		return os.listdir(mydirs[11])
	def docxDocuments(self):
		return os.listdir(mydirs[12])
	def pdfDocuments(self):
		return os.listdir(mydirs[13])
	def pythonProjects(self):
		return os.listdir(mydirs[14])
	def rustProjects(self):
		return os.listdir(mydirs[15])
	def cppProjects(self):
		return os.listdir(mydirs[16])
	def goProjects(self):
		return os.listdir(mydirs[17])
	
	

	def current(self):
		cc = os.getcwd()
		return os.listdir(cc)
show = Lister()

class Mover:
	def home(self, fileobj):
		shutil.move(fileobj, mydirs[0])
	def desktop(self, fileobj):
		shutil.move(fileobj, mydirs[1])
	def pictures(self, fileobj):
		shutil.move(fileobj, mydirs[2])
	def documents(self, fileobj):
		shutil.move(fileobj, mydirs[3])
	def templates(self, fileobj):
		shutil.move(fileobj, mydirs[4])
	def downloads(self, fileobj):
		shutil.move(fileobj, mydirs[5])
	def music(self, fileobj):
		shutil.move(fileobj, mydirs[6])
	def projects(self, fileobj):
		shutil.move(fileobj, mydirs[7])
	def goProjects(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/projects/go")
	def rustProjects(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/projects/rust")
	def cppProjects(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/projects/cpp")
	def pyProjects(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/projects/python")
	def txtDocuments(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Documents/text")
	def pdfDocuments(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Documents/pdf")
	def docxDocuments(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Documents/docx")
	def jpgPictures(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Pictures/jpg")
	def pngPictures(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Pictures/png")
	def bmpPictures(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Pictures/jpg")
	def gifPictures(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Pictures/gif")
	def wavMusic(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Music/wav")
	def mpgMusic(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Music/mpg")
	def mp3Music(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Music/mp3")
	def mp4Music(self, fileobj):
		shutil.move(fileobj, f"/home/{username}/Music/mp4")
	def mpegMusic(self,fileobj):
		shutil.move(fileobj, f"/home/{username}/Music/mp4")
	def current(self, fileobj):
		shutil.move(fileobj, mydirs[8])
move = Mover()

class Changer:
	def home(self):
		os.chdir(mydirs[0])
	def desktop(self):
		os.chdir(mydirs[1])
	def pictures(self):
		os.chdir(mydirs[2])
	def documents(self):
		os.chdir(mydirs[3])
	def templates(self):
		os.chdir(mydirs[4])
	def downloads(self):
		os.chdir(mydirs[5])
	def music(self):
		os.chdir(mydirs[6])
	def projects(self):
		os.chdir(mydirs[7])
goto = Changer()


class Logger:
	log = f"{mydirs[0]}/.cleaner_log"
	actions = ["listed", "changed to", "moved", "deleted"]

	def moved(self, fileobj, destination):
		time = datetime.now()
		f = open(self.log, "a")
		f.write(f"[{time.month}/{time.day}/{time.year} {time.hour}:{time.minute}:{time.second}] ~ {fileobj} moved to {destination} ")
		f.close()
		os.system(f"sudo notify-send -t 2000 'File Cleaner' '{fileobj} moved to {destination}' ")

	def changedTo(self, destination):
		time = datetime.now()
		f = open(self.log, "a")
		f.write(f"[{time.month}/{time.day}/{time.year} {time.hour}:{time.minute}:{time.second}] ~ changed to {destination}\n ")
		f.close()


	def deleted(self, fileobj):
		time = datetime.now()
		f = open(self.log, "a")
		f.write(f"[{time.month}/{time.day}/{time.year} {time.hour}:{time.minute}:{time.second}] ~ deleted {fileobj}\n ")
		f.close()
		os.system(f"notify-send -t 2000 'File Cleaner' '{fileobj} deleted'")


	def listed(self, directory):
		time = datetime.now()
		f = open(self.log, "a")
		f.write(f"[{time.month}/{time.day}/{time.year} {time.hour}:{time.minute}:{time.second}] ~ scanned {directory} \n ")
		f.close()

	def read(self):
		f = open(self.log, "r")
		lines = f.readlines()
		for index, line in enumerate(lines):
			print(index,"|",line)
		f.close()

log = Logger()


#show goto paths log
class Scanner:
	def home(self):
		
		goto.home()
		log.changedTo(mydirs[0])
		self.files = show.home()
		log.listed(mydirs[0])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def desktop(self):
		
		goto.desktop()
		print(os.getcwd())
		log.changedTo(mydirs[1])
		self.files = show.desktop()
		print(self.files)
		log.listed(mydirs[1])
		for file in self.files:
			print(file)
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def pictures(self):
		
		goto.pictures()
		log.changedTo(mydirs[2])
		self.files = show.pictures()
		log.listed(mydirs[2])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def documents(self):
		
		goto.documents()
		log.changedTo(mydirs[3])
		self.files = show.documents()
		log.listed(mydirs[3])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def templates(self):
		
		goto.templates()
		log.changedTo(mydirs[4])
		self.files = show.templates()
		log.listed(mydirs[4])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def downloads(self):
		
		goto.downloads()
		log.changedTo(mydirs[5])
		self.files = show.downloads()
		log.listed(mydirs[5])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def projects(self):
		
		goto.projects()
		log.changedTo(mydirs[6])
		self.files = show.projects()
		log.listed(mydirs[6])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)

	def music(self):
		
		goto.music()
		log.changedTo(mydirs[7])
		self.files = show.music()
		log.listed(mydirs[7])
		for file in self.files:
			is_file = self.isFile(file)
			if is_file:
				self.endswith(file)
	
	def isFile(self, file):
		z = True
		try:
			f = open(file, "a")
		except:
			z=False
		finally:
			return z


	def endswith(self, file):
		already = False
		myext = "none"
		newfile = file
		newthing = file.split(".")
		ext = "." + newthing[1]

		for x in document_filter:
			if x == ext:
				myext = "docs"
				already = True
		if already == True:
			pass
		else:
			for x in projects_filter:
				if x == ext:
					myext = "proj"
					already = True
		if already == True:
			pass
		else:
			for x in picture_extensions:
				if x == ext:
					myext = "pics"
					already = True
		if already == True:
			pass
		else:
			for x in music_filter:
				if ext == x:
					myext = "musi"
					already = True

		match myext:
			case "docs":
				self.matchDocuments(ext, newfile)
			case "proj":
				self.matchProjects(ext, newfile)
			case "pics":
				self.matchPictures(ext, newfile)
			case "musi":
				self.matchMusic(ext, newfile)
			case "none":
				pass


	def matchDocuments(self, ext, file):
		match ext:
			case ".txt":
				move.txtDocuments(file)
				log.moved(file, mydirs[13])
			case ".docx":
				move.docxDocuments(file)
				log.moved(file, mydirs[14])
			case ".pdf":
				move.pdfDocuments(file)
				log.moved(file, mydirs[15])
			case other:
				pass
	
	def matchPictures(self, ext, file):
		match ext:
			case ".jpg":
				move.jpgPictures(file)
				log.moved(file, mydirs[8])
			case ".jpeg":
				move.jpgPictures(file)
				log.moved(file, mydirs[9])
			case ".png":
				move.pngPictures(file)
				log.moved(file, mydirs[10])
			case ".BMP":
				move.bmpPictures(file)
				log.moved(file, mydirs[11])
			case ".gif":
				move.gifPictures(file)
				log.moved(file, mydirs[12])
			case other:
				pass

	def matchProjects(self, ext, file):
		match ext:
			case ".py":
				move.pyProjects(file)
				log.moved(file, mydirs[16])
			case ".rs":
				move.rustProjects(file)
				log.moved(file, mydirs[17])		
			case ".cpp":
				move.cppProjects(file)
				log.moved(file, mydirs[18])
			case ".go":
				move.goProjects(file)
				log.moved(file, mydirs[19])
			case other:
				pass


	def matchMusic(self, ext, file):
		match ext:
			case ".wav":
				move.wavMusic(file)
				log.moved(file, mydirs[20])
			case ".mpg":
				move.mpgMusic(file)
				log.moved(file, mydirs[21])
			case ".mpeg":
				move.mpegMusic(file)
				log.moved(file, mydirs[22])
			case ".mp4":
				move.mp4Music(file)
				log.moved(file, mydirs[23])
			case ".mp3":
				move.mp3Music(file)
				log.moved(file, mydirs[24])
			case other:
				pass

scan = Scanner()


def scanAll():
	scan.home()
	scan.projects()
	scan.desktop()
	scan.pictures()
	scan.downloads()
	scan.documents()
	scan.templates()
	scan.music()

def help_me():
	print("""
file manager
	[description]
		sort files to their correct homes
	[options]
		all          -> scan all folder
		pictures     -> scan pictures directory
		projects     -> scan projects directory
		documents    -> scan documents directory
		templates    -> scan templates directory
		music        -> scan music directory
		home         -> scan home directory
		desktop      -> scan desktop
""")


if __name__ == '__main__':
	scans = {
		"home":scan.home, 
		"projects":scan.projects, 
		"desktop":scan.desktop, 
		"pictures":scan.pictures, 
		"downloads":scan.downloads, 
		"documents":scan.documents, 
		"templates":scan.templates, 
		"music":scan.music,
		"pics":scan.pictures,
		"proj":scan.projects,
		"dt":scan.desktop,
		"dl":scan.downloads,
		"all":scanAll,
		}
	from sys import argv

	try:
		args = argv[1:]
	except:
		help_me()
		exit()
	finally:
		match args[0]:
			case "home":
				scan.home()
			case "desktop":
				scan.desktop()
			case "dt":
				scan.desktop()
			case "pictures":
				scan.pictures()
			case "pics":
				scan.pictures()
			case "downloads":
				scan.downloads()
			case "dl":
				scan.downloads()
			case "docs":
				scan.documents()
			case "documents":
				scan.documents()
			case "templates":
				scan.templates()
			case "projects":
				scan.projects()
			case "proj":
				scan.projects()
			case "music":
				scan.music()
			case "log":
				log.read()
			case "all":
				scanAll()
			case "help":
				help_me()
			case "-h":
				help_me()
			case "--help":
				help_me()
			case "clear":
				try:
					match argv[1]:
						case "log":
							os.system(f"sudo rm -r {mydirs[0]}/.cleaner_log")
						case "logs":
							os.system(f"sudo rm -r {mydirs[0]}/.cleaner_log")
				except:
					print("clear what?")










