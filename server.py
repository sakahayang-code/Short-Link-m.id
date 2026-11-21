#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import urllib.parse

PORT = 3000
DIRECTORY = "/home/antigravity"
DATA_FILE = os.path.join(DIRECTORY, "links.json")

# Initialize default database
default_links = {
    "custom": {
        "alias": "custom",
        "long_url": "https://shopee.co.id/toko-kopi-nusantara/promo-spesial-diskon-50",
        "clicks": 148,
        "created_at": "2026-11-21T12:00:00Z"
    },
    "promo": {
        "alias": "promo",
        "long_url": "https://google.com",
        "clicks": 42,
        "created_at": "2026-11-21T12:00:00Z"
    },
    "wa-pesan": {
        "alias": "wa-pesan",
        "long_url": "https://wa.me/628123456789",
        "clicks": 12480,
        "created_at": "2026-11-21T12:00:00Z"
    },
    "toko-shopee": {
        "alias": "toko-shopee",
        "long_url": "https://shopee.co.id",
        "clicks": 3216,
        "created_at": "2026-11-21T12:00:00Z"
    },
    "survey-2026": {
        "alias": "survey-2026",
        "long_url": "https://forms.gle/sample",
        "clicks": 1904,
        "created_at": "2026-11-21T12:00:00Z"
    }
}

def load_links():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return default_links.copy()
    else:
        save_links(default_links)
        return default_links.copy()

def save_links(links):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(links, f, indent=2)
    except Exception as e:
        print("Error saving links:", e)

class ShortLinkHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/shorten":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body)
                long_url = data.get("long_url", "").strip()
                alias = data.get("alias", "").strip().lower()
                
                # Sanitize alias
                alias = urllib.parse.unquote(alias)
                alias = alias.replace("https://m.id/", "").replace("m.id/", "")
                alias = "".join(c for c in alias if c.isalnum() or c in "-_")
                if not alias:
                    alias = "custom"

                # Ensure URL has protocol
                if not long_url.startswith("http://") and not long_url.startswith("https://"):
                    long_url = "https://" + long_url

                links = load_links()
                links[alias] = {
                    "alias": alias,
                    "long_url": long_url,
                    "clicks": links.get(alias, {}).get("clicks", 0),
                    "created_at": "2026-11-21"
                }
                save_links(links)

                host = self.headers.get("Host", f"localhost:{PORT}")
                response_data = {
                    "success": True,
                    "alias": alias,
                    "long_url": long_url,
                    "short_url": f"https://m.id/{alias}",
                    "local_url": f"http://{host}/{alias}",
                    "clicks": links[alias]["clicks"]
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return
        
        elif parsed.path == "/api/click":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body)
                alias = data.get("alias", "").strip().lower()
                links = load_links()
                if alias in links:
                    links[alias]["clicks"] = links[alias].get("clicks", 0) + 1
                    save_links(links)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "clicks": links[alias]["clicks"]}).encode("utf-8"))
                    return
            except Exception:
                pass
            self.send_response(404)
            self.end_headers()
            return

        super().do_POST()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_HEAD(self):
        self.handle_get_or_head(is_head=True)

    def do_GET(self):
        self.handle_get_or_head(is_head=False)

    def handle_get_or_head(self, is_head=False):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.lstrip("/")

        # API check
        if path == "api/links":
            links = load_links()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            if not is_head:
                self.wfile.write(json.dumps(links).encode("utf-8"))
            return

        # Check root or static asset files
        if path == "" or path == "index.html" or path.startswith("assets/") or path == "favicon.svg":
            if is_head:
                super().do_HEAD()
            else:
                super().do_GET()
            return

        # Check if the requested path is a shortened alias
        alias = path.lower()
        links = load_links()
        if alias in links:
            # Increment click count
            links[alias]["clicks"] = links[alias].get("clicks", 0) + 1
            save_links(links)

            target = links[alias]["long_url"]
            print(f"[REDIRECT] Short link m.id/{alias} accessed! Redirecting to -> {target}")

            # Send 302 Redirect to destination
            self.send_response(302)
            self.send_header("Location", target)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()
            return

        # Check if another static file exists on disk
        local_file_path = os.path.join(DIRECTORY, path)
        if os.path.isfile(local_file_path):
            if is_head:
                super().do_HEAD()
            else:
                super().do_GET()
            return
        
        # If alias not found, redirect to home with info
        self.send_response(302)
        self.send_header("Location", "/?not_found=" + urllib.parse.quote(alias))
        self.end_headers()

if __name__ == "__main__":
    load_links()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ShortLinkHandler) as httpd:
        print(f"Serving m.id with live redirect engine on port {PORT}...")
        httpd.serve_forever()
