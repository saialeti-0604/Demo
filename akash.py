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

Important: Never use your actual GitHub password - it won't work. Always use a Personal Access Token for HTTPS authentication.)
