import json
import requests


def dish_fetch(num):

    response = requests.get("https://api-colombia.com/api/v1/TypicalDish" )

    dishes = json.loads(response.content)

    names = {
        1: "Bandeja paisa",
        2: "Ajiaco",
        3: "Lechona",
        4: "Sancocho"
    }

    selected_name = names[num]

    for dish in dishes:

        if selected_name.lower() in dish["name"].lower():

            return {
                "name": dish["name"],
                "description": dish["description"]
            }


def main():

    print("Hello learners!")

    while True:

        print("\n--- MENU DE PLATOS TIPICOS ---")
        print("1. Bandeja Paisa")
        print("2. Ajiaco")
        print("3. Lechona")
        print("4. Sancocho")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "5":
            print("Programa finalizado")
            break

        elif option in ["1", "2", "3", "4"]:

            result = dish_fetch(int(option))

            print("\nNombre:", result["name"])
            print("Descripción:", result["description"])

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
