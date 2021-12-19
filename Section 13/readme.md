# Chain of Responsibility Pattern
- A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and ability to terminate the processing chain
- Command = asking for an action or change (e.g., please set your attack value to 2)
- Query = asking for information (e.g, please give me your attack value)
- Command Query Separation (CQS) = having separate means of sending commands and queries to e.g, direct field access

- Chain of Responsibility can be implemented as a chain of references or a centralized construct
- Enlist objects in the chain, possibly controlling their order
- Object removal from chain (e.g. in __exit__)
