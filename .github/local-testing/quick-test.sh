#!/bin/bash

# Quick CI/CD Test Script
# Fast pre-commit validation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "⚡ Quick CI/CD Test"
echo "==================="

# Run the most critical tests quickly
echo "🔍 Schema validation..."
./test-local.sh schema --quiet 2>/dev/null || { echo "❌ Schema validation failed"; exit 1; }

echo "🏗️ Build test..."
./test-local.sh build --quiet 2>/dev/null || { echo "❌ Build test failed"; exit 1; }

echo "✅ All quick tests passed! Ready to commit/push."