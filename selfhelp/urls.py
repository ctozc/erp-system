from django.conf.urls import include, url,static
import selfhelp.views

urlpatterns = [
    url(r"change/export/", selfhelp.views.export_excel, name="export"),
    # url(r"(?P<model>\w+)/(?P<object_id>\d+)/pay", selfhelp.views.pay_action),
]
