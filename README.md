# Tomodoro PyQt / SqlAlchemy Implementation Notes

## SqlAlchemy is half-baked
Needing to write a lot of what is probably "boilerplate" in order to get ORM to do the "right thing".  This is not specifically SqlAlchemy.ORM 
though, just the core database config/ table definition, session interop is requiring a lot of code-around, arranging class hierarchy in special 
ways to allow imports/modules to work.

Last activity : attempting to write doctest on database.Synchrony - session commit appears to have taken no action on inserted record - 
documentation says object should have been mutated after commit.
What would be better is a more-functional database interface that punts the mutability.