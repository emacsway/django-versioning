from django.conf.urls.defaults import patterns, url

from .views import RevisionReapplyView, RevisionListView

urlpatterns = patterns('versioning.views',
    url(r'^revision_list/(?P<content_type>[\w\-]+)/(?P<object_id>[\w\-]+)/',
        RevisionListView.as_view(),
        name="versioning_revision_list"),
    url(r'^revision_reapply/(?P<pk>[\w\-]+)/',
        RevisionReapplyView.as_view(),
        name="versioning_revision_reapply"),
)