#### 使用说明

`zbx_export_templates_all.xml`包含了多个模板，`web自动发现`、`端口自动发现`等

通过web浏览器登录zabbix,导入模板。

脚本和文本文件放入相应的目录，

#### 自动发现本地测试

- 端口

```
zabbix_get -s IP -k socket.discovery

```




- web

```
zabbix_get -s 10.11.19.16 -p 10050 -k web_site_discovery
```

都是通过构造json文件被zabbax调用。
