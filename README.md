# Odoo-stop-session-cleaning

### Avoid having odoo itself cleaning sessions

Every ~1000 requests, Odoo list sessions, and remove the too old ones.
As it’s not a problem on a local filesystem, this can be problematic on a shared filesystem, like the NFS one we’re using.
To avoid this performance bottleneck, we’ll stop to check this with Odoo itself, and use a linux cron to achieve this.

### Stop cleaning session in Python code

It’s a bit tricky to change this behaviour. The method consist in a monkey patch of the method. Beware that this code
will reside in a module, and even if the module is not installed, due to the monkey patch nature of the module, the cod e
will be executed.
