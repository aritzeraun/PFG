
def username_domain(username):

    username.replace(' ', '')
    if '@opendeusto.es' in username or '@deusto.es' in username:
        userTipology = 0
        if '@opendeusto.es' in username:
            username = username.replace('@opendeusto.es', '')
            userTipology = 1
        if '@deusto.es' in username:
            username = username.replace('@deusto.es', '')
            userTipology = 2
        if len(username) == 0:
            data = [username, userTipology, False]
        else:
            data = [username, userTipology, True]
    else:
        data = [username, 0, False]
    return data
