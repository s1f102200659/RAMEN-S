from django.db import models

# usersテーブルのモデル
class User(models.Model):
    ID = models.AutoField(primary_key=True)  # プライマリーキーとしてIDを追加
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    balance = models.FloatField()
    image_filename = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# 請求テーブルのモデル
class Invoice(models.Model):
    ID = models.AutoField(primary_key=True)  # プライマリーキーとしてIDを追加
    user_id = models.IntegerField()  # ユーザーIDの追加（ForeignKeyではなく単純な整数型）
    amount = models.FloatField()
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.ID} - {self.amount}-{self.created_at}"

# paymentテーブルのモデル
class Payment(models.Model):
    ID = models.AutoField(primary_key=True)  # プライマリーキーとしてIDを追加
    Invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Invoice_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.ID} for Invoice {self.Invoice_id.ID}"
