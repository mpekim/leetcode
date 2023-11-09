# Python sub-repository auto-commit.
echo "Starting auto-commit for .py files..."
git add python/

git commit -m "Auto-commit for Python files."

git pull origin main
git push origin main