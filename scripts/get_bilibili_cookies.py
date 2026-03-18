#!/usr/bin/env python3
"""
全自动获取B站cookies
"""
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_bilibili_cookies():
    """获取B站cookies"""
    
    print("=" * 60)
    print("🔐 B站登录助手（全自动版）")
    print("=" * 60)
    
    # 配置Chrome
    options = Options()
    options.add_argument('--user-data-dir=/root/browser_profile/chrome_new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # 打开B站
        print("\n🌐 打开B站...")
        driver.get("https://www.bilibili.com")
        time.sleep(5)
        
        print("\n" + "=" * 60)
        print("⚠️  请在VNC中登录B站（扫码或账号密码）")
        print("   VNC地址: http://47.238.93.130:8443/vnc.html")
        print("=" * 60)
        print("\n⏳ 等待120秒，请在此时完成登录...")
        
        # 等待2分钟让用户登录
        for i in range(120, 0, -1):
            print(f"\r倒计时: {i}秒  ", end='', flush=True)
            time.sleep(1)
            
            # 检查是否已登录（检测SESSDATA cookie）
            cookies = driver.get_cookies()
            for cookie in cookies:
                if cookie['name'] == 'SESSDATA' and len(cookie['value']) > 10:
                    print(f"\n\n✅ 检测到登录成功！")
                    break
            else:
                continue
            break
        
        # 获取cookies
        print("\n📝 提取cookies...")
        cookies = driver.get_cookies()
        
        # 转换为字典
        cookies_dict = {}
        for cookie in cookies:
            if 'bilibili.com' in cookie.get('domain', ''):
                cookies_dict[cookie['name']] = cookie['value']
        
        print(f"✅ 提取到 {len(cookies_dict)} 个B站cookies")
        
        # 检查关键cookies
        required = ['SESSDATA', 'bili_jct', 'DedeUserID']
        found = [c for c in required if c in cookies_dict]
        missing = [c for c in required if c not in cookies_dict]
        
        if missing:
            print(f"\n❌ 缺少关键cookies: {', '.join(missing)}")
            print("可能未成功登录B站")
            return False
        
        print(f"✅ 找到所有关键cookies: {', '.join(found)}")
        
        # 创建biliup格式的cookies.json
        biliup_cookies = {
            "bilibili.com": cookies_dict
        }
        
        # 保存
        cookies_file = "/root/youtube_to_bilibili/cookies.json"
        with open(cookies_file, 'w', encoding='utf-8') as f:
            json.dump(biliup_cookies, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ cookies.json已保存: {cookies_file}")
        
        # 显示部分内容
        print(f"\n关键cookies预览:")
        for key in required:
            value = cookies_dict.get(key, '')
            if len(value) > 20:
                print(f"  {key}: {value[:20]}...")
            else:
                print(f"  {key}: {value}")
        
        return True
    
    except Exception as e:
        print(f"\n❌ 提取cookies失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        driver.quit()
        print("\n🔚 浏览器已关闭")

if __name__ == "__main__":
    success = get_bilibili_cookies()
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 Cookies获取成功！")
        print("=" * 60)
        print("\n现在可以运行上传脚本：")
        print("  python3 /root/youtube_to_bilibili/simple_upload.py")
    else:
        print("\n❌ Cookies获取失败，请重试")
