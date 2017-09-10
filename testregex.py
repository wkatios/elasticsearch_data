#coding=utf-8
import re

a=u'fwlog: 日志类型:服务控制或应用控制, 用户:(null), 源IP:0.0.0.0, 源端口:0, 目的IP:224.0.0.1, 目的端口:0, 应用类型:(null), 应用名称:(null), 系统动作:被记录'
pattern =ur'[\u4e00-\u9fa5]{4}:([^,]+),\s+[\u4e00-\u9fa5]{2}:(.*),\s+[\u4e00-\u9fa5]IP:([\d+\.?]+),\s+' \
         ur'[\u4e00-\u9fa5]{3}:(\d+),\s+[\u4e00-\u9fa5]{2}IP:([\d+\.?]+),\s+[\u4e00-\u9fa5]{4}:(\d+),\s+' \
         ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*)\s*'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(5),
    'dport':msg.group(6),
    'srcip':msg.group(3),
    'sport':msg.group(4),
    'action': u'日志类型:%s;用户:%s;应用类型:%s;应用名称:%s;系统动作:%s'%(msg.group(1),msg.group(2),msg.group(7),msg.group(8),msg.group(9))
}


a=u'fwlog: 日志类型:WAF应用防护日志, 源IP:142.54.171.66, 源端口:62436, 目的IP:10.1.1.29, 目的端口:80, 攻击类型:WEBSHELL, 严重级别:高, 系统动作:被记录, URL:218.78.240.29/'
# a=u"fwlog: 日志类型:WAF应用防护日志, 源IP:91.247.38.57, 源端口:53464, 目的IP:10.1.1.35, 目的端口:80, 攻击类型:SQL 注入, 严重级别:高, 系统动作:被记录, URL:﻿218.78.241.67/HttpCombiner.ashx?s=indexCss&t=text/css&v=0101&LsRk=9286 AND 1=1 UNION ALL SELECT 1,NULL,'<script>alert()</script>',table_name FROM information_schema.tables WHERE 2>1--/**/; EXEC xp_cmdshell('cat ../../../etc/passwd')#"
pattern = ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]IP:([\d+\.?]+),\s[\u4e00-\u9fa5]{3}:(\d+),\s+' \
          ur'[\u4e00-\u9fa5]{2}IP:([\d+\.?]+),\s+[\u4e00-\u9fa5]{4}:(\d+),\s+[\u4e00-\u9fa5]{4}:(.*),\s+' \
          ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*),\s+.'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(4),
    'dport':msg.group(5),
    'srcip':msg.group(2),
    'sport':msg.group(3),
    'action': u'日志类型:%s;攻击类型:%s;严重等级:%s;动作:%s'%(msg.group(1),msg.group(6),msg.group(7),msg.group(8))
}


a=u'fwlog: 日志类型:IPS防护日志, 源IP:113.223.98.195, 源端口:55621, 目的IP:10.1.1.73, 目的端口:80, 协议:tcp, 攻击类型:web漏洞攻击, 漏洞名称:Apache Struts 远程代码执行漏洞, 严重等级:高, 动作:拒绝'
pattern = ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]IP:([\d+\.?]+),\s[\u4e00-\u9fa5]{3}:(\d+),\s+' \
          ur'[\u4e00-\u9fa5]{2}IP:([\d+\.?]+),\s+[\u4e00-\u9fa5]{4}:(\d+),\s+[\u4e00-\u9fa5]{2}:(\w+),\s+' \
          ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{2}:(.*)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(4),
    'dport':msg.group(5),
    'srcip':msg.group(2),
    'sport':msg.group(3),'action': u'日志类型:%s;协议:%s;攻击类型:%s;漏洞名称:%s;严重等级:%s;动作:%s'%(msg.group(1),msg.group(6),msg.group(7),msg.group(8),msg.group(9), msg.group(10))
}


a=u'fwlog: 日志类型:DOS攻击日志, 源IP:192.168.254.25, 目的IP:10.1.7.50, 攻击方向:外网, 攻击类型:UDP洪水攻击, 严重等级:高, 系统动作:被记录'
pattern = ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]IP:([\d+\.?]+),\s' \
          ur'[\u4e00-\u9fa5]{2}IP:([\d+\.?]+),\s+[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*),\s+' \
          ur'[\u4e00-\u9fa5]{4}:(.*),\s+[\u4e00-\u9fa5]{4}:(.*)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(3),
    'dport':'',
    'srcip':msg.group(2),
    'sport':'',
    'action': u'日志类型:%s;攻击方向:%s;攻击类型:%s;严重等级:%s;系统动作:%s'%(msg.group(1),msg.group(4),msg.group(5),msg.group(6),msg.group(7))
}


