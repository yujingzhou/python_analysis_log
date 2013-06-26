#!/bin/sh
#######################################
##    此脚本为远程拷贝log到本地      ##
##    author:bo.yu                   ##
##    email:bo.yu@renren-inc.com     ##
#######################################

#设置定时执行，位置：/etc/crontab
#10 *    * * *   root    sh /home/robert/Desktop/scp.sh

echo "监测kerberos"
if [ -f /etc/krb5.keytab ]; then
echo "进行kerberos登录"

export PATH="/usr/kerberos/bin:$PATH"
export KRB5CCNAME=/tmp/krb5cc_pub_$$
trap kdestroy 0 1 2 3 5 15
kinit -k -t /etc/krb5.keytab
fi

echo "kerberos 监测成功"

#取得系统前一天的时间，如：2013-05-28
yourdate=$(date -d yesterday +%Y-%m-%d)
echo ${yourdate}
#设置log存储位置，需要修改
myPath="/data/boyu/token_issue/logs"
#拷贝文件存放地址
myFold=${myPath}/${yourdate}
if [ ! -d "${myFold}" ];then
    mkdir ${myFold}
fi

echo "开始拷贝log"
logpath="/data/logs/graph/"
#log格式
logForm="token_issuing_statistic.log_${yourdate}.log"

scp root@10.3.18.178:${logpath}${logForm} ${myFold}/178.log
scp root@10.3.18.179:${logpath}${logForm} ${myFold}/179.log

echo "拷贝log完毕"
