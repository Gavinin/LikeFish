# 使用文档

本文档介绍了如何使用以下配置文件来设置应用程序的各种参数。

## tolerance

取值范围：1-10
类型：整数
用于设置容差参数，越小越精准，越大越宽泛,将一个介于1和10之间的整数值赋给tolerance参数。

## hasVideo

取值范围：true 或 false
类型：布尔值
用于指定是否启用视频功能。将true赋给hasVideo参数以启用视频功能，或将false赋给该参数以禁用视频功能,默认为False，通常只有Debug时打开。

### window

类型：对象
包含以下子属性来定义窗口的宽度和高度。

### width

类型：整数
用于设置窗口的宽度。请将一个整数值赋给width参数。

### height

类型：整数
用于设置窗口的高度。请将一个整数值赋给height参数。

## userMap

类型：对象
用于定义用户映射的配置,"example"需要被替换。

### example:

类型：对象
定义了用户"example"的映射配置，和image里的照片名字要一致，不区分大小写，建议使用英文。

### keyMap

类型：数组
用于设置当匹配成功所执行的快捷键，可以的多条，不区分大小写，支持CMD、Option、Ctrl、F1-F12。可以为空。

### funcMap

类型：数组
用于设置当匹配成功所执行的命令或功能，目前只有隐藏进程窗口，所以目前是进程名，macOS下通过htop或者活动监视器可以看到。可以为空。

## 示例

以下是一个示例配置文件：

```yaml
# tolerance 1-10
tolerance: 4

# true or false
hasVideo: false

window:
  width: 800
  height: 600

#
userMap:
  example:
    keyMap:
      - "CMD a"
      - "cmd m"
    funcMap:
      - "Pycharm"
      - "idea"
```

请根据需要修改配置文件中的值，并按照上述说明进行配置。