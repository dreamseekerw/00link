#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
00.LINK 零界弦译 — static site builder.
Generates index.html and product-*.html from the data below.
Run: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------- i18n ----------
# 每次 build 时设置：LANG 决定取哪一路文案，ASSET 决定静态资源前缀
#   中文页在根目录   → LANG="zh", ASSET=""
#   英文页在 /en/ 下 → LANG="en", ASSET="../"
LANG = "zh"
ASSET = ""

# 页面内导航（同语言目录内相对路径），两种语言目录结构完全一致
LANGS = {
    "zh": {"dir": "", "html": "zh-CN", "og": "zh_CN", "switch": "en/", "label": "EN", "name": "中文"},
    "en": {"dir": "en/", "html": "en", "og": "en_US", "switch": "../", "label": "中文", "name": "EN"},
}

# 站点正式域名（sitemap / robots 用），上线时按实际域名改这里
SITE_URL = "https://00.link"


def T(zh, en):
    """按当前语言二选一。"""
    return en if LANG == "en" else zh


def L(v):
    """取 (中文, English) 二元组中的当前语言项；非二元组原样返回。"""
    if isinstance(v, tuple):
        return v[1] if LANG == "en" else v[0]
    return v


CONTACT = {
    "email": "00link@163.com",
    "wechat": "seasonmap09",
}

# 全系共有的能力：六款产品都带，改这里即全站同步（不要写进单个产品数据）
AI_MODEL_LINE = (
    "搭载 6 款主流 AI 大模型，随心切换对话。",
    "Six leading AI models on board — switch conversations as you like.",
)
AI_MODEL_FEAT = (
    "6 款主流 AI 大模型 · 对话随心切换",
    "Six leading AI models · switch conversations freely",
)
AI_MODEL_SPEC = (
    "AI 模型", "6 款主流大模型 · 随心切换",
    "AI models", "Six leading AI models · switch freely",
)


def ai_extended(p):
    """把「6 款 AI 大模型」插进每款的卖点与参数里：卖点放在充电之前，参数紧跟翻译类参数之后。"""
    feats = list(p["feats"])
    feats = (feats[:-1] + [AI_MODEL_FEAT] + feats[-1:]) if feats else [AI_MODEL_FEAT]
    specs = list(p["specs"])
    hits = [i for i, s in enumerate(specs) if s[0].startswith("翻译") or s[2].startswith("Translation")]
    idx = hits[-1] if hits else len(specs) - 1
    specs = specs[: idx + 1] + [AI_MODEL_SPEC] + specs[idx + 1 :]
    return feats, specs



