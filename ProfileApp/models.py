from django.db import models
import datetime
class GoodsCategory(models.Model):
    id = models.CharField(max_length=10,primary_key=True,default="")
    gc_name = models.CharField(max_length=50,default="")
    desc = models.TextField(max_length=300,default="")
    def __str__(self):
        return self.id + " : " + self.gc_name + " : " + self.desc

class Goodds(models.Model):
    goodsCategory = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,default=None)
    gid = models.CharField(max_length=10,primary_key=True,default="")
    name = models.CharField(max_length=50,default="")
    brand = models.CharField(max_length=50,default="")
    Model = models.CharField(max_length=50,default="")
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.goodsCategory.id) + " : " + str(self.goodsCategory.gc_name) + " : " +  self.gid + " : " + self.name + " : " + self.brand

class Customer(models.Model):
    cid = models.CharField(max_length=10,primary_key=True,default="")
    name = models.CharField(max_length=50,default="")
    surname = models.CharField(max_length=20,default="")
    address = models.TextField(max_length=200,default="")
    telephone = models.CharField(max_length=10,default="")
    gender = models.CharField(max_length=5,default="")
    carreer = models.CharField(max_length=20,default="")
    password = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.cid + " : " + self.name + " : " + self.telephone
class Order(models.Model):
    oid = models.CharField(max_length=10,primary_key=True,default="")
    date = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)
    status = models.CharField(max_length=10,default="")
    def __str__(self):
        return self.oid + " : " + str(self.date) + " : " + str(self.customer.cid)+ " : " + str(self.customer.name) + " : " + self.status

class OrderDetail(models.Model):
    id = models.CharField(max_length=10,primary_key=True,default="")
    order = models.ForeignKey(Order,on_delete=models.CASCADE,default=None)
    goodds = models.ForeignKey(Goodds,on_delete=models.CASCADE,default=None)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.id + " : " + str(self.order.id)+ " : " + str(self.goodds.id)+ " : " + str(self.goodds.name)+ " : " + str(self.price)+ " : " + str(self.quantity)

class Productinit():
    def __init__(self,PID,Pname,price,brand,size,type,amount):
        self.__PID = PID
        self.__Pname = Pname
        self.__price = price
        self.__brand = brand
        self.__size = size
        self.__type = type
        self.__amount = amount
        self.__setTotal()
        self.__setvat()
        self.__setnet()
    def __setTotal(self):
        self.__total = self.__price * self.__amount
    def __setvat(self):
        self.__vat = self.__total * 0.07

    def __setnet(self):
        self.__net = self.__total + self.__vat

    def getPID(self):
        return self.__PID

    def getPname(self):
        return self.__Pname

    def getBrand(self):
        return self.__brand

    def getPrice(self):
        return self.__price
    def getSzie(self):
        return self.__size
    def getType(self):
        return self.__type
    def getAmount(self):
        return self.__amount
    def getTotal(self):
        return self.__total
    def getVat(self):
        return self.__vat
    def getNet(self):
        return self.__net

