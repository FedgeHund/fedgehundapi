# Generated by Django 3.0.5 on 2020-09-08 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.TextField(max_length=80)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('companyId', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField(max_length=120)),
                ('companyType', models.CharField(choices=[('HF', 'Hedge Fund'), ('IA', 'Investment Advisor'), ('HC', 'Holdings Company')], default=None, max_length=2)),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='FailsToDeliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settlementDate', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('cusip', models.TextField()),
                ('ticker', models.CharField(max_length=7)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='Filer',
            fields=[
                ('fileNumber', models.CharField(max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('filerId', models.AutoField(primary_key=True, serialize=False)),
                ('fileType', models.CharField(choices=[('13F', '13F'), ('13G', '13G'), ('13D', '13D')], max_length=3)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Company')),
            ],
            options={
                'ordering': ['companyId'],
            },
        ),
        migrations.CreateModel(
            name='QuarterlyHolding',
            fields=[
                ('quarter', models.IntegerField()),
                ('filingType', models.CharField(choices=[('CR', 'Combined Report'), ('NT', 'Notice'), ('HR', 'Holdings Report')], max_length=2)),
                ('filedOn', models.DateTimeField(blank=True)),
                ('acceptedAt', models.DateTimeField(blank=True)),
                ('totalValue', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('quarterlyHoldingId', models.AutoField(primary_key=True, serialize=False)),
                ('filerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Filer')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='QuarterlyOtherManager',
            fields=[
                ('number', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('otherManagerId', models.AutoField(primary_key=True, serialize=False)),
                ('childFilerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_filer', to='edgar.Filer')),
                ('parentFilerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_filer', to='edgar.Filer')),
                ('quarterlyHoldingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.QuarterlyHolding')),
            ],
            options={
                'ordering': ['quarterlyHoldingId'],
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('cusip', models.TextField()),
                ('securityName', models.TextField()),
                ('securityType', models.TextField()),
                ('ticker', models.CharField(max_length=5)),
                ('titleOfClass', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('securityId', models.AutoField(primary_key=True, serialize=False)),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Company')),
            ],
            options={
                'ordering': ['ticker'],
            },
        ),
        migrations.CreateModel(
            name='QuarterlySecurityHolding',
            fields=[
                ('value', models.FloatField()),
                ('amount', models.FloatField()),
                ('holdingType', models.CharField(choices=[('SHR', 'SH'), ('PRN', 'PRN'), ('PUT', 'PUT'), ('CAL', 'CALL')], max_length=3)),
                ('investmentDiscretion', models.CharField(choices=[('SOLE', 'SOLE'), ('DFND', 'DFND'), ('OTHR', 'OTHER')], max_length=4)),
                ('sole', models.IntegerField()),
                ('shared', models.IntegerField()),
                ('none', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('quarterlySecurityHoldingId', models.AutoField(primary_key=True, serialize=False)),
                ('quarterlyHoldingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.QuarterlyHolding')),
                ('securityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Security')),
            ],
            options={
                'ordering': ['quarterlyHoldingId'],
            },
        ),
        migrations.CreateModel(
            name='QuarterlyOtherManagerDistribution',
            fields=[
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('quarterlyOtherManagerDistributionId', models.AutoField(primary_key=True, serialize=False)),
                ('quarterlyOtherManagerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.QuarterlyOtherManager')),
                ('quarterlySecurityHoldingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.QuarterlySecurityHolding')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
