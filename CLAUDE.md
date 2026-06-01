# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

餐饮文案助手 (Restaurant Copywriter Assistant) — an online copywriting tool for Chinese restaurant owners. Select a category (12 cuisines) + scene (9 scenarios) → AI generates 5 marketing copies. Target: small restaurant owners who struggle with social media.

Tech: Python Flask backend + DeepSeek API (via OpenAI SDK) + single-file HTML/JS frontend (Tailwind CSS). Deployed on Railway via Gunicorn.

## Commands

### Local Development

```bash
# Install dependencies
pip install -r src/requirements.txt

# Set environment variables (Windows PowerShell)
$env:DEEPSEEK_API_KEY="your-key"
$env:DEEPSEEK_BASE_URL="https://api.deepseek.com"
$env:DEEPSEEK_MODEL="deepseek-v4-flash"

# Start Flask dev server
cd src && python server.py
# Opens at http://localhost:5000
```

Or double-click `src/run_local.bat` (edit the API key first).

### Testing

```bash
# End-to-end test against running server (requires server up)
cd src && python test_api.py

# Direct DeepSeek API test (bypasses Flask)
cd src && python debug_direct.py

# Flask test client test (no HTTP, tests logic directly)
cd src && python debug_server.py
```

### Production Deployment

Deployed via Railway. Push to GitHub, Railway auto-deploys. See `docs/05-部署指南.md`.

```bash
# Procfile entry (used by Railway)
web: gunicorn server:app --chdir src
```

## Architecture

### Source Files (3 core files in `src/`)

| File | Role |
|------|------|
| `server.py` | Flask app — routes, request handling, error handling, startup |
| `prompts.py` | Prompt template registry — categories, scenes, `build_prompt()` factory |
| `index.html` | Single-page frontend — HTML + Tailwind CSS + Vanilla JS |

### Data Flow

```
User clicks category/scene → fills form → POST /api/generate
  → server.py validates → prompts.py builds prompt → DeepSeek API (OpenAI SDK)
  → parse_copies() splits response → returns JSON {copies: [...]}
  → index.html renders results → user taps "复制" (clipboard)
```

### Backend (`server.py`)

- Flask app serves `index.html` statically at `/`
- 5 API routes: `GET /` (page), `GET /api/categories` (12 cuisines), `GET /api/scenes` (9 scenarios), `POST /api/generate` (core), `GET /api/health`
- `parse_copies()` — regex-based text splitter handling numbered lists / bold headers / Chinese labels
- Environment variables: `DEEPSEEK_API_KEY` (required), `DEEPSEEK_BASE_URL`, `DEEPSEEK_MODEL`, `PORT`

### Prompt System (`prompts.py`)

- **`CATEGORIES`**: 12 cuisine items with id/name/icon (e.g. `fast_food`/快餐/🍚)
- **`SCENES`**: 9 scenarios split into two groups:
  - 朋友圈 (Moments): `daily_special`, `new_product`, `weather`, `review`, `holiday`, `daily_normal`
  - 外卖 (Takeaway): `takeaway_title`, `takeaway_desc`, `takeaway_batch`
- Each scene has: `name`, `icon`, `group`, `fields` (user input definitions with validation), and a corresponding template in `build_prompt()`
- `build_prompt(category_name, scene_id, params)` → returns a Chinese-language prompt string
- Templates are f-string based, each targeting 30-80 char copies with emoji and conversational tone

### Frontend (`index.html`)

- Single-file SPA, no build step, Tailwind via CDN
- Mobile-first (viewport, tap highlight, scroll animations)
- Step-based wizard: 品类 → 场景 → 补充信息 → 生成 → 显示结果
- **State**: plain JS object tracking `categories`, `scenes`, `selectedCategory`, `selectedScene`, `loading`, `results`
- **Free tier**: localStorage-based daily limit of 5 generations (`checkUsageLimit()` / `incrementUsage()`)
- Copy-to-clipboard via `navigator.clipboard` with fallback
- Results animate in with staggered `fadeUp` CSS animations

### Key Design Decisions

- **No router/build system**: Serves static HTML from Flask — keeps deployment simple (one Procfile)
- **Prompt templates in Python, not DB**: Easy to iterate and version-controlled. Adding a scene = add to `SCENES` dict + add template in `build_prompt()`
- **Client-side usage limit**: localStorage-based (not server-side) — acceptable for MVP, upgrade to server-side auth when monetizing

## Common Development Tasks

**Add a new scene (e.g. "抖音文案")**:
1. Add entry to `SCENES` dict in `prompts.py` with id, name, icon, group, fields
2. Add corresponding f-string template in `build_prompt()` with the same scene_id
3. No frontend changes needed — index.html iterates `GET /api/scenes` response

**Add a new category (e.g. "日料")**:
1. Add object to `CATEGORIES` list in `prompts.py`
2. No other changes needed

**Switch AI provider**:
1. Change `DEEPSEEK_BASE_URL` env var (e.g. to Qwen: `https://dashscope.aliyuncs.com/compatible-mode/v1`)
2. Update model name if needed via `DEEPSEEK_MODEL` env var
3. The OpenAI SDK is provider-agnostic with compatible endpoints

**Update copy quality**: Edit the SYSTEM_PROMPT or individual scene templates in `prompts.py`
