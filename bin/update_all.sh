# Auto-commit for all files.
echo "Starting auto-commit for entire repository..."
git add .

git commit -m "Auto commit."

git pull origin main
git push origin main