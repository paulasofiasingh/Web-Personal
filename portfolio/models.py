from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    link = models.URLField(verbose_name="Dirección web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # Esto significa que en este campo se añadirá la hora automáticamente cuando se cree la primera vez
    updated = models.DateTimeField(auto_now=True, verbose_name='Última actualización') # Este se ejecuta cada vez que se actualiza una instancia

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos" # Si no le ponemos este atributo automáticamente le agregará una s al final
        ordering = ["-created"] # Ordenar por fecha de creación del más nuevo al más antiguo. Que salgan primero los últimos que hemos creado

    def __str__(self):
        return self.title