a=u'2017-7-5 5:55:36#WAFSPLIT#91.196.50.33#WAFSPLIT#45734#WAFSPLIT#10.1.1.41#WAFSPLIT#80#WAFSPLIT#IIS信息泄漏 v2#WAFSPLIT#信息泄露#WAFSPLIT#低#WAFSPLIT#黑客通过恶意构造提交数据等方法，使得IIS服务出错。错误内容中可能包含服务器中的一些敏感信息，从而被黑客获取以便进一步的利用。#WAFSPLIT#关闭此服务的出错显示功能，即使出错也不返回敏感信息。#WAFSPLIT#拦截#WAFSPLIT#Response#WAFSPLIT#http://testp3.pospr.waw.plhttp://testp3.pospr.waw.pl/testproxy.php'
a=u'2017-7-5 5:55:36#WAFSPLIT#91.196.50.33#WAFSPLIT#45734#WAFSPLIT#10.1.1.41#WAFSPLIT#80#WAFSPLIT#IIS信息泄漏 v2#WAFSPLIT#信息泄露#WAFSPLIT#低#WAFSPLIT#黑客通过恶意构造提交数据等方法，使得IIS服务出错。错误内容中可能包含服务器中的一些敏感信息，从而被黑客获取以便进一步的利用。#WAFSPLIT#关闭此服务的出错显示功能，即使出错也不返回敏感信息。#WAFSPLIT#拦截#WAFSPLIT#Response#WAFSPLIT#http://testp3.pospr.waw.plhttp://testp3.pospr.waw.pl/testproxy.php'
a=u'2017-7-5 5:40:47#WAFSPLIT#106.11.153.45#WAFSPLIT#44737#WAFSPLIT#10.1.1.77#WAFSPLIT#80#WAFSPLIT#IIS信息泄漏 v2#WAFSPLIT#信息泄露#WAFSPLIT#低#WAFSPLIT#黑客通过恶意构造提交数据等方法，使得IIS服务出错。错误内容中可能包含服务器中的一些敏感信息，从而被黑客获取以便进一步的利用。#WAFSPLIT#关闭此服务的出错显示功能，即使出错也不返回敏感信息。#WAFSPLIT#拦截#WAFSPLIT#Response#WAFSPLIT#http://218.78.241.83/wzpy/Admin/SchoolInfo.aspx?SID=63'
a=u'2017-8-16 1:58:47#WAFSPLIT#2402:1980:105:5fe0:4e20:84bd:dcf8:fc1c#WAFSPLIT#54246#WAFSPLIT#10.1.1.41#WAFSPLIT#80#WAFSPLIT#IIS信息泄漏 v2#WAFSPLIT#信息泄露#WAFSPLIT#低#WAFSPLIT#黑客通过恶意构造提交数据等方法，使得IIS服务出错。错误内容中可能包含服务器中的一些敏感信息，从而被黑客获取以便进一步的利用。#WAFSPLIT#关闭此服务的出错显示功能，即使出错也不返回敏感信息。#WAFSPLIT#拦截#WAFSPLIT#Response#WAFSPLIT#http://218.78.241.91/Content/EBookStore/BookDetail.css'
pattern=ur'WAFSPLIT#([\w+\.|:?]+)#WAFSPLIT#(\d+)#WAFSPLIT#([\d+\.?]+)#WAFSPLIT#(\d+)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#' \
        ur'WAFSPLIT#(.*)#WAFSPLIT#(.*?)。.*WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#([a-zA-z]+://[^\s]*)'
# pattern=ur'WAFSPLIT#([\w+:?]+)#' \
#         ur'WAFSPLIT#(\d+)#WAFSPLIT#([\d+\.?]+)#WAFSPLIT#(\d+)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#(.*?)。.*WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#WAFSPLIT#([a-zA-z]+://[^\s]*)'


msg = re.search(pattern, a)
print msg.groups()
info ={
    'dstip':msg.group(3),
    'dport':msg.group(4),
    'srcip':msg.group(1),
    'sport':msg.group(2),
    'action': u'%s %s %s'%(msg.group(5), msg.group(7), msg.group(8))
}
{'dstip':msg.group(3),'dport':msg.group(4),'srcip':msg.group(1),'sport':msg.group(2),'action': u'%s %s %s'%(msg.group(5), msg.group(7), msg.group(8))}
print info

