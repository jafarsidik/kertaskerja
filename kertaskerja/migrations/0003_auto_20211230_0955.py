# Generated by Django 3.2 on 2021-12-30 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
        ('kertaskerja', '0002_alter_daftarsasaran_targetkinerja'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Masteraspek',
        ),
        migrations.DeleteModel(
            name='Masterdirektorat',
        ),
        migrations.DeleteModel(
            name='Masterdivisi',
        ),
        migrations.DeleteModel(
            name='Masterfaktorexternal',
        ),
        migrations.DeleteModel(
            name='Masterfaktorintenal',
        ),
        migrations.DeleteModel(
            name='Masterfungsi',
        ),
        migrations.DeleteModel(
            name='Masterkategoririsiko',
        ),
        migrations.DeleteModel(
            name='Masterkreteriadampak',
        ),
        migrations.DeleteModel(
            name='Masterkriteriakemungkinan',
        ),
        migrations.DeleteModel(
            name='Masterrisiko',
        ),
        migrations.DeleteModel(
            name='Mastertiperisiko',
        ),
        migrations.AlterField(
            model_name='daftarsasaran',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='daftarsasaran',
            name='indikatorkinerja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.masterindikatorkinerja'),
        ),
        migrations.AlterField(
            model_name='daftarsasaran',
            name='penanggungjawab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.masterpimpinanunitkerja'),
        ),
        migrations.AlterField(
            model_name='daftarsasaran',
            name='perspektifbsc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.masterperspektifbsc'),
        ),
        migrations.AlterField(
            model_name='daftarsasaran',
            name='unitkerja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.masterunitusaha'),
        ),
        migrations.DeleteModel(
            name='Masterindikatorkinerja',
        ),
        migrations.DeleteModel(
            name='Masterperspektifbsc',
        ),
        migrations.DeleteModel(
            name='Masterpimpinanunitkerja',
        ),
        migrations.DeleteModel(
            name='Masterunitusaha',
        ),
    ]