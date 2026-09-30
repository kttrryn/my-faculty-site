app_name = 'faculty_app'
urlpatterns = [
    path('', views.main, name='main'),
    path('programs/', views.program_list, name='programs'),
    path('programs/<int:id>/', views.program_detai, name='program_id'),
    path('departments/', views.department_list, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='departments'),
]
