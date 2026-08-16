import os
import base64
import requests

DEVICON_BASE_URL = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons"

# Local Icons Directory
LOCAL_ICONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "icons"))

_ICON_CACHE = {}

def get_as_base64(path_or_url: str, headers: dict = None) -> str:
    """Fetches icon/image from local file or URL, converts to Base64 data URI, and caches it."""
    if not path_or_url:
        return ""
        
    if path_or_url in _ICON_CACHE:
        return _ICON_CACHE[path_or_url]

    # 1. Check if it's a local file in GitFlex/icons/ or absolute path
    local_candidate = path_or_url
    if not os.path.isabs(local_candidate):
        local_candidate = os.path.join(LOCAL_ICONS_DIR, path_or_url)

    if os.path.isfile(local_candidate):
        try:
            with open(local_candidate, "rb") as f:
                content = f.read()
            ext = os.path.splitext(local_candidate)[1].lower()
            if ext == ".svg":
                ct = "image/svg+xml"
            elif ext == ".png":
                ct = "image/png"
            elif ext in [".jpg", ".jpeg"]:
                ct = "image/jpeg"
            else:
                ct = "image/svg+xml"
            encoded = base64.b64encode(content).decode("utf-8")
            data_uri = f"data:{ct};base64,{encoded}"
            _ICON_CACHE[path_or_url] = data_uri
            return data_uri
        except Exception as e:
            print(f"Error reading local icon ({local_candidate}): {e}")

    # 2. Remote URL fallback (Devicon, etc.)
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        try:
            response = requests.get(path_or_url, headers=headers, timeout=10)
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "")
            if not content_type:
                if path_or_url.endswith(".svg"):
                    content_type = "image/svg+xml"
                elif path_or_url.endswith(".png"):
                    content_type = "image/png"
                else:
                    content_type = "image/jpeg"
            else:
                if ";" in content_type:
                    content_type = content_type.split(";")[0]
            
            encoded = base64.b64encode(response.content).decode("utf-8")
            data_uri = f"data:{content_type};base64,{encoded}"
            _ICON_CACHE[path_or_url] = data_uri
            return data_uri
        except Exception as e:
            print(f"Warning: Could not fetch/encode remote icon ({path_or_url}): {e}")

    return path_or_url

def list_local_icons() -> list:
    """Returns list of available local icon names from GitFlex/icons/."""
    if not os.path.exists(LOCAL_ICONS_DIR):
        return []
    valid_exts = [".svg", ".png", ".jpg", ".jpeg"]
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(LOCAL_ICONS_DIR)
        if any(f.lower().endswith(ext) for ext in valid_exts)
    ]

def resolve_icon(tech_name: str) -> tuple:
    """
    Resolves tech name to (Display Name, Path/URL).
    Checks local GitFlex/icons/ directory first, then fallback to Devicon.
    """
    clean_name = tech_name.strip().lower()
    
    # Check local icons folder first
    if os.path.exists(LOCAL_ICONS_DIR):
        for ext in [".svg", ".png", ".jpg", ".jpeg"]:
            local_file = f"{clean_name}{ext}"
            local_path = os.path.join(LOCAL_ICONS_DIR, local_file)
            if os.path.isfile(local_path):
                return (tech_name.strip().capitalize(), local_file)

    # Fallback to Devicon URL
    devicon_url = f"{DEVICON_BASE_URL}/{clean_name}/{clean_name}-original.svg"
    return (tech_name.strip().capitalize(), devicon_url)
