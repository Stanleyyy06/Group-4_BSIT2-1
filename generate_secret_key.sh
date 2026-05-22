#!/bin/bash
# generate_secret_key.sh - Generate a secure SECRET_KEY for production

echo "🔐 Generating secure SECRET_KEY..."

# Python method (recommended)
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")

echo ""
echo "✅ Your SECRET_KEY (64 characters):"
echo ""
echo "SECRET_KEY=$SECRET_KEY"
echo ""
echo "📋 Copy this to your .env or Railway variables"
