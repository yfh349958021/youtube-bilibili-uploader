# GitHub仓库设置指南

## 第一步：在GitHub创建仓库

### 访问链接：
https://github.com/new

### 填写信息：
- **Repository name**: `youtube-bilibili-uploader`
- **Description**: `Automatically download YouTube videos and upload to Bilibili`
- **选择**: Public
- **不要勾选**: "Initialize this repository with a README"
- **点击**: "Create repository"

---

## 第二步：配置GitHub认证（选择一种）

### 方法A：使用Personal Access Token（推荐）

1. **创建Token**:
   - 访问: https://github.com/settings/tokens/new
   - Note: `youtube-bilibili-uploader`
   - Expiration: `No expiration` 或选择一个期限
   - 勾选: `repo` (完整的仓库访问权限)
   - 点击: "Generate token"
   - **⚠️ 复制Token（只显示一次）**

2. **推送代码**:
   ```bash
   cd /root/youtube-bilibili-uploader
   
   # 使用Token推送（替换YOUR_TOKEN）
   git remote set-url origin https://YOUR_TOKEN@github.com/yfh349958021/youtube-bilibili-uploader.git
   git push -u origin main
   ```

### 方法B：使用SSH密钥

1. **生成SSH密钥**（如果还没有）:
   ```bash
   ssh-keygen -t ed25519 -C "yfh349958021@github"
   # 按回车使用默认设置
   ```

2. **查看公钥**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. **添加到GitHub**:
   - 访问: https://github.com/settings/ssh/new
   - Title: `OpenClaw Server`
   - Key: 粘贴公钥内容
   - 点击: "Add SSH key"

4. **推送代码**:
   ```bash
   cd /root/youtube-bilibili-uploader
   git remote set-url origin git@github.com:yfh349958021/youtube-bilibili-uploader.git
   git push -u origin main
   ```

---

## 第三步：验证推送成功

推送成功后，访问：
https://github.com/yfh349958021/youtube-bilibili-uploader

你应该能看到所有文件！

---

## 快速命令（使用Token）

如果你已经有了GitHub Personal Access Token，直接运行：

```bash
cd /root/youtube-bilibili-uploader

# 设置远程URL（包含Token）
git remote set-url origin https://YOUR_TOKEN@github.com/yfh349958021/youtube-bilibili-uploader.git

# 推送
git push -u origin main
```

---

## 需要帮助？

- 创建Token: https://github.com/settings/tokens
- SSH设置: https://github.com/settings/ssh
- 仓库设置: https://github.com/yfh349958021/youtube-bilibili-uploader/settings
