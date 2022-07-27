# Generated by Django 4.0.5 on 2022-06-27 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lymessages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mymessageuser',
            name='revuserid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagerevuserid', to=settings.AUTH_USER_MODEL, verbose_name='接收者用户ID'),
        ),
        migrations.AddField(
            model_name='mymessageuser',
            name='senduserid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagesenduserid', to=settings.AUTH_USER_MODEL, verbose_name='发送者用户ID'),
        ),
        migrations.AddField(
            model_name='mymessagetemplate',
            name='creator',
            field=models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='mymessage',
            name='creator',
            field=models.ForeignKey(db_constraint=False, help_text='创建人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='mymessage',
            name='msg_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lymessages.mymessagetemplate', verbose_name='消息类型'),
        ),
    ]
