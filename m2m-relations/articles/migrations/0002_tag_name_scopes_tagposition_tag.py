# Generated by Django 4.0.3 on 2022-04-01 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=1, max_length=256, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Scopes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(related_name='scopes', to='articles.article')),
                ('tags', models.ManyToManyField(related_name='scopes', to='articles.tag')),
            ],
        ),
        migrations.AddField(
            model_name='tagposition',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.scopes'),
            preserve_default=False,
        ),
    ]
