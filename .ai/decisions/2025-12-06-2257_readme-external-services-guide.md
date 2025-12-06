# Decision Record: External Service Setup Documentation

**Date:** 2025-12-06 22:57 UTC  
**Previous Record Hash:** `f52f965081b89edf7d1dd073cc84521c14981ab00701ff618cad2f70451bd26e`

## Context

User requested comprehensive onboarding documentation for the external services required by F.R.I.D.A.Y. The existing README contained only brief links to Google AI Studio and the Discord Developer Portal, with no guidance for users who are new to these platforms.

## Decision

Added a new "External Service Setup" section to README.md with complete step-by-step guides covering:

**Google Gemini API:**
- Google account creation
- Accessing AI Studio
- Creating a Google Cloud project (optional but recommended)
- Generating and copying an API key
- Verifying the key works via curl

**Discord Bot:**
- Creating a Discord server
- Creating a Discord application in the Developer Portal
- Creating the bot and obtaining the token
- Configuring bot permissions (Message Content Intent)
- Generating OAuth2 invite URL with correct scopes
- Inviting the bot to a server
- Enabling Developer Mode to copy channel IDs
- Creating dedicated channels for reports

This comprehensive approach was chosen to enable users with no prior experience to get F.R.I.D.A.Y. running without external tutorials.

## Changes

**Modified:** `README.md`
- Added new section "🔑 External Service Setup" between Quick Start and Customization
- Added subsection "Google Gemini API Setup" with 5 numbered steps
- Added subsection "Discord Bot Setup" with 7 numbered steps
- Included security warnings for API keys and bot tokens
- Added verification command for Gemini API key

## Verification

Manual review confirms:
- All steps are numbered and sequential
- Links to external portals are correct and current
- Security best practices are highlighted
- Both complete beginners and experienced users can follow the guide
