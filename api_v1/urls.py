from django.urls import path
from api_v1 import views
# from django.conf.urls import url, include

urlpatterns = [
    path("v1/student/<slug:studentId>",views.manageStudentRecord.as_view()),
    path("v1/student",views.CreateStudent.as_view()),

    path("v1/subject/<slug:subjectCode>",views.manageStudentRecord.as_view()),
    path("v1/attendance/<int:id>",views.manageAttendanceRecord.as_view()),
    path("v1/attendance",views.CreateAttendance.as_view()),
    

    path("home",views.homePage,name="home"),
    path("student_insert",views.student_insert,name="student_insert"),
    path("student_delete",views.student_delete,name="student_delete"),
    path("student_update",views.student_update,name="student_update"),
    path("student_viewsingle",views.student_viewsingle,name="student_viewsingle"),
    path("student_viewall",views.student_viewall,name="student_viewall"),
    path("attendance_insert",views.attendance_insert,name="attendance_insert"),
    path("attendance_delete",views.attendance_delete,name="attendance_delete"),
    path("attendance_update",views.attendance_update,name="attendance_update"),
    path("attendance_viewsingle",views.attendance_viewsingle,name="attendance_viewsingle"),
    path("attendance_viewall",views.attendance_viewall,name="attendance_viewall"),
    path("subjects_viewall",views.subjects_viewall,name="subjects_viewall"),
    path("viewPersonal",views.viewPersonal,name="viewPersonal"),
]
