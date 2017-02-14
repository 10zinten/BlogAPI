from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'publish', 
		]


"""
	
data = {
	"title": "Cool Buddy",
	"content": "Cool content",
	"publish": "2017-2-14",
	"slug": "Cool-Buddy",
}

new_item = PostSerializer(data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)	

"""
