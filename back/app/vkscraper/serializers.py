from rest_framework import serializers


class SearchUserRequestSerializer(serializers.Serializer):
    q = serializers.CharField(help_text="Поисковый запрос в ВК")
    page = serializers.IntegerField(
        required=False, help_text="Номер страницы результата"
    )
    count = serializers.IntegerField(
        required=False, help_text="Количество элементов на странице"
    )


class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField(
        required=False, help_text="Номер страницы результата"
    )
    count = serializers.IntegerField(
        required=False, help_text="Количество элементов на странице"
    )


class CeleryTaskSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        required=False, help_text="Количество постов для сбора, по умолчанию будут собраны все посты"
    )
    socket_id = serializers.IntegerField(
        required=False, help_text="Webscoket ID, по которому будут отправляться собранные посты"
    )


class EmptySerializer(serializers.Serializer):
    pass
