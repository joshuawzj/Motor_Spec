# Generated by Django 2.1.1 on 2018-09-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=10)),
                ('customerName', models.CharField(max_length=50)),
                ('customerPhone', models.CharField(max_length=50)),
                ('customerAddress', models.CharField(max_length=75)),
                ('customerDOB', models.CharField(max_length=15)),
                ('customerGender', models.CharField(max_length=10)),
                ('customerOccupation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RentalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.CharField(max_length=5)),
                ('storeName', models.CharField(max_length=100)),
                ('orderID', models.CharField(max_length=10)),
                ('orderCreationDate', models.CharField(max_length=25)),
                ('orderPickupOrReturn', models.CharField(max_length=10)),
                ('orderPickupOrReturnDate', models.CharField(max_length=250)),
                ('customerID', models.CharField(max_length=10)),
                ('customerName', models.CharField(max_length=50)),
                ('carID', models.CharField(max_length=10)),
                ('carMakeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RentalTrends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mostPopularVehicle', models.CharField(max_length=50)),
                ('mostPopularType', models.CharField(max_length=50)),
                ('mostPopularMonth', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StoreTrends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeID', models.CharField(max_length=250)),
                ('storeProductivity', models.CharField(max_length=50)),
                ('mostProductiveMonth', models.CharField(max_length=50)),
                ('mostRentedVehicle', models.CharField(max_length=50)),
                ('mostPickupOrReturn', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carID', models.CharField(max_length=10)),
                ('carMakeName', models.CharField(max_length=50)),
                ('carModel', models.CharField(max_length=50)),
                ('carSeries', models.CharField(max_length=50)),
                ('carSeriesYear', models.CharField(max_length=10)),
                ('carPriceNew', models.CharField(max_length=15)),
                ('carEngineSize', models.CharField(max_length=10)),
                ('carFuelSystem', models.CharField(max_length=50)),
                ('carTankCapacity', models.CharField(max_length=10)),
                ('carPower', models.CharField(max_length=10)),
                ('carSeatingCapacity', models.CharField(max_length=5)),
                ('carStandardTransmission', models.CharField(max_length=10)),
                ('carBodyType', models.CharField(max_length=50)),
                ('carDrive', models.CharField(max_length=10)),
                ('carWheelbase', models.CharField(max_length=10)),
            ],
        ),
    ]
