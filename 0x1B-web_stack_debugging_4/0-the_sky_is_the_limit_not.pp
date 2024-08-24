# Increase the file limit for nginx service
file { '/etc/default/nginx':
  ensure  => file,
  content => '# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 4096"'
}
-> exec {'Restart the service':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
