from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import get_reader, get_book_reader, get_new_reader, borrow_book, return_book

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    # нажата кнопка Найти if
    if request.values.get('reader'):
        reader_id = int(request.values.get('reader'))
        session['reader_id'] = reader_id
        # нажата кнопка Добавить со страницы Новый читатель
        #(взять в комментарии, пока не реализована страница Новый читатель)
    
    elif request.values.get('new_reader'):
        new_reader = request.values.get('new_reader')
        new_reader_id = get_new_reader(conn, new_reader)
        print(new_reader_id)
        session['reader_id'] = new_reader_id
        # нажата кнопка Взять со страницы Поиск
        #(взять в комментарии, пока не реализована страница Поиск)
    elif request.values.get('book_reader_id'):
        book_reader_id = request.values.get('book_reader_id')
        return_book(conn, book_reader_id)
    elif request.values.get('book'):
        book_id = int(request.values.get('book'))
        borrow_book(conn, book_id, session['reader_id'])
        # нажата кнопка Не брать книгу со страницы Поиск
        #(взять в комментарии, пока не реализована страница Поиск)

    else:
        session['reader_id']= 1
        book_reader_id = 0
    
    df_reader = get_reader(conn)
    df_book_reader = get_book_reader(conn, session['reader_id'])
    

    html = render_template(
        'index.html',
        reader_id = session['reader_id'],
        combo_box = df_reader,
        book_reader = df_book_reader,
        len = len
    )
    return html
