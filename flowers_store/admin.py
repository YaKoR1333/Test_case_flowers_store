from django.contrib import admin
from .models import Shade, Status, Profile, Lot, Comment, TradeBook


class LotInLine(admin.TabularInline):
    model = Lot


class LotCommentInLine(admin.TabularInline):
    model = Lot.comment.through


class ProfileCommentInLine(admin.TabularInline):
    model = Profile.comment.through


class TradeBookInLine(admin.TabularInline):
    model = TradeBook
    fk_name = 'seller'


class ProfileAdmin(admin.ModelAdmin):
    exclude = ('comment',)
    inlines = [LotInLine, TradeBookInLine, ProfileCommentInLine]


class LotAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'title', 'shade', 'product_quantity', 'price', 'hide_mod')
    list_display_links = ('id', 'seller', 'title')
    search_fields = ('title',)
    list_editable = ('hide_mod',)
    list_filter = ('shade', 'hide_mod')
    exclude = ('comment',)
    inlines = [LotCommentInLine, ]


class TradeBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'order_number', 'description', 'buyer', 'created', 'status', 'purchase_sum')
    list_display_links = ('id', 'seller', 'buyer')
    search_fields = ('order_number',)
    list_filter = ('status',)


class LotsCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'created',)
    list_display_links = ('id', 'text', 'user')
    search_fields = ('id',)


admin.site.register(Shade)
admin.site.register(Status)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, LotsCommentAdmin)
admin.site.register(TradeBook, TradeBookAdmin)
admin.site.register(Lot, LotAdmin)
