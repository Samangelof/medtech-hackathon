from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import (base, childseets, library, ofline,
                            create_forum_post, forum, kursi,
                            prodaja, promokod, shop, sing_in_pregnant
                            )


urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),

    # Templates and css
    path('', base),
    path('cchildseets/', childseets),
    path('create_forum_post/', create_forum_post, name='create_forum_post'),
    path('forum/', forum, name='forum'),
    path('kursi/', kursi, name='library'),
    path('ofline/', ofline, name='ofline'),
    path('prodaja/', prodaja, name='prodaja'),
    path('promokod/', promokod, name='promokod'),
    path('shop/', shop, name='shop'),
    path('sing_in_pregnant/', sing_in_pregnant, name='sing_in_pregnant')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
