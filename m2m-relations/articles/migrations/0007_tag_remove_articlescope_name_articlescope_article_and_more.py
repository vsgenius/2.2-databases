# Generated by Django 4.0.3 on 2022-04-01 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_options_remove_tagposition_name_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='articlescope',
            name='name',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlescope',
            name='main',
            field=models.BooleanField(default=1, verbose_name='Основной'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TagPosition',
        ),
        migrations.AddField(
            model_name='articlescope',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Positions', to='articles.tag', verbose_name='Раздел'),
            preserve_default=False,
        ),
    ]
