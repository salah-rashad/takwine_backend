from adminsortable2.admin import SortableAdminMixin, SortableStackedInline
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from model_clone import CloneModelAdminMixin

from .models.document import Document
from .models.document_category import DocumentCategory
from .models.document_file import DocumentFile
from .models.featured_document import FeaturedDocument


@admin.register(Document)
class DocumentAdmin( SortableAdminMixin, CloneModelAdminMixin, SummernoteModelAdmin):

    class FileStackedInline(SortableStackedInline):
        model = DocumentFile
        extra = 0
        show_change_link = True
        fieldsets = [
            [None, {"fields": ['name', 'file', 'ordering']}]]
        ordering = ['ordering']

    summernote_fields = ['content']
    list_display = ['id', 'title', 'category', 'enabled', 'ordering']
    list_filter = ['enabled', 'category__title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'category', 'enabled']
    inlines = [FileStackedInline]


@admin.register(FeaturedDocument)
class FeaturedDocumentAdmin(SortableAdminMixin,CloneModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(CloneModelAdminMixin,admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id', 'title']
    ordering = ['id']


@admin.register(DocumentFile)
class DocumentFileAdmin(SortableAdminMixin,CloneModelAdminMixin, admin.ModelAdmin):
    pass
