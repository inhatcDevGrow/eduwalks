from django.urls import path
from .views import TestModelView, Get_test_models

urlpatterns = [
    path('test-models/', TestModelView.as_view(), name='test-models'),
    path('get-test-models/', Get_test_models.as_view(), name='get-test-models'),

]
