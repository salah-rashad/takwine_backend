# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions, status

# from django.contrib.auth import get_user_model

# # from users.models import User
# # from users.serializers import UserSerializer


# class SingleUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def getUserOr404(self, pk):
#         try:
#             User = get_user_model()
#             return User.objects.get(userId=pk)
#         except User.DoesNotExist:
#             return Response(
#                 {
#                     "error": "User does not exist"
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )

#     # def get(self, request, pk, *args, **kwargs):
#     #     object = self.getUserOr404(pk)
#     #     if type(object) is Response:
#     #         return object

#     #     serializer = UserSerializer(object)
#     #     return Response(serializer.data)

#     # def put(self, request, pk, *args, **kwargs):
#     #     object = self.getUserOr404(pk)
#     #     if type(object) is Response:
#     #         return object

#     #     request.data['userId'] = pk
#     #     serializer = UserSerializer(instance=object, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request, pk, *args, **kwargs):
#     #     object = self.getUserOr404(pk)
#     #     if type(object) is Response:
#     #         return object

#     #     object.delete()
#     #     return Response(
#     #         {
#     #             "message": "User deleted!"
#     #         },
#     #         status=status.HTTP_200_OK
#     #     )
