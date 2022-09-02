# Generated by Django 4.1 on 2022-09-02 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristics',
            options={'verbose_name': 'characteristicss', 'verbose_name_plural': 'characteristics'},
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mosvla', models.DateTimeField()),
                ('wasvla', models.DateTimeField()),
                ('comment', models.TextField(max_length=255)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.person')),
            ],
        ),
    ]
