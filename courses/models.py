from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, FloatField, DateField, \
    BooleanField


class Technology(Model):
    name = CharField(max_length=32)

    def __str__(self):
        return self.name


class Course(Model):
    title = CharField(max_length=100)
    technology = ForeignKey(Technology, on_delete=DO_NOTHING)
    price = FloatField()
    starts = DateField()
    finish = DateField()
    remote = BooleanField()

    def __str__(self):
        return self.title
