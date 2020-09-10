from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"User {self.id}: {self.username}"


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255, null=True)
    date_posted = models.DateTimeField()
    poster_id = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    current_price = models.FloatField(default=0)
    description = models.CharField(max_length=1000, null=True)
    photo_url = models.URLField(null=True)
    category = models.CharField(max_length=25, default="Misc")

    def __str__(self):
        return f"Item {self.id}: {self.item_name}  by user {self.poster_id} on {self.date_posted}"


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    post_on_which = models.ForeignKey(Listing, blank=True, related_name="bids", on_delete=models.CASCADE)
    bid_by = models.ForeignKey(User, related_name="past_bids_by_user", on_delete=models.CASCADE)
    bid_amount = models.FloatField()

    def __str__(self):
        return f"Bid {self.id}: {self.bid_amount}  by user {self.bid_by} on {self.post_on_which}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_on_which = models.ForeignKey(Listing, blank=True, related_name="comments", on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    date_posted = models.DateTimeField()
    comment_content = models.CharField(max_length=255)

    def __str__(self):
        return f"Comment {self.id}: {self.comment_content}  by user {self.commenter} on {self.post_on_which}"