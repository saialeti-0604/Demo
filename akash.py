print("Hellow World"
      ### **Option 2: Configure Git with Token**
bash
# Store credentials (will prompt once)
git config --global credential.helper store
git push origin akash
# Enter username and token when prompted


### **Option 3: Use SSH Instead (Best for Security)**

#### **Step 1: Generate SSH Key**
bash
ssh-keygen -t ed25519 -C "your-email@example.com"


#### **Step 2: Add SSH Key to GitHub**
bash
# Copy public key
cat ~/.ssh/id_ed25519.pub
# Add this to GitHub → Settings → SSH and GPG keys


#### **Step 3: Change Remote URL to SSH**
bash
git remote set-url origin git@github.com:AletiSaiChandra/Demo.git
git push origin akash


### **Option 4: Use GitHub CLI**
bash
# Install GitHub CLI and authenticate
gh auth login
git push origin akash


## Quick Fix:
The fastest solution is to create a Personal Access Token and use it as your password when prompted.





## Working Tree Information:
bash
# Show current working directory (Git root)
git rev-parse --show-toplevel

# Show relative path from Git root
git rev-parse --show-prefix

# Show if inside a Git working tree
git rev-parse --is-inside-work-tree


## Working Tree vs Index Comparison:
bash
# Show what's different between working tree and index
git diff-index HEAD

# Show files that differ between working tree and HEAD
git diff --name-only HEAD


## Git Worktree Commands (Multiple Working Trees):
bash
# List all worktrees
git worktree list

# Add a new worktree
git worktree add ../feature-branch feature-branch

# Remove a worktree
git worktree remove ../feature-branch

# Prune stale worktree references
git worktree prune


## Show Working Tree State:
bash
# Show current branch and working tree status
git branch --show-current

# Show working tree with file modifications
git status --porcelain


The most common command to see your working tree status is git status, which shows what files have been modified, staged, or are untracked in your current working 
directory.

> git command to reset all the changes

> Here are Git commands to reset all changes:

## Reset All Unstaged Changes (Working Tree):
bash
# Reset all modified files to last commit
git checkout -- .

# Alternative (newer syntax)
git restore .




Important: Never use your actual GitHub password - it won't work. Always use a Personal Access Token for HTTPS authentication.)
