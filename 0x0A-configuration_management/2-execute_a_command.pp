nstall flask
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
