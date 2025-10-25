# Git Commands for CI/CD Final Project

# Initialize Git repository (run these commands in the project directory)
git init
git config --global user.email "your_email@example.com"
git config --global user.name "Your Name"

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: CI/CD final project with GitHub Actions and Tekton workflows"

# Add your GitHub repository as remote (replace with your actual repo URL)
git remote add origin https://github.com/yourusername/ci-cd-final-project.git

# Push to GitHub
git branch -M main
git push -u origin main