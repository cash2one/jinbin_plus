#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals 



#from BeautifulSoup import BeautifulSoup SysSpotInfo
from django.db import models
from new_event.models import NewEventTable


class send_guest_invitation(models.Model):
    id =  models.AutoField(primary_key=True,max_length=11)
    in_company = models.CharField(u'公司名称',max_length=300,blank=True)
    in_meeting = models.CharField(u'会议名称',max_length=300,blank=True)
    event_id = models.CharField(u'嘉宾id',max_length=300,blank=True)
    in_name = models.CharField(u'联系人名称',max_length=300,blank=True)
    in_mobilphone = models.CharField(u'顾客电话',max_length=300,blank=True)
    in_message = models.CharField(u'说明',max_length=300,blank=True)
    in_guest = models.CharField(u'嘉宾名称',max_length=300,blank=True)
    class Meta:
        verbose_name = u'邀请信息管理'
        verbose_name_plural = u'邀请信息管理'
        managed = False
        db_table='send_guest_invitation'



class jiabin_m(models.Model):
    st=( (7,u'IT行业会议'),
          (8,u'能源化工会议'),
          (9,u'医疗行业会议'),
          (13,u'金融财经会议'),
          (18,u'农业林业会议'),
          (84,u'其他行业'),

          )
    ct=(

        (1,u'推荐'),
        (0,u'不推荐')

      )
    qt=(

        (1,u'发布'),
        (0,u'不发布')

      )
    id =  models.AutoField(primary_key=True,max_length=11)
    imgs = models.ImageField(u'图片文件',upload_to = 'temp',blank=True,null=True)
    username = models.CharField(u'嘉宾名称',max_length=300,blank=True,null=True)
    introduce = models.TextField(u'嘉宾简介',blank=True,null=True)
    homeurl = models.CharField(u'活动家对应链接',max_length=300,blank=True,null=True,editable=False)
    baikeURL = models.CharField(u'百科对应链接',max_length=300,blank=True,null=True,editable=False)
    cat_event_id = models.IntegerField(u'活动id',blank=True,max_length=11 ,null=True)
    jiabin_id=models.ManyToManyField(NewEventTable,blank=True,null=True,verbose_name='关联活动')
    # jiabin_id3=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动3')
    # jiabin_id4=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动4')
    # jiabin_id5=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动5')
    # jiabin_id6=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动6')
    # jiabin_id7=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动7')
    # jiabin_id8=models.ForeignKey(NewEventTable,to_field='old_event_id',blank=True,null=True,verbose_name='关联活动8')
    cat= models.IntegerField(u'类别',blank=True,max_length=11,choices=st,default=1 ,null=True)
    title  = models.CharField(u'活动标题',max_length=300,blank=True,null=True)
    create_time =models.DateTimeField(u'活动开始时间',blank=True,null=True,editable=False)
    rel_time = models.DateTimeField(u'活动结束时间',blank=True,null=True,editable=False)
    recommend= models.IntegerField(u'是否推荐(1推荐)',blank=True,max_length=11,choices=ct,default=0,null=True)
    company  = models.CharField(u'公司名称',max_length=300,blank=True,null=True)
    position  = models.CharField(u'所属职位',max_length=300,blank=True,null=True)
    picurl  = models.CharField(u'图片(不填，自动的)',max_length=300,blank=True,null=True,editable=False)
    display= models.IntegerField(u'是否发布',blank=True,max_length=11,choices=qt,default=0,null=True)
    new_login= models.IntegerField(u'新注册',blank=True,max_length=11,null=True)
    tel = models.CharField(u'电话号码',max_length=50,blank=True,null=True)
    def save(self,force_insert=False, force_update=False, using=None,
             update_fields=None):
        #try:
        super(jiabin_m, self).save(force_insert , force_update , using ,
             update_fields )


        if self.imgs:
            import ftplib,time,os
            server1='pic1.qkan.com'
            uid='imga'
            pwd='b@Veryevent'
            s = ftplib.FTP(server1,uid,pwd)
            spot='event'
            try:
                s.cwd(spot)
            except ftplib.error_perm:
                s.mkd(spot)
            #except:
            curTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            try:
                s.cwd(curTime)
            except ftplib.error_perm:
                s.mkd(curTime)
                try:
                    s.cwd(curTime)
                except:
                    pass
            f = open(self.imgs.path,'rb')
            #filename=    os.path.basename(self.imgs.path)         # file to send
            #img_name=self.img_url+"\\"+g.decode('utf-8').replace('/','\\').replace('%20',' ')
            from PIL import Image
            pixbuf = Image.open(self.imgs.path)
            self.width, self.height = pixbuf.size
            
            base, ext = os.path.splitext(os.path.basename(self.imgs.path))
            filename=spot+str(time.time())+ext
            s.storbinary('STOR '+filename, f)   # Send the file
            f.close()                          # Close file and FTP
            s.quit()
            self.picurl='http://pic.huodongjia.com/'+'%s/%s/%s' % (spot,curTime,filename) #os.path.join( spot+'/'+curTime,filename)
            # self.server=NewEventImgServer.objects.get(id=1)
            super(jiabin_m, self).save(force_insert , force_update , using ,update_fields )

    class Meta:
        verbose_name = u'嘉宾信息管理'
        verbose_name_plural = u'嘉宾信息管理'
        managed = False
        db_table='jiabin_info'

