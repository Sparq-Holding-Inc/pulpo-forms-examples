from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^example/', include('pulpo_example.urls')),
    url(r'^pulpo/', include('pulpo_forms.urls'), name='base'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^model_field_form/$',
        'pulpo_forms.views.render_form',
        {'instance': 'model-field-example'}),
]
