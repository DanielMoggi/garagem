# Generated by Django 4.1.7 on 2023-03-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_acessorio_cor_rename_descrição_categoria_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='Nome',
            field=models.CharField(default='Daniel', max_length=100),
            preserve_default=False,
        ),
    ]