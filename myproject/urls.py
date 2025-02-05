from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import (
    ConstructorViewSet, TeamViewSet, DriverViewSet, RaceViewSet,
    RacePicksViewSet, RaceResultViewSet, SprintResultViewSet, MatchupViewSet,
    AddRacePicksView, HomePageView
)
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'constructors', ConstructorViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'races', RaceViewSet)
router.register(r'racepicks', RacePicksViewSet)
router.register(r'raceresults', RaceResultViewSet)
router.register(r'sprintresults', SprintResultViewSet)
router.register(r'matchups', MatchupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('addracepicks/', AddRacePicksView.as_view(), name='addracepicks'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('', HomePageView.as_view(), name='home'),  # Página principal
]
