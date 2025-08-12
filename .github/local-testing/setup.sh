#!/bin/bash

# Local CI/CD Testing Setup Script
# This script sets up tools for testing GitHub Actions workflows locally

set -e

echo "🧪 Setting up local CI/CD testing environment..."

# Check system requirements
echo "🔍 Checking system requirements..."

# Check for required commands
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo "❌ $1 is required but not installed"
        return 1
    else
        echo "✅ $1 is available"
        return 0
    fi
}

# Basic requirements
REQUIRED_COMMANDS=("git" "python3" "pip" "docker")
MISSING_COMMANDS=()

for cmd in "${REQUIRED_COMMANDS[@]}"; do
    if ! check_command "$cmd"; then
        MISSING_COMMANDS+=("$cmd")
    fi
done

if [ ${#MISSING_COMMANDS[@]} -ne 0 ]; then
    echo "❌ Missing required commands: ${MISSING_COMMANDS[*]}"
    echo "Please install them and run this script again"
    exit 1
fi

# Install act (GitHub Actions runner)
echo "📦 Installing act (GitHub Actions local runner)..."

if command -v act &> /dev/null; then
    echo "✅ act is already installed ($(act --version))"
else
    echo "Installing act..."
    
    # Detect OS and install accordingly
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install act
        else
            echo "❌ Homebrew not found. Please install act manually:"
            echo "https://github.com/nektos/act#installation"
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
    else
        echo "❌ Unsupported OS. Please install act manually:"
        echo "https://github.com/nektos/act#installation"
        exit 1
    fi
fi

# Install Python dependencies for local testing
echo "🐍 Installing Python dependencies..."
pip3 install --user --upgrade \
    jsonschema \
    pydantic[email] \
    requests \
    bikeshed \
    PyYAML

# Initialize Bikeshed
echo "📚 Initializing Bikeshed..."
bikeshed update

# Create local testing directory structure
echo "📁 Creating local testing directories..."
mkdir -p .github/local-testing/{logs,artifacts,secrets}

# Create .env file for local testing
if [ ! -f ".github/local-testing/.env" ]; then
    echo "🔧 Creating local environment file..."
    cat > .github/local-testing/.env << 'EOF'
# Local Testing Environment Variables
# Copy and modify as needed for your testing

# GitHub token for API access (optional, for testing release workflows)
# Get from: https://github.com/settings/tokens
# GITHUB_TOKEN=ghp_your_token_here

# Version for testing release workflows
TEST_VERSION=v3.0.0

# Force release flag for testing
FORCE_RELEASE=true

# Repository information
GITHUB_REPOSITORY=carbondirect/BOOST
GITHUB_REF_NAME=main
GITHUB_SHA=abc123456789

# Paths
GITHUB_WORKSPACE=/tmp/act-workspace
EOF
    echo "✅ Created .env file at .github/local-testing/.env"
    echo "💡 Edit this file to customize your local testing environment"
fi

# Create .actrc file for act configuration
if [ ! -f ".github/local-testing/.actrc" ]; then
    echo "🔧 Creating act configuration..."
    cat > .github/local-testing/.actrc << 'EOF'
# act configuration file
# This configures how act runs GitHub Actions locally

# Use medium-sized Ubuntu image for better compatibility
-P ubuntu-latest=catthehacker/ubuntu:act-latest
-P ubuntu-20.04=catthehacker/ubuntu:act-20.04
-P ubuntu-22.04=catthehacker/ubuntu:act-22.04

# Bind mount for workspace access
--bind

# Environment file
--env-file .github/local-testing/.env

# Artifacts directory
--artifact-server-path .github/local-testing/artifacts

# Verbose output for debugging
--verbose
EOF
    echo "✅ Created act configuration at .github/local-testing/.actrc"
fi

# Create secrets file template
if [ ! -f ".github/local-testing/.secrets" ]; then
    echo "🔐 Creating secrets template..."
    cat > .github/local-testing/.secrets << 'EOF'
# Local testing secrets
# Add your actual secrets here for testing workflows that require them

# GitHub token for API access
GITHUB_TOKEN=your_token_here

# Any other secrets your workflows might need
# CUSTOM_SECRET=value
EOF
    echo "✅ Created secrets template at .github/local-testing/.secrets"
    echo "⚠️  Remember to add .github/local-testing/.secrets to .gitignore"
fi

# Update .gitignore
echo "📝 Updating .gitignore..."
if [ -f ".gitignore" ]; then
    if ! grep -q ".github/local-testing/.secrets" .gitignore; then
        echo "" >> .gitignore
        echo "# Local CI/CD testing" >> .gitignore
        echo ".github/local-testing/.secrets" >> .gitignore
        echo ".github/local-testing/.env" >> .gitignore
        echo ".github/local-testing/logs/" >> .gitignore
        echo ".github/local-testing/artifacts/" >> .gitignore
        echo "✅ Updated .gitignore"
    else
        echo "✅ .gitignore already configured"
    fi
else
    echo "⚠️  No .gitignore found - you may want to create one"
fi

echo ""
echo "🎉 Local CI/CD testing setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Edit .github/local-testing/.env with your configuration"
echo "2. Add your GitHub token to .github/local-testing/.secrets (optional)"
echo "3. Run './test-local.sh' to test workflows locally"
echo ""
echo "🔗 Useful commands:"
echo "- act -l                          # List available workflows"
echo "- act -j validate-schemas         # Run specific job"
echo "- act --dry-run                   # Simulate without running"
echo "- act -W .github/workflows/       # Run all workflows"
echo ""
echo "📖 Documentation: https://github.com/nektos/act"