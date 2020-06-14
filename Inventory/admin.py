from django.contrib import admin

# Register your models here.

from .models import Item,Category,Client,Transaction,Account_Details

class TransInline(admin.TabularInline):
    model=Transaction
    extra = 2

class ItemInline(admin.TabularInline):
    model=Item
    extra = 2

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Details', {'fields': ['place','description','balance'], 'classes': ['collapse']}),
    ]
    inlines = [TransInline]

class ClientListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Details', {'fields': ['place','description','balance'], 'classes': ['collapse']}),
    ]
    inlines = [TransInline]

    list_display = ('name','place','description','balance')

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Details', {'fields': ['category','quantity','price',], 'classes': ['collapse']}),
    ]
    inlines = [TransInline]

class ItemListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['name']}),
        ('Details', {'fields': ['category','quantity','price',], 'classes': ['collapse']}),
    ]
    inlines = [TransInline]

    list_display = ('name','category','quantity','price')

class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['item']}),
        ('Details', {'fields': ['client','quantity',], 'classes': ['collapse']}),
    ]

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category']}),
        # ('Details', {'fields': ['client','quantity',]}),
    ]
    inlines = [ItemInline]

class AccDetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction',               {'fields': ['transaction']}),
        ('Details', {'fields': ['client','description',], 'classes': ['collapse']}),
        ('Amounts', {'fields': ['debit_amount','credit_amount','balance_amount'], 'classes': ['collapse']}),
    ]

class AccDetListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transaction',               {'fields': ['transaction']}),
        ('Details', {'fields': ['client','description',], 'classes': ['collapse']}),
        ('Amounts', {'fields': ['debit_amount','credit_amount','balance_amount'], 'classes': ['collapse']}),
    ]

    list_display = ('client','transaction','time')

admin.site.register(Item,ItemListAdmin)
# admin.site.register(Client,ClientAdmin)
admin.site.register(Client,ClientListAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Account_Details,AccDetListAdmin)
