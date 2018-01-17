# CMS
云监控(Cloud Monitor System).


## 安装
安装命令行工具

```
新建一个venv,避免干扰现有环境
# mkvirtualenv aliyun

安装cli相关的工具
# pip install aliyuncli
# pip install -Iv aliyun-python-sdk-cms==5.0.0

配置ak、sk, 默认的region和输出格式
# aliyuncli configure
```

* 注意: 如果报安装失败错误,先用这个命令统一xcode协议, sudo xcodebuild -license

## 使用

cli的github地址: https://github.com/aliyun/aliyun-cli

### 列出所有告警

```
默认显示一页,一页的数据是100条
# aliyuncli cms ListAlarm

指定一页的大小
# aliyuncli cms ListAlarm --PageSize 1

查看rds告警规则
# aliyuncli cms ListAlarm --PageSize 3 --Namespace acs_rds_dashboard

查看ecs告警规则
# aliyuncli cms ListAlarm --PageSize 3 --Namespace acs_ecs_dashboard
```



