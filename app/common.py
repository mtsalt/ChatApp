def authentication(id_val, password_val):

    # get id and password from db
    id_data = "abc"
    password_data = "123"

    if id_data == id_val and password_data == password_val:
        return True
    else:
        return False