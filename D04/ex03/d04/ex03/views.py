from django.shortcuts import render
from .shade import getColorShade

def index(request):
	blacklist = getColorShade((0, 0, 0))
	redlist = getColorShade((255, 0, 0))
	bluelist = getColorShade((0, 0, 255))
	greenlist = getColorShade((0, 255, 0))
	print(blacklist[0][0])
	return render(request, "ex03/index.html", {"colors": [blacklist, redlist, bluelist, greenlist]})