# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8;
__author__ = 'iswing'
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import urllib2
Fristname='王李张刘' \
          '陈杨黄赵吴周徐孙马朱胡郭何高林罗' \
          '郑梁谢宋唐许韩冯邓曹彭曾肖田董袁潘于蒋蔡' \
          '余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金' \
          '石廖贾夏韦傅方白邹孟熊秦邱江尹薛闫段雷侯' \
          '龙史陶黎贺顾毛郝龚邵万钱严覃武戴莫孔向汤' \
          '庞樊兰殷施陶洪翟安颜倪严牛温芦季俞章鲁葛　' \
          '伍韦申尤毕聂柴焦向柳邢路岳齐沿梅莫庄辛管　' \
          '祝左涂谷祁时舒耿牟卜路詹关苗凌费纪靳盛童　' \
          '欧甄项曲成游阳裴席卫查屈鲍位覃霍翁隋植甘　' \
          '景薄单包司柏宁柯阮桂闵欧阳解强丛华车冉房边　' \
          '辜吉饶刁瞿戚丘古米池滕晋苑邬臧畅宫来嵺苟　' \
          '全褚廉简娄盖符奚木穆党燕郎邸冀谈姬屠连郜　' \
          '晏栾郁商蒙计喻揭窦迟宇敖糜鄢冷卓花仇艾蓝　' \
          '都巩稽井练仲乐虞卞封竺冼原官衣楚佟栗匡宗　' \
          '应台巫鞠僧桑荆谌银扬明沙薄伏岑习胥保和蔺'

def fenci(text2):
    # try:
    #
    #     conn=MySQLdb.connect(host='221.236.172.241',user='vevent',passwd='DFG^&*()sdhf@#nhD',db='vevent',port=3306)
        #
        # cur=conn.cursor()
        #
        # cur.execute('select * from content order by id desc limit 0, 10')
        #
        # cur.close()
        #
        # conn.close()

    # except MySQLdb.Error,e:
    #
    #  print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    # text2="<p><st<p><strong>嘉宾介绍：</strong></p><p>汤敏：国务院参事、友成基金会副理事长、秘书长</p><p>教育部相关司局领导</p><p>教育部教育管理信息中心相关领导</p><p>赵沁平：教育部教育信息化专家组组长、中国科学院院士</p><p>袁亚湘：中国科学院院士</p><p>周向宇：中国科学院院士</p><p>王珠珠：中央电教馆馆长</p><p>山红红：中国石油大学（华东）校长</p><p>李志民：教育部科技发展中心主任</p><p>陆昉：复旦大学副校长</p><p>黄震：上海交通大学副校长</p><p>周一：中国教育信息化杂志社社长</p><p>严继昌：全国高等学校现代远程教育协作组秘书长</p><p>刘雍潜：中国教育技术协会秘书长</p><p>祝智庭：教育部教育技术标准委员会主任、华东师范大学开放教育学院院长</p><p>王天虎：中国石油大学（华东）教育发展中心主任</p><p>焦建利：华南师范大学教育信息学院副院长</p><p>李晓明：北京大学校长助理</p><p>程建刚：清华大学教育研究所所长</p><p>钟晓流：清华大学教育技术中心副主任</p><p>余建波：上海交通大学教务处处长</p><p>黄云清：湘潭大学校长</p><p>郭文革：北京大学教授</p><p>赵炳新：山东大学网络教育学院院长</p><p>魏民：全国职业院校教育信息化教育指导委员会</p><p>黎加厚：上海师范大学教授</p><p>唐锦兰：北京外国语大学网络教育学院院长</p><p>张国安：华中科技大学远程与继续教育学院院长</p><p>吕国斌：中国地质大学（武汉）远程教育学院院长</p><p>王立：东北农业大学网络教育学院院长</p><p>高澍萍：北京大学医学院网络教育学院院长</p><p>张伟春：广州天河区教育局副巡视员</p><p>胡铁生：佛山教育局、微课创始人</p><p>唐晓勇：深圳南方科技大学实验学校副校长</p><p>陈向东：跟谁学创始人</p><p>伏彩瑞：21世纪教育研究院理事、沪江网创始人、CEO</p><p>刘坚：北京师范大学中国创新教育研究院院长</p><p>李玉顺：北京师范大学教授</p><p>赵保和：北京市电教馆教研室主任</p><p>胡晓勇：华南师范大学教授</p><p>刘名卓：华东师范大学副教授</p><p>张福涛：山东昌乐一中常务副校长</p><p>刘希娅：重庆市九龙坡区谢家湾小学校长</p><p>李炳亭：中国教师报总编辑助理</p><p>杨国斌：湖南永州教科院</p>"
    t=1
    count=0
    if int(len(text2)) >200:
            count=int(len(text2))/200

    else:
        count=1
    temp=[]
    while t<=count:

        text=text2[t*200-200:t*200]
        # print text

        url_get_base = "http://ltpapi.voicecloud.cn/analysis/?"
        api_key = 'R3q7F680SkhOmfpcjNClyAsArDao3uKeMWrS8CdF'

        format = 'json'
        pattern = 'all'
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
        content = result.read().strip()




        hjson = json.loads(str(content))

        # print content
        global arr,arr2
        arr=[0]*1
        arr2=[0]*1
        for x in hjson[0][0]:

               if x['pos']=='nh':

                   if (str(x['cont'][0]) in Fristname) and int(len(str(x['cont'])))==3:
                       arr[0]=str(x['cont'])
                       arr2[0]=int(x['id'])


                   if  int(len(str(x['cont'])))>3:

                       if int(x['id'])-1==int(arr2[0]):

                            str(arr[0])+str(x['cont'])
                            temp.append(str(arr[0])+str(x['cont']))
                       else:

                            temp.append(x['cont'])

        t+=1
    return temp


