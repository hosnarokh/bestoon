from django.contrib import admin

from .models import Expense, Income


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'description', 'created_date',)
    fields = ('amount', 'description', 'created_date', 'updated_date')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'description', 'created_date',)
    fields = ('amount', 'description', 'created_date', 'updated_date')
