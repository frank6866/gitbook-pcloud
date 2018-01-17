# 镜像管理



## 修改镜像
自定义镜像不能跨region使用



用待修改的镜像创建一个规格最小的按量付费实例。



0.升级内核
sudo yum makecache  ;  sudo yum --enablerepo=eleme  --disablerepo=updates install kernel-3.10.0-514.el7


1.添加tool.ops用户


修改ssh启动端口为2014


2.dns修改

vi /etc/resolv.conf

```
search elenet.me cloud.elenet.me

options rotate
options timeout:1

nameserver 10.100.0.31
nameserver 10.100.0.32
```

3.安装默认包

下载镜像文件
cd /etc/yum.repos.d/
mv *.repo backup/

wget albj-common-gateway-public-42:8000/CentOS-Base.repo
wget albj-common-gateway-public-42:8000/eleme.repo
wget albj-common-gateway-public-42:8000/epel.repo

yum clean all; yum makecache
yum install yum-plugin-priorities vim-enhanced wget rpm grep rpm-build cmake curl git htop iftop iotop logrotate mosh ntp sudo tzdata ipmitool OpenIPMI cracklib numactl cronie psmisc net-tools md5deep gcc gcc-c++ make autoconf telnet socat python-requests python2-bitmath openssl-devel libcurl-devel bash-completion supervisor salt-minion python-pip ntp ansible





"云服务ECS" - ""

https://www.alibabacloud.com/help/zh/doc-detail/25460.htm?spm=a3c0i.o25461zh.b99.104.30d517feEbNIhN




打开实例页面 - "本实例磁盘" -"创建快照"

centos7.1-514-prepare


"本实例快照" - "创建自定义镜像"




