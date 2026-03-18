#!/usr/bin/env python3
"""
最终上传脚本
"""
import json
import os
from biliup.plugins.bili_webup import BiliBili, Data

def upload_video():
    """上传视频"""
    
    # 读取上传信息
    with open('/root/youtube_to_bilibili/current_upload_info.json', 'r') as f:
        upload_info = json.load(f)
    
    # 读取cookies
    with open('/root/youtube_to_bilibili/cookies.json', 'r') as f:
        cookies_data = json.load(f)
    
    video_path = "/root/youtube_to_bilibili/downloads/dotacinema_latest.Dragon Knight vs Bounty Hunter Dota 2.mp4"
    
    print("=" * 60)
    print("🚀 上传视频到B站")
    print("=" * 60)
    print(f"视频: {video_path}")
    print(f"标题: {upload_info['title']}")
    print("=" * 60)
    
    # 检查视频文件
    if not os.path.exists(video_path):
        print(f"❌ 视频文件不存在: {video_path}")
        return False
    
    try:
        # 创建上传数据
        data = Data(
            title=upload_info['title'][:80],
            desc=upload_info['description'][:2000],
            tag=','.join(upload_info['tags'][:12]),
            tid=171,  # 游戏分区
            source=upload_info['original_url'],
            copyright=2,  # 转载
        )
        
        print("\n📤 初始化上传器...")
        
        # 创建上传器
        bili = BiliBili(data)
        
        # 使用cookies登录
        print("🔐 使用cookies登录...")
        bili.login_by_cookies(cookies_data)
        print("✅ 登录成功")
        
        # 上传视频文件
        print(f"\n📤 上传视频文件...")
        video_info = bili.upload_file(video_path)
        
        print(f"✅ 视频上传完成")
        print(f"视频信息: {json.dumps(video_info, indent=2, ensure_ascii=False)}")
        
        # 将视频添加到稿件的分P列表（使用data.append）
        print("\n📝 添加视频到稿件...")
        data.append(video_info)
        print("✅ 视频已添加到稿件")
        
        # 提交稿件
        print("\n📝 提交稿件...")
        result = bili.submit()
        
        print("\n✅ 上传成功！")
        print(f"提交结果: {json.dumps(result, indent=2, ensure_ascii=False)}")
        
        if hasattr(bili, 'bvid') and bili.bvid:
            print(f"\n🎉 BV号: {bili.bvid}")
            print(f"视频链接: https://www.bilibili.com/video/{bili.bvid}")
        
        return True
    
    except Exception as e:
        print(f"\n❌ 上传失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = upload_video()
    
    if success:
        print("\n🎉🎉🎉 上传完成！")
    else:
        print("\n❌ 上传失败")
