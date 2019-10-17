# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-17 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20181115_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='reservation_message',
            field=models.CharField(blank=True, help_text='Which event the question is reserved for', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='reserved',
            field=models.BooleanField(default=False, help_text='This question is reserved for an event, do not publish yet'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='author_email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='question',
            name='comment',
            field=models.TextField(blank=True, default='', help_text='Comments for admins and contributors, not displayed on the site'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Not set'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Expert')], default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, default='', help_text='Use markdown, and refer to the standard like this: [section.subsection]Â§x.yÂ¶z.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='hint',
            field=models.TextField(blank=True, default='No hint', help_text='Use markdown, and refer to the standard like this: [section.subsection]Â§x.yÂ¶z.'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.CharField(choices=[('OK', 'The program is guaranteed to output:'), ('CE', 'The program has a compilation error'), ('US', 'The program is unspecified / implementation defined'), ('UD', 'The program is undefined')], default='OK', max_length=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='retraction_message',
            field=models.TextField(blank=True, default='', help_text='Use markdown'),
        ),
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.CharField(choices=[('NEW', 'New'), ('WAI', 'Waiting'), ('ACC', 'Accepted'), ('REF', 'Refused'), ('PUB', 'Published'), ('RET', 'Retracted')], default='NEW', max_length=3),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='key',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='usersanswer',
            name='answer',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='usersanswer',
            name='ip',
            field=models.CharField(blank=True, default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='usersanswer',
            name='result',
            field=models.CharField(choices=[('OK', 'The program is guaranteed to output:'), ('CE', 'The program has a compilation error'), ('US', 'The program is unspecified / implementation defined'), ('UD', 'The program is undefined')], default='OK', max_length=2),
        ),
    ]
