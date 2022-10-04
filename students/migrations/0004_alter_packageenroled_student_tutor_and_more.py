# Generated by Django 4.1.1 on 2022-10-04 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_packageenroled_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageenroled',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='students.student'),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=8)),
                ('adress', models.CharField(max_length=100, unique=True)),
                ('package', models.ManyToManyField(to='students.package')),
            ],
        ),
        migrations.AddField(
            model_name='packageenroled',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutor', to='students.tutor'),
        ),
    ]
