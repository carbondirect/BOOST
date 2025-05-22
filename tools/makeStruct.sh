#!/bin/bash

# Define directory structure
dirs=(
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
  "drafts/images"
  "drafts/scripts"
  "proposals"
  "meetings/templates"
  "use-cases"
  "presentations"
  "tools"
  "data"
  "tests"
)

# Create directories if they don't exist
for dir in "${dirs[@]}"; do
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    echo "Created directory: $dir"
  fi
done


# Create GitHub issue templates
cat > .github/ISSUE_TEMPLATE/bug_report.md <<EOF
---
name: Bug report
about: Report a problem in this project
title: "[Bug] "
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment (please complete the following information):**
- OS: [e.g., Windows, macOS, Linux]
- Browser [e.g., Chrome, Firefox]
- Spec version/date [if applicable]

**Additional context**
Add any other context about the problem here.
EOF

cat > .github/ISSUE_TEMPLATE/feature_request.md <<EOF
---
name: Feature request
about: Suggest a new feature for the project
title: "[Feature] "
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem?**
Please describe what the problem is and how this feature would help.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
Any alternative solutions or features you've thought of.

**Additional context**
Add any other context or examples here.
EOF

echo "Created issue templates"
