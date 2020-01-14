# Cascading Auths with Django
a project to demonstrate cascading authorizations using django-role-permissions and django-registration

Let's say you need more than the standard User/Admin level of authorization in your project. What if you want a tree of authorizations, in which people at the top can auth lower tiers, who can in turn auth lower tiers? There is no great solution out of the box for this in Django. This project uses Django Role Permissions and Django Registration to 

1. Create finely-grained authorizations
2. Allow users to create users at their "tier" or lower
3. Allow users to create users by email address with no password
4. Who can then activate and initiate an immediate password reset (eliminating the need for the creating users to create or communicate temporary passwords)
