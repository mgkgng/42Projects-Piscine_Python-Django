from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def remove(request):
	movielist = Movies.objects.all()
	if len(movielist) == 0:
		return HttpResponse("No data available")
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			r = Movies.objects.filter(title=form.title)
			r.delete()
			redirect("/remove")
	return render(request, "ex04/remove.html", {"movielist": movielist})