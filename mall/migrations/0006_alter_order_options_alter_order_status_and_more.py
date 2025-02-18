# Generated by Django 5.1.2 on 2024-10-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mall", "0005_orderpayment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["-pk"],
                "verbose_name": "주문",
                "verbose_name_plural": "주문",
            },
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("requested", "주문요청"),
                    ("failed_payment", "결제실패"),
                    ("paid", "결제완료"),
                    ("prepared_product", "상품준비중"),
                    ("shipped", "배송중"),
                    ("delivered", "배송완료"),
                    ("cancelled", "주문취소"),
                ],
                db_index=True,
                default="requested",
                max_length=20,
                verbose_name="진행상태",
            ),
        ),
        migrations.AlterField(
            model_name="orderpayment",
            name="pay_status",
            field=models.CharField(
                choices=[
                    ("ready", "결제 준비"),
                    ("paid", "결제 완료"),
                    ("cancelled", "결제 취소"),
                    ("failed", "결제 실패"),
                ],
                default="ready",
                max_length=20,
                verbose_name="결제상태",
            ),
        ),
    ]
