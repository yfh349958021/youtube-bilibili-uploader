# 常见问题

## Q1: 为什么上传失败？
A: 检查以下几点：
1. B站cookies是否过期（重新运行get_bilibili_cookies.py）
2. 视频格式是否正确（使用H.264编码）
3. 标题、简介是否符合B站要求

## Q2: 如何避免YouTube下载限制？
A: 使用Firefox/Chrome的cookies：
```bash
yt-dlp --cookies /path/to/youtube_cookies.txt --video-url
```

## Q3: 视频上传到哪个分区？
A: 默认上传到游戏区（tid=171），可在脚本中修改。

## Q4: 如何设置自动监控？
A: 使用systemd服务或cron定时任务：
```bash
# 每小时检查一次
0 * * * * cd /path/to/youtube-bilibili-uploader && python3 scripts/monitor_youtube.py
```
