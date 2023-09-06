from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Raquel Nayyara',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
