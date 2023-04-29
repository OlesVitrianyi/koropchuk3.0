import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import BookingPier



# class BookingPierModel:
#     def __init__(self, pier_id, pier_status, wish):
#         self.pier_id = pier_id
#         self.pier_status = pier_status
#         self.wish = wish


class BookingPierSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # pier_status = serializers.HiddenField()

    class Meta:
        model = BookingPier
#        fields = ("pier", "pier_status", "wish")
        fields = "__all__"

    # this block add Chat GPT
    def validate(self, data):
        instance = BookingPier(**data)
        instance.clean()
        return data
    #endblock

    #test
#     pier_id = serializers.IntegerField()
#     # PIER_STATUS_CHOICES = [
#     #      ('<span class="bk">booked</span>', 'booked'),
#     #      ('<span class="fr">free</span>', 'free'),
#     # ] choices=PIER_STATUS_CHOICES,
#     pier_status = serializers.CharField(max_length=40, default='free')
#     wish = serializers.CharField(max_length=255)
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return BookingPier.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.pier_id = validated_data.get("pier_id", instance.pier_id)
#         instance.pier_status = validated_data.get("pier_status", instance.pier_status)
#         instance.wish = validated_data.get("wish", instance.wish)
# #        instance.time_create = validated_data.get("time_create", instance.time_create)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.save()
#         return instance

    # def delete(self, instance):
    #     instance.pier_id = "pier_id", instance.pier_id
    #     instance.pier_status = "pier_status", instance.pier_status
    #     instance.wish = "wish", instance.wish
    #     instance.time_create = "time_create", instance.time_create
    #     instance.time_update = "time_update", instance.time_update
    #     instance.is_published = "is_published", instance.is_published
    #     instance.save()
    #     return instance

# def encode():
#     model = BookingPierModel('1', '<span class="bk">booked</span>', "Wish_test_Oct_6")
#     model_sr = BookingPierSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"pier_id":"1", "pier_status":"booked", "wish":"Wish_test_Oct_6"}')
#     data = JSONParser().parse(stream)
#     serializer = BookingPierSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
