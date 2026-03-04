# Caching Strategy for GitHub Pages

GitHub Pages does not natively support setting custom `Cache-Control` or `Expires` headers. To effectively cache static assets (like images, CSS, and fonts) and improve Core Web Vitals, you must integrate a CDN or migrate to a host that provides header controls.

## Option A: Cloudflare Setup (Recommended & Free)

Cloudflare sits in front of your GitHub Pages site and allows you to enforce caching rules without changing hosts.

### Steps:
1. **Create a Free Account:** Sign up at [Cloudflare](https://www.cloudflare.com/).
2. **Add Your Site:** Enter your domain (`techstackglobal.com` or `techstackglobal.github.io` if custom domain isn't fully set up yet; note that Cloudflare requires a root domain you own, so if using `.github.io`, you must use a custom domain first to proxy through Cloudflare).
3. **Update DNS Nameservers:** Follow Cloudflare’s instructions to change your domain registrar's nameservers to point to Cloudflare.
4. **Create Cache Rules (Page Rules):**
   Navigate to **Caching** > **Cache Rules** (or **Rules** > **Page Rules**) and create the following to cache assets for 1 month:

   **Rule 1 (Post Images):**
   - **If the URL matches:** `*techstackglobal.github.io/posts/images/*` (replace with custom domain when live)
   - **Then:** Set `Browser Cache TTL` to `1 month`

   **Rule 2 (Global Assets):**
   - **If the URL matches:** `*techstackglobal.github.io/assets/*`
   - **Then:** Set `Browser Cache TTL` to `1 month`

5. **Edge Cache (Optional but Recommended):** Under **Caching** > **Configuration**, set Edge Cache TTL to a long duration to keep assets cached globally on Cloudflare's servers.

---

## Option B: Migrate Host (Netlify or Vercel)

If you prefer not to use Cloudflare and want native control via configuration files (`_headers` or `vercel.json`), migrating to Netlify or Vercel is free and easy for static sites.

### Migration Guide for Netlify:
1. Create a free account on [Netlify](https://www.netlify.com/).
2. Click **Add new site** > **Import an existing project**.
3. Connect your GitHub account and select your `techstackglobal.github.io` repository.
4. Leave the build command blank (it's a static HTML site) and set the publish directory to `/`.
5. Create a `_headers` file in your repository root with the following to enable caching:
   ```text
   /assets/*
     Cache-Control: public, max-age=2592000
   /posts/images/*
     Cache-Control: public, max-age=2592000
   ```
6. Deploy and update your DNS to point to Netlify.

### Migration Guide for Vercel:
1. Create a free account on [Vercel](https://vercel.com/).
2. Click **Add New** > **Project** and import your GitHub repository.
3. Skip build commands and deploy.
4. Create a `vercel.json` file in your repository root with caching headers:
   ```json
   {
     "headers": [
       {
         "source": "/assets/(.*)",
         "headers": [
           { "key": "Cache-Control", "value": "public, max-age=2592000, immutable" }
         ]
       },
       {
         "source": "/posts/images/(.*)",
         "headers": [
           { "key": "Cache-Control", "value": "public, max-age=2592000, immutable" }
         ]
       }
     ]
   }
   ```
5. Commit the file and update your DNS.
