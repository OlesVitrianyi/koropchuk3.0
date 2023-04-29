from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from mainapp.views import *
from .models import BookingPier, Pier
from .serializers import BookingPierSerializer
from datetime import datetime, timedelta
from .forms import *

class BookingPierAPIList(generics.ListCreateAPIView):
    queryset = BookingPier.objects.all()
    #queryset = BookingPier.booking_pier_unique.self.all()
    #queryset = BookingPier.objects.exclude(wish="j")
    # pier_id = BookingPier.objects.filter(pier_id="pier_id")  # test
    # time_booking_start = BookingPier.objects.filter(time_booking_start="time_booking_start")  # test
    # time_booking_finish = BookingPier.objects.filter(time_booking_finish="time_booking_finish")  # test
    # time_booking_startt = time_booking_start_lte = time_booking_start  # test
    # time_booking_finishh = time_booking_finish_gte = time_booking_finish  # test
    # time_booking_start = index.objects.filter(time_booking_start__lte="time_booking_start")  # test
    # time_booking_finish = index.objects.filter(time_booking_finish__gte="time_booking_finish")  # test
    # queryset = BookingPier.objects.all().exclude(pier_id=pier_id and time_booking_startt and time_booking_finishh)  # test
    #queryset = BookingPier.objects.exclude(time_booking__gte=datetime.date(2005, 1, 3))  # test
    serializer_class = BookingPierSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
#test

    # def bookingapier(request):
    #     form = BookingAPierForm()
    #     return render(request, 'mainapp/bookingapier.html', {'form': form})
        # if request.method == 'POST':
        #     form = BookingAPierForm(request.POST)
        #     if form.is_valid():
        #         print(form.cleaned_data)
        # else:
        #     form = BookingAPierForm()
        # return render(request, 'mainapp/bookingapier.html', {'form': form, 'title': 'Бронювання місця'})
#test

    # def booking_pier_api(self):
    #     if checkPierID(pier_id=1):
    #         raise Http404()


class BookingPierAPIUpdate(generics.UpdateAPIView):
    queryset = BookingPier.objects.all()
    serializer_class = BookingPierSerializer


class BookingPierAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingPier.objects.all()
    serializer_class = BookingPierSerializer


# class BookingPierViewSet(mixins.CreateModelMixin,
#                          mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
# #                         mixins.DestroyModelMixin,
#                          mixins.ListModelMixin,
#                          GenericViewSet):
# #    queryset = BookingPier.objects.all()
#     serializer_class = BookingPierSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return BookingPier.objects.all()[:3]
#
#         return BookingPier.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def pier(self, request, pk=None):
#         piers = Pier.objects.get(pk=pk)
#         return Response({'piers': piers.name})
#
# # class BookingPierAPIList(generics.ListCreateAPIView):
# #     queryset = BookingPier.objects.all()
# #     serializer_class = BookingPierSerializer
# #
# #
# # class BookingPierAPIUpdate(generics.UpdateAPIView):
# #     queryset = BookingPier.objects.all()
# #     serializer_class = BookingPierSerializer
# #
# #
# # class BookingPierAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = BookingPier.objects.all()
# #     serializer_class = BookingPierSerializer
#
#
# # class BookingPierAPIView(APIView):
# #     def get(self, request):
# #         w = BookingPier.objects.all()
# #         return Response({'post': BookingPierSerializer(w, many=True).data})
# #
# #     def post(self, request):
# #         serializer = BookingPierSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         # post_new = BookingPier.objects.create(
# #         #     pier_id=request.data['pier_id'],
# #         #     pier_status=request.data['pier_status'],
# #         #     wish=request.data['wish'],
# #         # )
# #         return Response({'post': serializer.data})
# #
# #     def put(self, request, *args, **kwargs):
# #         pk = kwargs.get("pk", None)
# #         if not pk:
# #             return Response({"error": "Method PUT not allowed"})
# #
# #         try:
# #             instance = BookingPier.objects.get(pk=pk)
# #         except:
# #             return Response({"error": "Object does not exists"})
# #
# #         serializer = BookingPierSerializer(data=request.data, instance=instance)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response({"post": serializer.data})
#
# # def delete(self, request, *args, **kwargs):
# #     pk = kwargs.get("pk", None)
# #     if not pk:
# #         return Response({"error": "Method DELETE not allowed"})
# #
# #     try:
# #         instance = BookingPier.objects.delete(pk=pk)
# #     except:
# #         return Response({"error": "Object does not exists for delete"})
# #
# #     serializer = BookingPierSerializer(data=request.data, instance=instance)
# #     serializer.is_valid(raise_exception=True)
# #     serializer.save()
# #
# #     return Response({"post": "delete post " + str(pk)})
#
# # class BookingPierAPIView(generics.ListAPIView):
# #     queryset = BookingPier.objects.all()
# #     serializer_class = BookingPierSerializer
