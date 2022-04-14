
def username_domain(username):

    username.replace(" ", "")
    if "@opendeusto.es" in username or "@deusto.es" in username:
        userTypology = 0
        if "@opendeusto.es" in username:
            username = username.replace("@opendeusto.es", "")
            userTypology = 1
        if "@deusto.es" in username:
            username = username.replace("@deusto.es", "")
            userTypology = 2
        if len(username) == 0:
            data = [username, userTypology, False]
        else:
            data = [username, userTypology, True]
    else:
        data = [username, 0, False]
    return data
