from django.shortcuts import render

from myapp1.models import Musician, Album

from myapp1 import forms

from django.db.models import Q # Search

from django.db.models import Avg



def home(request):
    # Search
    if 'q' in request.GET:
        q = request.GET['q']
        # musician_list = Musician.objects.filter(first_name__icontains=q)
        multiple_q = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        musician_list = Musician.objects.filter(multiple_q)
    else: # Main kaj suru ekhan thke
        musician_list = Musician.objects.all()

    dict = {'title': "Home page", 'musician_list': musician_list}
    return render(request, 'myapp1/home.html', context=dict)



def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id) # primary_key dhore call korle/korte chaile get() use korbo
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_datefield')
    artist_rate = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    dict = {'title': "List of albums", 'artist_info': artist_info, 'album_list':album_list, 'artist_rate':artist_rate}
    return render(request, 'myapp1/album_list.html', context=dict)



def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

    dict = {'title': "Add musician", 'musician_form':form}
    return render(request, 'myapp1/musician_form.html', context=dict)



def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

    dict = {'title': "Add albums", 'album_form':form}
    return render(request, 'myapp1/album_form.html', context=dict)



def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id) # same model er object   load same info
    form = forms.MusicianForm(instance=artist_info) # same model er form      eki model er duijon

    dict={}

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info) #1st parameter e notun value achy, 2nd parameter e old value achy

        if form.is_valid():
            form.save(commit=True)
            # return album_list(request, artist_id)
            dict.update({'success_text': 'Successfully Updated!'})


    dict.update({'title': "Edit Artist",'edit_form' : form })
    return render(request, 'myapp1/edit_artist.html', context=dict)



def edit_album(request, album_id):

    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    dict={}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            dict.update({'success_text': 'Successfully Updated!'})

    dict.update({'title': 'Edit Album','edit_form' : form })

    dict.update({'album_id': album_id}) # eta pass korlam album delete korar jonno

    return render(request, 'myapp1/edit_album.html', context=dict)



def delete_album(request, album_id):
    Album.objects.get(pk=album_id).delete()

    dict={'title':'Delete Album', 'delete_success_text': 'Album deleted Successfully!' }
    return render(request, 'myapp1/delete.html', context=dict)


def delete_artist(request, artist_id):
    Musician.objects.get(pk=artist_id).delete()

    dict={'title':'Delete Artist', 'delete_success_text': 'Artist deleted Successfully!' }
    return render(request, 'myapp1/delete.html', context=dict)
