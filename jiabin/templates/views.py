#! -*- coding:utf-8 -*-
from django.shortcuts import  RequestContext
from django.http import HttpResponse
from new_event.common import  Telcaptcha


from django.views.decorators.csrf import csrf_exempt
#加这个post提交不会403
from django.core.cache import cache
from admin_self.common import  NewformatEvent

from django.shortcuts import render_to_response

import json
from new_event.models import NewEventImg

import pagination
import datetime
import models


import hashlib
#md5=hashlib.md5(‘字符串’.encode(‘utf-8′)).hexdigest()

from django.core.files.base import ContentFile
from django.db.models import Q


#嘉宾邀请页面
def jiabin_guest_invitation(request,page):

    lstInfo = []
    ret = {}

    lstInfo.append(jiabin_info(int(page)))

    ret['data'] = lstInfo

    #cache.set('jiabin_data_%s' % page,ret,86400)
    return render_to_response('guest_info.html',ret,context_instance=RequestContext(request))

def Search_guest(request,page=1):
    keywords = request.GET.get('keyword','')
    new=request.GET.get('new',False)
    keywords_md5=hashlib.md5(keywords.encode('utf-8')).hexdigest()
    ret = cache.get('jiabin_data_%s_%s' % (page,keywords_md5))
    if not ret or new:
        
        jiabin_value = models.jiabin_m.objects.filter(username__icontains=keywords,display=1)
        ret = {}
        lstInfo = []

        offset = 12
    
        try:
            ret = cache.get('jiabin_data_%s' % page)
        except:
            ret = None
    
        new = True
        if new or not ret:
            ret = {}
            lstJiabin = models.jiabin_m.objects.filter(username__icontains=keywords,display=1)
            #获取所有嘉宾信息
    
    
            totalpage = lstJiabin.count()/offset
            page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
            (curpage,offset) = page_obj.getCurpageOffset()
            start = (curpage-1)*offset
            end = curpage*offset
            (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()
    
            ret['firstPage'] = firstPage
            ret['lastPage'] = lastPage
            ret['prePage'] = prePage
            ret['nextPage'] = nextPage
            ret['pageList'] = pageList
    
    
            lstInfo = []
        for ji in jiabin_value[start:end]:
                mid_dct = jiabin_info(ji.id)

    
                mid_dct['guest_invitation_url'] ='/jiabin/guest_invitation/'+str(ji.id)+'/'
                lstInfo.append(mid_dct)
    
        ret['data'] = lstInfo
    
        cache.set('jiabin_data_%s_%s' % (page,keywords_md5),ret,86400)



    #return HttpResponse(json.dumps(ret),content_type='application/json')
    return render_to_response('search_guest.html',ret,context_instance=RequestContext(request))


# 嘉宾分类列表页
def cat_guest(request,page=1):
    offset = 24
    new = request.GET.get('new',False)


    list5=[]
    ret={}

    lstInfo = []
    lstInfo.append(cat_guests(None,1,u'推荐',new=new))

    list1=cat_guests(7,None,u'互联网IT',new=new)
    if list1:
        lstInfo.append(list1)
    list2=cat_guests(8,None,u'能源行业',new=new)
    if list2:
        lstInfo.append(list2)
    list3=cat_guests(9,None,u'医疗行业',new=new)
    if list3 :
        lstInfo.append(list3)
    list5.extend(cat_guests(None,10,u'学术',new=new))

    list6=cat_guests(13,None,u'金融财经',new=new)
    if list6:
        lstInfo.append(list6)
    list5.extend(cat_guests(14,None,u'零售',new=new))

    list5.extend(cat_guests(15,None,u'公共服务',new=new))

    list4=cat_guests(18,None,u'农业农林',new=new)
    if list4:
        lstInfo.append(list4)
    list5.extend(cat_guests(10000,None,u'商业',new=new))

    list5.extend(cat_guests(84,None,u'其他行业',new=new))
    if list5:
        lstInfo.append(list5)

    ret['data'] = lstInfo

    return render_to_response('guest_cat.html',ret,context_instance=RequestContext(request))
#-------------------------------------------------------------------------
#嘉宾详情输出
def jiabin_info(jiabin_id,new=False):
    mid_dct=cache.get('jiabin_info_%s' % jiabin_id)
    if new or not mid_dct:
        ji=models.jiabin_m.objects.get(pk=jiabin_id)
        mid_dct = {}
        dang=[]
        mid_dct['cat_name'] = ji.cat
        mid_dct['jiabin_name'] = ji.username
        mid_dct['jiabin_intro'] = ji.introduce
        mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
        mid_dct['jiabin_company'] = ji.company
        mid_dct['jiabin_position'] = ji.position
        mid_dct['user_id'] = ji.id
        mid_dct['title'] = []
        for ev in ji.jiabin_id.all():
            try:
                mid_dct['title'].append(NewformatEvent(ev))
            except:
                pass
        
        
        mid_dct['picurl'] = ji.picurl
        mid_dct['jiabin_more'] ='/jiabin/jiabin_cat_list_index/'+str(ji.cat)+'/'+str(1)+'/'
        try:
        
        
            if ji.jiabin_id[0].begin_time>datetime.datetime.now():
                    mid_dct['time_now']=u'有档期'
            elif ji.jiabin_id[0].begin_time>datetime.datetime.now() and ji.jiabin_id[0].end_time<ji.jiabin_id[0].begin_time:
                    mid_dct['time_now']=u'正在演讲'
            elif ji.jiabin_id[0].begin_time>datetime.datetime.now() and ji.jiabin_id[0].begin_time<datetime.date.today()+datetime.timedelta(-7):
                    mid_dct['time_now']=u'即将演讲'
        
            else:
                mid_dct['time_now']=u'无档期'
            if mid_dct['time_now']==u'有档期':
                dang.append(u'有档期')
            elif mid_dct['time_now']==u'正在演讲':
                dang.append(u'正在演讲')
            elif mid_dct['time_now']==u'即将演讲':
                dang.append(u'即将演讲')
            elif mid_dct['time_now']==u'无档期':
                dang.append(u'无档期')
        
        
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None
        except:
            pass
        if u'有档期' in dang:
            mid_dct['time_now']=u'有档期'
        elif '有档期' not in   dang and u'无档期' in dang:
            mid_dct['time_now']=u'无档期'
        mid_dct['guest_invitation_url'] ='/jiabin/guest_invitation/'+str(ji.id)+'/'
        
        cache.set('jiabin_info_%s' % jiabin_id,mid_dct,3600*30)
    return mid_dct
#嘉宾分类列表输出
def cat_guests(cat=None,recom=0,tuijian=None,end=9,begin=0,new=False):
    
    cat_list=cache.get('jiabin_cat_guests_%s_%s_%s' % (cat,recom,tuijian))
    
    if new or not cat_list:
        
        
        if cat is None:
            lstJiabin = models.jiabin_m.objects.filter(recommend=recom,display=1)
        else:
            lstJiabin = models.jiabin_m.objects.filter(cat=cat,display=1)
     
    
        cat_list=[]
        
        for ji in lstJiabin:
            cat_list.append(ji.id)
        cache.set('jiabin_cat_guests_%s_%s_%s' % (cat,recom,tuijian),cat_list,3600*30)
    
    
    if not end:
        return cat_list
     
    list1=[]

    for ji in cat_list[begin:end]:
        info=jiabin_info(ji,new)
        info['cat_name']=tuijian
        list1.append(info)
         
    
    
    return list1
    
    
    


#发送邀请函 apache
@csrf_exempt
@Telcaptcha
def send_guest_invitation(request):

    company=request.POST.get('company')
    meeting=request.POST.get('meeting')
    id=request.POST.get('id')
    name=request.POST.get('name')
    mobilphone=request.POST.get('mobilphone')
    message=request.POST.get('message')
    guestName=request.POST.get('guestName')

    models.send_guest_invitation.objects.create(

        in_company=company,
        in_meeting=meeting,
        event_id=id,
        in_name=name,
        in_mobilphone=mobilphone,
        in_guest=guestName,
        in_message=message
        )

    return HttpResponse(json.dumps({'success':1}),content_type='text/html')





def apply_guest(request):

    ret={}
    lstInfo=[0]*6
    mid_dct={}
    mid_dct2={}
    mid_dct3={}
    mid_dct4={}
    mid_dct5={}
    mid_dct6={}
    mid_dct['cat_name']=u'互联网IT'
    mid_dct['cat_value']='7'
    lstInfo[0]=mid_dct
    mid_dct2['cat_name']=u'能源行业'
    mid_dct2['cat_value']='8'
    lstInfo[1]=mid_dct2
    mid_dct3['cat_name']=u'医疗行业'
    mid_dct3['cat_value']='9'
    lstInfo[2]=mid_dct3
    mid_dct4['cat_name']=u'金融财经'
    mid_dct4['cat_value']='13'
    lstInfo[3]=mid_dct4
    mid_dct5['cat_name']=u'农业农林'
    mid_dct5['cat_value']='18'
    lstInfo[4]=mid_dct5
    mid_dct6['cat_name']=u'其它行业'
    mid_dct6['cat_value']='84'
    lstInfo[5]=mid_dct6

    ret['data'] = lstInfo
    return render_to_response('guest_regist.html',ret,context_instance=RequestContext(request))



#嘉宾注册 ajax apache

@csrf_exempt
@Telcaptcha
def apply_guest_send(request):
    p={}
    p['flag']=False
    # da=request.POST.get('data')
    name=request.POST.get('name')
    mobilphone =request.POST.get('mobilphone ')
    industry=request.POST.get('industry')
    resume=request.POST.get('resume')
    file_content = ContentFile(request.FILES['imgView'].read())


    m = NewEventImg.objects.create(name=name)
    m.imgs.save(request.FILES['imgView'].name, file_content)
    p['id']=m.id
    p['url']='%s%s' % (m.server.name, m.urls)
    p['flag']=True
    p['name']=name




    models.jiabin_m.objects.create(
        username=name,
        tel=mobilphone,
        cat=industry,
        introduce=resume,
        picurl=p['url'],
        new_login=1,
    )

    return HttpResponse(json.dumps({'flag':'','success':1}),content_type='text/html')

def jiabin_cat_list_index(request,cat_n,page=1):
    offset = 12
    new = request.GET.get('new',False)

    ret = {}
    Jiabin_count=len(cat_guests(cat_n,recom=False,new=new))
    totalpage = Jiabin_count/offset
    page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
    (curpage,offset) = page_obj.getCurpageOffset()
    start = (curpage-1)*offset
    end = curpage*offset
    (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

    ret['firstPage'] = firstPage
    ret['lastPage'] = lastPage
    ret['prePage'] = prePage
    ret['nextPage'] = nextPage
    ret['pageList'] = pageList
    if cat_n==7:

        cat_name=u'互联网IT'
        ret['cat_name']=cat_name
    elif cat_n==8:

        cat_name=u'能源行业'
        ret['cat_name']=cat_name
    elif cat_n==9:

        cat_name=u'医疗行业'
        ret['cat_name']=cat_name
    elif cat_n==13:

        cat_name=u'金融财经'
        ret['cat_name']=cat_name
    elif cat_n==18:

        cat_name=u'农业农林'
        ret['cat_name']=cat_name
    elif cat_n==8340:

        cat_name=u'其它行业'
        ret['cat_name']=cat_name



    
    ret['data'] = cat_guests(cat_n,recom=False,tuijian=ret['cat_name'],begin=start,end=end,new=new)
    return HttpResponse(json.dumps({'data':ret['data'],'success':1}),content_type='application/json')
    return render_to_response('guest_list.html',ret,context_instance=RequestContext(request))
