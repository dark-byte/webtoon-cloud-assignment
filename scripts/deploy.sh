#!/bin/bash
# This script sets up the EC2 instance and deploys the web application

# Update system
sudo yum update -y

# Install Node.js and Git
sudo yum install -y git
curl -sL https://rpm.nodesource.com/setup_16.x | sudo bash -
sudo yum install -y nodejs

# Clone the repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

# Install dependencies and start the app
npm install
node app.js
