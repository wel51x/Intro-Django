from rest_framework import serializers,viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
    # queryset = PersonalNoteSerializer.objects.all()
'''
        def create(self, validated_data):
            user = self.context['request'].user
            try:
                if user is None: # The variable
                    user = "admin"
            except NameError:
                user = "admin"
            note = PersonalNote.objects.create(user=user, **validated_data)
            return note 
'''