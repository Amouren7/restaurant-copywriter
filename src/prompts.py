"""
餐饮文案助手 - 提示词模板库
所有场景的提示词模板集中管理
"""

# ============================================================
# 品类列表
# ============================================================
CATEGORIES = [
    {"id": "fast_food",   "name": "快餐",   "icon": "🍚"},
    {"id": "hotpot",      "name": "火锅",   "icon": "🍲"},
    {"id": "milk_tea",    "name": "奶茶",   "icon": "🧋"},
    {"id": "bbq",         "name": "烧烤",   "icon": "🍖"},
    {"id": "noodle",      "name": "面馆",   "icon": "🍜"},
    {"id": "fish",        "name": "酸菜鱼", "icon": "🐟"},
    {"id": "dumpling",    "name": "饺子",   "icon": "🥟"},
    {"id": "malatang",    "name": "麻辣烫", "icon": "🫕"},
    {"id": "dessert",     "name": "甜品",   "icon": "🍰"},
    {"id": "bbq_skewer",  "name": "炸鸡",   "icon": "🍗"},
    {"id": "porridge",    "name": "粥店",   "icon": "🥣"},
    {"id": "other",       "name": "其他",   "icon": "🍽️"},
]

# ============================================================
# 场景注册表
# ============================================================
SCENES = {
    # ----- 朋友圈场景 -----
    "daily_special": {
        "name": "今日特价",
        "icon": "📢",
        "group": "朋友圈",
        "fields": [
            {"key": "dish",   "label": "特价菜名",     "placeholder": "如：红烧排骨盖饭", "required": True},
            {"key": "price",  "label": "现价",         "placeholder": "如：15元",         "required": False},
            {"key": "extra",  "label": "补充说明(选填)", "placeholder": "如：限50份/炖了3小时", "required": False},
        ],
    },
    "new_product": {
        "name": "新品推荐",
        "icon": "🆕",
        "group": "朋友圈",
        "fields": [
            {"key": "dish",   "label": "新菜名称",     "placeholder": "如：手切鲜牛肉",   "required": True},
            {"key": "extra",  "label": "菜品特点(选填)", "placeholder": "如：每天现切，涮8秒就能吃", "required": False},
        ],
    },
    "weather": {
        "name": "天气推荐",
        "icon": "🌧️",
        "group": "朋友圈",
        "fields": [
            {"key": "weather", "label": "今天天气",    "placeholder": "如：下雨/降温/大热天", "required": True},
            {"key": "dish",    "label": "推荐菜品",    "placeholder": "如：热汤面/火锅/冰粉",   "required": True},
        ],
    },
    "review": {
        "name": "好评晒单",
        "icon": "⭐",
        "group": "朋友圈",
        "fields": [
            {"key": "review", "label": "顾客评价",    "placeholder": "如：有客人说红烧肉是他吃过最好吃的", "required": True},
        ],
    },
    "holiday": {
        "name": "节日活动",
        "icon": "🎉",
        "group": "朋友圈",
        "fields": [
            {"key": "holiday",   "label": "什么节日",  "placeholder": "如：端午节/中秋/国庆",  "required": True},
            {"key": "promotion", "label": "活动内容",  "placeholder": "如：第二杯半价/满100减20", "required": True},
        ],
    },
    "daily_normal": {
        "name": "日常营业",
        "icon": "💬",
        "group": "朋友圈",
        "fields": [
            {"key": "highlight", "label": "今天亮点(选填)", "placeholder": "如：新到食材/延长营业/随便发", "required": False},
        ],
    },

    # ----- 外卖场景 -----
    "takeaway_title": {
        "name": "菜品标题",
        "icon": "📝",
        "group": "外卖",
        "fields": [
            {"key": "dish",      "label": "菜品名称",  "placeholder": "如：牛肉面",       "required": True},
            {"key": "features",  "label": "菜品特点",  "placeholder": "如：手工拉面+大块牛肉", "required": False},
            {"key": "price",     "label": "价格",      "placeholder": "如：28元",         "required": False},
        ],
    },
    "takeaway_desc": {
        "name": "菜品描述",
        "icon": "📖",
        "group": "外卖",
        "fields": [
            {"key": "dish",      "label": "菜品名称",  "placeholder": "如：红烧肉",       "required": True},
            {"key": "features",  "label": "食材/口味", "placeholder": "如：五花肉，红烧，甜口，300g", "required": True},
            {"key": "price",     "label": "价格",      "placeholder": "如：22元",         "required": False},
        ],
    },
    "takeaway_batch": {
        "name": "批量优化",
        "icon": "🏷️",
        "group": "外卖",
        "fields": [
            {"key": "dishes",    "label": "菜品列表",  "placeholder": "如：红烧肉22元/糖醋里脊20元/酸辣土豆丝12元", "required": True},
        ],
    },
}

# ============================================================
# 文案长度配置
# ============================================================
LENGTH_CONFIG = {
    "short": {
        "name": "简单",
        "desc": "精简直接，每条约30-60字",
        "consumes": 1,
        "instruction": "\n\n【长度要求】每条约30-60字，精简直接，一句话说清楚卖点即可。以这个长度为准，忽略前面的字数要求。",
    },
    "medium": {
        "name": "中等",
        "desc": "内容充实，每条约60-120字",
        "consumes": 2,
        "instruction": "\n\n【长度要求】每条约60-120字，内容充实，有场景和细节描写。以这个长度为准，忽略前面的字数要求。",
    },
    "long": {
        "name": "长篇",
        "desc": "详细完整，每条约120-250字",
        "consumes": 3,
        "instruction": "\n\n【长度要求】每条约120-250字，详细有画面感，包含完整的故事或场景叙述。以这个长度为准，忽略前面的字数要求。",
    },
}

