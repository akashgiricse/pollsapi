from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
# from .views import polls_list, polls_detail
from .apiviews import ChoiceList, CreateVote

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

]

urlpatterns += router.urls