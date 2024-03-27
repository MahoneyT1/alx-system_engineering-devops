exec { 'install_werkzeug':
  command  => '/usr/bin/pip3 install werkzeug==2.1.1',
  creates  => '/usr/local/lib/python3.X/dist-packages/werkzeug',  # Adjust the Python version accordingly
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  provider => shell,
}