# ============================================================
# 提示词模板（内部使用，用户不可见）
# ============================================================

SYSTEM_PROMPT = (
    "你是一位资深的餐饮行业营销文案专家，"
    "擅长写出接地气、有食欲感、能让顾客想来吃的营销文案。"
    "文风口语化，像老板本人在发朋友圈，不要书面语和广告腔。"
    "严禁编造不存在的食材、荣誉、资质等虚假信息。"
)

def build_prompt(category_name: str, scene_id: str, params: dict, length: str = "short") -> str:
    """
    根据品类、场景、用户参数、长度构造完整提示词
    """
    templates = {
        # ---- 朋友圈 ----
        "daily_special": f"""请为一家{category_name}店写5条朋友圈文案，突出今日特价。

今日特价菜：{params.get('dish', '')}
现价：{params.get('price', '未注明')}
补充信息：{params.get('extra', '无')}

要求：
1. 每条30-60字，口语化，像老板自己在发圈
2. 必须提到菜名
3. 有紧迫感（限时限购暗示）
4. 带2-4个emoji
5. 5条风格各异：实惠路线、品质路线、情感路线、场景路线、限时路线
直接输出5条，编号1-5，不要其他内容。""",

        "new_product": f"""请为一家{category_name}店写5条朋友圈文案，推新菜品。

新菜名：{params.get('dish', '')}
菜品特点：{params.get('extra', '暂无补充')}

要求：
1. 每条30-60字，突出"新"和"好吃"
2. 有食材/口感的画面感描写
3. 口语化，带emoji
4. 5条角度不同：食材、做法、口感、限量、场景
直接输出5条，编号1-5，不要其他内容。""",

        "weather": f"""请为一家{category_name}店写5条朋友圈文案，结合天气推荐菜品。

今天天气：{params.get('weather', '')}
推荐菜品：{params.get('dish', '')}

要求：
1. 每条30-60字，用天气引出"今天适合吃什么"
2. 有画面感和食欲感
3. 口语化，带emoji
4. 5条角度不同：天气感受、温度对比、场景联想、舒适感、互动引导
直接输出5条，编号1-5，不要其他内容。""",

        "review": f"""请为一家{category_name}店写5条朋友圈文案，晒顾客好评。

顾客评价：{params.get('review', '')}

要求：
1. 每条30-60字
2. 先引述/化用好评，再加一句老板的回应
3. 真诚不夸张
4. 带emoji
5. 结尾可邀请大家也来尝尝
直接输出5条，编号1-5，不要其他内容。""",

        "holiday": f"""请为一家{category_name}店写5条朋友圈文案，做节日促销。

节日：{params.get('holiday', '')}
活动内容：{params.get('promotion', '')}

要求：
1. 每条40-80字
2. 融入节日氛围元素
3. 活动信息清晰
4. 有紧迫感（限时/限量）
5. 口语化，带emoji
直接输出5条，编号1-5，不要其他内容。""",

        "daily_normal": f"""请为一家{category_name}店写5条日常朋友圈文案。

今日亮点：{params.get('highlight', '正常营业，没有特别的')}

要求：
1. 每条30-60字，轻松随意
2. 可以推招牌菜、分享日常、跟顾客互动
3. 口语化，像老板在跟朋友聊天
4. 带emoji
5. 5条风格各异
直接输出5条，编号1-5，不要其他内容。""",

        # ---- 外卖 ----
        "takeaway_title": f"""请为以下外卖菜品生成5个优化后的标题。

菜品：{params.get('dish', '')}
特点：{params.get('features', '无')}
价格：{params.get('price', '未注明')}

要求：
1. 每个标题15字以内
2. 包含卖点词（招牌/必点/超值/秘制/手工等）
3. 有吸引力，让人想点
直接输出5个标题，编号1-5。""",

        "takeaway_desc": f"""请为以下外卖菜品写3个版本的菜品描述。

菜品：{params.get('dish', '')}
食材/口味/份量：{params.get('features', '')}
价格：{params.get('price', '未注明')}

要求：
1. 每个版本50-80字
2. 包含：食材亮点+口感描写+适合场景+一句促成下单的话
3. 三个版本侧重不同：食材版、口感版、场景版
4. 末尾附上推荐标签（3-5个）
直接输出3个版本，标注版本名。""",

        "takeaway_batch": f"""请为以下外卖菜品逐个优化标题和描述。

菜品列表：
{params.get('dishes', '')}

要求：
1. 每个菜品输出：优化后的标题（15字内）+ 描述（50-80字）+ 标签（3个）
2. 标题含卖点词
3. 描述有食欲感
4. 按菜品逐个输出，格式：**菜名** / 标题：xxx / 描述：xxx / 标签：xxx
直接输出，不要解释。""",
    }

    prompt = templates.get(scene_id, "请为这家餐饮店写5条营销文案。")
    length_cfg = LENGTH_CONFIG.get(length, LENGTH_CONFIG["short"])
    prompt += length_cfg["instruction"]
    return prompt
