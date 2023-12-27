def filter_not_viewed_movies() -> list:
    movies = [
        'Побег из Шоушенка',
        'Крёстный отец',
        'Тёмный рыцарь',
        'Крёстный отец 2',
        '12 разгневанных мужчин',
        'Список Шиндлера',
        'Властелин колец: Возвращение короля',
        'Криминальное чтиво',
        'Властелин колец: Братство Кольца',
        'Хороший, плохой, злой',
        'Форрест Гамп',
        'Бойцовский клуб',
        'Властелин колец: Две крепости',
        'Начало',
        'Звёздные войны. Эпизод V: Империя наносит ответный удар',
        'Матрица',
        'Славные парни',
        'Пролетая над гнездом кукушки',
        'Семь',
        'Эта прекрасная жизнь'
    ]

    viewed_movies = [
        'Побег из Шоушенка',
        'Тёмный рыцарь',
        'Властелин колец: Возвращение короля',
        'Властелин колец: Братство Кольца',
        'Форрест Гамп',
        'Бойцовский клуб',
        'Властелин колец: Две крепости',
        'Начало',
        'Звёздные войны. Эпизод V: Империя наносит ответный удар',
        'Матрица',
        'Семь'
    ]

    not_viewed_movies = []

    for movie in movies:
        if movie not in viewed_movies:
            not_viewed_movies.append(movie)

    return not_viewed_movies


print(filter_not_viewed_movies())


def print_compare_movies_with_ratings():
    movies = [
        'Побег из Шоушенка',
        'Тёмный рыцарь',
        'Властелин колец: Возвращение короля',
        'Властелин колец: Братство Кольца',
        'Форрест Гамп',
        'Бойцовский клуб',
        'Властелин колец: Две крепости',
        'Начало',
        'Звёздные войны. Эпизод V: Империя наносит ответный удар',
        'Матрица',
        'Семь'
    ]

    movie_ratings = [10, 9, 6, 9, 10, 6, 10, 9, 6, 9, 10]

    for index in range(len(movies)):
        print(movies[index] + ": " + str(movie_ratings[index]))

print_compare_movies_with_ratings()