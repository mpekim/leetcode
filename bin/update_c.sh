# C repository auto-commit.
echo "Starting auto-commit for C-files..."
git add c/

git commit -m "Auto-commit for C-files."

git pull origin main
git push origin main