PRODUCTS = [
    {
        "id": "sunglass",
        "name": ("墨镜款", "Sunglass"),
        "en": ("SUNGLASS EDITION", "CLASSIC BROWLINE"),
        "tag": ("都市光影 / URBAN SHADE", "Urban Shade"),
        "price": 799,
        "img": "sunglass-1",
        "gallery": [
            ("sunglass-1", "正面 / FRONT", "Front / FRONT"),
            ("sunglass-2", "侧面 / SIDE", "Side / SIDE"),
            ("sunglass-3", "镜腿 / TEMPLE", "Temple / TEMPLE"),
        ],
        "video": "sunglass.mp4",
        "poster": "poster-sunglass.jpg",
        "swatch": "#1b1a17",
        "desc": (
            "黑银眉线，深色镜片。阳光下的从容，也是街头的锋利。",
            "Black-and-silver browline, dark lenses. Composure in the sun, an edge on the street.",
        ),
        "long": (
            "经典眉线半框与银色金属下缘相遇，深色镜片滤去刺眼的光，只留下城市的轮廓。它是一副墨镜，也是一副随时待命的翻译耳机——抬眼，即世界。",
            "A classic browline half-frame meets a silver metal rim. Dark lenses strip the glare and leave only the shape of the city. It is a pair of sunglasses, and an interpreter on standby — look up, and the world is there.",
        ),
        "feats": [
            ("黑银眉线 · 经典半框结构", "Black-and-silver browline · classic half-frame"),
            ("深色镜片 · 有效护眼，隔绝蓝光与强光", "Dark lenses · protect the eyes, blocking blue light and glare"),
            ("165+ 种语言实时同声传译", "Live interpretation in 165+ languages"),
            ("双麦波束 AI 通话降噪", "Dual-mic beamforming AI call noise reduction"),
            ("约 21g 轻盈佩戴，久戴无压", "Around 21g — light enough to forget"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("设计", "眉线半框 · 黑银撞色", "Design", "Browline half-frame · black & silver"),
            ("镜片", "深色墨镜镜片 · 护眼隔蓝光 · 可选变色 / 近视定制", "Lenses", "Dark sunglass lenses · eye care, blocks blue light · photochromic / prescription available"),
            ("翻译", "165+ 种语言 · 0.3 秒响应", "Translation", "165+ languages · 0.3s response"),
            ("降噪", "双麦波束 AI · 78dB 场景降噪", "Noise", "Dual-mic beamforming AI · 78dB reduction"),
            ("续航", "8 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "8 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("防水", "IP65 点胶防水工艺", "Water resistance", "IP65 sealed construction"),
            ("重量", "约 21g", "Weight", "Around 21g"),
        ],
    },
    {
        "id": "pink",
        "name": ("透粉款", "Transparent Pink"),
        "en": ("TRANSPARENT PINK", "21G FEATHERWEIGHT"),
        "tag": ("21g 轻颜 / FEATHER PINK", "Feather Pink"),
        "price": 799,
        "img": "pink-1",
        "gallery": [
            ("pink-1", "正面 / FRONT", "Front / FRONT"),
            ("pink-2", "侧面 / SIDE", "Side / SIDE"),
            ("pink-3", "镜腿 / TEMPLE", "Temple / TEMPLE"),
        ],
        "video": "pink.mp4",
        "poster": "poster-pink.jpg",
        "swatch": "#e2c4bd",
        "desc": (
            "21g 至轻，温润透粉。像空气一样，贴合日常。",
            "21g light, in a warm translucent pink. As easy as air, every day.",
        ),
        "long": (
            "轻若无物，美不过时。21g 的至轻机身配合温润透粉配色，把科技藏进温柔里。戴上它，气质与灵感随心而变。",
            "Light to the point of nothing, and never out of style. A 21g body in warm translucent pink hides the technology inside something gentle. Put them on and the mood follows.",
        ),
        "feats": [
            ("21g 至轻机身，久戴无压痕", "21g featherweight frame — no marks, no pressure"),
            ("温润透粉 · 时尚气质配色", "Warm translucent pink · a considered colour"),
            ("智能变色镜片 · 有效护眼，隔绝蓝光", "Photochromic lenses · protect the eyes, blocking blue light"),
            ("165+ 种语言实时同声传译", "Live interpretation in 165+ languages"),
            ("双麦波束 AI 通话降噪", "Dual-mic beamforming AI call noise reduction"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("配色", "温润透粉 · 半透明板材", "Colour", "Warm translucent pink · semi-transparent acetate"),
            ("重量", "21g 至轻设计", "Weight", "21g featherweight design"),
            ("镜片", "智能变色镜片 · 护眼隔蓝光 · 可定制墨镜 / 近视", "Lenses", "Photochromic · eye care, blocks blue light · sunglass / prescription available"),
            ("翻译", "165+ 种语言 · 0.3 秒响应", "Translation", "165+ languages · 0.3s response"),
            ("降噪", "双麦波束 AI · 78dB 场景降噪", "Noise", "Dual-mic beamforming AI · 78dB reduction"),
            ("续航", "8 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "8 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("防水", "IP65 点胶防水工艺", "Water resistance", "IP65 sealed construction"),
        ],
    },
    {
        "id": "tortoise",
        "name": ("玳瑁款", "Vintage Tortoise"),
        "en": ("VINTAGE TORTOISE", "FULL FRAME CLASSIC"),
        "tag": ("复古文艺 / VINTAGE SOUL", "Vintage Soul"),
        "price": 799,
        "img": "tortoise-1",
        "gallery": [
            ("tortoise-1", "正面 / FRONT", "Front / FRONT"),
            ("tortoise-2", "侧面 / SIDE", "Side / SIDE"),
            ("tortoise-3", "镜腿 / TEMPLE", "Temple / TEMPLE"),
        ],
        "video": "tortoise.mp4",
        "poster": "poster-tortoise.jpg",
        "swatch": "#6d4a2e",
        "desc": (
            "经典玳瑁纹理，复古而永不过时。",
            "Classic tortoiseshell, vintage and never out of date.",
        ),
        "long": (
            "时间是玳瑁的朋友。温润的纹理沉淀出复古文艺的气息，经典全框永不过时——科技，也有了温度。",
            "Time is a friend to tortoiseshell. The warm grain settles into something quietly vintage; a classic full frame that never dates — technology, with a temperature.",
        ),
        "feats": [
            ("经典玳瑁纹理 · 复古文艺气质", "Classic tortoiseshell · quietly vintage"),
            ("智能变色镜片 · 有效护眼，隔绝蓝光", "Photochromic lenses · protect the eyes, blocking blue light"),
            ("全框经典框型，永不过时", "Full-frame classic shape, never out of date"),
            ("165+ 种语言实时同声传译", "Live interpretation in 165+ languages"),
            ("轻盈日常佩戴，通勤旅行皆宜", "Light enough for commutes and long trips"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("设计", "全框经典 · 玳瑁纹理", "Design", "Full frame classic · tortoiseshell"),
            ("镜片", "智能变色镜片 · 护眼隔蓝光 · 可定制墨镜 / 近视", "Lenses", "Photochromic · eye care, blocks blue light · sunglass / prescription available"),
            ("翻译", "165+ 种语言 · 0.3 秒响应", "Translation", "165+ languages · 0.3s response"),
            ("降噪", "双麦波束 AI · 78dB 场景降噪", "Noise", "Dual-mic beamforming AI · 78dB reduction"),
            ("续航", "8 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "8 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("防水", "IP65 点胶防水工艺", "Water resistance", "IP65 sealed construction"),
            ("重量", "轻盈板材，久戴舒适", "Weight", "Lightweight acetate, comfortable all day"),
        ],
    },
    {
        "id": "blackgold",
        "name": ("黑金款", "Black Gold"),
        "en": ("BLACK GOLD", "GOLD RIM CLASSIC"),
        "tag": ("黑金经典 / BLACK & GOLD", "Black & Gold"),
        "price": 799,
        "img": "blackgold-1",
        "gallery": [
            ("blackgold-1", "正面 / FRONT", "Front / FRONT"),
            ("blackgold-2", "侧面 / SIDE", "Side / SIDE"),
            ("blackgold-3", "镜腿 / TEMPLE", "Temple / TEMPLE"),
        ],
        "video": "blackgold.mp4",
        "poster": "poster-blackgold.jpg",
        "swatch": "#211f1b",
        "desc": (
            "黑框金缘，沉稳里透一点光。",
            "Black frame, gold rim — composure with a glint.",
        ),
        "long": (
            "黑色板材压住眉线，金色金属顺着镜片下缘收进去——黑与金的分界，正好落在视线的高度。经典全框经得起日常，也经得起时间。",
            "Black acetate holds the brow line; gold metal runs along the lower edge of each lens — the seam between black and gold sits exactly at eye level. A classic full frame that survives the everyday, and the years.",
        ),
        "feats": [
            ("黑框金缘 · 经典眉线全框", "Black frame, gold rim · classic browline"),
            ("智能变色镜片 · 有效护眼，隔绝蓝光", "Photochromic lenses · protect the eyes, blocking blue light"),
            ("全框经典框型，永不过时", "Full-frame classic shape, never out of date"),
            ("165+ 种语言实时同声传译", "Live interpretation in 165+ languages"),
            ("轻盈日常佩戴，通勤旅行皆宜", "Light enough for commutes and long trips"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("设计", "全框经典 · 黑金配色", "Design", "Full frame classic · black & gold"),
            ("镜片", "智能变色镜片 · 护眼隔蓝光 · 可定制墨镜 / 近视", "Lenses", "Photochromic · eye care, blocks blue light · sunglass / prescription available"),
            ("翻译", "165+ 种语言 · 0.3 秒响应", "Translation", "165+ languages · 0.3s response"),
            ("降噪", "双麦波束 AI · 78dB 场景降噪", "Noise", "Dual-mic beamforming AI · 78dB reduction"),
            ("续航", "8 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "8 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("防水", "IP65 点胶防水工艺", "Water resistance", "IP65 sealed construction"),
            ("重量", "轻盈板材，久戴舒适", "Weight", "Lightweight acetate, comfortable all day"),
        ],
    },
    {
        "id": "business",
        "name": ("高端商务款", "Gold Business"),
        "en": ("GOLD BUSINESS", "GERMAN HINGE"),
        "tag": ("商务臻品 / EXECUTIVE", "Executive"),
        "price": 899,
        "img": "business-1",
        "gallery": [
            ("business-1", "正面 / FRONT", "Front / FRONT"),
            ("business-2", "细节 / DETAIL", "Detail / DETAIL"),
            ("business-3", "镜腿 / TEMPLE", "Temple / TEMPLE"),
        ],
        "video": "business.mp4",
        "poster": "business-1.jpg",
        "swatch": "#171614",
        "tone": True,
        "desc": (
            "黑金碰撞，沉稳而有锋芒。165 种语言，德国铰链。",
            "Black meets gold — composed, with an edge. 165 languages, German hinges.",
        ),
        "long": (
            "黑金质感，低调的锋芒。经典眉线半框与金色铰链相遇，德国进口工艺经得起 10 万次折叠。165 种语言实时翻译、AI 对话、语音与视频远程翻译、拍照即译——会议室里的可靠，谈判桌上的从容。",
            "Black and gold, an edge kept quiet. A classic browline half-frame meets a gold hinge, engineered in Germany to survive 100,000 folds. Live translation across 165 languages, AI conversation, voice and video remote translation, photo translation — reliable in the meeting room, composed at the table.",
        ),
        "caps": [
            ("ICON_LANG", "165 种语言", "实时翻译，覆盖全球主要语种",
             "165 languages", "Live translation across the world's major languages"),
            ("ICON_HINGE", "德国进口铰链", "10 万次折叠，依旧稳固如初",
             "German hinges", "100,000 folds, still firm as day one"),
            ("ICON_AUDIO", "超轻音质", "蓝牙连接，声音通透入耳",
             "Featherweight sound", "Bluetooth wireless, clear and open"),
            ("ICON_REMOTE", "远程翻译", "语音 / 视频通话实时互译",
             "Remote translation", "Voice and video calls, translated live"),
            ("ICON_SHOT", "拍照翻译", "抬眼即拍，所见即译",
             "Photo translation", "Look, shoot, understood"),
        ],
        "feats": [
            ("支持 165 种语言实时翻译，支持 AI 对话", "Live translation in 165 languages, with AI conversation"),
            ("德国进口铰链，10 万次折叠寿命", "German-imported hinges rated for 100,000 folds"),
            ("超轻音质，蓝牙无线连接", "Featherweight sound, Bluetooth wireless"),
            ("语音、视频远程翻译，跨时区对谈如面", "Voice and video remote translation, across time zones"),
            ("拍照翻译，抬眼即拍即译", "Photo translation — look, shoot, understood"),
            ("镜片有效护眼，隔绝蓝光与眩光", "Lenses protect the eyes — blue light and glare blocked"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("设计", "眉线半框 · 黑金撞色", "Design", "Browline half-frame · black & gold"),
            ("翻译", "165 种语言实时翻译 · 支持 AI 对话", "Translation", "165 languages live · AI conversation supported"),
            ("翻译方式", "语音 / 视频远程翻译 · 拍照翻译", "Modes", "Voice / video remote translation · photo translation"),
            ("铰链", "德国进口铰链 · 10 万次折叠", "Hinge", "German-imported hinge · 100,000 folds"),
            ("音频", "超轻音质 · 蓝牙无线连接", "Audio", "Featherweight sound · Bluetooth wireless"),
            ("镜片", "可定制墨镜 / 变色 / 近视 · 护眼隔蓝光", "Lenses", "Sunglass / photochromic / prescription · eye care, blocks blue light"),
            ("续航", "8 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "8 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("重量", "约 22g", "Weight", "Around 22g"),
        ],
    },
    {
        "id": "camera",
        "name": ("摄影款", "Camera Edition"),
        "en": ("CAMERA EDITION", "8MP FIRST PERSON"),
        "tag": ("全能旗舰 / FLAGSHIP", "Flagship"),
        "price": 999,
        "img": "camera-1",
        "gallery": [
            ("camera-1", "正面 / FRONT", "Front / FRONT"),
            ("camera-2", "镜头 / CAMERA", "Camera / CAMERA"),
            ("camera-3", "细节 / DETAIL", "Detail / DETAIL"),
        ],
        "video": "camera.mp4",
        "poster": "camera-1.jpg",
        "swatch": "#22211d",
        "tone": True,
        "battery": ("10 小时", "10-hour"),
        "desc": (
            "800 万像素第一视角，拍照、录影、录音、翻译与智能图像识别五位一体。",
            "8MP first-person view — photo, video, audio, translation and AI image recognition in one.",
        ),
        "long": (
            "第一视角，即刻记录。800 万像素摄像头藏于镜框之上，抬眼即拍，所见即所得——会议纪要、旅行 Vlog、即时翻译，一副眼镜全部搞定。智能图像识别更进一步：对准菜单、路牌或商品标签按下快门，画面中的文字与物件即刻被认出、翻译、留存。10 小时超长续航，全天在外也不断电。",
            "First person, captured instantly. An 8MP camera sits in the frame: look up, shoot, and keep exactly what you saw — meeting notes, travel vlogs, instant translation. One pair of glasses does it all. AI image recognition takes it further: aim at a menu, a street sign or a product label, press the shutter, and whatever is in frame is recognised, translated and kept. Ten hours of battery, so a day out never runs dry.",
        ),
        "feats": [
            ("800 万像素高清拍摄，第一视角即刻记录", "8MP first-person capture, recorded as you look"),
            ("拍照 / 录影 / 录音 / AI 翻译 / 智能识图，五位一体", "Photo / video / audio / AI translation / image recognition — five in one"),
            ("镜片有效护眼，隔绝蓝光与眩光", "Lenses protect the eyes — blue light and glare blocked"),
            ("10 小时超长续航，全天拍摄不断电", "10-hour battery — a full day of shooting"),
            ("双麦波束 AI 降噪 · 半框经典 · 约 35g", "Dual-mic AI noise reduction · classic half-frame · around 35g"),
            ("磁吸口充电，一贴即合，25 分钟快充", "Magnetic charging — snaps on, 25-minute fast charge"),
        ],
        "specs": [
            ("摄像头", "800 万像素高清摄像", "Camera", "8MP HD camera"),
            ("智能识别", "图像识别 · 文字 / 物体 / 场景", "Recognition", "AI image recognition · text / object / scene"),
            ("重量", "约 35g", "Weight", "Around 35g"),
            ("镜片", "智能变色镜片 · 护眼隔蓝光", "Lenses", "Photochromic · eye care, blocks blue light"),
            ("翻译", "165+ 种语言 · 0.3 秒响应", "Translation", "165+ languages · 0.3s response"),
            ("降噪", "双麦波束 AI · 78dB 场景降噪", "Noise", "Dual-mic beamforming AI · 78dB reduction"),
            ("续航", "10 小时 · 磁吸口充电 · 25 分钟快充", "Battery", "10 hours · magnetic charging · 25-minute fast charge"),
            ("包装清单", "眼镜盒 · 眼镜布袋 · 用户手册", "In the box", "Hard case · microfibre pouch · user manual"),
            ("防水", "IP65 点胶防水工艺", "Water resistance", "IP65 sealed construction"),
        ],
    },
]

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' fill='%2314130F'/%3E"
    "%3Ctext x='32' y='42' font-family='Helvetica,Arial' font-size='24' font-weight='700' "
    "fill='%23F3EFE8' text-anchor='middle'%3E00%3C/text%3E%3C/svg%3E"
)

ICON_ARROW = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4">'
    '<path d="M5 12h14M13 6l6 6-6 6"/></svg>'
)
ICON_CHECK = (
    '<svg viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

# ---------- 配件 / 磁吸充电图标（线性稿风格，与 tech 图标统一） ----------
ICON_MAGNET = (
    '<svg viewBox="0 0 24 24">'
    '<path d="M6 20V11a6 6 0 0 1 12 0v9"/>'
    '<path d="M6 15h4M14 15h4"/>'
    '<path d="M8 11V5.5M16 11V5.5"/>'
    '<path d="M8 5.5h2M14 5.5h2"/>'
    '</svg>'
)
ICON_CASE = (
    '<svg viewBox="0 0 24 24"><rect x="2.5" y="7.5" width="19" height="11" rx="1.6"/>'
    '<path d="M2.5 12.5h19M12 7.5v5"/></svg>'
)
ICON_POUCH = (
    '<svg viewBox="0 0 24 24"><path d="M4 9c0-1.4 1.1-2.5 2.5-2.5h11C18.9 6.5 20 7.6 20 9v8.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 17.5V9z"/>'
    '<path d="M8 6.5V5.2c0-.9.7-1.7 1.6-1.7h4.8c.9 0 1.6.8 1.6 1.7v1.3"/></svg>'
)
ICON_BOOK = (
    '<svg viewBox="0 0 24 24"><path d="M4 4.5h5.5c1.4 0 2.5 1.1 2.5 2.5v13c0-1.1-.9-2-2-2H4v-13z"/>'
    '<path d="M20 4.5h-5.5c-1.4 0-2.5 1.1-2.5 2.5v13c0-1.1.9-2 2-2H20v-13z"/></svg>'
)
ICON_PLAY = (
    '<svg viewBox="0 0 24 24"><path d="M8 5.5l10 6.5-10 6.5V5.5z" fill="currentColor" stroke="none"/></svg>'
)

# ---------- 商务款能力图标 ----------
ICON_LANG = (
    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/>'
    '<path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/></svg>'
)
ICON_HINGE = (
    '<svg viewBox="0 0 24 24"><path d="M10 8H7.2a4 4 0 0 0 0 8H10"/>'
    '<path d="M14 8h2.8a4 4 0 0 1 0 8H14"/><path d="M8.4 12h7.2"/></svg>'
)
ICON_AUDIO = (
    '<svg viewBox="0 0 24 24"><path d="M6.5 7.5l5.5-4.5 5.5 4.5L12 12l5.5 4.5L12 21l-5.5-4.5"/>'
    '<path d="M12 3v18"/></svg>'
)
ICON_REMOTE = (
    '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="12" height="12" rx="1.5"/>'
    '<path d="M15 10.5l6-3.5v10l-6-3.5"/></svg>'
)
ICON_SHOT = (
    '<svg viewBox="0 0 24 24"><path d="M3 8.5h3.5L8 6h8l1.5 2.5H21v10H3v-10z"/>'
    '<circle cx="12" cy="13" r="3.2"/></svg>'
)


TECH_ICONS = [
    # globe / real-time interpretation
    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/></svg>',
    # meeting / transcription
    '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H8l-4 4V5z"/><path d="M8 9h8M8 12.5h5"/></svg>',
    # video call
    '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="12" height="12" rx="1.5"/><path d="M15 10.5l6-3.5v10l-6-3.5"/></svg>',
    # assistant / spark
    '<svg viewBox="0 0 24 24"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z"/><path d="M18.5 16.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8.8-2.2z"/></svg>',
    # noise cancellation waves
    '<svg viewBox="0 0 24 24"><path d="M4 12h2M8 8v8M12 5v14M16 8v8M20 12h-2"/></svg>',
    # touch
    '<svg viewBox="0 0 24 24"><path d="M9 11V6.5a1.5 1.5 0 013 0V11"/><path d="M12 11V9.5a1.5 1.5 0 013 0V12"/><path d="M15 12v-1a1.5 1.5 0 013 0v4.5A5.5 5.5 0 0112.5 21H11a4 4 0 01-4-4v-3.5a1.5 1.5 0 013 0V15"/></svg>',
]

TECH_ITEMS = [
    (
        "实时同声传译",
        "165 种语言实时互译，跨国交流无障碍。语音翻译需连接网络，搭载 DeepSeek 与 GPT 双 AI 引擎。",
        "Live interpretation",
        "165 languages translated in real time, across any border. Voice translation needs a network connection and runs on both DeepSeek and GPT engines.",
    ),
    (
        "会议翻译模式",
        "实时翻译并记录会议内容，支持语音转文字，让每一次跨国会议高效流畅。",
        "Meeting mode",
        "Translates and records as you talk, with speech-to-text, so every cross-border meeting runs smoothly.",
    ),
    (
        "视频通话翻译",
        "支持微信、WhatsApp 等平台视频通话实时翻译，远程沟通零障碍。",
        "Video-call translation",
        "Real-time translation inside WeChat, WhatsApp and other video calls — remote conversations without barriers.",
    ),
    (
        "AI 语音助手",
        "智能问答、天气查询、信息检索，0.3 秒快速响应，即问即答。",
        "AI voice assistant",
        "Questions, weather, lookups — a 0.3-second response. Ask, and it answers.",
    ),
    (
        "双麦波束 AI 降噪",
        "智能增强通话效果，无惧 78dB 环境噪音，咖啡厅、街头、机场通话始终清晰。",
        "Dual-mic AI noise cancellation",
        "Beamforming keeps your voice clear against 78dB of ambient noise — cafés, streets, airports.",
    ),
    (
        "触控交互 · 指尖掌控",
        "双击播放 / 接听，滑动调音量，三击唤醒 AI 助手——指尖轻点，一切尽在掌控。",
        "Touch control",
        "Double-tap to play or answer, slide for volume, triple-tap to wake the assistant — all at your fingertips.",
    ),
]


def alt_href(page, target):
    """同一页面在另一种语言下的相对路径。"""
    if target == LANG:
        return page
    return (LANGS[target]["dir"] if LANG == "zh" else "../") + page


def head(title, desc, page="index.html", og_image="assets/img/pink-1.jpg"):
    return f"""<!DOCTYPE html>
<html lang="{LANGS[LANG]["html"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F3EFE8">
<meta property="og:type" content="website">
<meta property="og:locale" content="{LANGS[LANG]["og"]}">
<meta property="og:locale:alternate" content="{LANGS["en" if LANG == "zh" else "zh"]["og"]}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ASSET}{og_image}">
<link rel="alternate" hreflang="zh-CN" href="{alt_href(page, "zh")}">
<link rel="alternate" hreflang="en" href="{alt_href(page, "en")}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{ASSET}css/style.css">
<script>window.LINK_I18N={{copied:"{T("已复制", "Copied")}",menu:"{T("菜单", "Menu")}"}};</script>
</head>
<body>
"""


def lang_switch(page):
    zh_on = " on" if LANG == "zh" else ""
    en_on = " on" if LANG == "en" else ""
    return (
        f'<div class="lang-switch">'
        f'<a href="{alt_href(page, "zh")}" hreflang="zh-CN" class="lang-zh{zh_on}" '
        f'aria-label="中文">中</a>'
        f'<a href="{alt_href(page, "en")}" hreflang="en" class="lang-en{en_on}" '
        f'aria-label="English">EN</a>'
        f"</div>"
    )


def nav(active="", page="index.html"):
    def a(href, label, key):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    return f"""
<header class="nav">
  <div class="nav-inner">
    <a class="logo" href="index.html"><b>00.LINK</b><span>{T("零界弦译", "AI EYEWEAR")}</span></a>
    <nav class="nav-links">
      {a("index.html#series", T("产品系列", "Collection"), "series")}
      {a("index.html#craft", T("工艺设计", "Craft"), "craft")}
      {a("index.html#tech", T("核心技术", "Technology"), "tech")}
      {a("index.html#guide", T("使用指南", "Guide"), "guide")}
      {a("index.html#accessories", T("配件清单", "In the box"), "accessories")}
      {a("index.html#wild", T("真实佩戴", "In the wild"), "wild")}
      {a("index.html#contact", T("联系我们", "Contact"), "contact")}
    </nav>
    <div class="nav-right">
      {lang_switch(page)}
      <a class="nav-buy" href="index.html#series">{T("立即选购", "Shop now")}</a>
      <button class="menu-btn" aria-label="{T("菜单", "Menu")}"><i></i><i></i><i></i></button>
    </div>
  </div>
</header>
<div class="mobile-menu">
  <a href="index.html#series">{T("产品系列", "Collection")}</a>
  <a href="index.html#craft">{T("工艺设计", "Craft")}</a>
  <a href="index.html#tech">{T("核心技术", "Technology")}</a>
  <a href="index.html#guide">{T("使用指南", "Guide")}</a>
  <a href="index.html#accessories">{T("配件清单", "In the box")}</a>
  <a href="index.html#wild">{T("真实佩戴", "In the wild")}</a>
  <a href="index.html#contact">{T("联系我们", "Contact")}</a>
  <a class="btn btn-dark" href="index.html#series">{T("立即选购", "Shop now")}</a>
  {lang_switch(page)}
</div>
"""


def footer():
    prod_links = "".join(
        f'<a href="product-{x["id"]}.html">{L(x["name"])} · ¥{x["price"]}</a>' for x in PRODUCTS
    )
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <b>00.LINK</b><span>{T("零界弦译 · AI TRANSLATION EYEWEAR", "AI TRANSLATION EYEWEAR")}</span>
        <p>{T("我们相信，未来的科技不应是冰冷的工具，而是无缝融入生活的伙伴。把 165 种语言、一副好声音，藏进一副好看的眼镜里。", "We believe the technology of the future shouldn't be a cold tool, but a partner that disappears into daily life. 165 languages and a genuinely good pair of speakers, folded into glasses you'd wear anyway.")}</p>
      </div>
      <div class="foot-col">
        <h4>{T("产品系列", "Collection")}</h4>
        {prod_links}
      </div>
      <div class="foot-col">
        <h4>{T("支持", "Support")}</h4>
        <a href="index.html#tech">{T("技术参数", "Specifications")}</a>
        <a href="index.html#craft">{T("工艺与镜片", "Craft & lenses")}</a>
        <a href="index.html#guide">{T("使用指南", "Guide")}</a>
        <a href="index.html#accessories">{T("配件与充电", "Accessories & charging")}</a>
        <a href="index.html#contact">{T("购买咨询", "Order enquiries")}</a>
        <a href="index.html#contact">{T("售后与保修", "Warranty & service")}</a>
      </div>
      <div class="foot-col">
        <h4>{T("联系我们", "Contact")}</h4>
        <p>{T("客服微信：", "WeChat: ")}{CONTACT["wechat"]}</p>
        <a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a>
        <p>{T("周一至周日 09:00 — 21:00", "Mon–Sun, 09:00 — 21:00")}</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span data-year>2026</span> 00.LINK Technology · All Rights Reserved</span>
      <span>{T("* 语音翻译需连接网络使用 · Powered by DeepSeek &amp; GPT<br>* 镜片支持墨镜 / 蓝光 / 变色 / 近视定制，具体以客服确认为准", "* Voice translation requires a network connection · Powered by DeepSeek &amp; GPT<br>* Lenses made to order: sunglass / blue-light / photochromic / prescription")}</span>
    </div>
  </div>
</footer>
"""


def modal():
    return f"""
<div class="modal" id="buyModal">
  <div class="modal-card">
    <button class="modal-close" onclick="closeBuy()" aria-label="{T("关闭", "Close")}">×</button>
    <h3>{T("购买咨询", "Order enquiry")}</h3>
    <div class="en-line">CONCIERGE · 1 ON 1</div>
    <div class="modal-prod">
      <img data-buy-img src="{ASSET}assets/img/pink-1.jpg" alt="">
      <div><b data-buy-name>{T("透粉款", "Transparent Pink")}</b><span data-buy-price>¥799</span></div>
    </div>
    <div class="modal-contact">
      <div class="row"><span>01 &nbsp; {T("添加客服微信", "Add our WeChat")}</span><button onclick="copyText('{CONTACT["wechat"]}')">{T("复制微信号", "Copy ID")}</button></div>
      <div class="row"><span>02 &nbsp; {T("确认款式与镜片", "Confirm style & lenses")}</span><span style="color:var(--muted-2)">{CONTACT["wechat"]}</span></div>
      <div class="row"><span>03 &nbsp; {T("微信支付下单", "Pay via WeChat")}</span><span style="color:var(--muted-2)">{T("支持微信支付", "WeChat Pay accepted")}</span></div>
      <div class="row"><span>04 &nbsp; {T("顺丰包邮发货", "Ships by SF Express")}</span><span style="color:var(--muted-2)">{T("48 小时内", "Within 48 hours")}</span></div>
    </div>
    <div style="display:flex;gap:10px;margin-top:18px;">
      <button class="btn btn-dark" style="flex:1;height:48px" onclick="copyText('{CONTACT["wechat"]}')">{T("复制客服微信", "Copy WeChat ID")}</button>
      <a class="btn btn-outline" style="flex:1;height:48px" href="mailto:{CONTACT["email"]}">{T("邮件咨询", "Email us")}</a>
    </div>
    <p class="note">{T("支持微信支付 · 顺丰包邮 · 7 天无理由退换 · 一年质保", "WeChat Pay · Free SF Express shipping · 7-day returns · 1-year warranty")}</p>
  </div>
</div>
<div class="toast" id="toast"></div>
<script src="{ASSET}js/site.js"></script>
</body>
</html>
"""


def card(p, span="", lazy=True):
    span_cls = " " + span if span else ""
    name = L(p["name"])
    badge = L(p["tag"]).split(" / ")[0]
    vid = ""
    attr = ""
    if p["video"]:
        attr = " data-video"
        vid = (
            f'<video muted loop playsinline preload="none" poster="{ASSET}assets/img/{p["poster"]}" '
            f'src="{ASSET}assets/video/{p["video"]}"></video>'
        )
    loading = ' loading="lazy"' if lazy else ""
    return f"""
    <a class="card{span_cls} reveal{' tone' if p.get('tone') else ''}" href="product-{p["id"]}.html"{attr}>
      <div class="card-media">
        {vid}
        <img src="{ASSET}assets/img/{p["img"]}.jpg" alt="{name} · 00.LINK AI {T("翻译眼镜", "translation eyewear")}"{loading}>
        <span class="card-badge">{badge}</span>
      </div>
      <div class="card-meta">
        <div>
          <div class="card-name">{name}</div>
          <span class="card-en">{L(p["en"])}</span>
          <span class="card-arrow">{T("查看详情", "View")} {ICON_ARROW}</span>
        </div>
        <div class="card-price">¥{p["price"]}</div>
      </div>
    </a>"""


def build_index():
    by_id = {p["id"]: p for p in PRODUCTS}
    hero = by_id["pink"]
    cards = (
        card(by_id["sunglass"], span="wide")
        + card(by_id["pink"], span="half")
        + card(by_id["tortoise"], span="quarter")
        + card(by_id["blackgold"], span="quarter")
        + card(by_id["business"], span="quarter")
        + card(by_id["camera"], span="quarter")
    )

    tech_cards = "".join(
        f'<div class="tech-card reveal">{TECH_ICONS[i]}<h3>{T(t[0], t[2])}</h3><p>{T(t[1], t[3])}</p></div>'
        for i, t in enumerate(TECH_ITEMS)
    )

    craft_items = [
        (
            "01",
            "5mm 超细镜腿",
            "芯片与电池精密嵌入仅 5mm 的镜腿之中，厚度直降 40%，轻盈到几乎忘记它的存在。",
            "5mm temples",
            "Chip and battery packed into a temple just 5mm thick — 40% thinner, light enough to forget you're wearing them.",
        ),
        (
            "02",
            "琴钢超弹铰链",
            "弹性均衡，轻巧贴合；万次折弯后依旧回弹如初，长久佩戴始终舒适。",
            "Piano-steel hinge",
            "Balanced spring tension and a light fit; still snapping back after ten thousand folds.",
        ),
        (
            "03",
            "智能变色镜片",
            "室内通透，户外渐深。有效过滤刺眼强光，一副眼镜应对一天的光线。",
            "Photochromic lenses",
            "Clear indoors, darker outdoors. Glare filtered, so one pair covers a whole day of light.",
        ),
        (
            "04",
            "镜片随心定制",
            "墨镜、防蓝光、变色、近视——按你的度数量身定制，好看也能看清。",
            "Made to your prescription",
            "Sunglass, blue-light, photochromic, prescription — built to your exact prescription. Good looking, and clearly seen.",
        ),
    ]
    craft_html = "".join(
        f'<div class="craft-item reveal"><span class="idx">{n}</span>'
        f"<div><h3>{T(t_zh, t_en)}</h3><p>{T(d_zh, d_en)}</p></div></div>"
        for n, t_zh, d_zh, t_en, d_en in craft_items
    )

    wild = [
        ("buyer7", "中国 / CN"), ("buyer8", "中国 / CN"),
        ("buyer3", "南非 / SA"), ("buyer5", "日本 / JP"), ("buyer2", "欧洲 / EU"),
        ("buyer4", "南非 / SA"), ("buyer6", "中国 / CN"), ("buyer1", "摩洛哥 / MA"),
    ]
    wild_html = "".join(
        f'<figure class="wild-item"><div class="ph"><img src="{ASSET}assets/img/{f}.jpg" '
        f'alt="00.LINK {T("真实佩戴", "worn for real")}" loading="lazy"></div>'
        f'<figcaption><span>{c.split(" / ")[1]}</span><span>REAL SHOT</span></figcaption></figure>'
        for f, c in wild
    )

    return (
        head(
            T(
                "00.LINK 零界弦译 · AI 智能翻译眼镜 | 165 种语言，戴上就懂",
                "00.LINK · AI Translation Eyewear | 165 languages, understood on sight",
            ),
            T(
                "00.LINK 零界弦译 AI 智能翻译眼镜：165 种语言实时同传、双麦波束 AI 降噪、21g 轻盈、8 小时续航。墨镜款 / 透粉款 / 玳瑁款 ¥799，高端商务款 ¥899，摄影款 ¥999。",
                "00.LINK AI translation eyewear: live interpretation in 165 languages, dual-mic beamforming AI noise cancellation, 21g on your face, 8-hour battery. Sunglass / Transparent Pink / Vintage Tortoise ¥799, Gold Business ¥899, Camera Edition ¥999.",
            ),
            page="index.html",
        )
        + nav(page="index.html")
        + f"""
<main>
  <section class="hero">
    <div class="wrap">
      <div class="hero-grid">
        <div class="hero-copy">
          <span class="eyebrow reveal">2026 · AI TRANSLATION EYEWEAR</span>
          <h1 class="display reveal">{T("让世界<br>说你的语言", "Let the world<br>speak your language")}</h1>
          <div class="en-line reveal">Speak anywhere. Understand everything.</div>
          <p class="hero-desc reveal">{T("165 种语言实时同译，双麦波束 AI 降噪，21g 轻盈上脸，8 小时续航。眼镜与耳机的边界，从此消失。", "165 languages translated live, dual-mic beamforming AI noise cancellation, 21g on your face, 8 hours of battery. The line between glasses and earphones disappears.")}</p>
          <div class="hero-actions reveal">
            <a class="btn btn-dark" href="#series">{T("探索系列", "Explore the range")} {ICON_ARROW}</a>
            <a class="btn btn-outline" href="product-pink.html">{T("透粉款 ¥799", "Transparent Pink ¥799")}</a>
          </div>
        </div>
        <div class="hero-visual reveal">
          <div class="hero-media">
            <video autoplay muted loop playsinline poster="{ASSET}assets/img/{hero["poster"]}" src="{ASSET}assets/video/{hero["video"]}"></video>
          </div>
        </div>
      </div>
      <div class="stats reveal">
        <div class="stat"><b>165+</b><span>{T("语言实时翻译", "Languages, live")}</span></div>
        <div class="stat"><b>21g</b><span>{T("轻盈佩戴", "Feather-light")}</span></div>
        <div class="stat"><b>8h</b><span>{T("超长续航", "Battery life")}</span></div>
        <div class="stat"><b>IP65</b><span>{T("防尘防水", "Dust & water resistant")}</span></div>
      </div>
    </div>
    <div class="hero-scroll">SCROLL</div>
  </section>

  <div class="marquee">
    <div class="marquee-track">
      <span>{T("实时同声传译", "Live interpretation")}</span><span>{T("165+ 种语言", "165+ languages")}</span><span>{T("双麦波束降噪", "Beamforming noise cancellation")}</span><span>{T("智能变色镜片", "Photochromic lenses")}</span>
      <span>{T("25 分钟快充", "25-minute fast charge")}</span><span>{T("8 小时续航", "8-hour battery")}</span><span>{T("5mm 超细镜腿", "5mm temples")}</span><span>{T("琴钢超弹铰链", "Piano-steel hinges")}</span>
    </div>
  </div>

  <section class="section" id="series">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">01 — Collection</span>
          <h2 class="h2 reveal">{T("六种气质，<br>同一副智慧", "Six characters,<br>one intelligence")}</h2>
        </div>
        <p class="lead reveal">{T("墨镜、透粉、玳瑁、黑金、商务、摄影——每一款都为不同的你而生。进入产品页，查看三张细节图与实拍影像。", "Sunglass, pink, tortoise, black gold, business, camera — each built for a different you. Step inside for three detail shots and real footage.")}</p>
      </div>
      <div class="collection">{cards}</div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="split">
        <div class="split-media tall reveal">
          <video autoplay muted loop playsinline poster="{ASSET}assets/img/poster-split.jpg" src="{ASSET}assets/video/split.mp4"></video>
        </div>
        <div class="split-body">
          <span class="eyebrow reveal">Sound &amp; Silence</span>
          <h2 class="h2 reveal">{T("眼镜，<br>也是耳机", "Glasses,<br>that are also earphones")}</h2>
          <p class="lead reveal">{T("双麦波束 AI 降噪把 78dB 的嘈杂挡在耳外，只留下对方的声音。指尖轻点，播放、通话、唤醒助手——一切自然发生。", "Dual-mic beamforming AI holds up to 78dB of noise at bay and leaves only the voice in front of you. A tap plays, answers, wakes the assistant — naturally.")}</p>
          <ul class="bullets">
            <li class="reveal"><i>01</i><span>{T("双麦波束 AI 降噪 · 78dB 场景降噪，还原真实音色", "Dual-mic beamforming AI · 78dB scene noise reduction, true-to-life tone")}</span></li>
            <li class="reveal"><i>02</i><span>{T("双击播放 / 滑动调音量 / 三击唤醒 AI 助手", "Double-tap to play / slide for volume / triple-tap for the AI assistant")}</span></li>
            <li class="reveal"><i>03</i><span>{T("8 小时续航 · 25 分钟快充，290mAh 大电池", "8-hour battery · 25-minute fast charge · 290mAh cell")}</span></li>
          </ul>
          <div class="reveal" style="margin-top:30px">
            <a class="link-u" href="#tech">{T("了解核心技术", "Explore the technology")} {ICON_ARROW}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section dark" id="craft">
    <div class="wrap">
      <figure class="craft-media reveal">
        <img src="{ASSET}assets/img/craft-wide-a.jpg" alt="{T("透粉款 5mm 超细镜腿与铰链细节", "Transparent pink frame — 5mm temple and hinge detail")}" loading="lazy">
        <figcaption>Temple · Hinge · 5mm</figcaption>
      </figure>
      <div class="craft-head">
        <div>
          <span class="eyebrow reveal">02 — Craft</span>
          <h2 class="h2 reveal" style="margin-top:18px">{T("极细之处，<br>见真章", "The details,<br>down to the millimetre")}</h2>
        </div>
        <p class="lead reveal">{T("比铅笔还细的镜腿、琴钢超弹铰链、智能变色镜片——每一处细节，都为长久佩戴而生。", "Temples thinner than a pencil, piano-steel hinges, photochromic lenses — every detail is built for wearing all day.")}</p>
      </div>
      <div class="craft-list">{craft_html}</div>
    </div>
  </section>

  <section class="section" id="tech">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">03 — Technology</span>
          <h2 class="h2 reveal">{T("AI 翻译引擎，<br>声声入耳", "An AI engine<br>you can hear")}</h2>
        </div>
        <p class="lead reveal">{T("165 种语言实时翻译 · 0.3 秒快速响应 · 95%+ 翻译准确率 · 10 米有效拾音。语音翻译需连接网络。", "165 languages live · 0.3s response · 95%+ accuracy · 10m pickup range. Voice translation requires a network connection.")}</p>
      </div>
      <div class="tech-nums reveal">
        <div class="q"><b>165+</b><span>{T("支持语言", "Languages")}</span></div>
        <div class="q"><b>0.3s</b><span>{T("翻译响应", "Response")}</span></div>
        <div class="q"><b>95%+</b><span>{T("翻译准确率", "Accuracy")}</span></div>
        <div class="q"><b>10m</b><span>{T("有效拾音", "Pickup range")}</span></div>
      </div>
      <div class="tech-grid">{tech_cards}</div>
    </div>
  </section>

  <section class="band">
    <video autoplay muted loop playsinline poster="{ASSET}assets/img/poster-brand.jpg" src="{ASSET}assets/video/brand.mp4"></video>
    <div class="band-cap">
      <div>
        <div class="en-line" style="margin-bottom:14px">00.LINK · Real Life</div>
        <h2 class="h2">{T("戴上它，<br>世界变得很近", "Put them on,<br>the world comes closer")}</h2>
      </div>
      <div class="meta">21g / 165+ LANGUAGES<br>8H BATTERY / IP65</div>
    </div>
  </section>

  <section class="section" id="guide">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">04 — Guide</span>
          <h2 class="h2 reveal">{T("上手只要<br>三步", "Three steps<br>to get started")}</h2>
        </div>
        <p class="lead reveal">{T("下载 App、绑定设备、开始对话。完整的 82 秒使用说明视频，从包装开箱到各项功能演示，一次看完。", "Download the app, pair the device, start talking. The full 82-second guide covers everything from unboxing to every feature.")}</p>
      </div>
      <div class="guide">
        <div class="guide-media reveal">
          <video controls preload="none" poster="{ASSET}assets/img/guide-poster.jpg" src="{ASSET}assets/video/guide.mp4"></video>
        </div>
        <ol class="guide-steps">
          <li class="reveal">
            <span class="n">01</span>
            <div>
              <h3>{T("下载并绑定", "Download & pair")}</h3>
              <p>{T("扫描用户手册上的二维码，或直接输入设备码完成绑定。一码仅绑定一台设备。", "Scan the QR code in the manual, or enter the device code to pair. One code pairs one device.")}</p>
            </div>
          </li>
          <li class="reveal">
            <span class="n">02</span>
            <div>
              <h3>{T("轻触即译", "Tap to translate")}</h3>
              <p>{T("轻触镜腿开启翻译，支持自由说与双语对照模式，0.3 秒响应。", "Tap the temple to start translating. Free-speech and side-by-side modes, 0.3-second response.")}</p>
            </div>
          </li>
          <li class="reveal">
            <span class="n">03</span>
            <div>
              <h3>{T("更多模式", "More modes")}</h3>
              <p>{T("翻译机、AI 对话、语音笔记、拍照翻译——四种模式覆盖出国、开会与记录场景。", "Interpreter, AI conversation, voice notes, photo translation — four modes for travel, meetings and notes.")}</p>
            </div>
          </li>
        </ol>
      </div>
    </div>
  </section>

  <section class="section" id="wild">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">05 — In the wild</span>
          <h2 class="h2 reveal">{T("真实佩戴，<br>来自世界各地", "Worn for real,<br>around the world")}</h2>
        </div>
        <p class="lead reveal">{T("摩洛哥、南非、日本、欧洲与中国——来自真实用户的随手一拍。", "Morocco, South Africa, Japan, Europe and China — snapshots from real users.")}</p>
      </div>
      <div class="wild-strip reveal">{wild_html}</div>
    </div>
  </section>

  <section class="section" id="accessories">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">06 — In the box</span>
          <h2 class="h2 reveal">{T("磁吸一吸，<br>开箱即用", "Snap on,<br>ready out of the box")}</h2>
        </div>
        <p class="lead reveal">{T("镜腿内置磁吸充电口，对准即充，25 分钟快充即可出门。所有配件随盒附赠，无需另购。", "A magnetic charging port sits in the temple — align it and it charges. 25 minutes of fast charge and you're out the door. Everything else is in the box.")}</p>
      </div>

      <div class="acc-grid">
        <figure class="acc-media reveal">
          <img src="{ASSET}assets/img/acc-hero2.jpg" alt="{T("00.LINK 零界弦译随盒配件：磁吸充电线、收纳布袋与用户手册", "00.LINK accessories: magnetic charging cable, pouch and user manual")}">
          <figcaption>All accessories included in the box</figcaption>
        </figure>

        <div class="acc-side">
          <div class="acc-charge reveal">
            <div class="acc-charge-icon">{ICON_MAGNET}</div>
            <div>
              <span class="acc-kicker">Magnetic Charging</span>
              <h3>{T("磁吸口充电", "Magnetic charging")}</h3>
              <p>{T("镜腿内嵌磁吸触点，充电线一贴即合，不挑方向、不怕插错。摘下眼镜顺手一充，满电续航 8 小时；快充 25 分钟，可用 2 小时。", "Magnetic contacts sit inside the temple: the cable snaps on either way round, no plugging, no wrong way. Take them off and set them down to charge — 8 hours of playback, or 2 hours from a 25-minute top-up.")}</p>
            </div>
          </div>

          <ul class="acc-list">
            <li class="reveal">
              <span class="acc-ico">{ICON_CASE}</span>
              <div>
                <h4>{T("眼镜盒", "Hard case")}</h4>
                <p>{T("硬质收纳盒，防压防磕，随身放入包中不占地。", "A rigid case that shrugs off knocks and pressure, slim enough for any bag.")}</p>
              </div>
            </li>
            <li class="reveal">
              <span class="acc-ico">{ICON_POUCH}</span>
              <div>
                <h4>{T("眼镜布袋", "Microfibre pouch")}</h4>
                <p>{T("超细纤维软布袋，收纳眼镜同时防止镜片刮花。", "A soft microfibre pouch that stores the glasses and keeps the lenses from scratching.")}</p>
              </div>
            </li>
            <li class="reveal">
              <span class="acc-ico">{ICON_BOOK}</span>
              <div>
                <h4>{T("说明书", "User manual")}</h4>
                <p>{T("纸质用户手册，内含绑定二维码与各功能操作指引。", "A printed manual with the pairing QR code and a walkthrough of every feature.")}</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="cta" id="contact">
    <div class="wrap">
      <span class="eyebrow reveal" style="justify-content:center">07 — Contact</span>
      <h2 class="h2 reveal">{T("现在，把世界<br>戴在脸上", "Now, wear<br>the world")}</h2>
      <p class="lead reveal">{T("购买咨询、镜片定制、渠道合作与售后支持，随时与我们联系。", "Orders, lens customisation, partnerships and after-sales — talk to us any time.")}</p>
      <div class="cta-price reveal">¥799 <small>{T("起 / 六款可选", "from · six styles")}</small></div>
      <div class="cta-actions reveal">
        <a class="btn btn-light" href="#series">{T("立即选购", "Shop now")} {ICON_ARROW}</a>
        <button class="btn btn-ghost-light" onclick="openBuy('{T("透粉款", "Transparent Pink")}', 799, '{ASSET}assets/img/pink-1.jpg')">{T("微信咨询", "Chat on WeChat")}</button>
      </div>
      <p class="lead reveal" style="margin-top:26px;font-size:12px;letter-spacing:.14em">{T("客服微信", "WeChat")} {CONTACT["wechat"]} &nbsp;·&nbsp; {CONTACT["email"]}</p>
    </div>
  </section>
</main>
"""
        + footer()
        + modal()
    )


def build_product(p):
    page = f'product-{p["id"]}.html'
    name = L(p["name"])
    pline = L(p["en"])
    tag = L(p["tag"])
    desc = L(p["desc"])
    long_txt = L(p["long"]) + L(AI_MODEL_LINE)

    others = [x for x in PRODUCTS if x["id"] != p["id"]][:3]
    related = "".join(card(o, lazy=True) for o in others)

    thumbs = "".join(
        f'<button class="thumb{" active" if i == 0 else ""}" data-src="{ASSET}assets/img/{src}.jpg" aria-label="{T(lz, le)}">'
        f'<img src="{ASSET}assets/img/{src}.jpg" alt="{name} {T(lz, le)}" loading="lazy">'
        f'<span class="lab">{T(lz, le).split(" / ")[0]}</span></button>'
        for i, (src, lz, le) in enumerate(p["gallery"])
    )

    if p["video"]:
        film = (
            f'<div class="p-film-media{" tone" if p.get("tone") else ""}"><video autoplay muted loop playsinline '
            f'poster="{ASSET}assets/img/{p["poster"]}" src="{ASSET}assets/video/{p["video"]}"></video></div>'
            f'<div class="p-film-cap"><span>{name} · {T("实拍影像 / PRODUCT FILM", "PRODUCT FILM")}</span><span>00.LINK 2026</span></div>'
        )
        film_en = "PRODUCT FILM"
    else:
        film = (
            f'<div class="p-film-media still{" tone" if p.get("tone") else ""}"><img src="{ASSET}assets/img/{p["poster"]}" alt="{name}"></div>'
            f'<div class="p-film-cap"><span>{name} · {T("细节实拍 / STILL STUDY", "STILL STUDY")}</span><span>00.LINK 2026</span></div>'
        )
        film_en = "STILL STUDY"
    film_label = T("产品影像", "Product film")

    feat_list, spec_list = ai_extended(p)
    feats = "".join(f'<li>{ICON_CHECK}<span>{T(fz, fe)}</span></li>' for fz, fe in feat_list)
    specs = "".join(f"<tr><td>{T(kz, ke)}</td><td>{T(vz, ve)}</td></tr>" for kz, vz, ke, ve in spec_list)

    caps_html = ""
    if p.get("caps"):
        cap_items = "".join(
            f'<div class="cap reveal"><div class="cap-ic">{globals()[ic]}</div>'
            f"<h4>{T(tz, te)}</h4><p>{T(dz, de)}</p></div>"
            for ic, tz, dz, te, de in p["caps"]
        )
        caps_html = f"""
  <section class="section cap-sec">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">Capabilities</span>
          <h2 class="h2 reveal">{T("为商务场景，<br>逐项打磨", "Engineered for<br>the boardroom")}</h2>
        </div>
        <p class="lead reveal">{T(f"从一枚铰链到一句译文，{name}的每一项能力，都指向同一个目标——让你在谈判桌上更从容。", f"From a single hinge to a single sentence, every capability of the {name} points at one thing — composure at the table.")}</p>
      </div>
      <div class="cap-grid">{cap_items}</div>
    </div>
  </section>
"""

    gallery3 = "".join(
        f'<figure class="g{i + 1} reveal"><div class="ph"><img src="{ASSET}assets/img/{src}.jpg" '
        f'alt="{name} {T(lz, le)}" loading="lazy"></div>'
        f'<figcaption><span>0{i + 1} — {T(lz, le).split(" / ")[1]}</span>'
        f'<span>{T(lz, le).split(" / ")[0]}</span></figcaption></figure>'
        for i, (src, lz, le) in enumerate(p["gallery"])
    )

    swatches = "".join(
        f'<a class="swatch{" active" if x["id"] == p["id"] else ""}" href="product-{x["id"]}.html">'
        f'<i style="background:{x["swatch"]}"></i>{L(x["name"])}</a>'
        for x in PRODUCTS
    )

    bat = T(*p.get("battery", ("8 小时", "8-hour")))

    return (
        head(
            T(
                f'{name} {pline} · ¥{p["price"]} | 00.LINK 零界弦译 AI 翻译眼镜',
                f'{name} · ¥{p["price"]} | 00.LINK AI Translation Eyewear',
            ),
            T(
                f'{name}（{pline}）¥{p["price"]}。{desc}165+ 种语言实时同传、双麦波束 AI 降噪、{bat}续航。',
                f'{name} · ¥{p["price"]}. {desc} Live interpretation in 165+ languages, dual-mic beamforming AI noise cancellation, {bat} battery.',
            ),
            page=page,
            og_image=f'assets/img/{p["img"]}.jpg',
        )
        + nav(page=page)
        + f"""
<main>
  <section class="p-hero">
    <div class="wrap">
      <div class="crumb"><a href="index.html">{T("首页", "Home")}</a><i>/</i><a href="index.html#series">{T("产品系列", "Collection")}</a><i>/</i><span>{name}</span></div>
      <div class="p-grid">
        <div class="p-gallery{' tone' if p.get('tone') else ''}">
          <div class="gallery-main reveal"><img src="{ASSET}assets/img/{p["gallery"][0][0]}.jpg" alt="{name} · 00.LINK AI {T("翻译眼镜", "translation eyewear")}"></div>
          <div class="gallery-thumbs reveal">{thumbs}</div>
        </div>
        <div class="p-info">
          <div class="tag reveal">{tag}</div>
          <h1 class="reveal">{name}</h1>
          <div class="en-line reveal">{pline} · 00.LINK</div>
          <div class="p-price reveal"><b>¥{p["price"]}</b><span>{T("含标准镜片 · 顺丰包邮", "Standard lenses included · Free shipping")}</span></div>
          <p class="p-desc reveal">{long_txt}</p>
          <ul class="p-feats reveal">{feats}</ul>
          <div class="p-actions reveal">
            <button class="btn btn-dark" onclick="openBuy('{name}', {p["price"]}, '{ASSET}assets/img/{p["img"]}.jpg')">{T("立即购买", "Buy now")} {ICON_ARROW}</button>
            <button class="btn btn-outline" onclick="copyText('{CONTACT["wechat"]}')">{T("预约试戴", "Book a try-on")}</button>
          </div>
          <div class="p-notes reveal">
            <span>{T("微信支付", "WeChat Pay")}</span><span>{T("顺丰包邮", "Free shipping")}</span><span>{T("7 天无理由", "7-day returns")}</span><span>{T("一年质保", "1-year warranty")}</span>
          </div>
          <div class="swatches reveal">
            <h4>{T("其他款式", "Other styles")}</h4>
            <div class="swatch-row">{swatches}</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="p-film">
    <div class="wrap">
      <div class="p-film-head">
        <div>
          <span class="eyebrow reveal">{film_en}</span>
          <h2 class="h2 reveal" style="margin-top:14px">{film_label}</h2>
        </div>
        <div class="en-line">{name} · 00.LINK</div>
      </div>
      <div class="reveal">{film}</div>
    </div>
  </section>
{caps_html}
  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">Gallery</span>
          <h2 class="h2 reveal">{T("三张细节，<br>看清一副好眼镜", "Three details,<br>one good pair of glasses")}</h2>
        </div>
        <p class="lead reveal">{T(f"从正面到侧面，再到镜腿细节——{name}的每一面，都值得被看清。", f"Front, side, then the temple — every angle of the {name} deserves a closer look.")}</p>
      </div>
      <div class="detail-gallery{' tone' if p.get('tone') else ''}">{gallery3}</div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="spec-wrap">
        <div>
          <span class="eyebrow reveal">Specifications</span>
          <h2 class="h2 reveal" style="margin-top:16px;font-size:clamp(26px,3.4vw,40px)">{T("技术参数", "Specifications")}</h2>
          <p class="spec-note reveal">{T("* 语音翻译需连接网络使用，搭载 DeepSeek 与 GPT 双 AI 引擎。<br>* 镜片支持墨镜 / 蓝光 / 变色 / 近视定制，具体以客服确认为准。<br>* 实际重量与续航因配置和使用环境略有差异。", "* Voice translation requires a network connection and runs on both DeepSeek and GPT engines.<br>* Lenses made to order: sunglass / blue-light / photochromic / prescription — confirmed with our team.<br>* Actual weight and battery life vary slightly with configuration and conditions.")}</p>
        </div>
        <table class="spec-table reveal">{specs}</table>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head">
        <div>
          <span class="eyebrow reveal">More styles</span>
          <h2 class="h2 reveal" style="font-size:clamp(26px,3.4vw,40px)">{T("你可能也喜欢", "You may also like")}</h2>
        </div>
        <p class="lead reveal"><a class="link-u" href="index.html#series">{T("查看全部六款", "See all six")} {ICON_ARROW}</a></p>
      </div>
      <div class="related">{related}</div>
    </div>
  </section>
</main>
"""
        + footer()
        + modal()
    )


def build_sitemap():
    """双语 sitemap：每个页面同时列出中文与英文地址，并用 x-default 指向中文。"""
    slugs = ["index.html"] + [f'product-{p["id"]}.html' for p in PRODUCTS]
    rows = []
    for s in slugs:
        zh = f"{SITE_URL}/{s}"
        en = f"{SITE_URL}/en/{s}"
        alt = (
            f'    <xhtml:link rel="alternate" hreflang="zh-CN" href="{zh}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{zh}"/>\n'
        )
        home = s == "index.html"
        rows.append(f"  <url>\n    <loc>{zh}</loc>\n{alt}    <priority>{'1.0' if home else '0.8'}</priority>\n  </url>")
        rows.append(f"  <url>\n    <loc>{en}</loc>\n{alt}    <priority>{'0.9' if home else '0.7'}</priority>\n  </url>")
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows)
        + "\n</urlset>\n"
    )


def build_robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"


def main():
    global LANG, ASSET
    outdirs = {}
    for lang in ("zh", "en"):
        LANG = lang
        ASSET = "" if lang == "zh" else "../"
        outdir = os.path.join(ROOT, LANGS[lang]["dir"]) if LANGS[lang]["dir"] else ROOT
        os.makedirs(outdir, exist_ok=True)
        pages = {"index.html": build_index()}
        for p in PRODUCTS:
            pages[f'product-{p["id"]}.html'] = build_product(p)
        for fname, html in pages.items():
            path = os.path.join(outdir, fname)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            print("wrote", os.path.join(LANGS[lang]["dir"], fname), len(html))

    for name, content in (("sitemap.xml", build_sitemap()), ("robots.txt", build_robots())):
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote", name, len(content))


if __name__ == "__main__":
    main()
