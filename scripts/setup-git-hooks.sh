#!/bin/bash

# Setup script for BOOST git hooks
# This ensures version synchronization safeguards are in place

set -e

echo "🔧 Setting up BOOST git hooks for version synchronization..."

# Get the repository root
REPO_ROOT=$(git rev-parse --show-toplevel)

# Check if we're in the right place
if [ ! -f "$REPO_ROOT/.githooks/pre-commit" ]; then
    echo "❌ Error: .githooks/pre-commit not found. Are you in the BOOST repository?"
    exit 1
fi

# Configure git to use our hooks directory
git config core.hooksPath "$REPO_ROOT/.githooks"

echo "✅ Git hooks configured successfully!"
echo ""
echo "📋 What this enables:"
echo "   • Pre-commit validation prevents hardcoded versions from being committed"
echo "   • Ensures {{VERSION}} placeholders are used instead of hardcoded versions"  
echo "   • Maintains version synchronization between git tags and documentation"
echo ""
echo "💡 How it works:"
echo "   • When you commit, the hook checks for hardcoded version patterns"
echo "   • If found, the commit is blocked with helpful error messages"
echo "   • Replace hardcoded versions with {{VERSION}} placeholders to fix"
echo ""
echo "🎯 Result: Documentation always shows correct versions matching git tags"