
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=("Parent Category"),
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

    def my_children(self):
        """Return childrens of self-category """
        return Category.objects.filter(parent=self)

    def my_products(self):
        """ Return All the Products connected with self-category """
        return self.product_set.all()
    
    @property
    def is_parent(self):
        """ Return `True` if self-object is a main-category """
        if self.parent is not None:
            return False
        return True
