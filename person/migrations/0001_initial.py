# Generated by Django 4.1 on 2022-09-02 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristics', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ChildDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentdepartment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'sexs',
                'verbose_name_plural': 'Sex',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/')),
                ('cardnum', models.CharField(max_length=9, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('personalid', models.CharField(max_length=11, unique=True)),
                ('ChilrdDepartment1', models.CharField(max_length=150)),
                ('dateofbirth', models.DateField()),
                ('dateofexpiry', models.DateField()),
                ('Childepartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='person.childdepartment')),
                ('characteristics', models.ManyToManyField(to='person.characteristics')),
                ('parentdepartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='person.parentdepartment')),
                ('sex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.sex')),
            ],
        ),
        migrations.AddField(
            model_name='childdepartment',
            name='parentdepartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.parentdepartment'),
        ),
    ]
