#!/bin/bash

# Update system
sudo yum update -y

# Install Node.js and Git
sudo yum install -y git
curl -sL https://rpm.nodesource.com/setup_16.x | sudo bash -
sudo yum install -y nodejs

# Clone the repository
git clone https://github.com/dark-byte/webtoon-cloud-assignment
cd webtoon-cloud-assignment/backend

# Install dependencies and start the app
npm install
pm2 start app.js --name webtoon-app

