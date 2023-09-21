from rest_framework import serializers
from .models import Book, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name','description','book','parent','user','subsection')

    def get_fields(self):
        fields = super(SectionSerializer, self).get_fields()
        fields['subsection'] = SectionSerializer(many=True, read_only = True)
        return fields


class BookSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ('title','description','auther','sections')
