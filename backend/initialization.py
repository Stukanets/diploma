import os
import django
from time import sleep
from colorama import Fore
from mysql.connector import connect
from mysql.connector.errors import Error, ProgrammingError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

DELAY = 0.1


def database_creations():
    bd_creation_connect = connect(host='diploma-vasyl.mysql.database.azure.com',
                                  port='3306',
                                  user='vasyl',
                                  passwd='Password!')

    bd_creation_cursor = bd_creation_connect.cursor(buffered=True)

    with open('database/Creating_database.sql', encoding='UTF-8') as file:
        creating_database_file_info = file.read()

    with open('database/Deleting_database.sql', encoding='UTF-8') as file:
        deleting_database_file_info = file.read()

    try:
        bd_creation_cursor.execute(creating_database_file_info)
    except Error:
        print(Fore.RED + f"Database already exists!\n" + Fore.YELLOW)

        bd_creation_cursor.execute(deleting_database_file_info)
        print(Fore.GREEN + "Database successfully deleted!\n" + Fore.YELLOW)
        sleep(DELAY)
        bd_creation_cursor.execute(creating_database_file_info)
        print(Fore.GREEN + "Database DeCar_Database has been created!\n" + Fore.YELLOW)
    else:
        print(Fore.GREEN + "Database DeCar_Database has been created!\n" + Fore.YELLOW)


def database_migrations():
    files_list = os.listdir('application/migrations')

    for file in files_list:
        if file != '__init__.py' and file != '__pycache__':
            os.remove(f'application/migrations/{file}')
            print(Fore.CYAN + f'File {file} has been removed!' + Fore.YELLOW)
            sleep(DELAY)
    print()

    os.system('python manage.py makemigrations')
    print(Fore.GREEN + f"\nMigration file created!\n" + Fore.BLUE)
    sleep(DELAY)

    os.system('python manage.py migrate')
    print(Fore.GREEN + f"\nMigration successfully applied!\n")


def superuser_creations():
    from django.contrib.auth.models import User
    from django.db.utils import IntegrityError, ProgrammingError

    superuser_info = {'username': 'vasyl',
                      'password': 'Password!',
                      'email': 'admin@gmail.ua'}

    try:
        User.objects.create_user(username=superuser_info.get('username'),
                                 password=superuser_info.get('password'),
                                 email=superuser_info.get('email'),
                                 is_active=True,
                                 is_staff=True,
                                 is_superuser=True)

    except IntegrityError:
        print(Fore.RED + f"Username `{superuser_info.get('username')}` already exist!\n")
    except ProgrammingError:
        print(Fore.RED + f"Problem with database! Maybe it doesn't exist.\n")
    else:
        print(Fore.GREEN + f"Superuser profile `{superuser_info.get('username')}` has been created!\n")


def insert_information_info_db():
    db_already_exist_connect = connect(host='diploma-vasyl.mysql.database.azure.com',
                                       port='3306',
                                       user='vasyl',
                                       passwd='Password!',
                                       database='DeCar_Database')

    db_already_exist_cursor = db_already_exist_connect.cursor(buffered=True)

    with open('database/Inserting_data.sql', encoding='UTF-8') as file:
        file_data = file.read()

        queries = file_data.split("\n\n")
        for query in queries:
            table_name = ''
            for letter in query[27::]:
                if letter != ' ':
                    table_name += letter
                else:
                    break
            try:
                db_already_exist_cursor.execute(query)
                db_already_exist_connect.commit()
                sleep(DELAY)
            except ProgrammingError:
                print(Fore.RED + "Inserting error!")
            else:
                print(Fore.MAGENTA + f"Successfully inserted data into `{table_name}` table!")


if __name__ == '__main__':
    database_creations()
    sleep(DELAY)
    database_migrations()
    sleep(DELAY)
    superuser_creations()
    sleep(DELAY)
    insert_information_info_db()
    sleep(DELAY)
