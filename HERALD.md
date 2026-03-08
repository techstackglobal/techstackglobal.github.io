# 🌉 Connecting Claude Chat to TechStack Global (Herald)

This guide helps you link your **Claude Browser Chat** (Claude.ai) to this local repository, allowing you to manage your blog from anywhere.

## 🚀 Setup Steps

### 1. Get an ngrok Auth Token
Herald uses `ngrok` to create a secure tunnel. You need an auth token from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).

### 2. Configure Herald
Open `.herald/herald.yaml` and update the `tunnel` section:
```yaml
tunnel:
  enabled: true
  authtoken: "YOUR_NGROK_TOKEN_HERE"
```

### 3. Start the Bridge
Run the following command in this terminal:
```bash
.herald/herald.exe serve -config .herald/herald.yaml
```
*Note: On first start, it will display a **Client Secret**. Copy it immediately!*

### 4. Link Claude.ai
1. Go to **Claude.ai** → **Settings** (bottom left) → **Custom Connectors**.
2. Click **Add Connector**.
3. Use the **ngrok URL** displayed in your terminal (e.g., `https://xxxx.ngrok-free.app/mcp`).
4. Paste the **Client ID** (`herald-claude-chat`) and the **Client Secret** you just copied.
5. Authenticate and Approve.

## 🛠️ Remote Commands You Can Now Use
Once connected, you can tell Claude in your browser to:
- *"SEO Audit the site"*
- *"Draft a new guide for 2026 gaming monitors"*
- *"Check for broken links"*
- *"Update the sitemap"*

## 🛡️ Security Guardrails
- **Project Isolation**: Herald is configured to ONLY access this `b2b_blog` folder.
- **Tool Restrictions**: Only safe tools (`Read`, `Write`, `Edit`, `Bash`) are allowed via the bridge.
- **Git Sandboxing**: Every remote task starts on its own `herald/` branch for safety.
