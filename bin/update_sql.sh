# SQL sub-repository auto-commit.
echo "Starting auto-commit for .sql files..."

git add sql/

git commit -m "Auto-commit for SQL files."

git pull origin main
git push origin main