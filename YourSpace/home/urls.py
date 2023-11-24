from django.urls import path
from .views import *
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.cache import cache_page

urlpatterns = [
	path('', home, name = 'home'),
	path('start/', start, name = 'startpage'),
	path('guides/', guides, name = "guides"),
	path('signin/', signin.as_view(), name = 'signin'),
	path('signup/', signup.as_view(), name = 'signup'),
	path('userredirect/', userredirect, name = 'userredirect'),
	path('info/<slug:slug>/', info_focus.as_view(), name="info_focus"),
	path('profile/<slug:slug>/', Profile, name = 'profile'),
	path('logout/', logout, name = 'logout'),
	path(r'^(?P<o_id>\d+)delete/', delete, name = 'delete'),
	path('profileedit/', profileedit, name = 'profuleedit')
]