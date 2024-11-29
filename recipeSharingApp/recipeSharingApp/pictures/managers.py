from django.db.models import Manager


class PictureManager(Manager):

    def get_main(self):
        return self.filter(is_main=True).first()
