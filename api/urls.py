from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateSonView, DetailsSonView, UserView, UserDetailsView, CreateScheduleView, DetailsScheduleView, CreateActivityView, DetailsActivityView, CreatePanicButtonCallView, DetailsPanicButtonCallView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^sons/$', CreateSonView.as_view(), name="create"),
    url(r'^sons/(?P<pk>[0-9]+)/$', DetailsSonView.as_view(), name="details"),
    url(r'^schedules/$', CreateScheduleView.as_view(), name="create"),
    url(r'^schedules/(?P<pk>[0-9]+)/$', DetailsScheduleView.as_view(), name="details"),
    url(r'^activities/$', CreateActivityView.as_view(), name="create"),
    url(r'^activities/(?P<pk>[0-9]+)/$', DetailsActivityView.as_view(), name="details"),
    url(r'^panicbuttoncalls/$', CreatePanicButtonCallView.as_view(), name="create"),
    url(r'^panicbuttoncalls/(?P<pk>[0-9]+)/$', DetailsPanicButtonCallView.as_view(), name="details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
