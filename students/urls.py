from rest_framework import routers
from .views import StudentView, PackageView, EnrollStudentView

router = routers.DefaultRouter()



router.register('create-student', StudentView, 'create_student')
router.register('package', PackageView, 'package')
router.register('enroll-student', EnrollStudentView, 'enroll-student')