# from django.forms import forms
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
#
# from users.models import CustomUser
# from users.serializers.status_serializer import StatusSerializer, PopulatedStatusSerializer
#
#
# class StatusViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = StatusSerializer
#
#     @action(detail=True, methods=['GET'])
#     def status(self, request, pk):
#         user = CustomUser.objects.get(pk=pk)
#         serializer = StatusSerializer(user, context={'request': request})
#
#         return Response(serializer.data)
#
#     @action(detail=True, methods=['PUT'], url_path='set_status')
#     def set_status(self, request, pk):
#         self.serializer_class = PopulatedStatusSerializer
#         forms.FileField()
#         user = CustomUser.objects.get(pk=pk)
#         serializer = PopulatedStatusSerializer(user.status, context={'request': request}, partial=True)
#
#         if serializer.is_valid():
#             user.status.set_password(serializer.validated_data['status'])
#             user.status.save()
#             return Response({'status': 'status set'})
#             # return Response(serializer.data)
