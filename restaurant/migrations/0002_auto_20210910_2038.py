# Generated by Django 3.2.6 on 2021-09-10 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='restaurant.food')),
            ],
        ),
        migrations.DeleteModel(
            name='Ingreadient',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
