#!/bin/bash

echo ""
echo "========================================"
echo "   Ultimate Tutoring Program Setup"
echo "========================================"
echo ""
echo "Installing required Python packages..."
echo ""

python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "   Setup Complete!"
echo "========================================"
echo ""
echo "To start the tutor, run: ./run.sh"
echo "Or type: streamlit run tutor.py"
echo ""