a=u'2017-7-5 6:53:29#WAFSPLIT#10.1.10.103#WAFSPLIT#8080#WAFSPLIT#218.78.245.250#WAFSPLIT#80#WAFSPLIT#可疑的文件包含#WAFSPLIT#信息泄露#WAFSPLIT#低#WAFSPLIT#攻击者企图包含远程文件'
pattern=ur'WAFSPLIT#([\d+\.?]+)#WAFSPLIT#(\d+)#WAFSPLIT#([\d+\.?]+)#WAFSPLIT#(\d+)#WAFSPLIT#(.*)#WAFSPLIT#(.*)#' \
        ur'WAFSPLIT#(.*)#WAFSPLIT#(.*)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(3),
    'dport':msg.group(4),
    'srcip':msg.group(1),
    'sport':msg.group(2),
    'action': u'%s %s %s'%(msg.group(5), msg.group(7), msg.group(8))
}

a='%%10SSHS/6/SSHS_LOG: -DevIP=10.255.249.234; Authentication failed for oracle from 202.201.255.200 port 55578 ssh2.'
pattern=r'DevIP=([\d+\.?]+);\s.*for\s(.*)\sfrom\s([\d+\.?]+)\sport\s(\d+)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':msg.group(4),
    'action': 'SSH Authentication failed for %s'%msg.group(2)
}


a='%%10SSHS/6/SSHS_DISCONNECT: -DevIP=10.255.249.234; SSH user root (IP: 202.201.255.200) disconnected from the server.'
pattern=r'SSHS_DISCONNECT:\s-DevIP=([\d+\.?]+).*user\s(.*)\s\(IP:\s([\d+\.?]+)\)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':'',
    'action': 'SSH user %s disconnected from the server'%msg.group(2)
}


a='%%10SSHS/6/SSHS_LOG: -DevIP=10.255.249.234; Connection closed by 120.31.37.10.'
pattern=r'SSHS_LOG:\s-DevIP=([\d+\.?]+);\s(.*)\sby\s([\d+\.?]+)\.'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':'',
    'action': msg.group(2)
}

a='%%10SSHS/6/SSHS_LOG: -DevIP=10.255.249.234; Disconnecting: Too many authentication failures for admin.'
pattern=r'-DevIP=([\d+\.?]+);\s(.*).'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': '%s'%msg.group(2)
}

a='%%10SSHS/6/SSHS_VERSION_MISMATCH: -DevIP=10.255.249.234; SSH client 181.196.165.113 failed to log in because of version mismatch.'
pattern=r'-DevIP=([\d+\.?]+);\s(.*)\s([\d+\.?]+)(.*).'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':msg.group(3),'sport':'','action': '%s%s'%(msg.group(2),msg.group(4))
}

a='%%10SSHS/6/SSHS_AUTH_EXCEED_RETRY_TIMES: -DevIP=10.255.249.234; SSH user admin (IP: 193.201.224.232) failed to log in, because the number of authentication attempts exceeded the upper limit.'
pattern=r'-DevIP=([\d+\.?]+);\s(.*)\s\(IP:\s([\d+\.?]+)\)(.*),(.*).'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':msg.group(3),'sport':'','action': '%s%s%s'%(msg.group(2),msg.group(4), msg.group(5))
}

a='%%10SSHS/6/SSHS_LOG: -DevIP=10.255.249.234; Disconnecting: Change of username or service not allowed: (netman,ssh-connection) -> (nobody,ssh-connection).  '
pattern=r'-DevIP=([\d+\.?]+);\s(.*):\s\('
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': '%s'%msg.group(2)
}

a='%%10SSH/6/SSH_CONNECTION_CLOSE(l): -DevIP=101.95.104.218; STEL user admin (IP: 212.232.34.175) logged out because the SSH client closed the connection.'
pattern=r'SSH_CONNECTION_CLOSE\(l\):\s-DevIP=([\d+\.?]+).*user\s+(.*)\s\(IP:\s([\d+\.?]+)\)\s(.*)\.'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':'','action':'SSH user %s logged out because the SSH client closed the connection' % msg.group(2)
}


a='%%10SHELL/5/SHELL_LOGINFAIL(l): -DevIP=101.95.104.218; SSH user admin2 failed to log in from 80.147.210.170 on VTY0..'
pattern=r'SHELL_LOGINFAIL\(l\):\s-DevIP=([\d+\.?]+);.*user\s(.*)\sfa.*from\s([\d+\.?]+)'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':'',
    'action':'SSH user %s failed to log in' % msg.group(2)
}


a='%%10LOGIN/6/LOGIN_FAILED: shell failed to log in from 178.251.111.194.'
pattern=r'([\d+\.?]+)\.'
msg = re.search(pattern, a)
info ={
    'dstip':'',
    'dport':'',
    'srcip':msg.group(1),
    'sport':'',
    'action': u'shell failed to log in'
}



