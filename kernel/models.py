from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Expense(models.Model):
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated date'), auto_now=True)
    amount = models.BigIntegerField(_('amount'), )
    description = models.TextField(_('description'), )
    user = models.ForeignKey(User, _('owner'), related_name='expenses')

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __str__(self):
        return '%s-%s' % (self.amount, self.description)


class Income(models.Model):
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('updated date'), auto_now=True)
    amount = models.BigIntegerField(_('amount'), )
    description = models.TextField(_('description'), )
    user = models.ForeignKey(User, _('owner'), related_name='incomes')

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')

    def __str__(self):
        return '%s-%s' % (self.amount, self.description)
