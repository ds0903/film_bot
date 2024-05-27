import sqlite3


async def search_films(films):
    """Запрос к базе по поиску рецептов"""
    conn = sqlite3.connect('bot_films.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, zhanr, year, rating FROM films WHERE name = ?", (films,))
    filmss = cursor.fetchone()

    cursor.close()
    conn.close()
    if filmss:
        film_id, name, zhanr, year, rating = filmss
        return name, zhanr, year, rating
    else:
        return None, None, None

async def search_films_new(films):

    conn = sqlite3.connect('bot_films.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM films_new WHERE name = ?", (films,))
    filmss = cursor.fetchone()

    cursor.close()
    conn.close()

    return filmss
