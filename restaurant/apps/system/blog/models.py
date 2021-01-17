from    django.db              import models
from    core.model_mixins      import AuditFields


class  Restaurant(AuditFields):

    title        = models.CharField('TITLE',  max_length=120, blank=True, null=True)
    image        = models.ImageField('IMAGE', upload_to='pictures/' )

    
    def __str__(self):
        return self.title
