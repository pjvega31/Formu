from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ConstructorViewSet, TeamViewSet, DriverViewSet, RaceViewSet,
    RacePicksViewSet, RaceResultViewSet, SprintResultViewSet, MatchupViewSet,
)

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
    path('', include(router.urls)),
]

]
