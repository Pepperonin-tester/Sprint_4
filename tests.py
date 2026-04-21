import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', 
                             [
                                 "P",                                
                                 "P" * 40,                           
                                 ])
    def test_add_new_book_valid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
    
    @pytest.mark.parametrize("name",
                             [
                                 "",
                                 "A" * 41
                                 ])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', 
                             [
                                 ('Дюна', 'Фантастика'),
                                 ('Оно', 'Ужасы'),
                                 ])
    def test_set_book_genre_success(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_book_not_exist(self):
        collector = BooksCollector()
        collector.set_book_genre('Шпингалет', 'Ужасы')
        assert collector.get_book_genre('Шпингалет') is None

    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert collector.get_book_genre("Шерлок Холмс") == "Детективы"

    def test_get_book_genre_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Интерстеллар")
        collector.set_book_genre("Интерстеллар", "Фантастика")
        assert "Интерстеллар" in collector.get_books_with_specific_genre("Фантастика")

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Золушка")
        collector.set_book_genre("Золушка", "Мультфильмы")
        children_books = collector.get_books_for_children()
        assert "Золушка" in children_books

    def test_books_with_age_rating_not_shown_to_children(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Оно" not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Король Лев")
        collector.add_book_in_favorites("Король Лев")
        assert "Король Лев" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Король Лев")
        collector.add_book_in_favorites("Король Лев")
        collector.delete_book_from_favorites("Король Лев")
        assert "Король Лев" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Двенадцать стульев")
        collector.add_book_in_favorites("Двенадцать стульев")
        assert "Двенадцать стульев" in collector.get_list_of_favorites_books()
