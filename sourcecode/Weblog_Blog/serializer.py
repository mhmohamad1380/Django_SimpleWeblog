from rest_framework import serializers
from Weblog_Blog.models import BlogContent

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = "__all__"