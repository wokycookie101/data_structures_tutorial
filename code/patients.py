# Collections is a library that includes the "deque" container, which allows you to pop off elements from either end of a list.
from collections import deque

global patients
patients = deque(["Greg", "Janice", "Tom", "Sharon", "Gavin", "Jane", "Alex"])

# Allows you to add patients in a queue
def add_patients(name):
    patients.append(name)
    return patients

# Allows you to delete patients:
def delete_patients():
    patients.popleft() # popleft() comes with the deque container that let's you pop elements form the left. 
    
def main():
   

    print("####################")
    print("# CURRENT PATIENTS #")
    print("####################\n")
    
    print(patients)
    print()
    
    delete_patients()
    delete_patients()
    add_patients("Amanda")
     
    print("#################")
    print("# PATIENTS LEFT #")
    print("#################\n")
    
    print(patients)
    print()

    
    
if __name__ == "__main__":
    main()
