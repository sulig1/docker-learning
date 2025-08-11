# Docker Learning

# 🐳 Docker Project – Flask + Redis

This repository contains a multi-container Docker application featuring a Python Flask web app and a Redis database. It demonstrates how to run and connect multiple services using Docker Compose.

## 📌 Overview

- Flask – Python web framework for serving pages.  
- Redis – Key-value store to track visit counts.  
- Docker Compose – Orchestrates multi-container setup.  

## 🚀 Features

- Shared visit count stored in Redis, accessible across all app instances.  
- Simple, lightweight setup for demonstrating Docker networking and service linking.  
- Easily scalable to run multiple Flask containers.  

## 🌐 Endpoints

- `/` → Welcome page with a button linking to `/count`.  
- `/count` → Increments and displays the global visit count.  

## 🛠 How to Run

1. Build and start services  

  docker compose up --build

## Access the app

Home page → http://localhost:5002
Count page → http://localhost:5002/count
