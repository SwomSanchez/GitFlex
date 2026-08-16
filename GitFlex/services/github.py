from collections import Counter
from datetime import datetime, timezone
import requests

class GitHubProvider:
    """GitHub REST API data provider."""
    
    def __init__(self, username: str, token: str = None):
        self.username = username
        self.token = token
        self.headers = {"Authorization": f"token {token}"} if token else {}
        self.base_url = "https://api.github.com"

    def fetch_user_data(self) -> dict:
        """Fetches user profile information from GitHub."""
        url = f"{self.base_url}/users/{self.username}"
        r = requests.get(url, headers=self.headers, timeout=10)
        r.raise_for_status()
        return r.json()

    def fetch_repositories(self) -> list:
        """Fetches all public repositories of the user."""
        repos = []
        page = 1
        while True:
            url = f"{self.base_url}/users/{self.username}/repos"
            params = {"per_page": 100, "page": page, "type": "owner"}
            r = requests.get(url, params=params, headers=self.headers, timeout=10)
            r.raise_for_status()
            batch = r.json()
            if not batch:
                break
            repos.extend(batch)
            page += 1
            if page > 10:  # Safety limit
                break
        return repos

    def calculate_stats(self, user: dict, repos: list) -> dict:
        """Calculates profile metrics, language percentages, and recent active focus."""
        total_stars = sum(r.get("stargazers_count", 0) for r in repos)
        total_forks = sum(r.get("forks_count", 0) for r in repos)
        public_repos = user.get("public_repos", len(repos))
        followers = user.get("followers", 0)

        # Most used languages
        lang_counter = Counter()
        for repo in repos:
            lang = repo.get("language")
            if lang:
                lang_counter[lang] += 1
        
        total_lang_count = sum(lang_counter.values()) or 1
        top_languages = [
            {"name": lang, "percentage": (count / total_lang_count) * 100}
            for lang, count in lang_counter.most_common(5)
        ]

        # Recent Focus active repository
        own_repos = [r for r in repos if not r.get("fork")]
        if not own_repos:
            own_repos = repos
        
        recent_focus = None
        if own_repos:
            own_repos.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
            top_repo = own_repos[0]
            recent_focus = {
                "name": top_repo.get("name", ""),
                "language": top_repo.get("language", "Unknown"),
                "updated_at": top_repo.get("updated_at", ""),
                "relative_time": self._format_relative_time(top_repo.get("updated_at", "")),
                "url": top_repo.get("html_url", f"https://github.com/{self.username}/{top_repo.get('name', '')}"),
            }

        return {
            "total_stars": total_stars,
            "total_forks": total_forks,
            "public_repos": public_repos,
            "followers": followers,
            "top_languages": top_languages,
            "recent_focus": recent_focus,
        }

    @staticmethod
    def _format_relative_time(date_str: str) -> str:
        """Formats ISO date string to human-friendly relative time (e.g., '2h ago')."""
        if not date_str:
            return ""
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
            diff = now - dt
            seconds = diff.total_seconds()
            if seconds < 60:
                return "Just now"
            minutes = seconds / 60
            if minutes < 60:
                return f"{int(minutes)}m ago"
            hours = minutes / 60
            if hours < 24:
                return f"{int(hours)}h ago"
            days = hours / 24
            if days < 30:
                return f"{int(days)}d ago"
            return dt.strftime("%b %d, %Y")
        except Exception:
            return date_str[:10]
