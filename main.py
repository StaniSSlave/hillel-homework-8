"""
Написати валідації за допомогою регулярних виразів:

﻿- домашній номер телефону (тільки цифри та довжина номера)

- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

додатково:

- Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
"""
import re
task_n = 1

while task_n != 5:
    try:
        task_n = int(input("Select please task number, that you want to check: \n"
                           "\t1. Перевірка домашнього номеру тф.\n"
                           "\t2. Перевірка мобільного номеру тф.\n"
                           "\t3. Перевірка email.\n"
                           "\t4. Перевірка ПІБ.\n"
                           "\t5. Stop checking tasks\n"
                           "Enter choise here: "))

        match task_n:
            case 1:
                finish_t1_l = "y"
                while finish_t1_l == "y":

                    a = 0
                    while a != 1:
                        try:
                            home_number = input("Enter you home phone number(6-num format): ")
                            if re.match(r"\d{6}", home_number) and len(home_number) == 6:
                                print("Your number saved successfully!")
                                a = 1
                            elif re.search(r"[a-zA-ZА-Яа-яЇїІіЄєҐґ]",home_number):
                                raise Exception("Enter only integers, please!")
                            else:
                                raise Exception("Enter please only 6 numbers")
                        except Exception as e:
                            print(f"\tError: {e}")


                    while finish_t1_l != "y" or finish_t1_l != "n":
                        finish_t1_l = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t1_l = finish_t1_l.lower()
                        try:
                            if finish_t1_l == "y":
                                break
                            elif finish_t1_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 2:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    a = 0
                    while a != 1:
                        try:
                            home_number = input("Enter you mobile phone number with the country code: ")
                            if re.match(r"[+]{1}+\d{12}", home_number) and len(home_number) == 13:
                                print("Your number saved successfully!")
                                a = 1
                            elif re.match(r"\d{12}", home_number) and len(home_number) == 12:
                                print("Your number saved successfully!")
                                a = 1
                            elif len(home_number) != 12:
                                raise Exception("Enter please only 12 numbers")
                            elif re.search(r"[+]{2,100}", home_number) or re.search(r"\+", home_number).start() != 0:
                                raise Exception("Something went wrong with \"+\" symbol!")
                            elif re.search(r"[a-zA-ZА-Яа-яЇїІіЄєҐґ]",home_number):
                                raise Exception("Enter only integers, please!")
                            else:
                                "Oops! Something went wrong! try one more time"
                        except Exception as e:
                            print(f"\tError: {e}")

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 3:
                finish_t3_l = "y"
                while finish_t3_l == "y":

                    a = 0
                    while a != 1:
                        try:
                            home_number = input("Enter your email, please. "
                                                "Email should consist of 6 letters in username and "
                                                "8 characters in domain including \".\"\n"
                                                "Example: stassk@qwer.tyu.\n"
                                                "Enter yours here:")
                            if (re.search(r".", home_number).start() + re.search(r".", home_number).end()) != re.search(r".", home_number).start():
                                print("Only one \".\" near to each other!")
                            elif re.match(r"[a-zA-Z!#$%&'*+\-/=?^_`{|}~.]{6}+{8}", home_number) and len(home_number) == 13:
                                print("Your number saved successfully!")
                                a = 1
                            elif re.match(r"\d{12}", home_number) and len(home_number) == 12:
                                print("Your number saved successfully!")
                                a = 1
                            elif len(home_number) != 12:
                                raise Exception("Enter please only 12 numbers")
                            elif re.search(r"[+]{2,100}", home_number) or re.search(r"\+", home_number).start() != 0:
                                raise Exception("Something went wrong with \"+\" symbol!")
                            elif re.search(r"[a-zA-ZА-Яа-яЇїІіЄєҐґ]",home_number):
                                raise Exception("Enter only integers, please!")
                            else:
                                "Oops! Something went wrong! try one more time"
                        except Exception as e:
                            print(f"\tError: {e}")

                    while finish_t3_l != "y" or finish_t3_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t3_l = finish_t3_l.lower()
                        try:
                            if finish_t3_l == "y":
                                break
                            elif finish_t3_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 4:
                finish_t4_l = "y"
                while finish_t4_l == "y":

                    print("4")

                    while finish_t4_l != "y" or finish_t4_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t4_l = finish_t4_l.lower()
                        try:
                            if finish_t4_l == "y":
                                break
                            elif finish_t4_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 5:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")