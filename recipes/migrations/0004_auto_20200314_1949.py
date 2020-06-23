# Generated by Django 3.0.3 on 2020-03-14 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200304_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images')),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('recipe', models.ManyToManyField(related_name='tags', to='recipes.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.Category', blank = True, null=True),
            preserve_default=False,
        ),
    ]