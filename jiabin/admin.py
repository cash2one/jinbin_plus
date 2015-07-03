#! -*- coding:utf-8 -*-

from jiabin.models import jiabin_m,send_guest_invitation
#from new_event.models import NewEventTable
from admin_self.common import NewformatEvent
from django.contrib import admin


class jiabin_mAdmin(admin.ModelAdmin):


    search_fields =('id','username','cat_event_id')

    def id(self,obj):
        return obj.id

    id.short_description  = 'id'

    def username(self,obj):
        return obj.username

    username.short_description  = '名称'


    def introduce(self,obj):
        return obj.introduce

    introduce.short_description  = '简介'
    def baikeURL_s(self,obj):
        baike=obj.username
        return '<a href="http://baike.baidu.com/search/word?word=%s" target="_blank">%s</a>' % (baike, u'百度百科')
    baikeURL_s.short_description  = '百度百科'
    baikeURL_s.allow_tags = True

    def homeurl(self,obj):
        event=obj.cat_event_id
        return '<a href="http://www.huodongjia.com/event-%s.html" target="_blank">%s</a>' \
            % (event, event)
    homeurl.short_description  = '活动家'


    def cat_event_id_new(self,obj):
        try:
            ev=NewformatEvent(None,obj.cat_event_id)
            return '<a href="http://www.huodongjia.com/event-%s.html" target="_blank">%s</a>' % (obj.cat_event_id,ev['id'])

        except:
            return ''
        
    cat_event_id_new.short_description  = '活动id'
    cat_event_id_new.allow_tags = True

    def jiabin_id(self,obj):
        return obj.jiabin_id
    jiabin_id.short_description  = '活动关联id'


    def cat(self,obj):
        return obj.cat
    cat.short_description  = '类别'

    def title(self,obj):
        return obj.title
    title.short_description  = '活动名称'

    def begin_time(self,obj):
        return obj.create_time
    begin_time.short_description  = '创建时间'

    def end_time(self,obj):
        return obj.rel_time
    end_time.short_description  = '最后编辑时间'

    def recommend(self,obj):
        return obj.imgs
    recommend.short_description  = '是否推荐'

    def company(self,obj):
        return obj.company
    company.short_description  = '公司'

    def position(self,obj):
        return obj.position
    position.short_description  = '职位'


    raw_id_fields = ['jiabin_id']

    list_display=('id','username','company','position','introduce','baikeURL_s','cat_event_id_new','cat','title','begin_time','end_time','recommend')

admin.site.register(jiabin_m,jiabin_mAdmin)



class send_guest_invitation_admin(admin.ModelAdmin):
    list_display=('id','in_guest','in_company','in_meeting','event_id','in_name','in_mobilphone','in_message')
    search_fields =('id','in_company','in_meeting','event_id','in_name','in_mobilphone','in_message','in_guest')
    def in_guest(self,obj):
        return obj.in_guest
    in_guest.short_description  = 'in_guest'
    def id(self,obj):
        return obj.id
    id.short_description  = 'id'
    def in_company(self,obj):
        return obj.in_company
    in_company.short_description  = 'in_company'
    def in_meeting(self,obj):
        return obj.in_meeting
    in_meeting.short_description  = 'in_meeting'
    def event_id(self,obj):
        return obj.event_id
    event_id.short_description  = 'event_id'
    def in_name(self,obj):
        return obj.in_name
    in_name.short_description  = 'in_name'
    def in_mobilphone(self,obj):
        return obj.in_mobilphone
    in_mobilphone.short_description  = 'in_mobilphone'
    def in_message(self,obj):
        return obj.in_message
    in_message.short_description  = 'in_message'

    # raw_id_fields = ['event_id']


admin.site.register(send_guest_invitation,send_guest_invitation_admin)
#admin.site.register(NewEventTable)