a='%%10SC/6/SC_AAA_LAUNCH(l): -DevIP=101.95.104.218-AAAType=AUTHEN-AAAScheme= local-Service=login-UserName=root@system; AAA launched.'
pattern=r'([\d+\.?]+)-(.*);\s'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':'',
    'sport':'',
    'action': msg.group(2)
}

a='%%10LS/5/LS_AUTHEN_FAILURE(l): -DevIP=101.95.104.218-AccessType=login-UserName=admin; Authentication is failed. User not found.'
pattern=r'([\d+\.?]+)-(.*)\.'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':'',
    'sport':'',
    'action': msg.group(2)
}


# a='%%10DPBLS/5/BLS_ENTRY_OPERATION(l): -DevIP=101.95.104.218; blsOptMode(1026)=delete;srcIPAddr(1017)=80.147.210.170;blsOptReason(1027)= Auto delete;blsHoldTime(1028)=10'
a='%%10DPBLS/5/BLS_ENTRY_OPERATION(l): -DevIP=101.95.104.218-Chassis=1-Slot=4; blsOptMode(1026)=delete;srcIPAddr(1017)=60.205.202.48;blsOptReason(1027)= Auto delete;blsHoldTime(1028)=10'
pattern=r'([\d+\.?]{7,16});?\s?-?.*;(.*);.*=([\d+\.?]{7,16})'
msg = re.search(pattern, a)
info ={
    'dstip':msg.group(1),
    'dport':'',
    'srcip':msg.group(3),
    'sport':'',
    'action': msg.group(2)
}


a='41300604 Event@SYS: cloud urgent: cloud urgent message number 0'
pattern=r'Event@SYS:\s(.*)'
msg = re.search(pattern, a)
info ={
    'dstip':'',
    'dport':'',
    'srcip':'',
    'sport':'',
    'action': 'SYS %s'%msg.group(1)
}

a='421c0402 Event@MGMT: Admin user "root" attempted to login through SSH failed, and the IP is 14.17.121.130.'
pattern=r'Event@MGMT:\s(.*),.*\s([\d+\.?]{7,15})\.'
msg = re.search(pattern, a)
info ={
    'dstip':'',
    'dport':'',
    'srcip':msg.group(2),
    'sport':'',
    'action': 'MGMT %s'%msg.group(1)
}

a='47040613 Event@AAA: receive authentication request from LOGIN module for administrator zhangli.'
pattern=r'Event@AAA:\s(.*)\.'
msg = re.search(pattern, a)
info ={
    'dstip':'',
    'dport':'',
    'srcip':'',
    'sport':'',
    'action': 'AAA %s'%msg.group(1)
}

a= '43240501 Event@NET: ARP entry is created, 192.168.254.65, 741f.4a3b.aa01, trust-vr'
pattern=r'Event@NET:\s(.*),\s([\d+\.?]+),'
msg = re.search(pattern, a)
info ={
'dstip':'','dport':'','srcip':msg.group(2),'sport':'','action': 'NET %s'%msg.group(1)
}
a='48088401 IPS@IPS: From 220.181.55.144:46158 to 218.78.245.154:80, detected network intrusion, ID:306349, Name:WEB Cross-site Scripting -22, action: log-only'
pattern=r'From\s([\d+\.?]+):(\d*)\sto\s([\d+\.?]+):(\d*),\s(.*),\sI.*:(.*)\s\(?.*,'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(3),'dport':msg.group(4),'srcip':msg.group(1),'sport':msg.group(2),'action': 'IPS %s %s'%(msg.group(5),msg.group(6))
}

a='%%10SSH/6/SSH_AUTH_TIMEOUT(l): -DevIP=101.95.104.218; SSH user  (IP: 75.118.9.107) failed to log in because of authentication timeout.'
pattern=r'([\d+\.?]{7,16});?\s?(.*)\s+\(IP:\s+([\d+\.?]{7,16})\)\s(.*).'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':msg.group(3),'sport':'','action': '%s%s'%(msg.group(2),msg.group(4))
}


a='%%10LOGIN/6/LOGIN_INVALID_USERNAME_PWD: Invalid username or password from 115.173.203.62.'
pattern=r'PWD:\s(.*)\sfrom\s([\d+\.?]{7,16}).'
msg = re.search(pattern, a)
info ={
'dstip':'','dport':'','srcip':msg.group(2),'sport':'','action': '%s'%msg.group(1)
}


a='41140601 Event@SYS: AV updates signature successfully'
pattern=r'SYS:\s(.*).'
msg = re.search(pattern, a)

