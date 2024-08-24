ncrease the upper limit for the holberton user
exec { 'Change the hard and soft limits':
  command => "sed -i -e 's/nofile [1-9]/nofile 1024/' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
