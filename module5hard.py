import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, login: str, password: str): #Метод, принимает на вход аргументы

        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int): #  Принимает три аргумента: nickname, password, age

        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self): # Сброса текущего пользователя на None.
        self.current_user = None

    def add(self, *args): # Метод, принимающий неограниченное кол-во объектов класса Video
        for movie in args:
            self.videos.append(movie)

    def get_videos(self, text: str) -> list:  # Метод get_videos

        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str) -> None:   # Метод watch_video

        if self.current_user and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title  # заголовок
        self.duration = duration  # продолжительность
        self.time_now = time_now  # секунда остановки, в начале 0
        self.adult_mode = adult_mode  # возрастное ограничение

    def __str__(self):
        return f"{self.title}"


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname  # имя пользователя
        self.password = password  # пароль
        self.age = age  # возраст

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)





    #Код для проверки:
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')