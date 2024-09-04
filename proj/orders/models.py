from django.db import models
from django.contrib.auth import get_user_model
from django.views import generic as generic_views
from acc.models import CustomerProfile
# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="carts",
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name="Created Date",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="Created Date",
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self) -> str:
        return f"Cart #{self.pk} for {self.user}"

    @property
    def order_price(self):
        books = self.books.all()
        total_order_price = 0
        for book in books:
            total_order_price += book.price
        return total_order_price


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name="Cart",
        related_name="books"
    )
    book = models.ForeignKey(
        "goods.Book",
        on_delete=models.PROTECT,
        verbose_name="Book",
        related_name="book_in_cart"
    )
    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=1
    )
    price_per_book = models.DecimalField(
        verbose_name="Price per Book",
        max_digits=5,
        decimal_places=2
    )

    @property
    def price(self):
        return self.quantity * self.price_per_book

    def __str__(self) -> str:
        return f"Book{self.book.pk} in cart#{self.cart.pk}, quantity{self.quantity}"


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT, related_name="cart")
    tel = models.ForeignKey(CustomerProfile, on_delete=models.PROTECT, related_name="telephone")


    def __str__(self) -> str:
        return f" Order #{self.pk}"




