# BOOST Documentation Architecture

## ⚠️ CRITICAL: ReSpec-Style Layout System

**The BOOST documentation uses a HYBRID architecture that must NOT be "simplified" or "cleaned up"**

### Architecture Overview

```
Bikeshed (Content Generation) → Python Processing (Layout) → ReSpec-Style Output
```

### Core Components (DO NOT REMOVE)

1. **respec-style.css** - Critical styling that overrides Bikeshed defaults
2. **main-content-wrapper** - Essential div structure for responsive layout  
3. **Python HTML Processing** - build.sh contains sophisticated HTML manipulation
4. **Sidebar TOC** - Fixed navigation with collapse/expand functionality

### ⚠️ Common Mistakes to Avoid

❌ **NEVER** think the ReSpec styling is "inappropriate" for Bikeshed
❌ **NEVER** remove the Python HTML processing thinking it's "unnecessary"  
❌ **NEVER** "simplify" the CSS thinking it's "redundant"
❌ **NEVER** remove `main-content-wrapper` thinking it's "not standard Bikeshed"

✅ **This is INTENTIONAL DESIGN** - A sophisticated overlay system that:
- Uses Bikeshed for semantic HTML generation
- Applies ReSpec-style layout for professional presentation
- Provides responsive design and navigation

### Critical Files

| File | Purpose | Never Remove |
|------|---------|--------------|
| `respec-style.css` | ReSpec-style layout and navigation | ✅ CRITICAL |
| `build.sh` (Python section) | HTML processing and layout injection | ✅ CRITICAL |
| Workflow validation | Checks for `main-content-wrapper` | ✅ CRITICAL |

### If Someone Says "This Looks Wrong"

1. **Check commit v3.1.3-5-g725c24a** - This is the REFERENCE implementation
2. **The system is WORKING AS DESIGNED** if it has:
   - Fixed sidebar TOC
   - `main-content-wrapper` div
   - Responsive layout
   - Professional ReSpec-style appearance

### Historical Context

- **v3.1.3-5-g725c24a**: WORKING reference implementation
- **Problem**: Someone mistakenly removed this system thinking it was "broken"
- **Solution**: Complete restoration of the sophisticated layout system
- **Lesson**: The hybrid architecture is intentional and should be preserved

## Architecture Decision Records (ADRs)

### ADR-001: Hybrid Bikeshed + ReSpec Layout (APPROVED)

**Decision**: Use Bikeshed for content generation with ReSpec-style layout overlay

**Rationale**: 
- Bikeshed provides excellent semantic HTML and specification features
- ReSpec provides superior navigation and responsive design
- Hybrid approach gets benefits of both systems

**Status**: ✅ APPROVED - Do not change without extensive consultation

### ADR-002: Python HTML Processing (APPROVED)

**Decision**: Use Python in build.sh to modify Bikeshed output for ReSpec layout

**Rationale**:
- Bikeshed centering constraints must be removed
- `main-content-wrapper` div must be injected
- Critical CSS overrides must be applied

**Status**: ✅ APPROVED - This processing is essential, not optional

## For Future Maintainers

**Before making ANY changes to the HTML/CSS system:**

1. ✅ Read this entire document
2. ✅ Check the reference commit v3.1.3-5-g725c24a  
3. ✅ Understand the hybrid architecture
4. ✅ Test changes thoroughly before deployment
5. ✅ Consult with original architect if making significant changes

## Testing the Layout System

```bash
# 1. Build locally
cd /Users/peter/src/BOOST/drafts/current/specifications
./build.sh

# 2. Check for critical components
grep -c "main-content-wrapper" boost-spec.html  # Should be > 5
grep -q "respec-style.css" boost-spec.html && echo "CSS found" || echo "❌ CSS MISSING"

# 3. Test in browser - should have:
# - Fixed sidebar TOC on left
# - Content area that adapts to sidebar
# - Responsive collapse on mobile
# - Professional ReSpec appearance
```

**Remember**: This architecture exists because it works. Don't fix what isn't broken.