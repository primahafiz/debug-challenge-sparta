from django.urls import path,include
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',views.index),
    path('add/',views.addPage),
    path('delete/<task_id>', views.delete_task, name='delete'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]