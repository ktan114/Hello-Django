from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

class PersonalNoteViewSet(viewsets.ModelViewSet):

    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        user = self.request.user
        superuser = self.request.user.is_superuser

        if user.is_anonymous:
            return PersonalNote.objects.none()
        elif superuser:
            return PersonalNote.objects.all()
        else:
            return PersonalNote.objects.filter(user=user)


