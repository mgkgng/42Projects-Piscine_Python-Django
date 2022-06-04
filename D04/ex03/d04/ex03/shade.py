def getColorShade(base_color, nb = 50):
	res = list()
	diff = ((255 - base_color[0])/ nb, (255 - base_color[1])/ nb, (255 - base_color[2])/ nb)
	for i in range(nb + 1):
		res.append(
			(int(base_color[0] + diff[0] * i), int(base_color[1] + diff[1] * i), int(base_color[2] + diff[2] * i)))
	return res
