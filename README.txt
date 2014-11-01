pyramid_turnout
=================

Getting Started
-----------------

Or, in your application's configuration development.ini add:

   pyramid.includes =
     pyramid_turnout
     ...
     pyramid_debugtoolbar
     pyramid_tm


Or, in your application’s configuration stanza use the pyramid.config.Configurator.include() method:

   config.include('pyramid_turnout')


Configuration
---------------

example:

   [app:myproject]
   turnout.enabled = true
   turnout.settings_file = %(here)s/maintenance.cfg
   turnout.template = myproj:templates/maintenance.pt
