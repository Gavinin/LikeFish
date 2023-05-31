# LikeFish

[English](..%2FREADME.md) | 中文

## 描述

这是一个基于面部识别的，多功能处理工具

## 开始使用

### 使用方法

首先，请安装cmake

```shell
# macOS
brew install cmake
```

```shell
git clone git@github.com:Gavinin/FishKeyboard.git
cd FishKeyboard
python3 install requirements.txt
# 修改config.yaml并将图片放入images文件夹中,请替换掉Example.png 和 Config.yaml 中的 example:
python3 main.py
```

## 帮助

如何修改Config.yaml，请参阅 [CONFIG.md](CONFIG_ZH.md)。

## 作者

[Gavinin](https://github.com/Gavinin)

## 版本历史

## 许可证

本项目使用 [NAME HERE] 许可证 - 详见 LICENSE.md 文件。

## 致谢

灵感、代码片段等。

* [face_recognition](https://github.com/ageitgey/face_recognition)
* [pynput](https://pynput.readthedocs.io/en/latest/index.html)