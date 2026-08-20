# 配置文件，包含直播源URL、黑名单URL、公告信息、EPG URL、测速超时时间和线程池最大工作线程数

# 优先使用的IP版本，这里设置为ipv4
ip_version_priority = "ipv4"

# 直播源URL列表
source_urls = [
"https://m3u.ibert.me/fmml_ipv6.m3u",
"https://live.zbds.org/tv/iptv6.m3u",
"https://raw.githubusercontent.com/suxuang/myIPTV/refs/heads/main/ipv4.m3u",
"https://zbds.org/tv/iptv4.m3u",

"https://raw.githubusercontent.com/fafa002/yf2025/refs/heads/main/yiyifafa.txt",
"https://raw.githubusercontent.com/zxmlxw520/5566/refs/heads/main/cjdszb.txt",
"https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://tv.anbox.ip-ddns.com/live",
"https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
"https://raw.githubusercontent.com/JE668/m3u-checker-max/main/output/live.txt",
"http://wangziduoqing.com/yuan/zb.txt",
"https://raw.githubusercontent.com/807080747/zv/refs/heads/main/sese.txt",
"https://raw.githubusercontent.com/fleung49/star/refs/heads/main/mit",
"http://ge.html-5.me//ii/黄蚂蚁先锋推流源.txt",
"https://www.985pan.com/down.php/bf5e9607ff407fcdd71f63928ea5bc79.txt",
"https://raw.githubusercontent.com/alantang1977/iptv8/refs/heads/main/bbxx_lite.m3u",
"https://raw.githubusercontent.com/wujiangliu/live-sources/refs/heads/main/wangzizb.txt",
"https://raw.githubusercontent.com/wujiangliu/live-sources/refs/heads/main/shenqu.txt",
"https://gitee.com/main-stream/tv/raw/master/BOSS.json",
"https://raw.githubusercontent.com/alantang1977/iptv-auto/refs/heads/main/my.txt",
"https://raw.githubusercontent.com/ajqubbs/zhiboyuan/refs/heads/main/gatzb.txt",
"https://gitee.com/alexkw/app/raw/master/kgk.txt",

"https://live.445569.xyz/live.m3u",
"https://raw.githubusercontent.com/alantang1977/JunTV/refs/heads/main/output/result.m3u",
"https://raw.githubusercontent.com/swhtv/1/refs/heads/main/swtvlive",
"https://raw.githubusercontent.com/mhmdxahmd/mafly/refs/heads/main/MAfly1/mafly.m3u",
"http://tvv.tw/github.com/fafa002/yf2025/raw/main/yiyifafa.txt",
"https://l.gmbbk.com/upload/39183918.txt",
"https://tv123.cc.cd/tv.m3u",
"https://cdn.qd.je/live.m3u",
"https://raw.githubusercontent.com/nianxinmj/nxpz/refs/heads/main/lib/live.txt",
"https://raw.githubusercontent.com/JE668/get-m3u/main/output/source-m3u.txt",
"https://raw.githubusercontent.com/yihad168/tv/refs/heads/main/live.m3u",
"https://raw.githubusercontent.com/a2256569/tv/refs/heads/main/sdzb.txt",
"https://raw.githubusercontent.com/alantang1977/alan/main/proxy/mg.m3u",
"https://raw.githubusercontent.com/jn950/live/main/tv/pllive.txt",
"https://raw.githubusercontent.com/xJEYDAin/iptv-scraper/master/output/hk_merged.m3u",
"https://raw.githubusercontent.com/alantang1977/tvboxlive/main/tv/pllive.txt",
"https://raw.githubusercontent.com/tianze889/tvds/refs/heads/main/fyzb.txt",
"https://raw.githubusercontent.com/YueChan/Live/main/GNTV.m3u",
"https://raw.githubusercontent.com/ljlfct01/ljlfct01.github.io/refs/heads/main/zb",
"https://raw.githubusercontent.com/zilong7728/Collect-IPTV/refs/heads/main/best_sorted.m3u",
"https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/iptv-org/iptv/gh-pages/countries/cn.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cn.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/develop202/migu_video/refs/heads/main/interface.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/mhmdxahmd/mafly/refs/heads/main/MAfly1/mafly.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/suxuang/myIPTV/main/ipv4.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/others_output.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/alantang1977/iptv8/refs/heads/main/bbxx_lite.m3u",
"http://1.94.31.214/live/live9/dgtv.txt",
"http://1.94.31.214/live/livelite.txt",
"http://210.245.166.84:1299/live/live1.txt",
"http://210.245.166.84:1299/live/live.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/TianmuTNT/iptv/main/iptv.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/aiyakuaile/easy_tv_live/refs/heads/main/temp",
"https://gh-proxy.org/https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/mzky/checklist/refs/heads/master/itvlist.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/qingtingjjjjjjj/iptv-auto-update/main/my.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/Wirili/IPTV/main/live.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/mymsnn/DailyIPTV/main/outputs/full_validated.m3u",
"https://gh-proxy.org/https://raw.githubusercontent.com/fafa002/yf2025/refs/heads/main/yiyifafa.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/nianxinmj/nxpz/refs/heads/main/lib/live.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/yoursmile66/TVBox/main/live.txt",
"https://gh-proxy.org/https://raw.githubusercontent.com/Guovin/iptv-api/gd/output/result.m3u",
"https://gongdian.top/tv/ku9/webview.txt#JS=https://gongdian.top/tv/ku9/js/webview.js",
"https://wget.la/https://github.com/Kimentanm/aptv/raw/master/m3u/iptv.m3u",
"https://tvv.tw/github.com/alantang1977/X/raw/main/live/live_ipv4.m3u",
    "http://103.236.75.89:588/psy.m3u",
    "http://4gtv.cnlive.club/4gtv.m3u",
    "https://4gtv.tvbjack.ggff.net",
    "http://4gtv.158.qzz.io/4gtv.m3u",
    "https://raw.githubusercontent.com/iodata999/frxz751113-IPTVzb1/refs/heads/main/结果.m3u",
    "https://raw.githubusercontent.com/alantang1977/jtv/refs/heads/main/网络收集.txt",
    "",
    "",
    "",
    "https://raw.githubusercontent.com/develop202/migu_video/main/interface.txt",
    "https://www.iyouhun.com/tv/myIPTV/ipv6.m3u",
    "https://www.iyouhun.com/tv/myIPTV/ipv4.m3u",
    "",   
    "https://live.izbds.com/tv/iptv4.txt",
    "https://l.gmbbk.com/upload/39183918.txt",
    "http://rihou.cc:555/gggg.nzk",
    "http://1.94.31.214/live/livelite.txt",
    "",
    "",
    "",
    "",
    "",
    "",
    "https://live.zbds.top/tv/iptv4.txt",
    "",


]

# 直播源黑名单URL列表，去除了重复项
url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "http://[2409:8087:1a01:df::7005]:80/ottrrs.hl.chinamobile.com/PLTV/88888888/224/3221226419/index.m3u8",
    "http://[2409:8087:5e00:24::1e]:6060/000000001000/1000000006000233001/1.m3u8",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "stream1.freetv.fun",
    "chinamobile",
    "gaoma",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

# 公告信息
announcements = [
    {
        "channel": "更新日期",
        "entries": [
            {
                "name": None,
                "url": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Robot.mp4",
                "logo": "https://cnb.cool/junchao.tang/jtv/-/git/raw/main/Pictures/Chao.png"
            }
        ]
    }
]

# EPG（电子节目指南）URL列表
epg_urls = [
    "https://epg.v1.mk/fy.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
# 测速超时时间（秒）
TEST_TIMEOUT = 10

# 测速线程池最大工作线程数
MAX_WORKERS = 20
# 单个频道单协议（IPv4/IPv6）最多保留的线路数量
MAX_CHANNEL_SOURCES = 15
