from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Final Whistle',
        'name': 'Rindu Aurellia Zahra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
