# Java sub-repository auto-commit
echo "Starting auto-commit for Java files..."

git add java/

git commit -m "Auto-commit for Java files."

git pull origin main
git push origin main