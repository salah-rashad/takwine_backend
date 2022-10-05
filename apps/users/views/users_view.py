# from rest_framework import permissions, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from apps.users.models import User
# from users.serializers import UserSerializer

# # from users.serializers import UserSerializer


# class UsersView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all

#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create New
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 2. Delete All
#     def delete(self, request, *args, **kwargs):
#         User.objects.all().delete()
#         return Response(
#             {
#                 "message": "All users deleted!"
#             },
#             status=status.HTTP_200_OK
#         )
