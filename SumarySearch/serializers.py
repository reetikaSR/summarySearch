from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    """
    serializer for the book class
    """
    id = serializers.IntegerField()
    summary = serializers.CharField()
    author = serializers.SerializerMethodField()
    query = serializers.SerializerMethodField()

    #  custom method to get the author of the book
    def get_author(self, obj):
        return obj.get_author()

    # add the corresponding query string to the results
    def get_query(self, obj):
        return self.context.get('query', None)

    class Meta:
        fields = ('id', 'summary', 'author', 'query', )