# ⚡ GitFlex: Next-Gen Animated Profile & CV Engine for GitHub

<p align="center">
  <b>Forget static and boring GitHub profile READMEs. Build a plug-and-play, live-animated, slot-machine counter, neon-powered, and 100% customizable developer showcase with GitFlex!</b>
</p>

---

## 🚀 Quick Start (Super Easy!)

### 1. Clone the Repository
```bash
git clone https://github.com/SwomSanchez/GitFlex.git
cd GitFlex
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Setup Wizard! 🎯
```bash
python main.py
```

The interactive terminal wizard will guide you through:
1. Entering your GitHub username & target profile repository URL,
2. Setting your name & bio subtitle,
3. Choosing your theme (*Cyberpunk Nebula, Midnight Sapphire, Sunset Crimson, Matrix Emerald*),
4. Selecting your tech stack chips,
5. **Autonomous Deployment:** All assets are generated strictly inside `build/` and GitFlex will offer to automatically push directly to your profile repository!

> 💡 **Preview:** You can also run `python main.py preview` anytime to view your generated SVG in the browser.

---

## 🎨 Adding Custom Tech Stack Icons

Drop any `.svg`, `.png`, or `.jpg` icon files into `GitFlex/icons/`!
When you run `python main.py`, GitFlex will automatically detect your local icons and include them in your interactive Tech Stack chip matrix.

---

## 🧩 Plug-and-Play Architecture

GitFlex is built with a highly modular Python architecture inside `GitFlex/`:
- ⚙️ **`GitFlex/engine/`**: Core SVG renderer and standalone zero-dependency script synthesizer.
- 🧩 **`GitFlex/modules/`**: Isolated visual widgets (`stats`, `header`, `languages`, `current_focus`, `tech_stack`, `particles`) and theme definitions.
- 📁 **`GitFlex/icons/`**: Your custom tech icons directory for automatic detection.
- 🌐 **`GitFlex/services/`**: External services (GitHub API, Devicon resolver, automated GitOps deployer).
- 💻 **`GitFlex/ui/`**: Interactive Rich terminal CLI wizard & branding banner.

---

## 📁 Output Directory (`build/`)

All generated files are isolated inside `build/`:
```
build/
├── generate_profile.py
├── README.md
├── assets/
│   └── profile.svg
└── .github/
    └── workflows/
        └── generate_profile.yml
```

---

## 👨‍💻 Author
Created with ❤️ by **SwomSanchez**.
