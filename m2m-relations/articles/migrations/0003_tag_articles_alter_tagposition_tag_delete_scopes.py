# Generated by Django 4.0.3 on 2022-04-01 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_name_scopes_tagposition_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='article', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='tagposition',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.tag'),
        ),
        migrations.DeleteModel(
            name='Scopes',
        ),
    ]
