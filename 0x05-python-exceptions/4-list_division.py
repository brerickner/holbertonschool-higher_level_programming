#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        new_list = []

        for i in range(list_length):
                result = 0
                try:
                        result = my_list_1[i] / my_list_2[i]

                # If an element is not an integer or float
                except TypeError:
                        print("wrong type")

                # If my_list_1 or my_list_2 is too short
                except IndexError:
                        print("out of range")

                # If the division can’t be done (/0)
                except ZeroDivisionError:
                        print("division by 0")

                finally:
                        new_list.append(result)           

        return new_list
