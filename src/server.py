"""
餐饮文案助手 - Flask后端
"""
import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI

from prompts import CATEGORIES, SCENES, SYSTEM_PROMPT, build_prompt, LENGTH_CONFIG

# ============================================================
# 配置
# ============================================================
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")

app = Flask(__name__, static_folder=".", static_url_path="")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


# ============================================================
# 页面路由
# ============================================================
@app.route("/")
def index():
    return send_from_directory(".", "index.html")


# ============================================================
# API路由
# ============================================================

@app.route("/api/categories", methods=["GET"])
def get_categories():
    """返回品类列表"""
    return jsonify({"success": True, "categories": CATEGORIES})


@app.route("/api/scenes", methods=["GET"])
def get_scenes():
    """返回场景列表（不含模板，只给前端展示）"""
    scene_list = []
    for sid, s in SCENES.items():
        scene_list.append({
            "id": sid,
            "name": s["name"],
            "icon": s["icon"],
            "group": s["group"],
            "fields": s["fields"],
        })
    return jsonify({"success": True, "scenes": scene_list})


@app.route("/api/lengths", methods=["GET"])
def get_lengths():
    """返回文案长度选项"""
    return jsonify({"success": True, "lengths": LENGTH_CONFIG})


@app.route("/api/generate", methods=["POST"])
def generate():
    """核心接口：生成文案"""
    data = request.get_json(force=True)

    category_id = data.get("category", "")
    scene_id = data.get("scene", "")
    length = data.get("length", "short")
    params = data.get("params", {})

    # 校验
    if not category_id or not scene_id:
        return jsonify({"success": False, "error": "请选择品类和场景"}), 400

    if scene_id not in SCENES:
        return jsonify({"success": False, "error": "无效的场景"}), 400

    # 查找品类名
    category_name = "餐饮"
    for c in CATEGORIES:
        if c["id"] == category_id:
            category_name = c["name"]
            break

    # 校验必填字段
    scene = SCENES[scene_id]
    for field in scene["fields"]:
        if field["required"] and not params.get(field["key"], "").strip():
            return jsonify({"success": False, "error": f"请填写{field['label']}"}), 400

    # 构造提示词
    prompt = build_prompt(category_name, scene_id, params, length)

    # 调用DeepSeek
    try:
        response = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=1000,
        )
        content = response.choices[0].message.content.strip()
    except Exception as e:
        import traceback
        print(f"[ERROR] AI API call failed: {e}")
        print(traceback.format_exc())
        return jsonify({"success": False, "error": f"AI服务暂时不可用，请稍后重试"}), 502

    # 解析文案列表（按编号分割）
    copies = parse_copies(content)

    if not copies:
        return jsonify({"success": False, "error": "生成失败，请重试"}), 500

    return jsonify({"success": True, "copies": copies})


def parse_copies(text: str) -> list:
    """
    将AI返回的文本按编号/名称拆分为列表
    支持的格式：
      1. xxx  2. xxx  (编号)
      **食材版** ... **口感版** ...  (版本名称)
      文案1：xxx  文案2：xxx  (中文标签)
    """
    import re
    # 尝试多种分割方式
    # 方式1: 编号开头 (1.  2、 3))
    parts = re.split(r'\n\s*\d+[\.\、\)]\s*', '\n' + text)
    if len(parts) > 2:
        return _clean_parts(parts)

    # 方式2: **名称** 格式 (如 **食材版**)
    parts = re.split(r'\n\s*\*{2}[^*]+\*{2}\s*', '\n' + text)
    if len(parts) > 2:
        return _clean_parts(parts)

    # 方式3: "文案X：" 格式
    parts = re.split(r'\n\s*(?:文案|版本|方案)\s*\d*\s*[：:]\s*', '\n' + text)
    if len(parts) > 2:
        return _clean_parts(parts)

    # 方式4: 整体作为一条
    cleaned = text.strip().replace('\n', ' ')
    if cleaned and len(cleaned) > 10:
        return [{"id": 1, "text": cleaned}]
    return []


def _clean_parts(parts: list) -> list:
    """清理分割后的片段并编号"""
    result = []
    for part in parts:
        part = part.strip()
        if part and len(part) > 5:
            part = part.replace('\n', ' ').strip()
            result.append({"id": len(result) + 1, "text": part})
    return result


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# ============================================================
# 启动
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
