can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def can_create_bits(user_permissions):
    # validation is loaded with can_x_guild number if True or 0 if False
    validation = user_permissions & can_create_guild
    # comparison returns True or False
    return validation == can_create_guild

def can_review_bits(user_permissions):
    # validation is loaded with can_x_guild number if True or 0 if False
    validation = user_permissions & can_review_guild
    # comparison returns True or False
    return validation == can_review_guild

def can_delete_bits(user_permissions):
    # validation is loaded with can_x_guild number if True or 0 if False
    validation = user_permissions & can_delete_guild
    # comparison returns True or False
    return validation == can_delete_guild

def can_edit_bits(user_permissions):
    # validation is loaded with can_x_guild number if True or 0 if False
    validation = user_permissions & can_edit_guild
    # comparison returns True or False
    return validation == can_edit_guild

def main(user):
    print("Can create guild:", can_create_bits(user))
    print("Can review guild:", can_review_bits(user))
    print("Can delete guild:", can_delete_bits(user))
    print("Can edit guild:", can_edit_bits(user))

sam = main(0b1101)
