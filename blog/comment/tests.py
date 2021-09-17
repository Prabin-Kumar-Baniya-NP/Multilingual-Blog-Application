from json import encoder
from json.encoder import JSONEncoder
from comment.models import Comment
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
from category.models import Category
from post.models import Post
from django.core.serializers.json import Deserializer
import json
import io


class TestCommentView(TestCase):
    c = Client()

    def setUp(self):
        """
        Setup 2 test user, 2 post objects, 2 category objects, (8 + 8) comments objects 
        """
        self.user11 = User.objects.create(username="test_user11")
        self.user11.set_password("abcde@12345")
        self.user22 = User.objects.create(username="test_user22")
        self.user22.set_password("abcde@12345")

        self.user11.save()
        self.user22.save()

        self.category11 = Category.objects.create(
            name="Technical",
            description="This is an Technical Category.......",
            created_by=self.user11,
            status="A",
        )
        self.category22 = Category.objects.create(
            name="Fitness",
            description="This is a Fitness Category.......",
            created_by=self.user22,
            status="A",
        )
        self.post11 = Post.objects.create(
            title="The Technical System of My Country ........",
            body=
            "In this post, we will descuss about the technical system of our country",
            author=self.user11,
            status="A",
        )
        self.post22 = Post.objects.create(
            title="Top 10 Fitness Tips........",
            body="In this post, we will descuss about the fitness tips",
            author=self.user22,
            status="A",
        )
        self.post11.category.add(self.category11)
        self.post22.category.add(self.category22)

        self.comments_data_list1 = [
            {
                "body": "nice post",
                "commented_by": self.user11.username
            },
            {
                "body": "bad post",
                "commented_by": self.user11.username
            },
            {
                "body": "average post",
                "commented_by": self.user22.username
            },
            {
                "body": "excellent post",
                "commented_by": self.user22.username
            },
        ]
        self.comments_data_list2 = [
            {
                "body": "nice post",
                "commented_by": self.user11.username
            },
            {
                "body": "bad post",
                "commented_by": self.user11.username
            },
            {
                "body": "average post",
                "commented_by": self.user22.username
            },
            {
                "body": "excellent post",
                "commented_by": self.user22.username
            },
        ]

        for comment in self.comments_data_list1:
            Comment.objects.create(
                post=self.post11,
                body=comment["body"],
                commented_by=comment["commented_by"],
            )
        for comment in self.comments_data_list2:
            Comment.objects.create(
                post=self.post22,
                body=comment["body"],
                commented_by=comment["commented_by"],
            )

    def test_get_comment_ajax_view(self):
        """
        Tests the get comment ajax view for unauthenticated user
        """
        response = self.c.get(reverse("comments:get-comments",
                                      kwargs={
                                          "postID": self.post11.id,
                                          "startIndex": 0
                                      }),
                              HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        comments_data = json.loads(response.content)
        comments_objects = Comment.objects.filter(
            post=self.post11.id).order_by("id").values("body",
                                                       "commented_by")[:4]
        for i, obj in enumerate(comments_objects):
            self.assertEqual(obj["body"], comments_data[i]["fields"]["body"])
            self.assertEqual(obj["commented_by"], comments_data[i]["fields"]["commented_by"])


    def test_post_comment_ajax_view(self):
        """
        Tests the post comment ajax view
        """
        self.c.login(username="test_user11", password="abcde@12345")
        json_post_data = json.dumps({
            "post": self.post11.id,
            "body": "very very nice post",
            "commented_by": self.user11.username,
        })
        response = self.c.post(
            reverse("comments:post-comment"),
            json_post_data,
            content_type='JSON_CONTENT',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(response.status_code, 200)
