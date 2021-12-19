# Memento Pattern
- A token/handle representing the system state. Lets up roll back to the state when the token was generated. May or may not directly expose state information
- Mementos are used to roll back states arbitrarily
- A memento is simply a token/handle class with (typically) no functions of its own
- A memento is not required to expose directly the state(s) to which it reverts the system
- Can be used to implement undo/redo
