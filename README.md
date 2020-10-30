<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://static.thenounproject.com/png/727275-200.png" alt="Project logo"></a>
</p>

<h3 align="center">NameME REST API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/YonLiud/nameme-API/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> An API written for the NameME Application.
    <br> 
</p>

## 🎥 Demo

[![image.png](https://i.postimg.cc/NMwCVf76/image.png)](https://postimg.cc/DWBc4hN0)
[![image.png](https://i.postimg.cc/28PQT9xv/image.png)](https://postimg.cc/fJfSRKpT)

## 🧐 About NameME

NameME is a database containing information about people who register and upload information about themselves!
The usage of NameME API is open for everyone interested in it contributing to it. The usage of NameME is completely free and available for everyone!

## ✂️ Editing this API

Everyone is authorized to use this source code by the (license)(/LICENSE) provided in this project

## 🔭 API's Database Must Structure
#### api_keys.db
```sql
"key"	TEXT NOT NULL UNIQUE,
"name"	TEXT NOT NULL UNIQUE,
"email"	TEXT NOT NULL UNIQUE,
PRIMARY KEY("key")
  ```
#### database.db
```sql
"id"	INTEGER NOT NULL,
"key"	TEXT NOT NULL,
-- ADD HERE YOUR WANTED COLUMNS
```
## ⛏️ Built Using

- [Python](https://www.python.org/) - Main API Language
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Main Frontend Module
- [SQLite](https://www.sqlite.org/index.html) - Database

## ✍️ Authors

- [@YonLiud](https://github.com/YonLiud) - Backend Lead Developer & Author of the current script
