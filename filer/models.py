from django.db import models
from edgar.models import QuarterlyHolding, Filer

class QuarterlyFilerView(models.Model):
    filerId = models.ForeignKey(Filer, on_delete=models.CASCADE)
    quarterId = models.ForeignKey(QuarterlyHolding, on_delete=models.CASCADE)
    previousMarketValue = models.FloatField(blank=True)
    previousHoldingsCount = models.FloatField(blank=True)
    newHoldingsCount = models.FloatField(blank=True)
    increasedHoldingsCount = models.FloatField(blank=True)
    decreasedHoldingsCount = models.FloatField(blank=True)
    soldOutHoldingsCount = models.FloatField(blank=True)
    top10HoldingsPercent = models.FloatField(blank=True)
    averageHoldingPeriod = models.FloatField(blank=True)
    filerDescription = models.TextField(blank=True)
    quarterlyFilerViewId = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=None, blank=True)
    deletedAt = models.DateTimeField(default=None, blank=True)
    class Meta:
        ordering = ['createdAt']