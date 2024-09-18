from django.contrib import admin
from .models import User, Invoice, Payment  # モデルをインポート

# モデルを管理画面に登録
admin.site.register(User)
admin.site.register(Invoice)
admin.site.register(Payment)
