from rest_framework import serializers

from webapp.models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id',
                  'text',
                  'name',
                  'email',
                  'rate',
                  'is_moderated',
                  'created_at'
                  )
        read_only_fields = ('id', 'created_at')


class QuoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
                  'text',
                'is_moderated',
                  )

