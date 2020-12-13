### 启动盘制作

要用官方的工具

### 安装页面

==按e==进入编辑，在linux行的最后（--前面）添加

```shell
ivrs=ioapic[32]=00:14.0 spec_bypass_store_disable=prctl iommu=soft
```

ctrl+x进入安装

### 启动页面

按e进入编辑，在linux行的==quiet splash==后面添加：同上

ctrl+x启动

### 进入系统

修改/etc/default/grub内容

```shell
sudo vim /etc/default/grub
```

在GRUB_CMDLINUX_LINUX=“”：“”里内容同上

更新grub

```shell
sudo update-grub
```



