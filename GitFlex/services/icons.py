import os
import base64
import requests

DEVICON_BASE_URL = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons"

# Local Icons Directory
LOCAL_ICONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "icons"))

_ICON_CACHE = {}

# Built-in verified catalog for instant resolution & custom name mapping
BUILTIN_ICON_CATALOG = {
    "python": ("Python", f"{DEVICON_BASE_URL}/python/python-original.svg"),
    "javascript": ("JavaScript", f"{DEVICON_BASE_URL}/javascript/javascript-original.svg"),
    "typescript": ("TypeScript", f"{DEVICON_BASE_URL}/typescript/typescript-original.svg"),
    "csharp": ("C#", f"{DEVICON_BASE_URL}/csharp/csharp-original.svg"),
    "dotnet": (".NET", f"{DEVICON_BASE_URL}/dot-net/dot-net-original.svg"),
    ".net": (".NET", f"{DEVICON_BASE_URL}/dot-net/dot-net-original.svg"),
    "playwright": ("Playwright", f"{DEVICON_BASE_URL}/playwright/playwright-original.svg"),
    "nodejs": ("Node.js", f"{DEVICON_BASE_URL}/nodejs/nodejs-original.svg"),
    "node": ("Node.js", f"{DEVICON_BASE_URL}/nodejs/nodejs-original.svg"),
    "docker": ("Docker", f"{DEVICON_BASE_URL}/docker/docker-original.svg"),
    "git": ("Git", f"{DEVICON_BASE_URL}/git/git-original.svg"),
    "react": ("React", f"{DEVICON_BASE_URL}/react/react-original.svg"),
    "vue": ("Vue.js", f"{DEVICON_BASE_URL}/vuejs/vuejs-original.svg"),
    "angular": ("Angular", f"{DEVICON_BASE_URL}/angularjs/angularjs-original.svg"),
    "go": ("Go", f"{DEVICON_BASE_URL}/go/go-original.svg"),
    "golang": ("Go", f"{DEVICON_BASE_URL}/go/go-original.svg"),
    "rust": ("Rust", f"{DEVICON_BASE_URL}/rust/rust-plain.svg"),
    "cpp": ("C++", f"{DEVICON_BASE_URL}/cplusplus/cplusplus-original.svg"),
    "c++": ("C++", f"{DEVICON_BASE_URL}/cplusplus/cplusplus-original.svg"),
    "java": ("Java", f"{DEVICON_BASE_URL}/java/java-original.svg"),
    "kotlin": ("Kotlin", f"{DEVICON_BASE_URL}/kotlin/kotlin-original.svg"),
    "swift": ("Swift", f"{DEVICON_BASE_URL}/swift/swift-original.svg"),
    "php": ("PHP", f"{DEVICON_BASE_URL}/php/php-original.svg"),
    "html": ("HTML5", f"{DEVICON_BASE_URL}/html5/html5-original.svg"),
    "css": ("CSS3", f"{DEVICON_BASE_URL}/css3/css3-original.svg"),
    "tailwind": ("Tailwind CSS", f"{DEVICON_BASE_URL}/tailwindcss/tailwindcss-original.svg"),
    "mongodb": ("MongoDB", f"{DEVICON_BASE_URL}/mongodb/mongodb-original.svg"),
    "postgresql": ("PostgreSQL", f"{DEVICON_BASE_URL}/postgresql/postgresql-original.svg"),
    "postgres": ("PostgreSQL", f"{DEVICON_BASE_URL}/postgresql/postgresql-original.svg"),
    "mysql": ("MySQL", f"{DEVICON_BASE_URL}/mysql/mysql-original.svg"),
    "redis": ("Redis", f"{DEVICON_BASE_URL}/redis/redis-original.svg"),
    "kubernetes": ("Kubernetes", f"{DEVICON_BASE_URL}/kubernetes/kubernetes-plain.svg"),
    "k8s": ("Kubernetes", f"{DEVICON_BASE_URL}/kubernetes/kubernetes-plain.svg"),
    "linux": ("Linux", f"{DEVICON_BASE_URL}/linux/linux-original.svg"),
    "aws": ("AWS", f"{DEVICON_BASE_URL}/amazonwebservices/amazonwebservices-original-wordmark.svg"),
    "gcp": ("Google Cloud", f"{DEVICON_BASE_URL}/googlecloud/googlecloud-original.svg"),
    "azure": ("Azure", f"{DEVICON_BASE_URL}/azure/azure-original.svg"),
    "firebase": ("Firebase", f"{DEVICON_BASE_URL}/firebase/firebase-plain.svg"),
    "graphql": ("GraphQL", f"{DEVICON_BASE_URL}/graphql/graphql-plain.svg"),
    "nextjs": ("Next.js", f"{DEVICON_BASE_URL}/nextjs/nextjs-original.svg"),
    "next": ("Next.js", f"{DEVICON_BASE_URL}/nextjs/nextjs-original.svg"),
}

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

    # 2. Remote URL fallback
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
    Checks:
      1. Local GitFlex/icons/ directory
      2. Built-in verified catalog (C#, .NET, Node.js, Next.js, etc.)
      3. Dynamic Devicon URL fallback
    """
    clean_name = tech_name.strip().lower()
    
    # 1. Check local icons folder first
    if os.path.exists(LOCAL_ICONS_DIR):
        for ext in [".svg", ".png", ".jpg", ".jpeg"]:
            local_file = f"{clean_name}{ext}"
            local_path = os.path.join(LOCAL_ICONS_DIR, local_file)
            if os.path.isfile(local_path):
                return (tech_name.strip(), local_file)

    # 2. Check Built-in verified catalog
    if clean_name in BUILTIN_ICON_CATALOG:
        return BUILTIN_ICON_CATALOG[clean_name]

    # 3. Dynamic Devicon URL fallback
    devicon_url = f"{DEVICON_BASE_URL}/{clean_name}/{clean_name}-original.svg"
    return (tech_name.strip().capitalize(), devicon_url)
