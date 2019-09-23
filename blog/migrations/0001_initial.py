# Generated by Django 2.2.5 on 2019-09-22 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/')),
                ('description', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Marketing', 'Marketing'), ('Student Consultancy', 'Student Consultancy'), ('Web Development', 'Web Development'), ('Teach', 'Teach'), ('Designing', 'Designing'), ('Other', 'Other')], default='Other', max_length=50)),
                ('featured', models.BooleanField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]