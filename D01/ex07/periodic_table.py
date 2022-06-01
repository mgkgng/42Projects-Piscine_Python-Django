from re import L
import sys

def init_html(fd):
	fd.write("""<!doctype html>
<html>
	<head>
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<h1>Table</h1>
		<table>
""")

def close_html(fd):
	fd.write("""				</td>
			</tr>
		</table>
	</body>
</html>
	""")

def writeInfo(fd, info):
	fd.write("\t\t\t\t\t<ul>\n")
	fd.write("\t\t\t\t\t\t<li>" + info["small"]+ "</li>\n")
	fd.write("\t\t\t\t\t\t<li>" + info["molar"]+ "</li>\n")
	fd.write("\t\t\t\t\t\t<li>" + info["electron"] +"</li>\n")
	fd.write("\t\t\t\t\t\t<li>" + info["number"] + "</li>\n")
	fd.write("\t\t\t\t\t</ul>\n")

def writeInfoCell(fd, name, info):
	fd.write("""\t\t\t\t<td style="border: 1px solid black; padding:10px" width="50" height="50" >\n""")		
	fd.write("\t\t\t\t\t<h4>" + name + "</h4>\n")
	writeInfo(fd, info)
	fd.write("\t\t\t\t</td>\n")

def parse(l):
	info = dict()
	for elem in l:
		s = elem.split(':')
		info[s[0].strip()] = s[1].strip()
	return (info)

def	periodic_table():
	txt = open("periodic_table.txt", 'r').readlines()
	fd = open("test.html", 'w')
	init_html(fd)
	last = 0
	for line in txt:
		l = line.split('=')
		name = l[0].rstrip()
		info = parse(l[1].split(","))
		if int(info["position"]) == 0:
			if (int(info["number"]) != 1):
				fd.write("\t\t\t</tr>\n")
			fd.write("\t\t\t<tr>\n")
		if int(info["position"]) > last + 1:
			for i in range(last, int(info["position"])):
				fd.write("""\t\t\t\t<td style="border: 1px solid black; padding:10px; width:100%">\n""")		
				i += 1
		writeInfoCell(fd, name, info)
		last = int(info["position"])
	close_html(fd)

if __name__=="__main__":
	periodic_table()