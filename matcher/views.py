from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import handle_file, match
from .forms import UploadFileForm
import mimetypes

# Create your views here.
def index(request):
    return render(request, "matcher/index.html")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print(request.FILES['file'])
        if form.is_valid():
            file1 = request.FILES['reference']
            handle_file(file1, 'img1.jpg')

            file2 = request.FILES['source']
            handle_file(file2, 'img2.jpg')
            # match(file1, file2)
            form = UploadFileForm()
            context = {
                "results": True,
                "form": form
            }

            return render(request, "matcher/upload.html", context)
    else:
        form = UploadFileForm()
        # context = {
        #     "results": False,
        #     "form": form
        # }
        return render(request, 'matcher/upload.html', {'form': form})



def download_file(request):
    # fill these variables with real values
    fl_path = 'matcher/static/matcher/images/results/result.jpg'
    filename = 'result.jpg'
    # have to read the file as binary to avoid encoding error
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
