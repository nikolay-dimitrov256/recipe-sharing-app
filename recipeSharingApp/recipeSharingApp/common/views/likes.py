from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from recipeSharingApp.common.models import Like
from recipeSharingApp.common.serializers import LikeSerializer


class LikeCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            author = self.request.user
            recipe = serializer.validated_data.get('recipe')

            if Like.objects.filter(author=author, recipe=recipe).exists():
                return Response({'detail': 'You have already liked this recipe.'}, status=HTTP_400_BAD_REQUEST)

            like = Like.objects.create(author=author, recipe=recipe)
            return Response(LikeSerializer(like).data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LikeRetrieveDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        author_id = self.request.user.pk
        recipe_id = self.kwargs.get('recipe_id')

        try:
            like = Like.objects.get(author_id=author_id, recipe_id=recipe_id)
            like.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'detail': 'Like not found.'}, status=HTTP_404_NOT_FOUND)


    def get(self, request, *args, **kwargs):
        recipe_id = self.kwargs.get('recipe_id')

        likes_count = Like.objects.filter(recipe_id=recipe_id).count()
        data = {'likes_count': likes_count}

        return Response(data, status=200)
