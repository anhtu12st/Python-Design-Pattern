# Proxy Pattern
- An interface for accessing a particular resource
- Proxy provides an identical interface; decorator provides an enhanced interface
- Decorator typically aggregates (or has reference to) what it is decorating; proxy doesn't have to
- Proxy might not even be working with a materialized object

- A proxy has the same interface as the underlying object
- To create a proxy, simply replicate the existing interface of an object
- Add relevant functionality to the redefined member functions
- Different proxies (communication, logging, caching, etc.) have completely different behaviors
