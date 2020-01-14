from rolepermissions.roles import AbstractUserRole

# Roles are automatically generated for use elsewhere in the code using snake case ('pink_diamond'). For
# example, when using the assign_role() function, use the snake case version to refer to the abstract user role
# listed here ('PinkDiamond').

class PinkDiamond(AbstractUserRole):
    available_permissions = {
        'create_rose_quartz': True,
        'create_pearl': True,
        'view_gem_list': True,
    }

class RoseQuartz(AbstractUserRole):
    available_permissions = {
        'create_pearl': True,
        'view_gem_list': True,
    }

class Pearl(AbstractUserRole):
    available_permissions = {
        'view_gem_list': True,
    }