# Todo App

React / TypeScript と FastAPI を用いて開発した、シンプルなTodo管理Webアプリケーションです。

フロントエンド・バックエンド・データベースを含むWebアプリケーション開発の一連の流れを学ぶことを目的として、個人開発しました。

## 概要

タスクの登録・一覧表示・削除・完了状態の変更ができるTodoアプリです。

フロントエンドからREST APIを通じてバックエンドへアクセスし、MySQLにタスク情報を保存します。

## 主な機能

- タスクの一覧表示
- タスクの新規追加
- タスクの削除
- タスクの完了 / 未完了の切り替え
- データベースへのタスク情報の保存

## 使用技術

### Frontend
- React
- TypeScript
- Axios

### Backend
- Python 3.9
- FastAPI
- SQLAlchemy
- Uvicorn

### Database
- MySQL 8.0

### Development Environment
- Docker
- Docker Compose
- Poetry

## システム構成

```text
Browser
  |
  | HTTP
  v
React / TypeScript
  |
  | REST API (Axios)
  v
FastAPI
  |
  | SQLAlchemy
  v
MySQL
