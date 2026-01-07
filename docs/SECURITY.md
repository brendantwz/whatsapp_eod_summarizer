# Security Guidelines

## 🔒 Protecting Your API Keys

API keys are sensitive credentials that provide access to paid services. Exposing them can lead to:
- Unauthorized usage and unexpected bills
- Account compromise
- Service suspension

## ✅ What We've Implemented

### 1. `.gitignore` Protection

The `.gitignore` file prevents sensitive files from being committed to Git:

```gitignore
# Environment variables and secrets
.env
.env.local
*.key

# Sensitive input files
input/*_sensitive.txt
input/*_private.txt
```

**Files Protected:**
- `.env` - Your API keys and configuration
- `.env.local` - Local overrides
- `*.key` - Any key files
- Sensitive input files

### 2. Environment Variable Storage

API keys are stored in environment variables, NOT in code:

```python
# ✅ GOOD - Reading from environment
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ❌ BAD - Hardcoded in code
API_KEY = "sk-ant-1234567890"  # NEVER DO THIS!
```

### 3. Template Files

We provide `.env` templates without actual keys:
- `ENV_SETUP.md` - Setup instructions
- Users create their own `.env` file locally (not committed)

## 📋 Security Checklist

Before committing code, verify:

- [ ] `.env` file is listed in `.gitignore`
- [ ] No API keys in source code
- [ ] No API keys in commit history
- [ ] `.env` file is NOT tracked by Git
- [ ] Template files contain placeholder values only

## 🔍 Checking for Exposed Keys

### Before First Commit

```bash
# Check if .env is properly ignored
git status

# You should NOT see .env in the list
# If you do, it means .gitignore isn't working
```

### Check Git History

```bash
# Search for potential API keys in history
git log -S "sk-ant-" --all
git log -S "sk-or-" --all
git log -S "ANTHROPIC_API_KEY" --all
```

## 🚨 If You Accidentally Commit an API Key

### Immediate Actions:

1. **Revoke the exposed key immediately**
   - Anthropic: https://console.anthropic.com/settings/keys
   - OpenAI: https://platform.openai.com/api-keys
   - OpenRouter: https://openrouter.ai/keys

2. **Generate a new key**

3. **Update your local `.env` file**

4. **Remove from Git history** (if already pushed):
   ```bash
   # Use git filter-branch or BFG Repo-Cleaner
   # See: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
   ```

## 🎯 Best Practices

### Development

1. **Use `.env` for local development**
   ```bash
   # Create your .env file
   cp ENV_SETUP.md .env
   # Edit with your actual keys
   ```

2. **Never share your `.env` file**
   - Don't send via email, Slack, or messaging apps
   - Don't screenshot it
   - Don't paste it in support tickets

3. **Use different keys for different environments**
   ```
   Development: dev-key-xxxxx
   Production: prod-key-xxxxx
   ```

### Production/Deployment

1. **Use platform-specific secret management**
   - AWS: AWS Secrets Manager
   - Azure: Azure Key Vault
   - Heroku: Config Vars
   - Vercel: Environment Variables

2. **Set environment variables in deployment platform**
   ```bash
   # Example: Heroku
   heroku config:set ANTHROPIC_API_KEY=sk-ant-xxxxx
   ```

3. **Rotate keys periodically**
   - Set a reminder to rotate keys every 90 days
   - Rotate immediately if compromise suspected

### Team Collaboration

1. **Share setup instructions, not keys**
   - Point teammates to `ENV_SETUP.md`
   - Each person gets their own API key

2. **Use separate accounts/keys per team member**
   - Easier to track usage
   - Easier to revoke if someone leaves

3. **Document which services need keys**
   - Keep `ENV_SETUP.md` updated
   - List all required environment variables

## 🔐 Environment Variable Hierarchy

The application checks for environment variables in this order:

1. **System environment variables** (highest priority)
   ```bash
   export ANTHROPIC_API_KEY=sk-ant-xxxxx
   ```

2. **`.env` file** (loaded by python-dotenv)
   ```env
   ANTHROPIC_API_KEY=sk-ant-xxxxx
   ```

3. **Default values** (fallback, if any)
   ```python
   AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")
   ```

## 📚 Additional Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [12 Factor App: Config](https://12factor.net/config)

## ⚠️ Common Mistakes to Avoid

1. ❌ Hardcoding keys in source files
2. ❌ Committing `.env` file to Git
3. ❌ Sharing keys in team chat
4. ❌ Using production keys in development
5. ❌ Leaving keys in code comments
6. ❌ Storing keys in documentation files
7. ❌ Embedding keys in error messages or logs

## ✅ Quick Verification

Run this command to ensure your setup is secure:

```bash
# Check that .env is ignored
git check-ignore .env
# Should output: .env

# Check that .env is not tracked
git ls-files | grep .env
# Should output: nothing

# Verify no keys in code
grep -r "sk-ant-" --exclude-dir=.git --exclude="*.md" .
grep -r "sk-or-" --exclude-dir=.git --exclude="*.md" .
# Should output: nothing (or only in .env which is ignored)
```

---

**Remember**: When in doubt, regenerate your API key. It's better to be safe than sorry!

