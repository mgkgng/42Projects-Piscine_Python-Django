import sys

def init_html(fd):
	fd.write("""<!doctype html>
<html lang="en">
	<head>
		<title>Periodic Table</title>
		<link rel="stylesheet" href="periodic_table.css">
		<meta charset="utf-8"/>
	</head>
	<body>
		<h1>Periodic Table</h1>
		<table>
""")

def init_css():
	fd = open("periodic_table.css", 'w')
	fd.write("""tr {
	height : 2px;
}

td {
	border : 1px solid black;
	padding : 10px;
	width : 20px;
}

h4 {
	text-align: center;
	font-size: 12px;
}

li {
	text-align: left;
	font-size: 10px;
}
""")

def close_html(fd):
	fd.write("""			</tr>
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
	fd.write("""\t\t\t\t<td>\n""")		
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
	fd = open("periodic_table.html", 'w')
	init_html(fd)
	init_css()
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
			for i in range(last + 1, int(info["position"])):
				fd.write("""\t\t\t\t<td></td>\n""")		
				i += 1
		writeInfoCell(fd, name, info)
		last = int(info["position"])
	close_html(fd)

if __name__=="__main__":
	periodic_table()