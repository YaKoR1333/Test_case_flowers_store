from django.shortcuts import render
from django.db.models import Sum

from .models import TradeBook


def get_sellers_info(request):
    trade_book_set = TradeBook.objects.all()
    sellers_data = []
    sellers_list = []
    sellers = list(
        map(lambda seller: sellers_list.append(seller['seller__user__username']),  # выборка имён всех продавцов
            list(trade_book_set.values('seller__user__username').distinct())))
    for s in sellers_list:
        buyer_list = []
        buyers = list(map(lambda seller: buyer_list.append(seller['buyer__user__username']),
                          list(trade_book_set.values('buyer__user__username').  # Выборка имён всех покупателей которые
                               # делали покупки у определённого продавца
                               filter(seller__user__username=s).distinct())))
        sellers_sum_lot = (trade_book_set.filter(status__title='Закрыт', seller__user__username=s).
                           aggregate(Sum('purchase_sum')))['purchase_sum__sum']  # Сумма покупок
        # совершённых у данного продавца, status__title нужен для того чтобы выбрать уже закртытые
        # сделки, а не те которые находятся в промежуточном состоянии при желании можно удалить данный фильтр.
        sellers_data += [[s, buyer_list, sellers_sum_lot], ]  # собираем все данные в отдельный список
    data = {'sellers': sellers_data}
    return render(request, 'base.html', context=data)
