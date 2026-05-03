# AutoContent Development Setup Guide

This guide will help you set up the complete development environment for AutoContent.

## Prerequisites Installation

### 1. Install Python 3.10+ 

**Option A: From python.org (Recommended)**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 (latest recommended)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" before clicking Install
5. Click "Install Now"
6. Verify installation:
   ```powershell
   python --version
   ```

**Option B: Using Windows Package Manager**
```powershell
winget install Python.Python.3.11
```

---

### 2. Install Node.js (for Angular frontend)

**Option A: From nodejs.org (Recommended)**
1. Go to https://nodejs.org/
2. Download the LTS version (recommended for stability)
3. Run the installer (use all default settings)
4. Verify installation:
   ```powershell
   node --version
   npm --version
   ```

**Option B: Using Windows Package Manager**
```powershell
winget install OpenJS.NodeJS
```

---

### 3. Install Docker & Docker Compose (Optional but Recommended)

For complete containerized development:
1. Download Docker Desktop from https://www.docker.com/products/docker-desktop
2. Run the installer
3. Verify installation:
   ```powershell
   docker --version
   docker-compose --version
   ```

---

## Environment Setup After Installation

Once Python and Node.js are installed, run these commands from the project root:

### 1. Create Python Virtual Environment for Backend

```powershell
cd C:\home\workspace\autocontent\backend

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Verify installation
python -c "import fastapi; print('FastAPI installed successfully')"
```

### 2. Install Frontend Dependencies

```powershell
cd C:\home\workspace\autocontent\frontend

# Install dependencies
npm install

# Verify installation
npm list angular

# Optional: Install Angular CLI globally
npm install -g @angular/cli
```

---

## Running the Project

### Option 1: Using Docker Compose (Recommended)

```powershell
cd C:\home\workspace\autocontent

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Then access:
- Frontend: http://localhost:4200
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Option 2: Local Development (Python + Node)

**Terminal 1 - Backend:**
```powershell
cd C:\home\workspace\autocontent\backend
.\venv\Scripts\Activate.ps1
python main.py
```

Backend runs at: http://localhost:8000

**Terminal 2 - Frontend:**
```powershell
cd C:\home\workspace\autocontent\frontend
npm start
```

Frontend runs at: http://localhost:4200

---

## Verification Checklist

After setup, verify everything works:

```powershell
# Check Python
python --version           # Should be 3.10+
pip list | grep fastapi    # Should show FastAPI

# Check Node.js
node --version            # Should be 16+
npm --version             # Should be 8+

# Check Git
git --version             # Should be installed

# Optional: Check Docker
docker --version
docker-compose --version
```

---

## Troubleshooting

### Python Issues

**"python command not found"**
- Ensure Python was added to PATH during installation
- Restart PowerShell after installing Python
- Try `py` instead of `python`

**Virtual environment activation fails**
- Try: `python -m venv venv` (recreate environment)
- Or use: `py -m venv venv`

**Pip install fails**
- Upgrade pip: `python -m pip install --upgrade pip`
- Check internet connection
- Try: `pip install --upgrade pip setuptools wheel`

### Node.js Issues

**"npm command not found"**
- Ensure Node.js was installed with npm
- Restart PowerShell after installation
- Check PATH environment variable

**npm install takes too long**
- Clear cache: `npm cache clean --force`
- Try different npm registry: `npm config set registry https://registry.npmjs.org/`

### Docker Issues

**"docker command not found"**
- Restart computer after Docker installation
- Check if Docker daemon is running
- Add Docker to PATH

### Port Already in Use

**"Port 8000 already in use"**
```powershell
# Find and kill the process
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**"Port 4200 already in use"**
```powershell
# Find and kill the process
netstat -ano | findstr :4200
taskkill /PID <PID> /F
```

---

## Next Steps

1. ✅ Install Python 3.10+
2. ✅ Install Node.js LTS
3. ✅ Install Docker (optional)
4. ✅ Set up Python virtual environment
5. ✅ Install backend dependencies
6. ✅ Install frontend dependencies
7. ✅ Run the project
8. 📖 Read the main README.md
9. 🚀 Start developing!

---

## Getting Help

- Check [README.md](README.md) for architecture overview
- Read [DEVELOPMENT.md](DEVELOPMENT.md) for code standards
- Review [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Check the [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for quick reference

---

**Last Updated**: May 3, 2026
**Version**: 1.0
