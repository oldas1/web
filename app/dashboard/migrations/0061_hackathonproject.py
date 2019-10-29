# Generated by Django 2.2.4 on 2019-10-29 21:55

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0060_auto_20191023_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('work_url', models.URLField(help_text='Repo or PR url')),
                ('summary', models.TextField(blank=True, default='')),
                ('badge', models.URLField(blank=True, db_index=True, help_text='badge img url', null=True)),
                ('status', models.CharField(blank=True, choices=[('invalid', 'invalid'), ('pending', 'pending'), ('accepted', 'accepted'), ('completed', 'completed')], max_length=20)),
                ('bounty', models.ForeignKey(help_text='bounty prize url', on_delete=django.db.models.deletion.CASCADE, related_name='project_bounty', to='dashboard.Bounty')),
                ('hackathon', models.ForeignKey(help_text='Hackathon event', on_delete=django.db.models.deletion.CASCADE, related_name='project_event', to='dashboard.HackathonEvent')),
                ('profiles', models.ManyToManyField(related_name='project_profiles', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
