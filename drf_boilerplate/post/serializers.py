from rest_framework import serializers

from post.models import Post, Comment


class HandMadePostSerializer:
    """
    serializer 의 serialize, deserialize 작동 방식을 간단하게 풀어 쓴 class 입니다.
    """
    class Meta:
        model = Post

    def __init__(self, instance=None, data=None):
        self.instance = instance
        self.initial_data = data

    @property
    def data(self):
        """
        받은 instance 를 serialize 해서 dictionary(JSON) 형태로 돌려주는 함수입니다.
        """
        ret_dict = {
            'id': self.instance.id,
            'title': self.instance.title,
            'contents': self.instance.contents
        }
        return ret_dict

    def create(self):
        """
        받은 JSON data 를 instance 로 deserialize 해서 python instance 로 돌려주는 함수입니다.
        """
        instance = self.Meta.model.objects.create(**self.initial_data)
        return instance

    """
    def is_valid(self):
    def errors(self):
    many=True handling
    등등 다양한 기능들을 굳이 손으로 구현해야 하나?
    serializer.ModelSerializer : Do magic!
    serializer
    modelserializer
    hyperlinkedserializer
    """


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    serializer 에서 주로 override 하는 함수들을 정리했습니다.
    """
    class Meta:
        model = Comment
        fields = ['id', 'contents', ]

    def validate(self, attrs):
        """
        serializer.is_valid() 를 할 시에 call 되는 함수입니다.
        기본적으로 type checking 은 내부적으로 구현되어 있고,
        추가로 validation 을 하고싶은 경우에 해당 함수를 override 해주시면 됩니다.
        override 를 하기 위해 존재하는 method 라서 소스코드는 return attrs 가 끝입니다.
        """
        contents = attrs.get('contents', '')
        if 'fuxk' in contents:
            raise Exception('욕설은 금지입니다!')
        return attrs

    def create(self, validated_data):
        """
        serializer.save() 를 할 시에 call 되는 함수입니다.
        소스코드를 보시면 뭔가 복잡하지만, 간추려서 적으면 아래와 같습니다.
        """
        _model_class = self.Meta.model
        return _model_class.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class PostVerySecretSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # nested serializer 의 경우 create 를 추가로 구현해주거나 read_only=True
    first_comment = serializers.SerializerMethodField()  # 원하는 field 를 추가할 수 있습니다.
    secret_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'contents', 'secret_comments', 'comments', 'first_comment', ]

    def get_first_comment(self, obj):
        """
        위에 정의한 first_comment 의 값을 돌려주는 함수입니다.
        serializer 의 정보들을 사용할 필요가 없을 경우 @staticmethod 를 사용하셔도 무방합니다.
        """
        return obj.comments.first().contents

    def get_secret_comments(self, obj):
        """
        viewset 에 들어온 요청이 admin 유저일 경우 값을 돌려주고
        아닐 경우 빈 스트링을 돌려줍니다.
        """
        request = self.context.get('request', None)  # viewset 의 정보에 접근할 수 있습니다.
        if request.user.is_admin:
            return obj.very_secret
        return ''
