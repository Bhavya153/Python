def explore_module():
    module_name = input("Enter module name to explore: ")

    try:
        module = __import__(module_name)
        attributes = dir(module)

        print("\nAvailable Attributes in", module_name, ":")
        print(attributes)

    except:
        print("Module not found.")


def explorer_menu():
    print("\n==============================")
    print("Explore Module Attributes (dir())")
    print("==============================")

    explore_module()
