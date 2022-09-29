from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):