info ={
'dstip':'','dport':'','srcip':'','sport':'','action': '%s'%msg.group(1)
}

a="%%10SSHS/6/SSHS_AUTH_FAIL: -DevIP=10.255.249.234; SSH user ubuntu (IP: 81.217.210.119) didn't pass public key authentication for wrong public key."
pattern=r'([\d+\.?]+);\s(.*)\s\(IP:\s([\d+\.?]+)\)(.*)\.'
msg = re.search(pattern, a)

info ={
'dstip':msg.group(1),'dport':'','srcip':msg.group(3),'sport':'','action': '%s%s'%(msg.group(2),msg.group(4))
}


a='47040614 Event@AAA: receive authentication request from SCVPND module for user sanfor.'
pattern=r'AAA:\s(.*)\.'
msg = re.search(pattern, a)

info ={
'dstip':'','dport':'','srcip':'','sport':'','action': '%s'%(msg.group(1))
}


a='4514061f Event@VPN: User sanfor on SCVPN scvpn logs on from 116.226.110.66(client), login failed, user name or password is incorrect'
pattern=r'VPN:\s.*from\s([\d+.?]+)'
msg = re.search(pattern, a)
info ={
'dstip':'','dport':'','srcip':msg.group(1),'sport':'','action': 'VPN login failed user name or password is incorrect'
}


a='%%10SSHS/6/SSHS_AUTH_TIMEOUT: -DevIP=10.255.249.234; Authentication timed out for 182.254.151.134'
pattern=r'([\d+\.?]{7,16});?\s?(.*)\s+for\s([\d+\.?]{7,16})'
msg = re.search(pattern, a)

info ={
'dstip':msg.group(1),'dport':'','srcip':msg.group(3),'sport':'','action': msg.group(2)
}


a='%%10SSHS/6/SSHS_LOG: -DevIP=10.255.249.234; Invalid user sreevastav.'
pattern=r'([\d+\.?]{7,16});?\s?(.*).'
msg = re.search(pattern, a)

info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': msg.group(2)
}


a='%%10ENTITY/1/PHONY ENTITY(t): -DevIP=101.95.104.218-Chassis=1-Slot=2;   Trap 1.3.6.1.4.1.25506.2.6.2.0.11<hh3cEntityExtSFPPhony>: Entity ID is 1318, entity extend ID is 1318, entity name is Ten-GigabitEthernet1/2/0/3, admin status is 4, alarm light status is 0'
pattern=r'([\d+\.?]{7,16})'
msg = re.search(pattern, a)

info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': 'PHONY ENTITY'
}


a='%%10OPTMOD/4/PHONY_MODULE: -DevIP=10.255.249.234-Chassis=1-Slot=0; Ten-GigabitEthernet1/0/0/8: This transceiver is NOT sold by H3C. H3C therefore shall NOT guarantee the normal function of the device or assume the maintenance responsibility thereof!'
pattern=r'([\d+\.?]{7,16})'
msg = re.search(pattern, a)

info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': 'PHONY_MODULE This transceiver is NOT sold by H3C'
}

a='%%10IFNET/3/PHY_UPDOWN: -DevIP=192.168.254.9; GigabitEthernet1/7/0/8 link status is up.'
pattern=r'([\d+\.?]{7,16})'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': 'PHY_UPDOWN GigabitEthernet link status is up'
}

a='%%10IFNET/5/LINK_UPDOWN: -DevIP=192.168.254.9; Line protocol on the interface GigabitEthernet1/7/0/8 is up.'
pattern=r'([\d+\.?]{7,16});\s(.*).+'
msg = re.search(pattern, a)
info ={
'dstip':msg.group(1),'dport':'','srcip':'','sport':'','action': msg.group(2)
}

a='%%10SOCKET/6/TCP_SYNFLOOD: atckType(1016)=(05)SYN-flood;srcIPAddr(1017)=;destIPAddr(1019)=202.121.2.254;atckSpeed(1047)=300;atckTime_cn(1048)=20170813192943 '
pattern=r'TCP_SYNFLOOD'
msg = re.search(pattern, a)
info ={
'dstip':'','dport':'','srcip':'','sport':'','action': 'TCP_SYNFLOOD atckType SYN-flood'
}


a='45140608 Event@VPN: User dwh on SCVPN scvpn disconnect due to connection timeout, allocated IP 10.3.0.21, SPI 038ef8b6'
pattern=r'VPN:\s(.*),.*IP\s([\d+\.?]{7,15})'
msg = re.search(pattern, a)
print msg.groups()
info ={
'dstip':'','dport':'','srcip':msg.group(2),'sport':'','action': 'VPN %s'%msg.group(1)
}
print info




