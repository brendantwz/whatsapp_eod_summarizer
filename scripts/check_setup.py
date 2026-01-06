"""
Environment Setup Checker

Run this script to verify your environment is correctly configured.
"""

import os
import sys

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is compatible (3.8+)")
        return True
    else:
        print("❌ Python 3.8+ required")
        return False


def check_dependencies():
    """Check if required packages are installed"""
    packages = {
        "anthropic": "Claude API support",
        "openai": "OpenAI GPT support",
    }
    
    installed = []
    missing = []
    
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✅ {package:20s} - {description}")
            installed.append(package)
        except ImportError:
            print(f"❌ {package:20s} - {description} (not installed)")
            missing.append(package)
    
    return installed, missing


def check_env_variables():
    """Check environment variables"""
    ai_provider = os.getenv("AI_PROVIDER", "anthropic")
    print(f"\n📍 AI_PROVIDER: {ai_provider}")
    
    if ai_provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
            print(f"✅ ANTHROPIC_API_KEY: {masked_key}")
            return True
        else:
            print("❌ ANTHROPIC_API_KEY not set")
            print("\nTo set it:")
            print("  Windows: $env:ANTHROPIC_API_KEY='your-key'")
            print("  Mac/Linux: export ANTHROPIC_API_KEY='your-key'")
            return False
    
    elif ai_provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
            print(f"✅ OPENAI_API_KEY: {masked_key}")
            return True
        else:
            print("❌ OPENAI_API_KEY not set")
            print("\nTo set it:")
            print("  Windows: $env:OPENAI_API_KEY='your-key'")
            print("  Mac/Linux: export OPENAI_API_KEY='your-key'")
            return False
    
    elif ai_provider == "openrouter":
        api_key = os.getenv("OPENROUTER_API_KEY")
        if api_key:
            masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
            print(f"✅ OPENROUTER_API_KEY: {masked_key}")
            return True
        else:
            print("❌ OPENROUTER_API_KEY not set")
            print("\nTo set it:")
            print("  Windows: $env:OPENROUTER_API_KEY='your-key'")
            print("  Mac/Linux: export OPENROUTER_API_KEY='your-key'")
            print("  Get your key at: https://openrouter.ai/keys")
            return False
    
    else:
        print(f"❌ Unknown AI_PROVIDER: {ai_provider}")
        print("   Valid options: 'anthropic', 'openai', or 'openrouter'")
        return False


def check_directories():
    """Check if required directories exist"""
    dirs = ["input", "output"]
    all_exist = True
    
    print("\n📁 Directory Structure:")
    for d in dirs:
        if os.path.exists(d):
            print(f"✅ {d}/ exists")
        else:
            print(f"⚠️  {d}/ not found (will be created when needed)")
    
    return all_exist


def check_sample_file():
    """Check if sample file exists"""
    sample = "input/Netcore & Convx - QSR Team - test text.txt"
    
    print("\n📄 Sample File:")
    if os.path.exists(sample):
        print(f"✅ Sample file found: {sample}")
        return True
    else:
        print(f"⚠️  Sample file not found: {sample}")
        print("   (Optional - for testing only)")
        return False


def main():
    print("=" * 70)
    print("WhatsApp EOD Report Generator - Setup Checker")
    print("=" * 70)
    print()
    
    # Check Python version
    print("🐍 Checking Python...")
    python_ok = check_python_version()
    print()
    
    # Check dependencies
    print("📦 Checking Dependencies...")
    installed, missing = check_dependencies()
    print()
    
    # Check environment variables
    print("🔑 Checking API Configuration...")
    env_ok = check_env_variables()
    print()
    
    # Check directories
    check_directories()
    
    # Check sample file
    check_sample_file()
    
    # Summary
    print("\n" + "=" * 70)
    print("SETUP SUMMARY")
    print("=" * 70)
    
    all_checks = []
    
    if python_ok:
        print("✅ Python version compatible")
        all_checks.append(True)
    else:
        print("❌ Python version incompatible")
        all_checks.append(False)
    
    if installed:
        print(f"✅ {len(installed)} AI package(s) installed: {', '.join(installed)}")
        all_checks.append(True)
    else:
        print("❌ No AI packages installed")
        print("   Run: pip install -r requirements.txt")
        all_checks.append(False)
    
    if env_ok:
        print("✅ API key configured")
        all_checks.append(True)
    else:
        print("❌ API key not configured")
        all_checks.append(False)
    
    print()
    
    if all(all_checks):
        print("🎉 All checks passed! You're ready to generate reports.")
        print("\nQuick Start:")
        print('  python generate_report.py "input/your-chat.txt" "Site Name"')
        return 0
    else:
        print("⚠️  Some checks failed. Review the issues above.")
        print("\nSee SETUP.md for detailed configuration instructions.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

