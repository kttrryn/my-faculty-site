from django.urls import path

from faculty_app import views

app_name = "faculty_app"
urlpatterns = [
    path("", views.main, name="main"),
    path("programs/", views.program_list, name="programs"),
    path("programs/<int:id>/", views.program_detail, name="program_id"),
    path("departments/", views.department_list, name="departments"),
    path("departments/<int:id>/", views.department_detail, name="departments"),
    path('exchange/', views.exchange_list, name='exchange_list'),
]
