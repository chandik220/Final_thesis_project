# Generated by Django 4.0.4 on 2022-08-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_alter_donation_id_alter_donationarea_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='adminremark',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='collectionloc',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donationarea',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='donation.donationarea'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donationname',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donationpic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='donation',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='updationdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='donation.volunteer'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='volunteerremark',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
