# Generated by Django 2.2.4 on 2019-08-07 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offices.Office')),
            ],
        ),
    ]