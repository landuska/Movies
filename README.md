# 🎬 Movie App

## Overview

This project is a **Python Movie Application** that allows users to manage a collection of movies.  
Movies can be loaded from **local storage (JSON / SQLite)** or fetched from the **OMDb Web API**.  
The application also allows generating **statistics, graphs, and a website displaying the movies**.

---

## Features

- 📋 List all movies
- ➕ Add a movie (data fetched automatically from the OMDb API)
- ❌ Delete a movie
- 🔎 Search for a movie
- ⭐ Sort movies by rating
- 🎲 Select a random movie
- 📊 Show movie statistics (average, median, best and worst rating)
- 📈 Generate a histogram of movie ratings
- 🌐 Generate a **website page with all movies**

---

## Technologies Used

- **Python**
- **SQLite / JSON storage**
- **OMDb API**
- **Matplotlib** (for charts)
- **Colorama** (for colored console output)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/landuska/Movies.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

```
colorama==0.4.6
matplotlib==3.10.8
python-dotenv==1.2.2
requests==2.32.5
SQLAlchemy==2.0.48
```

---

## Run the Application

```bash
python main.py
```

---

## Menu

When the program starts, you will see the menu:

```
0. Exit
1. List movies
2. Add movie
3. Update movie
4. Delete movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Histogram
10. Generate Website
```

---

## Website Generation

The application can generate a **HTML page showing all movies** with posters.

The program uses:

- an **HTML template**
- movie data from the database
- poster images from the **OMDb API**

The generated page will be saved as:

```
index.html
```

---

## Example Output

The generated website displays:

- movie title
- release year
- poster image

---

## Project Structure

```
movies/
├── main.py
├── api_movies.py
├── generate_web.py
├── movie_storage/
│    ├── movie_storage_sql.py
├── data/
│    ├── movies.db
├── static/
│    ├── index_template.html
│    ├── index.html
│    ├── style.css
├── config/
│    ├── requirements.txt
│    └── README.md
```

---

## API

This project uses the **OMDb API** to fetch movie information.

You can get a free API key here:

https://www.omdbapi.com/

---

## Author

Created as part of a Python learning project.
