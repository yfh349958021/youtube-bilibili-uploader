# YouTube to Bilibili 自动上传工具

> **📝 代码说明**
> 
> 本项目代码由 **OpenClaw** 开发
> 
> **灵感来源: yfh349958021**

---

自动监控YouTube频道，下载视频并上传到B站的完整解决方案。

## 功能特性

✅ **YouTube监控** - 自动监控指定频道的最新视频  
✅ **视频下载** - 使用yt-dlp下载高质量视频（支持H.264编码）  
✅ **B站上传** - 使用biliup工具自动上传到B站  
✅ **Cookies管理** - 自动从Chrome提取B站登录cookies  
✅ **完整流程** - 从下载到上传的完整自动化流程  

## 快速开始

### 1. 安装依赖

```bash
pip3 install yt-dlp biliup selenium browser-cookie3
```

### 2. 获取B站Cookies

```bash
export DISPLAY=:99
python3 scripts/get_bilibili_cookies.py
```

### 3. 下载YouTube视频

```bash
python3 scripts/download_youtube.py --url "https://www.youtube.com/watch?v=xxx"
```

### 4. 上传到B站

```bash
python3 scripts/upload_to_bilibili.py
```

## 技术栈

- yt-dlp - YouTube视频下载
- biliup - B站视频上传
- selenium - 浏览器自动化

## 许可证

MIT License

---

**开发者**: OpenClaw  
**灵感来源**: yfh349958021  
**创建时间**: 2026-03-18
