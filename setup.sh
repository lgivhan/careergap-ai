#!/bin/bash

# 1. Colors for pretty output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Initializing CareerGap AI Environment...${NC}"

# 2. Check and Activate Virtual Environment
if [ -d "venv" ]; then
    echo "✅ Found venv. Activating..."
    source venv/bin/activate
else
    echo -e "${RED}❌ venv not found. Creating one...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# 3. Check if Docker is running
if ! docker info >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker engine is not running. Please open Docker Desktop!${NC}"
    exit 1
fi

# 4. Prompt: Run locally or in Docker?
read -p "Do you want to run in Docker? (y/n): " choice

if [ "$choice" == "y" ]; then
    echo -e "${GREEN}🐳 Building and starting Docker container...${NC}"
    docker-compose up --build
else
    echo -e "${GREEN}🐍 Starting Python application locally...${NC}"
    python3 main.py
fi

echo "---------------------------"
echo "Select a Mode:"
echo "1) Run New Analysis"
echo "2) View Search History"
echo "3) Generate Strategic Aggregate Report"
read -p "Selection (1-3): " mode

case $mode in
  1) python3 main.py ;;
  2) read -p "Search Company: " co; python3 history.py $co ;;
  3) python3 aggregate_analysis.py ;;
  *) echo "Invalid choice";;
esac