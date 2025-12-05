from Employee import Employee

def recup_nom_long(employee, limite=3):
    """ récupère et affiche un nom s'il contient plus de limite lettres """
    if employee.last: 
        if len(employee.last>=limite):
            print("nom long")
            return employee.last
        else: 
            return f"nom trop court" 