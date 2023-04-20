from apps.mailer.process import MailerProcess
from apps.common.querysets.order_queryset import OrderQuerySet
from apps.common.querysets.user_queryset import UserQuerySet
from config import Session


def send_email(*recipients, **settings):
    try:
        p = MailerProcess(*recipients, **settings)
        p.run()
    except Exception as e:
        print(e)
    else:
        print('Report sent successfully')


def send_orders_report():
    subject = 'Report of orders of today'

    with Session() as db:
        order_qs = OrderQuerySet(db)
        user_qs = UserQuerySet(db)

        orders = order_qs.get()
        users = user_qs.where(user_qs.model.is_admin == True).all()

    if orders:
        body = "Report of new orders made:\n" \
            f"Number of orders: {len(orders)}"
    else:
        body = "There are not new orders made today"

    recipients = [
        u.email
        for u in users
    ]

    send_email(*recipients, subject=subject, body=body)
