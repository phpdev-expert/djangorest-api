from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Permission, User

class UpdateUserPermissions(APIView):
    def get(self, request):
        if(request.user.has_perm('auth.change_user')):
            prem = Permission.objects.get(codename = 'change_section')
            user_id = request.data['user_id']
            user = User.objects.get(pk = user_id)
            user.user_permissions.remove(prem)
            content = {'message':"Permission removed successfully"}
            return Response(content)
        else:
            content = {'message':"Not have permissions to update user"}
            return Response(content)

    def post(self, request):
        if(request.user.has_perm('auth.change_user')):
            prem = Permission.objects.get(codename = 'change_section')
            user_id = request.data['user_id']
            user = User.objects.get(pk = user_id)
            user.user_permissions.add(prem)
            content = {'message':"Permission added successfully"}
            return Response(content)
        else:
            content = {'message':"Not have permissions to update user"}
            return Response(content)
