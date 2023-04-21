# kill a process using puppet

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
