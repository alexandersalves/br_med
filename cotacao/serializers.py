from rest_framework import serializers


class GetRateSerializer(serializers.Serializer):
    currency_from = serializers.CharField(max_length=3)
    currency_to = serializers.CharField(max_length=3)
    start_date = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')
    end_date = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')

    def validate(self, attrs):
        if attrs.get('start_date') > attrs.get('end_date'):
            raise serializers.ValidationError(
                'Data inicial deve ser anterior ou igual à data final.'
            )

        if (attrs.get('end_date') - attrs.get('start_date')).days >= 5:
            raise serializers.ValidationError(
                'As datas não podem ter mais de 5 dias de diferença'
            )

        if attrs.get('currency_from') == attrs.get('currency_to'):
            raise serializers.ValidationError(
                'As moedas devem ser diferentes.'
            )

        return attrs
