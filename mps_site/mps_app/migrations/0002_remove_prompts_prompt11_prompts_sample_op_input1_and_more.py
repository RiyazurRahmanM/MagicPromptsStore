# Generated by Django 4.2.1 on 2023-05-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mps_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompts',
            name='prompt11',
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input1',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input10',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input2',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input3',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input4',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input5',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input6',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input7',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input8',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='prompts',
            name='sample_op_input9',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AlterField(
            model_name='prompts',
            name='prompt1',
            field=models.CharField(default='Null', max_length=1000),
        ),
    ]
