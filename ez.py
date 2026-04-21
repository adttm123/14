from random import randint
################################################################################################################
def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get("id"))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id
################################################################################################################
def add_new_user(data: list[dict])-> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname":input("Enter surname: ").strip().lower() or None,
        "date of birth":input("date of birth: ").strip().lower() or None,
        "grades mathematics": [],
        "grades polish": [], 
        "grades english":[]        
    }    
################################################################################################################
def add_or_remove_grades(data: list[dict])->None:
    user_id = int(input("Podaj id ucznia: "))

    user = None
    for i in data:
        if i["id"] == user_id:
            user = i
################################################################################################################
    if user == None:
        print("Nie ma takiego id")
        return
################################################################################################################    
    subject = input("mathematics / polish / english:").strip().lower()
    if subject == "mathematics":
        key = "grades mathematics"
    elif subject == "polish":
        key = "grades polish"
    elif subject == "english":
        key = "grades english"
    else:
        print("Zły przedmiot")
        return
    operacja = input('''
                     Co chcesz zrobić ?
                     1 - usunąć ocene
                     2 - dodać ocene
                     ''').strip().lower()
    ocena = int(input("Podaj ocene:"))
    if operacja == "1":
        if ocena in user[key]:
            user[key].remove(ocena)
            print("Usunięto ocene")
            return
        else:
            print("Złą ocena")
    elif operacja == "2":
        user[key].append(ocena)
        print("Dodano ocene")
        return
    else:
        print("Zła operacja")
################################################################################################################
def find_user_by_id(data: list[dict]) -> dict | None:
    szukane_id = int(input("Podaj ID ucznia: "))

    for user in data:
        if user["id"] == szukane_id:
            return user
    return None
################################################################################################################
def find_users_by_name(data: list[dict], name: str) -> list[dict]:
    szukane = []
    for user in data:
        if user["name"].lower() == name.lower():
            szukane.append(user)
    return szukane
################################################################################################################
def delete_user_by_id(data: list[dict], user_id: int) -> bool:
    szukane_id = int(input("Podaj ID ucznia: "))

    for user in data:
        if user["id"] == szukane_id:
            data.remove(user)
            return True
    else:
        return False
################################################################################################################   
def update_user_name(data: list[dict], user_id: int, new_name: str) -> bool:
    for user in data:
        if user["id"] == user_id:
            user["name"] = new_name
            return True

    return False
################################################################################################################
def update_user_surname(data: list[dict], user_id: int, new_surname: str) -> bool:
    for user in data:
        if user["id"] == user_id:
            user["surname"] = new_surname
            return True
    return False
################################################################################################################
def update_user_birth_date(data: list[dict], user_id: int, new_birth_date: str) -> bool:
    for user in data:
        if user["id"] == user_id:
            user["date of birth"] = new_birth_date
            return True
    return False
################################################################################################################
def is_name_taken(data: list[dict], name: str, surname: str) -> bool:
    for user in data:
        if user["name"].lower() == name.lower() and user["surname"].lower() == surname.lower():
            return True
    return False
################################################################################################################
def show_one_user(user: dict) -> None:
    print(f"ID: {user['id']}")
    print(f"Imię: {user['name']}")
    print(f"Nazwisko: {user['surname']}")
    print(f"Data urodzenia: {user['date of birth']}")
    print(f"Matematyka: {user['grades mathematics']}")
    print(f"Polski: {user['grades polish']}")
    print(f"Angielski: {user['grades english']}")
################################################################################################################
def count_all_users(data: list[dict]) -> int:
    return len(data)
################################################################################################################
def count_users_with_missing_name(data: list[dict]) -> int:
    x = 0
    for user in data:
        if user["name"] ==  None or user["name"] == "":
            x += 1
    return x
################################################################################################################
def average_math_for_user(user: dict) -> float | None:
    oceny = user["grades mathematics"]

    if len(oceny) == 0:
        return None

    return sum(oceny) / len(oceny)
################################################################################################################
def average_polish_for_user(user: dict) -> float | None:
    oceny = user["grades polish"]

    if len(oceny) == 0:
        return None

    return sum(oceny) / len(oceny)
################################################################################################################
def average_english_for_user(user: dict) -> float | None:
    oceny = user["grades english"]

    if len(oceny) == 0:
        return None

    return sum(oceny) / len(oceny)
################################################################################################################
def overall_average_for_user(user: dict) -> float | None:
    oceny = user["grades mathematics"] + user["grades polish"] + user["grades english"]

    if len(oceny) == 0:
        return None

    return sum(oceny) / len(oceny)
################################################################################################################
def best_student_in_subject(data: list[dict], subject: str) -> dict | None:
    best_user = None
    best_average = -1

    for user in data:
        if subject == "mathematics":
            avg = average_math_for_user(user)
        elif subject == "polish":
            avg = average_polish_for_user(user)
        elif subject == "english":
            avg = average_english_for_user(user)
        else:
            return None

        if avg is not None and avg > best_average:
            best_average = avg
            best_user = user

    return best_user
################################################################################################################
def subject_average_for_all_users(data: list[dict], subject: str) -> float | None:
    wszystkie_oceny = []

    for user in data:
        if subject == "mathematics":
            wszystkie_oceny += user["grades mathematics"]
        elif subject == "polish":
            wszystkie_oceny += user["grades polish"]
        elif subject == "english":
            wszystkie_oceny += user["grades english"]
        else:
            return None

    if len(wszystkie_oceny) == 0:
        return None

    return sum(wszystkie_oceny) / len(wszystkie_oceny)
################################################################################################################