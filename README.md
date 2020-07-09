# Odoo-stop-session-cleaning

### Avoid having odoo itself cleaning sessions

Every ~1000 requests, Odoo list sessions, and remove the too old ones.
As it’s not a problem on a local filesystem, this can be problematic on a shared filesystem, like the NFS one we’re using.
To avoid this performance bottleneck, we’ll stop to check this with Odoo itself, and use a linux cron to achieve this.

### Stop cleaning session in Python code

It’s a bit tricky to change this behaviour. The method consist in a monkey patch of the method. Beware that this code
will reside in a module, and even if the module is not installed, due to the monkey patch nature of the module, the cod e
will be executed.


If the module is visible by Odoo, this line will be present in the log at startup:
```shell
INFO ? odoo.addons.stop_session_gc.models.inherited_ir_http: Odoo session garbage collector status: DISABLED
```


### Installation

##### Odoo v11
```ruby
pip3 install "git+https://github.com/Horanet/Odoo-stop-session-cleaning.git@11.0#egg=odoo11-addon-stop_session_gc&subdirectory=setup/stop_session_gc"
```

##### Odoo v10
```ruby
pip3 install "git+https://github.com/Horanet/Odoo-stop-session-cleaning.git@10.0#egg=odoo10-addon-stop_session_gc&subdirectory=setup/stop_session_gc"
```
