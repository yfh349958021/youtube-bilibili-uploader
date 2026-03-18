# 如何推送到GitHub

## 方法1: 创建新仓库并推送

### 1. 在GitHub上创建仓库

1. 访问 https://github.com/new
2. 仓库名称: `youtube-bilibili-uploader`
3. 描述: `Automatically download YouTube videos and upload to Bilibili`
4. 选择 Public
5. **不要**勾选 "Initialize this repository with a README"（我们已经有了）
6. 点击 "Create repository"

### 2. 推送到GitHub

```bash
cd /root/youtube-bilibili-uploader

# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/youtube-bilibili-uploader.git

# 推送到GitHub
git push -u origin main
```

## 方法2: 使用GitHub CLI（如果已安装）

```bash
# 安装GitHub CLI
# Ubuntu/Debian: sudo apt install gh
# macOS: brew install gh

# 登录
gh auth login

# 创建仓库并推送
cd /root/youtube-bilibili-uploader
gh repo create youtube-bilibili-uploader --public --source=. --push
```

## 方法3: 使用SSH（推荐）

```bash
# 1. 生成SSH密钥（如果还没有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 查看公钥并添加到GitHub
cat ~/.ssh/id_ed25519.pub
# 复制内容到 https://github.com/settings/ssh/new

# 3. 使用SSH URL
cd /root/youtube-bilibili-uploader
git remote add origin git@github.com:YOUR_USERNAME/youtube-bilibili-uploader.git
git push -u origin main
```

## 仓库内容

```
youtube-bilibili-uploader/
├── scripts/
│   ├── upload_to_bilibili.py      # B站上传脚本
│   ├── get_bilibili_cookies.py    # 获取B站cookies
│   ├── download_youtube.py        # YouTube下载
│   └── monitor_youtube.py         # YouTube监控
├── docs/
│   └── FAQ.md                     # 常见问题
├── examples/
│   └── example_config.json        # 配置示例
├── README.md                      # 说明文档
├── requirements.txt               # Python依赖
└── .gitignore                     # Git忽略文件
```

## 更新仓库

```bash
# 修改文件后
git add .
git commit -m "Update description"
git push
```
