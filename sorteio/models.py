import uuid
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Pessoa(BaseModel):
    qr_code = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    perfil_instagram = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return f'/user/{self.pk}/'

class Sorteio(BaseModel):
    premio = models.CharField(max_length=1024)
    post_instagram = models.CharField(max_length=1024, blank=True)
    perfil_instagram = models.CharField(max_length=1024, blank=True)
    inscritos = models.ManyToManyField(Pessoa, blank=True, null=True)
    vencedor_unico = models.BooleanField(default=False)
    vencedor = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT, related_name='sorteios_vencidos')
    aberto = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/sorteio/{self.pk}'