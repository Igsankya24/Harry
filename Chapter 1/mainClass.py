from Self_Practice1.GetterAndSetter import Employee

if __name__ == "__main__":
    # Code here will only execute if the file is run directly, not when imported
    a = Employee("Babai", 114000, "IT", "QA")
    a.getInfo()
    a.dept = "FINSRV"
    a.role = "SDET"
    a.getInfo()