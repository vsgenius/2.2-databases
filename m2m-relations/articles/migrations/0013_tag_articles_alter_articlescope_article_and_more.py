# Generated by Django 4.0.3 on 2022-04-07 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_remove_tag_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Positions', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
