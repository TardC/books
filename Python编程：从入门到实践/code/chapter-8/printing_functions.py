def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until there are no unprinted designs.
    After printing each design, move it to the list completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate the process of making a 3D printed model
        # based on design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all printed models."""
    print("\nThe followinng models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
