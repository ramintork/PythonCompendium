import approvaltests
import pytest

from model_objects import SpecialOfferType
from receipt_printer import ReceiptPrinter


def test_no_discount(teller, cart, toothbrush, apples):
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_ten_percent_discount(teller, cart, toothbrush):
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)
    cart.add_item_quantity(toothbrush, 2)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))


def test_three_for_two_discount(teller, cart, toothbrush):
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, toothbrush, 10.0)
    cart.add_item_quantity(toothbrush, 3)

    receipt = teller.checks_out_articles_from(cart)

    approvaltests.verify(ReceiptPrinter().print_receipt(receipt))
