# Generated by Django 4.1.7 on 2023-03-03 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mall", "0003_alter_product_options_cartproduct_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("total_amount", models.PositiveIntegerField(verbose_name="결제금액")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("requested", "주문요청"),
                            ("failed_payment", "결제실패"),
                            ("paid", "결제완료"),
                            ("prepared_product", "상품준비중"),
                            ("shipped", "배송중"),
                            ("delivered", "배송완료"),
                            ("canceled", "주문취소"),
                        ],
                        db_index=True,
                        default="requested",
                        max_length=20,
                        verbose_name="진행상태",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderedProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="주문 시점의 상품명을 저장합니다.",
                        max_length=100,
                        verbose_name="상품명",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="주문 시점의 상품가격을 저장합니다.", verbose_name="상품가격"
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="수량")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mall.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mall.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="product_set",
            field=models.ManyToManyField(
                through="mall.OrderedProduct", to="mall.product"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
