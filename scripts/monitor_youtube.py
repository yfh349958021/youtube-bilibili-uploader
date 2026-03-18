import logging
from playwright.sync_api import sync_playwright
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_video_list():
    """获取YouTube频道的视频列表"""
    videos = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            logger.info(f"访问频道: {config.YOUTUBE_CHANNEL}")
            page.goto(config.YOUTUBE_CHANNEL, wait_until='networkidle', timeout=60000)
            page.wait_for_selector('ytd-rich-item-renderer', timeout=30000)
            
            # 获取视频元素
            video_elements = page.query_selector_all('ytd-rich-item-renderer')
            logger.info(f"找到 {len(video_elements)} 个视频")
            
            for elem in video_elements[:20]:
                try:
                    # 获取标题
                    title_elem = elem.query_selector('#video-title')
                    if not title_elem:
                        continue
                    
                    title = title_elem.inner_text()
                    
                    # 尝试多种方式获取链接
                    href = title_elem.get_attribute('href')
                    if not href:
                        # 尝试从父元素获取
                        link_elem = elem.query_selector('a#video-title, a[href*="watch"]')
                        if link_elem:
                            href = link_elem.get_attribute('href')
                    
                    if not href:
                        # 尝试从整个元素获取
                        link_elem = elem.query_selector('a')
                        if link_elem:
                            href = link_elem.get_attribute('href')
                    
                    if not title:
                        continue
                    
                    # 提取视频ID
                    video_id = None
                    if href:
                        if '/watch?v=' in href:
                            video_id = href.split('/watch?v=')[-1].split('&')[0]
                        elif '/shorts/' in href:
                            video_id = href.split('/shorts/')[-1].split('?')[0]
                    
                    if not video_id:
                        # 如果没有找到ID，使用标题的hash作为临时ID
                        import hashlib
                        video_id = hashlib.md5(title.encode()).hexdigest()[:11]
                    
                    # 检查关键词
                    title_lower = title.lower()
                    if 'dota' in title_lower:
                        videos.append({
                            'id': video_id,
                            'title': title,
                            'url': f"https://www.youtube.com/watch?v={video_id}" if '/watch?v=' in (href or '') else f"https://www.youtube.com/shorts/{video_id}"
                        })
                        logger.info(f"✅ 匹配: {title}")
                    
                except Exception as e:
                    logger.debug(f"解析视频元素失败: {e}")
                    continue
                    
        finally:
            browser.close()
    
    return videos

if __name__ == "__main__":
    videos = get_video_list()
    print(f"\n找到 {len(videos)} 个匹配的视频:")
    for v in videos:
        print(f"  - {v['title']}")
        print(f"    ID: {v['id']}")
        print(f"    URL: {v['url']}")
