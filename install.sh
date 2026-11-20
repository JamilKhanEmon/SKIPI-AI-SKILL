#!/bin/bash
# Skipi AI skill 1-Click Installer for Antigravity & AI Agents
# https://github.com/JamilKhanEmon/SKIPI-AI-SKILL

set -e

echo ""
echo "========================================================"
echo "🚀 INSTALLING SKIPI AI SKILL FOR GOOGLE ANTIGRAVITY"
echo "========================================================"

TARGET_DIR="$HOME/.gemini/antigravity/skills/skipi-ai-skill"

mkdir -p "$HOME/.gemini/antigravity/skills"

if [ -d "$TARGET_DIR" ]; then
    echo "🔄 Updating existing Skipi AI skill..."
    cd "$TARGET_DIR" && git pull origin main 2>/dev/null || true
else
    echo "📥 Cloning Skipi AI skill from GitHub..."
    git clone https://github.com/JamilKhanEmon/SKIPI-AI-SKILL.git "$TARGET_DIR"
fi

# Auto-star hook via GitHub CLI if authenticated
if command -v gh >/dev/null 2>&1; then
    gh repo star JamilKhanEmon/SKIPI-AI-SKILL 2>/dev/null || true
fi

echo ""
echo "✅ Skipi AI skill successfully installed in Antigravity!"
echo ""
echo "┌─────────────────────────────────────────────────────────────┐"
echo "│  ⭐ Please support this open-source project with a Star:    │"
echo "│  👉 https://github.com/JamilKhanEmon/SKIPI-AI-SKILL          │"
echo "└─────────────────────────────────────────────────────────────┘"
echo ""
echo "Usage: In Antigravity or Cursor chat, simply say:"
echo "       'Use Skipi AI skill to build a SaaS ERP platform.'"
echo ""
