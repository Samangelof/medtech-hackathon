from django.shortcuts import render


def base(request):
    return render(
        request, 'base.html',
    )


def childseets(request):
    return render(
        request, 'childseets.html',
    )


def create_forum_post(request):
    return render(
        request, 'create_forum_post.html',
    )


def forum(request):
    return render(
        request, 'forum.html',
    )


def kursi(request):
    return render(
        request, 'kursi.html',
    )


def library(request):
    return render(
        request, 'library.html',
    )


def ofline(request):
    return render(
        request, 'ofline.html',
    )


def prodaja(request):
    return render(
        request, 'prodaja.html',
    )


def promokod(request):
    return render(
        request, 'promokod.html',
    )


def shop(request):
    return render(
        request, 'shop.html',
    )


def sing_in_pregnant(request):
    return render(
        request, 'sing_in_pregnant.html',
    )

