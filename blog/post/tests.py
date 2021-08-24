from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls.base import reverse
from category.models import Category
from post.models import Post


class PostViewTest(TestCase):
    """
    Tests the Post View Context Data
    """
    c = Client()

    def setUp(self):
        """
        Creating some user, category, post objects in the database
        """
        self.user1 = User.objects.create(username="test_user1")
        self.user1.set_password("abcde@12345")
        self.user2 = User.objects.create(username="test_user2")
        self.user2.set_password("abcde@12345")

        self.user1.save()
        self.user2.save()

        self.category1 = Category.objects.create(
            name="Educational",
            description="This is an Educational Category",
            created_by=self.user1,
            status="A",
        )
        self.category2 = Category.objects.create(
            name="Programming",
            description="This is a Programming Category",
            created_by=self.user2,
            status="A",
        )
        self.post1 = Post.objects.create(
            title="The Education System of My Country",
            body=
            "In this post, we will descuss about the education system of our country",
            author=self.user1,
            status="A",
        )
        self.post2 = Post.objects.create(
            title="Top 10 Python Framework",
            body=
            "In thi post, we will descuss about the lastest framework of python",
            author=self.user2,
            status="A",
        )
        self.post1.category.add(self.category1)
        self.post2.category.add(self.category2)

    def test_view_dashboard_context(self):
        response = self.c.get(reverse("post:dashboard"))
        posts_queryset = Post.objects.filter(
            status="A").order_by("-last_updated")
        category_queryset = Category.objects.filter(
            status="A").order_by("id").values("id", "name")[:4]
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["posts"], posts_queryset)
        self.assertQuerysetEqual(response.context["categories"],
                                 category_queryset)

    def test_post_detailView(self):
        posts = Post.objects.all()
        postSlug_list = [post.slug for post in posts]
        for slug in postSlug_list:
            response = self.c.get(
                reverse("post:view-post", kwargs={"slug": slug}))
            self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        """
        Tests both get and post method of PostCreateView
        """
        # First we test the get method
        self.c.login(username="test_user1", password="abcde@12345")
        response = self.c.get(reverse("post:create-post"))
        self.assertEqual(response.status_code, 200)
        # Now we test the post method
        response = self.c.post(
            reverse("post:create-post"), {
                "title": "This is a test post",
                "body": "post description",
                "category": self.category1.id,
                "author": User.objects.get(username="test_user1").id
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("post:manage-post"))
        self.assertTrue(Post.objects.filter(title="This is a test post"))

    def test_post_update_view(self):
        """
        Tests the get and post method of post update view
        """
        # First we test the get method
        self.c.login(username="test_user1", password="abcde@12345")
        response = self.c.get(
            reverse("post:update-post", kwargs={"pk": self.post1.id}))
        self.assertEqual(response.status_code, 200)
        # Now we test the post method
        response = self.c.post(
            reverse("post:update-post", kwargs={"pk": self.post1.id}), {
                "title": "Education System of My Country ........",
                "body":
                "In this post, we will descuss about the education system of our country",
                "author": self.user1,
                "status": "A",
            })
        self.assertRedirects(response, reverse("post:manage-post"))
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.title,
                         "Education System of My Country ........")

    def test_post_delete_view(self):
        """
        Tests the post delete view
        """
        # Checks whether the user can delete their own post
        self.c.login(username="test_user1", password="abcde@12345")
        response = self.c.post(
            reverse("post:delete-post", kwargs={"pk": self.post1.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("post:manage-post"))
        self.assertFalse(Post.objects.filter(id=self.post1.id))
        # Checks whether the user can't delete other user post
        response = self.c.post(
            reverse("post:delete-post", kwargs={"pk": self.post2.id}))
        self.assertEqual(response.status_code, 403)

    def test_manage_post_listview(self):
        self.c.login(username="test_user1", password="abcde@12345")
        response = self.c.get(reverse("post:manage-post"))
        self.assertEqual(response.status_code, 200)
        posts_queryset = Post.objects.filter(author=self.post1.id)
        self.assertQuerysetEqual(response.context["posts"], posts_queryset)