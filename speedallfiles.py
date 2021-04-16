import os
import sys
import re
import speedwatcher

vidtypes = ["mp4", "mkv"]
subtypes = ["srt", "ass"]
formats = [r"[sS]\d{1,2}[eE]\d{1,2}", r"[eE][pP]?\d{1,2}(\D|$)", r"\W+\d{1,2}\W+", r"\s+\d{1,2}\s+"]

def main():
	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
	mypath = sys.argv[1]
	factor = sys.argv[2]
	durations = []
	subs = None
	if len(sys.argv) > 3:
		subs = sys.argv[3]
	speeder = speedwatcher.SpeedSilBySubs(factor)

	if os.path.isfile(mypath) and mypath[-3:] in vidtypes:
		if subs != None:
			dur = speeder.speed(mypath, subs)
			durations.append(dur)
	elif os.path.isdir(mypath):
		f = []
		for (dirpath, dirnames, filenames) in os.walk(mypath):
			f.extend(filenames)

		# for x in f:
		# 	print(x)
		ep_format = None
		sub_format = None
		found_vids = None
		found_subs = None
		def getFileFromFormat(alist, ftype):
			res = []
			for form in formats:
				for ext in ftype:
					res = res + list(filter(re.compile(r".*"+form+r".*"+ext).findall, alist))
				if len(res) > 0:
					return (res, form)

		(found_vids, ep_format) = getFileFromFormat(f, vidtypes)
		(found_subs, sub_format) = getFileFromFormat(f, subtypes)

		
		episode = re.compile(ep_format)
		subtitle = re.compile(sub_format)
		for file in found_vids:
			current_vid = re.search(episode, file).group()
			current_vid = re.search(r'\d+', current_vid[::-1]).group()[::-1]
			current_sub = None
			for sub in found_subs:
				# results = list(filter(re.compile(r".*"+subtitle+r".*").findall, found_subs))
				current_sub = re.search(subtitle, sub).group()
				current_sub = re.search(r'\d+', current_sub[::-1]).group()[::-1]
				if current_sub != None:
					if int(current_vid) == int(current_sub):
						part1 = mypath +"\\"+ file
						part2 = mypath +"\\"+ sub
						print(part1+"\n"+part2)
						dur = speeder.speed(part1, part2)
						print(dur)
						durations.append(dur)
						break

		total = 0.0
		speeded = 0.0
		for d in durations:
			total = total + float(d[0])
			speeded = speeded + float(d[1])
			print(d)
		print("Total Time: ",total, speeded)
		print("Total Time Saved: ",total - speeded)

	# not file or directory
	else:
		print("It is a special file (socket, FIFO, device file) or unsupported one, and will not work." )



if __name__ == '__main__':
	if len(sys.argv) > 1:
		main()