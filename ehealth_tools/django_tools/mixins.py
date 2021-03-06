from django.db import models

class HistoryFieldsMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('auth.User', null=True, blank=True)

    # Used by django-simple-history
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    # END: Used by django-simple-history

    class Meta:
        abstract = True