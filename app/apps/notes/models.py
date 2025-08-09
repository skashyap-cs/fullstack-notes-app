import uuid
from django.db import models
from django.conf import settings

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # note_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255)     # note_title
    content = models.TextField(blank=True)       # note_content
    created_on = models.DateTimeField(auto_now_add=True)  # created_on
    last_update = models.DateTimeField(auto_now=True)     # last_update

    def __str__(self):
        return self.title
