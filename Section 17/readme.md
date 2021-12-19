# Mediator Pattern
- A component that facilitates communication between other components without them necessarily being aware of each other or having direct (reference) access to each other
- Create the mediator and have each object in the system refer to it (in the property)
- Mediator engages in bidirectional communication with its connected components
- Mediator has functions the components can call
- Components have functions the mediator can call
- Event processing (eg Rx) libraries make communication easier to implement
