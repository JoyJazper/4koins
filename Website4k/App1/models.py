from django.db import models

class Users(models.Model):
    userID = models.IntegerField()
    userName = models.CharField(max_length=100)
    userAddress = models.CharField(max_length=500)
    userPhone = models.IntegerField()
    userPinCode = models.IntegerField()

    def __str__(self):
        return self.userName

class Stores(models.Model):
    storeID = models.IntegerField()
    storeName = models.CharField(max_length=250)
    storeDescription = models.CharField(max_length=500)
    storeAddress = models.CharField(max_length=500)
    storeCatagory = models.CharField(max_length=100)

    def __str__(self):
        return self.storeName

class Products(models.Model):
    store = models.ForeignKey(Stores,on_delete=models.CASCADE)
    productID = models.IntegerField()
    productName = models.CharField(max_length=250)
    productDescription = models.CharField(max_length=500)
    productPrize = models.FloatField()
    productQuantity = models.CharField(max_length=250)

    def __str__(self):
        return self.productName

class OrdersList(models.Model):
    storeID = models.ForeignKey(Stores,on_delete=models.DO_NOTHING)
    userID = models.ForeignKey(Users,on_delete=models.CASCADE)
    orderID = models.IntegerField()
    orderAmount = models.FloatField()
    status = models.CharField(max_length=250)

    #def __str__(self):
    #    return self.userID.userName + ' - ' + self.storeID.storeName

class OrderData(models.Model):
    orderDataID = models.ForeignKey(OrdersList,on_delete=models.CASCADE)
    orderedProduct = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    orderedQuantity = models.IntegerField()
