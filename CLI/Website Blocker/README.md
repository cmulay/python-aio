# Website Blocker

### How to use:
Add websites to 
``
    sites_to_block
`` after that select your ``default host`` from the host list provided for example if you are using a linux machine ``default_host = linux``.


set your working hours in 24 hours format.
``blockers(9, 18)`` here 9 is staring hour and 18 is the ending hour

---
### How to remove websites from your hosts:

1. Open a new terminal ``Ctrl + Alt + T``
2. Type ``sudo nano /etc/hosts`` and hit enter
3. Input your password 
4. Clear the fields which have local IP redirection
5. Click ``Ctrl + X`` then press ``y`` and then hit ``Enter``.
6. If prompted another program is editing this file press ``y`` and hit ``Enter``
