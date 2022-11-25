# BAEquipDrop

___

基于HoshinoBot实现的碧蓝档案装备掉落分布查询插件，主要为了查询一些不显示的副掉落，方便在刷高级设计图时顺便补充缺失的低级素材。

**查询格式**

```
查掉落 t[1234567]+[装备种类]
```

**装备种类名**

帽子|手套|鞋子|背包|徽章|符咒|发卡|手表

___

**实际使用例：**

```
查掉落 t4帽子
响应
装备:t4帽子的掉落分布为:
|   关卡   |   概率   |
|  10-1H   |  68.8%   |
|  11-1H   |  51.6%   |
|  16-1H   |  40.0%   |
|  10-1N   |  34.4%   |
|  16-3H   |  30.0%   |
|  10-2N   |  25.8%   |
|  10-3N   |  25.8%   |
|  10-5N   |  25.8%   |
|  16-1N   |  20.0%   |
|  19-1H   |  20.0%   |
|  16-2N   |  15.0%   |
|  16-3N   |  15.0%   |
|  16-5N   |  15.0%   |
|  19-3H   |  15.0%   |
|  19-1N   |  10.0%   |
|  19-2N   |   7.5%   |
|  19-3N   |   7.5%   |
|  19-5N   |   7.5%   |
太丑了以后再改
```

___

#### 安装方式

跟其他插件一样

```
bot设置中添加BAEquipQuery插件
module中添加BAEquipQuery插件即可
```

___

**数据来源：**

**Schale DB: **https://lonqie.github.io/SchaleDB
