from django.contrib import admin
from .models import Author, Catagory, Blog, Tag, EmailSignUp,\
     Contact, Comment, Reply , Subcategory

from mptt.admin import DraggableMPTTAdmin
from .models import Catagory


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Catagory.objects.add_related_count(
                qs,
                # Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Catagory.objects.add_related_count(qs,
                #  Product,
                 'categories',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'



admin.site.register(Catagory)

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(EmailSignUp)
admin.site.register(Contact)
admin.site.register(Subcategory)
