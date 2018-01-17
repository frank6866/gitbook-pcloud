# SLB

## 性能规格
性能共享型实例不能提供性能保障,其他配置性能如下:

* 超强型: 100w连接


## 使用实践
* 如果流量超过lb的上限,或者为了防止攻击,可以对一组后端服务器,创建多个slb,然后用dns轮询不同的slb。比如阿里上海区slb带宽的峰值是5GB,如果业务流量是30GB;backend servers有30台,每台带宽2G;可以创建10个slb,每个slb的backendservers都是一样的30台ecs,slb的前端再用dns做轮询,这样可以解决单个slb带宽小于backend servers总带宽的问题。



## 注意事项
* 截止2017.10,使用接口创建slb的时候, 传递的LoadBalancerSpec不会生效(默认会创建性能保障型slb.s1.small的slb);并且也没有接口修改slb的规格参数
* 截止2017.10,slb使用udp的listener时,如果不在后端服务器上做改造,健康检查功能会失效(后端服务器关机也无法检测到)
* 默认一个账户下的某个region中,最多可以创建300个slb,如果快超过了,及时联系阿里云调大这个限制。


## ref
* 不同规格slb的性能指标: https://www.alibabacloud.com/help/zh/doc-detail/27657.htm
* slb的带宽不是按照规格区分,是按照地域区分的,不同地域的带宽上限不一样,https://help.aliyun.com/document_detail/58760.html?spm=5176.doc27657.6.600.CEFKgD
