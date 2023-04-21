# creating a file

file { 'school':
  ensure  => 'present',  
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school',
  group   => 'www-data',
  content => 'I love Puppet',
}
