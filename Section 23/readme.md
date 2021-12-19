# Visitor Pattern
- A component (visitor) that knows how to traverse a data structure composed of (possibly related) types
- OOP double-dispatch approach is not necessary in Python
- Make a visitor, decorating each 'overload' with @visitor
- Call visit() and the entire structure gets traversed
