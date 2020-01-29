import os

from skimage import data, io
from skimage import exposure
from skimage.exposure import match_histograms

location = os.path.abspath(os.getcwd()) + '/matcher/static/matcher/images'

def match():
    file1 = location + '/uploads/img1.jpg'
    file2 = location + '/uploads/img2.jpg'

    reference = io.imread(file1)
    image = io.imread(file2)

    # print(image.shape)
    # image = data.astronaut()

    matched = match_histograms(image, reference, multichannel=True)
    result = location + '/results/result.jpg'
    io.imsave(result, matched)
    

def handle_file(f, name):
    # name = 'img.jpg'
    # print(f.size)
    link = location + '/uploads/' + name
    # print(link)
    with open(link, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    match()

