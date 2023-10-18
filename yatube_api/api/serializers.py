from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = ("user", "following")
        model = Follow

    def validate_following(self, value):
        user = self.request.user
        if value == user:
            raise serializers.ValidationError("Подписка на самого себя.")
        if Follow.objects.filter(following=value, user=user).exists():
            raise serializers.ValidationError("Повторная подписка невозможна.")
        return value







# from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField


# from posts.models import Comment, Post


# class PostSerializer(serializers.ModelSerializer):
#     author = SlugRelatedField(slug_field='username', read_only=True)

#     class Meta:
#         fields = '__all__'
#         model = Post


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True, slug_field='username'
#     )

#     class Meta:
#         fields = '__all__'
#         model = Comment
