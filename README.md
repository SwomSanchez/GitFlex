<p align="center">
  <img src="build/assets/profile.svg" alt="GitFlex Hero" width="850" />
</p>

<h1 align="center">⚡ GitFlex</h1>

<p align="center">
  <b>Next-Gen Modular Animated SVG Profile & CV Engine for GitHub</b><br>
  <i>Say goodbye to static, boring GitHub profile READMEs. Build a live-animated, slot-machine counter, neon-powered, and 100% self-hosted developer showcase in seconds.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
  <img src="https://img.shields.io/badge/Aesthetics-Cyberpunk%20Nebula-7f5af0?style=for-the-badge" alt="Cyberpunk Nebula" />
  <img src="https://img.shields.io/badge/Dependencies-Zero%20External%20Runtime-2cb67d?style=for-the-badge" alt="Zero Dependencies" />
</p>

---

## ✨ Features That Stand Out

- 🌌 **Cyberpunk Glow & Animated Avatar Ring**: Shimmering metallic headline gradients, rotating neon avatar border, and floating ambient space particles.
- 🎰 **Rolling Slot-Machine Counters**: Real-time roll-in keyframe animations for Repositories, Total Stars, Followers, and Forks.
- 🟢 **Live Current Focus Radar**: Live pulsing green radar dot automatically tracking and highlighting your most recently active repository.
- 📊 **Vibrant Language Breakdown**: Dynamic percentage bars with neon gradients reflecting your real codebase analytics.
- 🛠️ **Dynamic Tech Matrix**: Interactive hover-glow chip grid powered by local verified icons or custom additions in `GitFlex/icons/`.
- 📦 **Clean Isolated Build Architecture**: Output files are generated strictly inside `build/`, keeping root workspaces 100% pristine.
- 🤖 **Zero-Dependency GitHub Actions**: Scheduled daily autonomous workflow running directly on GitHub's infrastructure—no external servers, no broken links.
- 🚫 **Zero Mock / Zero Fallback Policy**: Powered 100% by genuine GitHub API telemetry.

---

## 🚀 Quick Start in 3 Steps

### 1. Clone the Engine
```bash
git clone https://github.com/SwomSanchez/GitFlex.git
cd GitFlex
```

### 2. Install Minimal Requirements
```bash
pip install -r requirements.txt
```

### 3. Launch the Setup Studio 🎯
```bash
python main.py
```

The interactive terminal wizard will guide you through:
1. Entering your GitHub username & target repository,
2. Customizing your display name & bio subtitle,
3. Selecting your preferred neon palette (*Cyberpunk Nebula, Midnight Sapphire, Sunset Crimson, Matrix Emerald*),
4. Choosing your tech stack chips from the live catalog,
5. **One-Click Autonomous Deployment:** Automatically pushes the generated `build/` files directly to your GitHub profile repository!

> 💡 **Live Preview:** Run `python main.py preview` anytime to inspect your generated SVG directly in your default browser.

---

## 🎨 Adding Custom Tech Stack Icons

GitFlex automatically detects custom icons! Simply drop any `.svg`, `.png`, or `.jpg` file into the `GitFlex/icons/` directory:

```
GitFlex/icons/
├── unreal.svg
├── blender.png
└── godot.svg
```

When you launch `python main.py`, GitFlex will detect and list them in your setup wizard automatically.

---

## 🧩 Modular (Plug-and-Play) Architecture

```
GitFlex/
├── GitFlex/                     # Core Engine Package
│   ├── engine/                  # SVG Renderer & Autonomous Script Synthesizer
│   ├── modules/                 # Plug-and-Play Widgets & Themes
│   │   ├── widgets/             # Header, Stats, Languages, Focus, TechStack, Particles
│   │   └── themes/              # Google Outfit Font, Palettes, CSS Keyframes
│   ├── services/                # GitHub API, Icon Resolvers & Automated GitOps
│   ├── icons/                   # Custom Developer Icons Directory
│   └── ui/                      # Rich Terminal Wizard & Cyberpunk Banner
├── build/                       # Isolated Output (Pushed to your Profile Repo)
│   ├── assets/profile.svg       # Generated Profile SVG
│   ├── generate_profile.py      # Standalone GitHub Actions Script
│   ├── .github/workflows/       # Daily Auto-Sync Action
│   └── README.md                # Profile Showcase README
├── main.py                      # One-Click CLI Entry Point
└── requirements.txt             # Minimal Setup Dependencies
```

---

## 🛡️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  Crafted with ❤️ by <b><a href="https://github.com/SwomSanchez">SwomSanchez</a></b>
</p>
