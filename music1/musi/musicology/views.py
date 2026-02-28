from django.shortcuts import render, redirect, get_object_or_404
from .models import Music, Category, Comment

def home(request):
    return render(request, 'home.html')

def music(request):
    mus = Music.objects.all()
    return render(request, 'music.html', {'art': mus})

def detail(request, id):
    item = get_object_or_404(Music, id=id)
    if request.method == 'POST':
        email = request.POST.get('user_email')
        text = request.POST.get('user_comment')
        Comment.objects.create(email=email, comment=text, post=item)
        return redirect('detailurl', id=id)
    comments = Comment.objects.filter(post=item)
    return render(request, 'detail.html', {'tt': item, 'comments': comments})

def admin_music(request):
    musics = Music.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        action = request.POST.get('action')
        m_id = request.POST.get('m_id')

        if action == 'create':
            cat_id = request.POST.get('category')
            Music.objects.create(
                name=request.POST.get('name'),
                singer=request.POST.get('singer'),
                mugory=Category.objects.filter(id=cat_id).first(),
                rating=request.POST.get('rating') or 0,
                description=request.POST.get('description', ''),
                image=request.FILES.get('image'),
                file=request.FILES.get('file')
            )

        elif action == 'update':
            m = Music.objects.filter(id=m_id).first()
            if m:
                m.name = request.POST.get('name')
                m.singer = request.POST.get('singer')
                m.rating = request.POST.get('rating') or 0
                m.description = request.POST.get('description', '')
                
                cat_id = request.POST.get('category')
                if cat_id:
                    m.mugory = Category.objects.filter(id=cat_id).first()

                if 'image' in request.FILES:
                    m.image = request.FILES['image']
                if 'file' in request.FILES:
                    m.file = request.FILES['file']
                
                m.save()

        elif action == 'delete':
            Music.objects.filter(id=m_id).delete()

        return redirect('admin_music')

    return render(request, 'admin_music.html', {'musics': musics, 'categories': categories})
