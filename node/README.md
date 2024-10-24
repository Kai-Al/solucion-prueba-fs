### OBSERVER PATTERN

---

As a developer I want to be able to have a system that allows me to perform actions
triggered by events, to accomplish this we designed a solution that should allow us
to store and manage those events.

Based on a TDD experience we designed the unit tests that would guide the development
of the solution, the goal of this exercise is complement the code base from
`src/eventDispatcher.js` to fulfill successfully all tests defined in `eventDispatcher.spec.js`
(tests can't be modified).

### System Methods :

| Method              | Concept                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| addEventListener    | Access the store and save callback for event name                                                                                              |
| removeEventListener | Access the store and remove callback for event name                                                                                            |
| dispatchEvent       | Execute every callback in store related to certain event name                                                                                  |
| hasListenerFor      | Access the store and check certain event name has callbacks                                                                                    |
| hasCallbackFor      | Access the store and check certain callback exists for related event name                                                                      |
| mixin               | Mixin concept in Javascript relates to a form of object composition where methods or properties are added to objects without using inheritance |

### Testing your changes :

To see the actual output of the tests open `index.html` in a browser, you'll see their
status displayed on the page, that should be enough to get you started.

### Notes :

Feel free to use any ai/library/google search, but we want to see your development skills.
