__author__ = 'iswing'
import django.dispatch
from django.dispatch import Signal

from jiabin.models import  jiabin_m,jiabin_wait
from django.db.models.signals import post_save
def test(**kwargs):
    jiabin_m = kwargs["instance"]
    jiabin_wait.objects.create(
            id=jiabin_m.id,
            username=jiabin_m.username,
            introduce=jiabin_m.introduce,
            homeurl=jiabin_m.homeurl,
            baikeURL=jiabin_m.baikeURL,
            cat_event_id=jiabin_m.cat_event_id,

    )



post_save.connect(test, sender=jiabin_m)
# save_done = django.dispatch.Signal(providing_args=['obj'])
