from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField
from drf_extra_fields.fields import Base64ImageField


class BasePostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username',
                              read_only=True, )


class PostSerializer(BasePostSerializer):
    group = PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following',)
        model = Follow

    def validate_following(self, value):
        user = self.context['request'].user
        following = User.objects.get(
            username=self.context['request'].data['following']
        )
        if user == value:
            raise serializers.ValidationError(
                'Нельзя подписки теребонькать >:['
            )
        if Follow.objects.filter(user=user, following=following):
            raise serializers.ValidationError(
                'Нельзя подписки размножать против их воли >:['
            )
